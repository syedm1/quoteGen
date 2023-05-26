import random

import random 

class QuoteRepository:
    def __init__(self, quotes):
        self.quotes = quotes

    def search_by_category(self, category, limit=None):
        filtered_quotes = [quote for quote in self.quotes if quote.get('Category') == category]
        return self._paginate(filtered_quotes, limit)

    def search_by_author(self, author, limit=None):
        filtered_quotes = [quote for quote in self.quotes if quote.get('Author') == author]
        return self._paginate(filtered_quotes, limit)

    def search_by_tag(self, tag, limit=None):
        filtered_quotes = [quote for quote in self.quotes if tag in quote.get('Tags', [])]
        return self._paginate(filtered_quotes, limit)

    def search_by_tags(self, tags, limit=None):
        filtered_quotes = [quote for quote in self.quotes if all(tag in quote.get('Tags', []) for tag in tags)]
        return self._paginate(filtered_quotes, limit)

    def get_random_quote(self):
        return random.choice(self.quotes)

    def _paginate(self, quotes, limit=None):
        if limit is not None and limit > 0:
            return quotes[:limit]
        return quotes
