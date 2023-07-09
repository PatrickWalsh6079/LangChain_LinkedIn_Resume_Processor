
from langchain import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

# load the indexed data
embeddings = OpenAIEmbeddings()
new_db = FAISS.load_local("indexes", embeddings)

# search documents with semantic search
query = "What are Patrick's skills?"
docs = new_db.similarity_search(query, k=2)

# call model to return query
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
chain = load_qa_chain(llm=llm, chain_type="stuff")
run = chain.run(input_documents=docs, question=query)

print(run)

