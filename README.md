# py-playground

Playing around with LLMs and Python.

## gpt4all example

1. Go to `gpt4all` folder, create a virtual env and install requirements.
2. Download an LLM model and update `llm_path` in `main.py`
3. Run `./main.py`

Example conversation:

```
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
```


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
