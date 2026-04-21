# LangChain Groq AI Project

A Python project using LangChain and Groq API to query information using the Llama 3.3 70B model.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- A Groq API key ([Get one here](https://console.groq.com))

## Installation Steps

### 1. Clone or Setup the Project

```bash
cd c:\Users\nani9\OneDrive\Desktop\Projects\AgentAi\langchain
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv .venv
```

**Activate the Virtual Environment:**

**Windows (PowerShell) - First Time Setup:**

If you get an error about execution policy, run this command first (one time only):

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
.venv\Scripts\activate
```

**MacOS/Linux:**
```bash
source .venv/bin/activate
```

### 3. Install Dependencies

Install the required packages from `req.txt`:

```bash
pip install -r req.txt
```

This will install:
- `langchain==1.2.15`
- Other required dependencies

### 4. Setup Environment Variables

Create a `.env` file in the project directory:

```bash
# .env file
GROQ_API_KEY=your_groq_api_key_here
```

Replace `your_groq_api_key_here` with your actual Groq API key from [https://console.groq.com](https://console.groq.com)

## How to Use

### Running the Script

```bash
python llm.py
```

### Script Explanation

The `llm.py` script:
1. Imports necessary libraries (LangChain, dotenv)
2. Loads environment variables from `.env` file
3. Initializes a ChatGroq instance with the Llama 3.3 70B model
4. Sends a query: "what are the metro palette city in india"
5. Prints the response from the AI model

### Modifying Queries

To change the query, edit the `llm.py` file:

```python
# Change this line to your desired query
result = llm.invoke("your custom question here")
```

## File Structure

```
langchain/
├── llm.py           # Main script with Groq API integration
├── req.txt          # Project dependencies
├── .env             # Environment variables (create this file)
└── read.md          # This file
```

## Troubleshooting

**Error: `GROQ_API_KEY not found`**
- Make sure your `.env` file exists in the project directory
- Verify your Groq API key is correct

**Error: `ModuleNotFoundError: No module named 'langchain_groq'`**
- Run `pip install -r req.txt` again
- Make sure your virtual environment is activated

## Additional Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Groq Console](https://console.groq.com)
- [Llama 3.3 Model Info](https://groq.com/)
