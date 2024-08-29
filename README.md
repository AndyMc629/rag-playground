# rag-playground
Playing with RAG.

We will build this solution in two ways:

1. First we will install the postgres database in the same container as the main application logic, this is simpler and easier to get going with. This will be useful for the tutorial to focus more on embeddings, chunking and LLM querying techniques.
2. Secondly, we will run the postgres container seperately and connect to it via exposed ports. This has more steps but is a more robust 

## Postgres
Good tutorial for a seperate docker container running postgres.

- https://scriptable.com/postgresql/how-to-install-pgvector-postgresql-mac-docker/

Resources:

- https://docs.llamaindex.ai/en/stable/examples/low_level/oss_ingestion_retrieval/
- https://medium.com/@johannes.ocean/setting-up-a-postgres-database-with-the-pgvector-extension-10ab7ff212cc
- https://github.com/pamelafox/pgvector-playground/blob/main/.devcontainer/Dockerfile
- https://medium.com/rahasak/build-rag-application-using-a-llm-running-on-local-computer-with-ollama-and-langchain-e6513853fda0

