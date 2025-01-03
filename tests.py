import unittest
import rag_api as rag


class RagFunctionTestCase(unittest.TestCase):

    def test_rag_find(self):
    
        query = "Trees are cool."
        expected = "The Redwood Forest in California is home to some of the tallest trees on Earth, known as coast redwoods, which can reach several hundred feet in height."

        result = rag.find_similar(query)

        self.assertEqual(result, expected)

    def test_rag_update(self):
        json = [
            {"id": 1, "text": "This is a test sentence."},
            {"id": 2, "text": "Filler text."},
        ]

        query = "Testing query."
        expected = "This is a test sentence."

        rag.create_embeddings_post(json)
        result = rag.find_similar(query)

        self.assertEqual(result, expected)


if __name__ == "__main__":
    # run tests if called

    unittest.main()
