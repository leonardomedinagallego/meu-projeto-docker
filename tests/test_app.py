import sys
import os

# Garante que o Python encontre o app.py na raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

# Cria o cliente de teste
client = app.test_client()


def test_home_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_home_response_content():
    response = client.get("/")
    assert "Aplicação DevOps com Docker funcionando" in response.get_data(as_text=True)


def test_home_response_not_empty():
    response = client.get("/")
    assert response.data != b""


def test_home_content_type():
    response = client.get("/")
    assert "text/html" in response.content_type


def test_route_exists():
    routes = [rule.rule for rule in app.url_map.iter_rules()]
    assert "/" in routes