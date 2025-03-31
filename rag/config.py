"""
Configuration settings for the RAG (Retrieval-Augmented Generation) system.

This module contains all configuration parameters used by the application,
including paths to models, data sources, and storage locations.
"""

import os
from pathlib import Path
from typing import Optional
import urllib.parse

# Model settings
# Path to the local LLM model file
LLM_PATH: str = os.environ.get(
    "RAG_LLM_PATH",
    "/Users/georgian/Library/Application Support/nomic.ai/GPT4All/Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf"
)

# Embedding model name used for vector embeddings
EMBEDDING_MODEL: str = os.environ.get(
    "RAG_EMBEDDING_MODEL",
    "all-MiniLM-L6-v2"
)

# Data source settings
# Directory containing PDF documents to be indexed
PDF_FOLDER: str = os.environ.get(
    "RAG_PDF_FOLDER",
    "/Users/georgian/projects/python/docs-pdf"
)

# URL to scrape for web content
TARGET_URL: str = os.environ.get(
    "RAG_TARGET_URL",
    "https://hotnews.ro/"
)

# Storage settings
# Directory where the vector database is stored
INDEX_PERSIST_DIRECTORY: str = os.environ.get(
    "RAG_INDEX_DIRECTORY",
    "./data/chromadb"
)

# Text splitting settings
# Size of text chunks for indexing
CHUNK_SIZE: int = int(os.environ.get("RAG_CHUNK_SIZE", "1000"))
# Overlap between chunks to maintain context
CHUNK_OVERLAP: int = int(os.environ.get("RAG_CHUNK_OVERLAP", "300"))

# Web scraping settings
# Maximum depth for recursive URL loading
MAX_DEPTH: int = int(os.environ.get("RAG_MAX_DEPTH", "1"))
# Timeout for web requests in seconds
REQUEST_TIMEOUT: int = int(os.environ.get("RAG_REQUEST_TIMEOUT", "600"))

# Validate configuration
def validate_config() -> list[str]:
    """Validate the configuration settings and return a list of any errors."""
    errors = []
    
    # Validate LLM_PATH
    if not os.path.isfile(LLM_PATH):
        errors.append(f"LLM model file not found at: {LLM_PATH}")
    
    # Validate PDF_FOLDER
    if not os.path.isdir(PDF_FOLDER):
        errors.append(f"PDF folder not found at: {PDF_FOLDER}")
    
    # Validate TARGET_URL
    try:
        result = urllib.parse.urlparse(TARGET_URL)
        if not all([result.scheme, result.netloc]):
            errors.append(f"Invalid URL format: {TARGET_URL}")
    except Exception as e:
        errors.append(f"Error parsing URL {TARGET_URL}: {str(e)}")
    
    # Ensure INDEX_PERSIST_DIRECTORY parent exists or can be created
    index_dir = Path(INDEX_PERSIST_DIRECTORY)
    if not index_dir.parent.exists():
        try:
            # Don't create it, just check if we can
            if not os.access(index_dir.parent.parent.absolute(), os.W_OK):
                errors.append(f"Cannot create index directory at: {INDEX_PERSIST_DIRECTORY}")
        except Exception as e:
            errors.append(f"Error checking index directory: {str(e)}")
    
    return errors

# Optional: Run validation when the module is imported
# Uncomment to enable automatic validation
# errors = validate_config()
# if errors:
#     print("Configuration errors:")
#     for error in errors:
#         print(f"  - {error}")
