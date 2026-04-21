from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

inventory = []

@app.route("/")
def home():
    return jsonify({"message": "Inventory API is running"})


@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory)


@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item)
    return jsonify({"error": "Item not found"}), 404


@app.route("/inventory", methods=["POST"])
def add_item():
    data = request.get_json()

    new_item = {
        "id": len(inventory) + 1,
        "product_name": data.get("product_name"),
        "brand": data.get("brand"),
        "price": data.get("price"),
        "stock": data.get("stock")
    }

    inventory.append(new_item)
    return jsonify(new_item), 201


@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_item(item_id):
    data = request.get_json()

    for item in inventory:
        if item["id"] == item_id:
            item["product_name"] = data.get("product_name", item["product_name"])
            item["brand"] = data.get("brand", item["brand"])
            item["price"] = data.get("price", item["price"])
            item["stock"] = data.get("stock", item["stock"])
            return jsonify(item)

    return jsonify({"error": "Item not found"}), 404


@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            return jsonify({"message": "Item deleted"})

    return jsonify({"error": "Item not found"}), 404


@app.route("/search/<product_name>", methods=["GET"])
def search_product(product_name):
    url = "https://world.openfoodfacts.org/cgi/search.pl"

    params = {
        "search_terms": product_name,
        "search_simple": 1,
        "action": "process",
        "json": 1
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (InventoryApp/1.0)"
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)

        if response.status_code != 200:
            return jsonify({
                "error": "API request failed",
                "status_code": response.status_code,
                "response_text": response.text[:200]
            }), 500

        data = response.json()

        products = data.get("products", [])

        if not products:
            return jsonify({"message": "No product found"}), 404

        product = products[0]

        return jsonify({
            "product_name": product.get("product_name"),
            "brand": product.get("brands"),
            "ingredients": product.get("ingredients_text")
        })

    except Exception as e:
        return jsonify({
            "error": "Request failed",
            "details": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)