# Local AI Agent for PC Store Reviews

This project demonstrates a local AI-powered question-answering system for a PC components store, using LangChain, Ollama, and ChromaDB. It leverages real customer reviews to answer user queries about products, pricing, shipping, and service.

## Features
- Uses a local LLM (default: DeepSeek-R1:8B via Ollama)
- Retrieves relevant reviews using vector search (ChromaDB)
- Interactive command-line interface for asking questions
- Easily switch to other local LLMs supported by Ollama

## Project Structure
- `main.py`: Main script for running the Q&A agent
- `vector.py`: Loads reviews, builds vector store, and exposes retriever
- `realistic_pcstore_reviews.csv`: Dataset of realistic PC store reviews
- `requirements.txt`: Python dependencies
- `chroma_db/`: ChromaDB vector store files

## Setup Instructions

### 1. Install Ollama
Download and install Ollama from [https://ollama.com/download](https://ollama.com/download) for your OS. Start the Ollama server locally.

### 2. Install Python Dependencies
Create a virtual environment and install requirements:
```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Download or Prepare LLM Model
Pull the desired model with Ollama, e.g.:
```powershell
ollama pull deepseek-r1:8b
```
You can use other models, such as:
- `llama3`
- `mistral`
- `phi3`
- `qwen`
- `gemma`
- `mixtral`

Update the model name in `main.py` and `vector.py` as needed.

### 4. Run the Project
Start the agent:
```powershell
python main.py
```
Enter your questions at the prompt. Type `q` to quit.

## Switching to Other Local LLMs
To use a different local LLM, change the model name in these lines:
- In `main.py`:
  ```python
  model = OllamaLLM(model='your-model-name')
  ```
- In `vector.py` (for embeddings):
  ```python
  embeddings = OllamaEmbeddings(model='your-embedding-model')
  ```
Make sure the model is available in Ollama (`ollama pull your-model-name`).

## Notes
- The first run will create a vector store from the CSV reviews. Subsequent runs will reuse the database.
- You can replace the CSV with your own reviews for other domains.
- For best results, use embedding models optimized for retrieval (e.g., `mxbai-embed-large`).

## Troubleshooting
- Ensure Ollama is running and the model is pulled.
- If you change the CSV, delete the `chroma_db/` folder to rebuild the vector store.
- For more info on LangChain, Ollama, or ChromaDB, see their official docs.

## License
MIT License. See LICENSE file for details.
