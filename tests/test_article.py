# tests/test_article.py
import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.seed import seed_database

@pytest.fixture
def setup_database():
    seed_database()
    yield

def test_article_creation(setup_database):
    author = Author.find_by_id(1)
    magazine = Magazine.find_by_id(1)
    article = Article("Test Article", author, magazine)
    assert article.title == "Test Article"
    assert article.author.name == "Jane Doe"
    assert article.magazine.name == "Tech Trends"
    assert article.id is not None

def test_article_find_by_id(setup_database):
    article = Article.find_by_id(1)
    assert article.title == "AI Revolution"
    assert article.author.name == "Jane Doe"
    assert article.magazine.name == "Tech Trends"