import unittest
from QuoteRepository import QuoteRepository 

class TestQuoteRepository(unittest.TestCase):
    def setUp(self):
        self.quotes = [
            {
                "Quote": "Don't cry because it's over, smile because it happened.",
                "Author": "Dr. Seuss",
                "Tags": [
                    "attributed-no-source",
                    "cry",
                    "crying",
                    "experience",
                    "happiness",
                    "joy",
                    "life",
                    "misattributed-dr-seuss",
                    "optimism",
                    "sadness",
                    "smile",
                    "smiling "
                ],
                "Popularity": 0.15566615566615566,
                "Category": "life"
            },
            {
                "Quote": "In three words I can sum up everything I've learned about life: it goes on.",
                "Author": "Robert Frost",
                "Tags": [
                    "life"
                ],
                "Popularity": 0.06127006127006127,
                "Category": "life"
            }
        ]
        self.repository = QuoteRepository(self.quotes)

    def test_search_by_category(self):
        category = "life"
        result = self.repository.search_by_category(category)
        expected = [
            {
                "Quote": "Don't cry because it's over, smile because it happened.",
                "Author": "Dr. Seuss",
                "Tags": [
                    "attributed-no-source",
                    "cry",
                    "crying",
                    "experience",
                    "happiness",
                    "joy",
                    "life",
                    "misattributed-dr-seuss",
                    "optimism",
                    "sadness",
                    "smile",
                    "smiling "
                ],
                "Popularity": 0.15566615566615566,
                "Category": "life"
            },
            {
                "Quote": "In three words I can sum up everything I've learned about life: it goes on.",
                "Author": "Robert Frost",
                "Tags": [
                    "life"
                ],
                "Popularity": 0.06127006127006127,
                "Category": "life"
            }
        ]
        self.assertEqual(result, expected)

    def test_search_by_author(self):
        author = "Dr. Seuss"
        result = self.repository.search_by_author(author)
        expected = [
            {
                "Quote": "Don't cry because it's over, smile because it happened.",
                "Author": "Dr. Seuss",
                "Tags": [
                    "attributed-no-source",
                    "cry",
                    "crying",
                    "experience",
                    "happiness",
                    "joy",
                    "life",
                    "misattributed-dr-seuss",
                    "optimism",
                    "sadness",
                    "smile",
                    "smiling "
                ],
                "Popularity": 0.15566615566615566,
                "Category": "life"
            }
        ]
        self.assertEqual(result, expected)

    def test_search_by_tag(self):
        tag = "life"
        result = self.repository.search_by_tag(tag)
        expected = [
            {
                "Quote": "Don't cry because it's over, smile because it happened.",
                "Author": "Dr. Seuss",
                "Tags": [
                    "attributed-no-source",
                    "cry",
                    "crying",
                    "experience",
                    "happiness",
                    "joy",
                    "life",
                    "misattributed-dr-seuss",
                    "optimism",
                    "sadness",
                    "smile",
                    "smiling "
                ],
                "Popularity": 0.15566615566615566,
                "Category": "life"
            },
            {
                "Quote": "In three words I can sum up everything I've learned about life: it goes on.",
                "Author": "Robert Frost",
                "Tags": [
                    "life"
                ],
                "Popularity": 0.06127006127006127,
                "Category": "life"
            }
        ]
        self.assertEqual(result, expected)

    def test_search_by_tags(self):
        tags = ["life", "happiness"]
        result = self.repository.search_by_tags(tags)
        expected = [
            {
                "Quote": "Don't cry because it's over, smile because it happened.",
                "Author": "Dr. Seuss",
                "Tags": [
                    "attributed-no-source",
                    "cry",
                    "crying",
                    "experience",
                    "happiness",
                    "joy",
                    "life",
                    "misattributed-dr-seuss",
                    "optimism",
                    "sadness",
                    "smile",
                    "smiling "
                ],  
                "Popularity": 0.15566615566615566,
                "Category": "life"
            }
        ]
        self.assertEqual(result, expected)

    def test_get_random_quote(self):
        result = self.repository.get_random_quote()
        self.assertIn(result, self.quotes)

if __name__ == '__main__':
    unittest.main()
