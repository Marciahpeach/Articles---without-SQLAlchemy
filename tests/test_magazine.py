# tests/test_magazine.py
import pytest
from lib.models.magazine import Magazine
from lib.db.seed import seed_database

@pytest.fixture
def setup_database():
    seed_database()
    yield

def test_magazine_creation(setup_database):
    magazine = Magazine("Test Magazine", "Test Category")
    assert magazine.name == "Test Magazine"
    assert magazine.category == "Test Category"
    assert magazine.id is not None

def test_magazine_articles(setup_database):
    magazine = Magazine.find_by_id(1)  # Tech Trends
    articles = magazine.articles()
    assert len(articles) == 2
    assert articles[0]['title'] in ["AI Revolution", "Quantum Computing"]

def test_magazine_contributors(setup_database):
    magazine = Magazine.find_by_id(2)  # Health Weekly
    contributors = magazine.contributors()
    assert len(contributors) == 2
    assert any(c['name'] == "John Smith" for c in contributors)

def test_magazine_article_titles(setup_database):
    magazine = Magazine.find_by_id(1)  # Tech Trends
    titles = magazine.article_titles()
    assert set(titles) == {"AI Revolution", "Quantum Computing"}