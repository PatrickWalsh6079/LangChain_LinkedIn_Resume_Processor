
from langchain import FAISS, PromptTemplate, LLMChain
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


def call_llm(query):
    # load the indexed data
    embeddings = OpenAIEmbeddings()
    new_db = FAISS.load_local("indexes", embeddings)

    # search documents with semantic search
    # query = "Where does Patrick Walsh work?"
    docs = new_db.similarity_search(query, k=2)

    # call model to return query
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    chain = load_qa_chain(llm=llm, chain_type="stuff")
    run = chain.run(input_documents=docs, question=query)

    print(run)
    return run


def interview_questions(input_profile):
    embeddings = OpenAIEmbeddings()
    new_db = FAISS.load_local("indexes", embeddings)

    # Perform semantic search to get relevant documents
    docs = new_db.similarity_search(input_profile, k=2)

    template = """
        You are a helpful AI assistant that reads LinkedIn profiles and generates interview questions for the candidate based on their profile.
        Generate 5-7 interview questions based on this LinkedIn profile: {profile}
        
        """

    prompt = PromptTemplate(template=template, input_variables=["profile"])

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.4)

    # Load the QA chain
    chain = load_qa_chain(llm=llm, prompt=prompt, chain_type="stuff")

    # Generate a response based on the search results and the query
    response = chain.run(input_documents=docs)
    print(response)

    return response
