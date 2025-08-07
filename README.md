# Mongo-CRUD-Agent

**AI-powered CLI to perform MongoDB CRUD operations using natural language instructions.**

---

## 🧠 Overview

Mongo-CRUD-Agent is a natural language-driven command-line tool built with Python that enables users to perform Create, Read, Update, and Delete operations on MongoDB databases using plain English. Powered by a local language model via Ollama, this tool simplifies database interactions without writing complex queries.

---

## 🚀 Features

- 🔹 **Natural Language Input**: Use human-readable commands instead of writing raw queries.
- 🔹 **Full CRUD Functionality**: Perform create, read, update, and delete operations on any MongoDB collection.
- 🔹 **Integrated with Ollama + Mistral**: Uses a local LLM backend to interpret and convert instructions into database operations.
- 🔹 **Typer-based CLI**: Clean and intuitive CLI interface built using `Typer`.
- 🔹 **Test Suite Included**: Comes with a testing script to validate all CRUD operations through the agent.

---

## 📁 Project Structure

```text
Mongo-CRUD-Agent/
├── .env                    # Environment variables (Mongo URI, etc.)
├── ai_agent.py             # Handles interaction with the local LLM (Ollama)
├── config.py               # Configuration utilities
├── main.py                 # Entry point with CLI commands
├── mongo_crud_tool.py      # Actual MongoDB CRUD logic
├── ollama_llm.py           # LLM-specific prompt logic
├── prompts.py              # Predefined system and user prompts
├── requirements.txt        # Python dependencies
├── test_mongoai.py         # Test script for Mongo-AI agent
└── README.md               # Project documentation
```

---

## 🛠️ Installation

1. **Clone the Repository**
```bash
git clone https://github.com/Magnus0969/Mongo-CRUD-Agent.git
cd Mongo-CRUD-Agent
```

2. **Set Up Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Configure Environment**
Create a `.env` file and add your MongoDB URI:
```
MONGO_URI=mongodb://localhost:27017/
```

4. **Ensure Ollama is Installed**
Make sure [Ollama](https://ollama.com) is running with a model (e.g., mistral):
```bash
ollama run mistral
```

---

## 💬 Example Usage

Run the CLI:
```bash
python main.py
```

Then enter natural language instructions like:

```text
create a new document in the "users" collection with name "Alice" and age 30
read all documents from "users"
update "users" set age to 31 where name is "Alice"
delete from "users" where name is "Alice"
```

---

## ✅ Run Tests

To test all CRUD operations via the agent:

```bash
python test_mongoai.py
```

This will feed sample natural language commands to Refract (the agent) and validate the outcomes.

---

## 📦 Dependencies

Main dependencies listed in `requirements.txt`:
```
typer[all]
pymongo
python-dotenv
requests
```

---

## 🧪 AI Agent: mongoai

The LLM agent, named **mongoai**, uses prompt engineering + local inference through Ollama and converts user instructions into database operations using a custom parsing logic.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Feel free to open issues or submit PRs. Any contribution toward better prompt design, improved NLP-to-CRUD logic, or UI enhancements is welcome!

---

## 🙋‍♂️ Author

**Karthik Magadi** – [Magnus0969](https://github.com/Magnus0969)

---

> Simplify your database workflow with natural language. Let Refract handle the rest.
