from flask import Flask, request
import rag_api as rag


app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome. Please make a documented POST or GET request."


@app.route("/ingest", methods=["POST"])
def ingest_text():

    sentences = request.get_json()
    embedded = rag.create_embeddings_post(sentences)

    return "Successfully ingested data."


@app.route("/query")
def get_similar_sentence():

    text = request.args.get("text")

    return rag.find_similar(text)


if __name__ == "__main__":

    app.run(debug=True)
