# tests/test_author.py
import pytest
from lib.models.author import Author
from lib.db.seed import seed_database

@pytest.fixture
def setup_database():
    seed_database()
    yield
    # Cleanup if needed

def test_author_creation(setup_database):
    author = Author("Test Author")
    assert author.name == "Test Author"
    assert author.id is not None

def test_author_find_by_id(setup_database):
    author = Author.find_by_id(1)
    assert author is not None
    assert author.name == "Jane Doe"

def test_author_articles(setup_database):
    author = Author.find_by_id(1)  # Jane Doe
    articles = author.articles()
    assert len(articles) == 2
    assert articles[0]['title'] in ["AI Revolution", "Quantum Computing"]

def test_author_magazines(setup_database):
    author = Author.find_by_id(1)  # Jane Doe
    magazines = author.magazines()
    assert len(magazines) == 1
    assert magazines[0]['name'] == "Tech Trends"

def test_author_topic_areas(setup_database):
    author = Author.find_by_id(1)  # Jane Doe
    topics = author.topic_areas()
    assert "Technology" in topics