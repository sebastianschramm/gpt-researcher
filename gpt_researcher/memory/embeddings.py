from langchain.vectorstores import FAISS


class Memory:
    def __init__(self, embedding_provider, **kwargs):

        _embeddings = None
        match embedding_provider:
            case "ollama":
                from langchain.embeddings import OllamaEmbeddings
                _embeddings = OllamaEmbeddings(model="mistral:v0.2")
            case "openai":
                from langchain.embeddings import OpenAIEmbeddings
                _embeddings = OpenAIEmbeddings()
            case "huggingface":
                from langchain.embeddings import HuggingFaceBgeEmbeddings as HuggingFaceEmbeddings
                _embeddings = HuggingFaceEmbeddings()

            case _:
                raise Exception("Embedding provider not found.")

        self._embeddings = _embeddings

    def get_embeddings(self):
        return self._embeddings
