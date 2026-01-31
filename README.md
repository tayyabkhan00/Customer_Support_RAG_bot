# 🤖 Customer Support RAG Bot  
**(Gemini + LangChain + FAISS + Streamlit)**

An end-to-end **Retrieval Augmented Generation (RAG)** based customer support chatbot that answers user queries from uploaded **customer support PDFs** (refunds, returns, policies, FAQs) using **Google Gemini**, **LangChain**, and **FAISS**.

🚀 Live Demo

🔗 Streamlit App:
👉 [https://customersupportragbot-cwcpwjupnqpu9caaaxmy3o.streamlit.app/]

This project demonstrates how modern **GenAI systems are built in production**, focusing on:
- Hallucination reduction
- Context-grounded answers
- Real-time streaming responses
- Practical customer support use cases

---

## 🚀 Features

- 📄 Upload multiple customer support PDFs  
- 🔍 Semantic search using vector embeddings (FAISS)  
- 🧠 Context-aware answers using RAG  
- ⚡ Streaming responses (ChatGPT-like UX)  
- 📚 Source-cited answers (document-aware)  
- 🖥️ Simple interactive UI using Streamlit  

---

## 🧠 Tech Stack

| Component | Technology |
|--------|-----------|
| LLM | Google Gemini (`gemini-flash-latest`) |
| Embeddings | `text-embedding-004` |
| Framework | LangChain (LCEL) |
| Vector Database | FAISS |
| UI | Streamlit |
| Document Loader | PyPDFLoader |
| Language | Python |

---

## 🔁 Architecture (RAG Flow)
```
PDF Documents
↓
Text Chunking
↓
Gemini Embeddings
↓
FAISS Vector Store
↓
Retriever
↓
Prompt + Context
↓
Gemini LLM (Streaming)
↓
Answer + Sources
```

---

## 📂 Project Structure

```
customer-support-rag-bot/
│
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── data/
└── uploads/ # Uploaded PDF files
```

---

## 🛠️ Setup Instructions (Run Locally)

Follow these steps **exactly** to run the project on your system.

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/tayyabkhan00/customer-support-rag-bot.git
cd customer-support-rag-bot
```
## 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate     # macOS / Linux
venv\Scripts\activate        # Windows
```
## 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
## 4️⃣ Set Gemini API Key
```bash
export GOOGLE_API_KEY="your_gemini_api_key"
```
(Windows)
```bash
set GOOGLE_API_KEY=your_gemini_api_key
```
## 5️⃣ Run the App
```bash
streamlit run app.py
```
## 📄 How It Works (Step-by-Step)

- Upload PDFs (refund, return, policy documents)
- PDFs are loaded and split into chunks
- Each chunk is converted into vector embeddings
- Embeddings are stored in FAISS vector database
- User question is embedded and matched semantically
- Relevant chunks are injected into the RAG prompt
- Gemini generates a streaming, grounded response

## 🧪 Example Questions

- What is the return policy for electronic items?
- How many days do I have to return a product?
- How does the refund process work?
- Are delivery charges refundable?
- Which products are not eligible for returns?

## 🔐 Hallucination Control

The chatbot is strictly instructed to:
- Answer only from retrieved document context
- Respond with “I don’t know” if information is missing
This makes it suitable for enterprise and customer-facing applications.

## 📈 Use Cases

- Customer Support Automation
- Policy & FAQ Assistant
- E-commerce Helpdesk
- Internal Company Knowledge Base
- Document Question Answering

## 🎯 Why This Project Matters

This project demonstrates:
- Practical GenAI application development
- End-to-end RAG pipeline design
- Real-world customer support use case
- Modern LangChain architecture (LCEL)
- Production-ready UI deployment
It is suitable for entry-level GenAI / AI Engineer / Data Scientist roles.

## 🚀 Future Enhancements

- Chat history & memory
- Source citations with page numbers
- Role-based access
- Multi-language support
- Database-backed vector persistence

## 👨‍💻 Author

Tayyab Khan<br>
BTech – AI & Data Science<br>
Aspiring GenAI / Data Science Engineer

**⭐ If You Like This Project**

Give it a ⭐ on GitHub — it really helps!
