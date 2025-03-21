#!/usr/bin/env python3

from langchain.llms import GPT4All
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings import HuggingFaceEmbeddings

from config import *

def init_conversation():
    # load index
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma(persist_directory=INDEX_PERSIST_DIRECTORY,embedding_function=embeddings)

    # create conversation
    llm = GPT4All(
        model=LLM_PATH,
        verbose=False,
    )
    return ConversationalRetrievalChain.from_llm(
        llm,
        retriever=vectordb.as_retriever(),
        return_source_documents=True,
        verbose=False,
    )


if __name__ == '__main__':
    conversation = init_conversation()

    try:
        while True:
            question = input("Enter your question: ")
            print("Generating answer...")
            chat_history = []
            response = conversation({"question": question, "chat_history": chat_history})
            print(response['answer'])
    except KeyboardInterrupt:
        print("\nGood bye!")
