# 🤖 Customer Support RAG Bot  
**(Gemini + LangChain + FAISS + Streamlit)**

An end-to-end **Retrieval Augmented Generation (RAG)** based customer support chatbot that answers user queries from uploaded **customer support PDFs** (refunds, returns, policies, FAQs) using **Google Gemini**, **LangChain**, and **FAISS**.

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


