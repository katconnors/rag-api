from flask import Flask, request
import rag_api as rag


app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome. Please make a post or get request."


@app.route("/ingest", methods=["POST"])
def ingest_text():

    # post method to ingest new text

    sentences = request.get_json()
    print(sentences)
    embedded = rag.create_embeddings_post(sentences)
    return "Successfully ingested data."


@app.route("/query")
def get_similar_sentence():

    # get method for user input and retrieving relevant sentence

    text = request.args.get("text")

    print(rag.index)

    return rag.find_similar(text)


if __name__ == "__main__":

    app.run(debug=True)
