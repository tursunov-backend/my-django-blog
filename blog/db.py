import json

DEMO_DB_PATH = "db.json"


class Database:
    def __init__(self, path=DEMO_DB_PATH):
        self.path = path
        self.data = self.load()

    def read(self):
        with open(self.path, "r") as f:
            return json.load(f)

    def write(self, data):
        with open(self.path, "w") as f:
            json.dump(data, f)
    
    def get_articles(self):
        return self.data.get("articles", [])
    
    def get_latest_articles(self, count=3):
        articles = self.get_articles()
        return articles[:count]
    
    def get_articles_by_slug(self, slug):
        articles = self.get_articles()
        for article in articles:
            if article.get("slug") == slug:
                return article
        return None
    