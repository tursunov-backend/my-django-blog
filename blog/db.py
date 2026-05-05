import json

DEMO_DB_PATH = 'db.json'


class Database:
    def __init__(self, path=DEMO_DB_PATH):
        self.path = path

    def read(self):
        with open(self.path, 'r') as f:
            return json.load(f)

        with open(self.path, 'r') as f:
            return json.load(f)

    def write(self, data):
        with open(self.path, 'w') as f:
            json.dump(data, f, indent=4)

    def get_articles(self):
        return self.read().get('articles', [])
    
    def get_latest_articles(self, count=3):
        articles = self.get_articles()
        return articles[:count]

    def get_article_by_slug(self, slug):
        return next(
            (article for article in self.get_articles() if article.get('slug') == slug),
            None
        )

    def add_article(self, article):
        data = self.read()
        data.setdefault('articles', []).append(article)
        self.write(data)

    def find_articles_by_search(self, search: str):
        data = self.read()
        articles = []
        for article in data['articles']:
            if search in article.get('title', '').lower():
                articles.append(article)
        return articles