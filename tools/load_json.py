
from langchain import FAISS
from langchain.document_loaders import JSONLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv
load_dotenv()

# transform data
loader = TextLoader("../data/patrickwalsh6079.json")
data = loader.load()

text_splitter = CharacterTextSplitter(
    separator=":",
    chunk_size=300,
    chunk_overlap=30,
    length_function=len,
)

texts = text_splitter.create_documents([data[0].page_content])
# print(texts)

# embed data
embeddings = OpenAIEmbeddings()
# print(embeddings)

# vector store
db = FAISS.from_documents(texts, embeddings)
db.save_local('../indexes')
