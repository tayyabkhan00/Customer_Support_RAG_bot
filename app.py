import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI
)
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from langchain_community.document_loaders import PyPDFLoader
import streamlit as st

# ----------------------------
# 🎨 Background Image Helper
# ----------------------------
def add_bg_from_local(image_file):
    import base64
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ----------------------------
# 1️⃣ Streamlit UI
# ----------------------------
st.set_page_config(page_title="Customer Support RAG Bot")
add_bg_from_local("assets/bg4.jpeg")
st.title("🤖 Customer Support RAG Bot")

# ----------------------------
# 📄 Sidebar: Sample PDFs
# ----------------------------
st.sidebar.markdown("## 📄 Sample Support PDFs")

st.sidebar.caption(
    "Don’t have a valid customer support PDF? "
    "Select a source below, download it, and upload."
)

sample_sources = {
    "Select a sample document": None,
    "Refund & Return Policy (Flipkart)": "https://www.flipkart.com/pages/returnpolicy",
    "Shipping & Delivery Policy (Flipkart)": "https://www.flipkart.com/pages/shipping",
    "Customer Support Help Center": "https://www.flipkart.com/helpcentre",
}

selected_source = st.sidebar.selectbox(
    "Choose a sample source",
    options=list(sample_sources.keys())
)

if selected_source != "Select a sample document":
    st.sidebar.markdown(
        f"🔗 **[Open Source]({sample_sources[selected_source]})**"
    )

# ----------------------------
# 📤 File Uploader (DEFINE IT HERE ✅)
# ----------------------------
uploaded_files = st.file_uploader(
    "Upload customer support PDFs (FAQs, refund, return, policy documents)",
    type=["pdf"],
    accept_multiple_files=True,
    help="Upload valid customer support PDFs to initialize the knowledge base."
)

# ----------------------------
# ❓ User Question Input
# ----------------------------
user_question = st.text_input(
    "Ask a customer support question:",
    help="Upload PDFs first before asking questions."
)

# ----------------------------
# 💡 Sidebar: Example Questions
# ----------------------------
st.sidebar.markdown("## 💡 Sueggested Questions")

st.sidebar.caption(
    "Try asking one of these questions to interact with the support bot."
)

example_questions = [
    "What is Flipkart’s return policy for electronic items?",
    "How many days do I have to return a product after delivery?",
    "Can I return a product if it is damaged or defective?",
    "Are there any items that are not eligible for return?",
    "How does the refund process work after a return?",
    "Will I get a full refund including delivery charges?"
]

selected_example = st.sidebar.selectbox(
    "Select a question",
    options=["Select an example question"] + example_questions
)

# ----------------------------
# 2️⃣ Load & Index PDFs
# ----------------------------
documents = []

if uploaded_files:
    for file in uploaded_files:
        file_path = f"data/uploads/{file.name}"
        os.makedirs("data/uploads", exist_ok=True)

        with open(file_path, "wb") as f:
            f.write(file.read())

        loader = PyPDFLoader(file_path)
        pdf_docs = loader.load()

        for doc in pdf_docs:
            doc.metadata["source"] = file.name
            documents.append(doc)

# ----------------------------
# 3️⃣ Text Splitting
# ----------------------------
if documents:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=80
    )
    chunks = splitter.split_documents(documents)

    # ----------------------------
    # 4️⃣ Embeddings + Vector Store
    # ----------------------------
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004"
    )

    vectorstore = FAISS.from_documents(chunks, embeddings)

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    # ----------------------------
    # 5️⃣ Gemini LLM
    # ----------------------------
    llm = ChatGoogleGenerativeAI(
    model="models/gemini-flash-latest",
    temperature=0.2,
    )

    # ----------------------------
    # 6️⃣ Prompt with Source Citations
    # ----------------------------
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are a customer support AI assistant.

Answer ONLY using the context below.
Cite sources with page number and document name.
If the answer is not found, say "I don't know".

Context:
{context}

Question:
{question}

Answer format:
- Answer
- Sources
"""
    )
# ----------------------------
# 🔧 Helper: Format Retrieved Docs  ← STEP 1 GOES HERE
# ----------------------------
def format_docs(docs):
    return "\n\n".join(
        f"Source: {d.metadata.get('source', 'unknown')}\nContent: {d.page_content}"
        for d in docs
    )

    # ----------------------------
    # 7️⃣ RAG Chain
    # ----------------------------
    rag_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
     )

    # ----------------------------
    # 8️⃣ Ask Question
    # ----------------------------
    if user_question:
        with st.spinner("Thinking..."):
            response = rag_chain.invoke(user_question)
        st.markdown("### ✅ Answer")
        st.write(response)
        if "I don't know" in response:
            st.warning(
                "The uploaded documents do not contain this information. "
                "Try uploading a valid customer support PDF from the sample sources above."
            )


else:
    st.info("Upload PDFs to initialize the knowledge base.")
