from flask import Flask, request, Response
from filters.filter_utils import sanitize_input, escape_output
import json

app = Flask(__name__)

# Загружаем фиктивные товары
with open("./data/fake_products.json", "r", encoding="utf-8") as f:
    all_products = json.load(f)


@app.route("/recommendations", methods=["GET"])
def get_recommendations():
    user_id = request.args.get("user_id", "")
    sanitized_user_id = sanitize_input(user_id)

    # Простая логика: просто возвращаем 3 первых товара
    recommended = all_products[:3]

    # Экранируем все названия товаров
    for item in recommended:
        item["name"] = escape_output(item["name"])
        item["description"] = escape_output(item["description"])

    response_data = {
        "user_id": sanitized_user_id,
        "recommendations": recommended
    }

    return Response(
        json.dumps(response_data, ensure_ascii=False),
        mimetype="application/json; charset=utf-8"
    )


@app.route("/")
def index():
    return "<h3>рекомендательная система онлайн магазина запущена.</h3>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)


# http://127.0.0.1:5050/recommendations?user_id=123
