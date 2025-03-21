#!/usr/bin/env python3

import os
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders.recursive_url_loader import RecursiveUrlLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from bs4 import BeautifulSoup as Soup
from langchain.utils.html import (PREFIXES_TO_IGNORE_REGEX,
                                  SUFFIXES_TO_IGNORE_REGEX)

from config import *

def init_index_url():
    # scrape data from web
    documents = RecursiveUrlLoader(
        TARGET_URL,
        max_depth=1,
        extractor=lambda x: Soup(x, "html.parser").text,
        prevent_outside=True,
        use_async=True,
        timeout=600,
        check_response_status=True,
        # drop trailing / to avoid duplicate pages.
        link_regex=(
            f"href=[\"']{PREFIXES_TO_IGNORE_REGEX}((?:{SUFFIXES_TO_IGNORE_REGEX}.)*?)"
            r"(?:[\#'\"]|\/[\#'\"])"
        ),
    ).load()

    print(f"creating the index with {len(documents)} documents")

    # split text
    # this chunk_size and chunk_overlap effects to the prompt size
    # execeed promt size causes error `prompt size exceeds the context window size and cannot be processed`
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=300)
    documents = text_splitter.split_documents(documents)

    # create embeddings with huggingface embedding model `all-MiniLM-L6-v2`
    # then persist the vector index on vector db
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=INDEX_PERSIST_DIRECTORY
    )
    vectordb.persist()
    print(f"Index successfully created and persisted at {INDEX_PERSIST_DIRECTORY}")

def init_index_pdfs():
     # Load all PDFs from the specified folder
    documents = []
    for file_name in os.listdir(PDF_FOLDER):
        if file_name.endswith(".pdf"):
            file_path = os.path.join(PDF_FOLDER, file_name)
            loader = PyPDFLoader(file_path)
            documents.extend(loader.load())
            print(file_path)

    print(f"Creating the index with {len(documents)} documents")

    # Split text into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=300)
    documents = text_splitter.split_documents(documents)

    # Create embeddings with the HuggingFace embedding model
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=INDEX_PERSIST_DIRECTORY
    )
    
    # Persist the vector database
    vectordb.persist()
    print(f"Index successfully created and persisted at {INDEX_PERSIST_DIRECTORY}")


if __name__ == '__main__':
    init_index_pdfs()
