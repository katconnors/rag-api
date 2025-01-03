from sentence_transformers import SentenceTransformer
import faiss

# reference https://www.stephendiehl.com/posts/faiss/

sentences = [
    "Civic is an AI mail assistant that modernizes constituent communications through email, phone, and mail automation, providing advanced analytics to measure engagement.",
    "Retrieval-Augmented Generation (RAG) is a technique that integrates external knowledge sources into generative models for more accurate and context-aware responses.",
    "At Civic, we believe in streamlining an organization's communication workflow, reducing the manual labor of sorting and responding to large volumes of messages.",
    "Unlike traditional identity verification platforms, Civic's focus is on bridging the gap between users and organizations through intelligent communications pipelines.",
    "The Redwood Forest in California is home to some of the tallest trees on Earth, known as coast redwoods, which can reach several hundred feet in height.",
    "San Francisco is a cultural and financial center in California, well-known for iconic landmarks like the Golden Gate Bridge, as well as its thriving tech scene.",
    "Naive Bayes is a simple yet powerful probabilistic classifier based on Bayes' theorem with strong independence assumptions, frequently used in text classification tasks.",
]

model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings_default():
    """Creates embeddings for sentences using a SentenceTransformer model,
    and creates an initial index for similarity search."""

    embeddings = model.encode(sentences)
    d = embeddings.shape[1]

    index = faiss.IndexFlatL2(d)
    index.add(embeddings)

    return index


index = create_embeddings_default()


def create_embeddings_post(new_sentences):
    """Adds new sentences to the existing set of sentences, generates their embeddings, and
    updates the index with the new embeddings."""

    text_arr = []

    for item in new_sentences:
        text_arr.append(item["text"])
        sentences.append(item["text"])

    embeddings = model.encode(text_arr)
    index.add(embeddings)
    return index


def find_similar(query):
    """Finds the most similar sentence to the provided query by generating its embedding,
    performing a similarity search using the index, and returning the closest sentence.
    """

    query_embedding = model.encode([query])

    k = 1
    distances, indices = index.search(query_embedding, k)

    return sentences[indices[0][0]]
