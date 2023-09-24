from starlette.testclient import TestClient

from main import app

client = TestClient(app)


# integrated test
def test_success():
    response = client.post(
        "/solution",
        json={
            "orders": [
                {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
                {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
                {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": "completed"},
                {"id": 4, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "canceled"}
            ],
            "criterion": "completed"
        }
    )
    assert response.status_code == 200
    assert response.json() == 1299.69


def test_error_negative():
    response = client.post(
        "/solution",
        json={
            "orders": [
                {"id": 1, "item": "Laptop", "quantity": -1, "price": -999.99, "status": "completed"}
            ],
            "criterion": "completed"
        }
    )

    expected_response = {
        "error": [
            {"quantity": "Input should be greater than or equal to 0"},
            {"price": "Input should be greater than or equal to 0"}
        ]
    }
    assert response.status_code == 422
    assert response.json() == expected_response


def test_error_invalid_status_criterion():
    response = client.post(
        "/solution",
        json={
            "orders": [
                {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "invalid_status"}
            ],
            "criterion": "invalid_status"
        }
    )

    expected_response = {
        "error": [
            {"status": "Input should be 'completed','pending' or 'canceled'"},
            {"criterion": "Input should be 'completed','pending' or 'canceled'"}
        ]
    }
    assert response.status_code == 422
    assert response.json() == expected_response
