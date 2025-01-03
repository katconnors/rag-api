## rag-api

- This is a simple Python/Flask service that can ingest text, convert it into embeddings, and store the embeddings within memory.
- Given a query, a relevant sentence is then returned.

## Setup

- Create a virtual environment

```sh
virtualenv env
```

- Activate the virtual environment

```sh
source env/bin/activate
```

- Install the dependencies in requirements.txt

```sh
pip install -r requirements.txt
```

## Usage

- Run the server by using the following command:

```sh
python3 server.py
```

- In order to ingest data, make a POST request to http://127.0.0.1:5000/ingest using JSON format in the body

```sh
curl --location 'http://127.0.0.1:5000/ingest' \
--header 'Content-Type: application/json' \
--data '[
{
"id": 1,
"text": "This is a test sentence."
}
]'
```

- In order to find a similar sentence, make a GET request to http://127.0.0.1:5000/query using query param "text"

```sh
curl --location 'http://127.0.0.1:5000/query?text=test%20query'
```

## Unit Tests

Unit tests can be found in tests.py <br>
To run tests, use:

```sh
python3 tests.py
```
