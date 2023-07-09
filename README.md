# LangChain_LinkedIn_Resume_Processor
This program scrapes a LinkedIn user's profile and saves it to a JSON file.

It then loads the JSON file, breaks it into chunks, vectorizes the data and stores
the vectorized data in a vector store, then uses a LLM to do Q&A over documents
using an OpenAI model.

Requires API keys for:
PROXYCURL_API_KEY
OPENAI_API_KEY
