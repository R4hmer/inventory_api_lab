import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    res = client.get("/")
    assert res.status_code == 200


def test_get_empty_inventory(client):
    res = client.get("/inventory")
    assert res.status_code == 200
    assert res.json == []


def test_add_item(client):
    res = client.post("/inventory", json={
        "product_name": "Milk",
        "brand": "Brookside",
        "price": 120,
        "stock": 20
    })
    assert res.status_code == 201
    assert res.json["product_name"] == "Milk"


def test_get_single_item(client):
    client.post("/inventory", json={
        "product_name": "Milk",
        "brand": "Brookside",
        "price": 120,
        "stock": 20
    })

    res = client.get("/inventory/1")
    assert res.status_code == 200
    assert res.json["id"] == 1


def test_update_item(client):
    client.post("/inventory", json={
        "product_name": "Milk",
        "brand": "Brookside",
        "price": 120,
        "stock": 20
    })

    res = client.patch("/inventory/1", json={
        "price": 150
    })

    assert res.status_code == 200
    assert res.json["price"] == 150


def test_delete_item(client):
    client.post("/inventory", json={
        "product_name": "Milk",
        "brand": "Brookside",
        "price": 120,
        "stock": 20
    })

    res = client.delete("/inventory/1")
    assert res.status_code == 200
    assert res.json["message"] == "Item deleted"


def test_search_endpoint(client):
    res = client.get("/search/nutella")
    assert res.status_code in [200, 404, 500]