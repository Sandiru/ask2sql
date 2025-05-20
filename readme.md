# 🧠 ASK2SQL — Natural Language to SQL Converter

ASK2SQL is an interactive Python tool that allows users to ask natural language questions and get answers from a SQL database. It uses Google's Gemini (via LangChain) to generate SQL queries from your questions, execute them on a connected MySQL database, and return human-readable answers.

## 🚀 Features

- 🌍 Converts natural language into SQL queries
- 🧠 Uses Google's Gemini model for LLM-powered query generation
- 💡 Automatically executes SQL queries on your MySQL database
- 🗣️ Returns easy-to-understand answers
- 🖥️ CLI-based interactive interface
- 🔒 Environment variable support for credentials

---

## 🛠️ Installation

### 1. Clone the repository
git clone https://github.com/yourusername/ask2sql.git
cd ask2sql

### 2. Set up a virtual environment
conda create -n ask2sql python=3.11
conda activate ask2sql

### 3. Install dependencies
pip install -r requirements.txt

### 🔑 Environment Variables
GOOGLE_API_KEY=your_google_api_key
USER=your_mysql_username
PASSWORD=your_mysql_password
HOST=your_mysql_host
PORT=3306
DB_NAME=your_database_name
MODEL=gemini-2.0-flash  # or another supported Google model

### ▶️ Usage
python main.py

### 🧩 Tech Stack
LangChain
Google Generative AI (Gemini)
MySQL
dotenv

### 📂 Project Structure

ask2sql/
│
├── ask2sql/             
│   └── main.py         
│
├── .env                
├── README.md            
└── requirements.txt    

### 🙌 Acknowledgements

OpenAI for inspiration on conversational apps
LangChain team for awesome abstractions
Google for the Gemini API



