from app import app

def test_home():
    resposta = app.test_client().get("/")
    assert resposta.status_code == 200
    assert "DevOps" in resposta.get_data(as_text=True)

def test_health():
    resposta = app.test_client().get("/health")
    assert resposta.get_json() == {"status": "ok"}
