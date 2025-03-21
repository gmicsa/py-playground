# py-playground

Playing around with local LLMs and Python.

## RAG using gpt4all example. Chat with your local PDFs.

Example conversation:

1. Go to `rag` folder, create a virtual env and install requirements.
2. Download an LLM model and update `LLM_PATH` in `config.py`
3. Update `PDF_FOLDER` to your local folder where you have the PDF files
3. Run `./load.py`. This will read the PDF files and save them to the vector DB.
4. Run `chat.py`. For each question, context will be loaded from the vector DB and a query will be made to the local LLM. You can chat with your local PDFs.

`
Enter your question: Is Python good for students?
Generating answer...
 A: Yes, Python is a great language to introduce beginners to programming concepts such as loops and procedures. It also has a large standard library that allows students to work on realistic applications early in their course while learning the fundamentals of programming. The interactive interpreter enables students to test language features while they're programming, making it easier for them to learn and experiment with Python. Additionally, there are good IDEs available like IDLE which is written in Python using Tkinter.
`

## Plain gpt4all example. Chat with a local LLM.

1. Go to `gpt4all` folder, create a virtual env and install requirements.
2. Download an LLM model and update `llm_path` in `main.py`
3. Run `./main.py`

Example conversation:

`
Enter your question: Output a JSON with top 10 countries by population. Should include name and population attributes. I need only the JSON.
Generating response...
[
    {
        "name": "China",
        "population": 1439323776
    },
    {
        "name": "India",
        "population": 1380004385
    },
    {
        "name": "United States",
        "population": 331449281
    },
    {
        "name": "Indonesia",
        "population": 273523615
    },
    {
        "name": "Pakistan",
        "population": 216565806
    },
    {
        "name": "Brazil",
        "population": 212559417
    },
    {
        "name": "Nigeria",
        "population": 202915211
    },
    {
        "name": "Bangladesh",
        "population": 166291804
    },
    {
        "name": "Russia",
        "population": 145934027
    },
    {
        "name": "Japan",
        "population": 128421000
    }
]
`


## Utils 

### Setup Python virtual env

create new local env:
```
python3 -m venv localenv
```

activate local env:
```
source localenv/bin/activate
```

deactivate local env:
```
deactivate
```

check if using local env:
```
which python3
```

### Lib requirements

install all libs from file:
```
pip install -r requirements.txt
```

output current libs in file:
```
pip freeze > requirements.txt
```
