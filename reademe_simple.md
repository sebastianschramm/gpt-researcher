# How to run it

Perform the following steps to get the gpt research interface running:

## Install ollama and load mistral:v0.2 model

Installation instructions: https://ollama.com/download

To download the model once ollama is installed:

```bash
ollama pull mistral:v0.2
```

## Install dependencies

With poetry install or using "ppip install -r requirements.txt".

## Start server

```bash
python -m uvicorn main:app
```

Go to http://localhost:8000 and start asking questions
