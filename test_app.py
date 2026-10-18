from app import create_app


def test_health_returns_ok():
    client = create_app().test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_hello_returns_message():
    client = create_app().test_client()

    response = client.get("/hello")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello from Flask"}


def test_unknown_path_returns_404():
    client = create_app().test_client()
    assert client.get("/unknown").status_code == 404
