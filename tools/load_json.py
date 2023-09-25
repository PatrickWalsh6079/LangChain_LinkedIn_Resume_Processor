import os
import pandas as pd
from langchain import FAISS
from langchain.document_loaders import TextLoader, DataFrameLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter, SpacyTextSplitter
from dotenv import load_dotenv

load_dotenv()


def embed_data():
    path = './data/'
    dir_list = os.listdir(path)

    print(dir_list)
    docs = []
    for doc in dir_list:
        with open('./data/' + doc, 'rb') as f:
            document = f.read()
            # use spaCy text splitter
            text_splitter = SpacyTextSplitter(chunk_size=300)
            texts = text_splitter.split_text(document.decode('utf-8'))
            df = pd.DataFrame({'doc': texts})
            print(len(df))
            # print(df)

            # Load dataframe into loader
            # loader = DataFrameLoader(df, page_content_column='doc')
            loader = TextLoader(f"./data/{doc}")
            docs.append(loader.load())

    all_docs = [doc for sublist in docs for doc in sublist]
    # print(all_docs)
    # embed data
    embeddings = OpenAIEmbeddings()
    fs = FAISS.from_documents(all_docs, embeddings)
    fs.save_local('./indexes')

    # transform data
    # loader = TextLoader(f"./data/{profile}.json")
    # data = loader.load()
    #
    # text_splitter = CharacterTextSplitter(
    #     separator=":",
    #     chunk_size=300,
    #     chunk_overlap=30,
    #     length_function=len,
    # )
    #
    # texts = text_splitter.create_documents([data[0].page_content])
    # # print(texts)
    #
    # # embed data
    # embeddings = OpenAIEmbeddings()
    # # print(embeddings)
    #
    # # vector store
    # db = FAISS.from_documents(texts, embeddings)
    # db.save_local('./indexes')

# embed_data('patrickwalsh6079')

