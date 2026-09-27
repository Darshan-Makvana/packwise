import os
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

# In-memory list of packing items: {"id", "name", "category", "packed"}
items = []
next_id = 1

COMMIT = os.getenv("RENDER_GIT_COMMIT", "local")[:7]


@app.route("/")
def home():
    packed_count = sum(1 for i in items if i["packed"])
    return render_template(
        "index.html",
        items=items,
        total=len(items),
        packed_count=packed_count,
        commit=COMMIT,
    )


@app.route("/add", methods=["POST"])
def add():
    global next_id
    name = request.form.get("name", "").strip()
    category = request.form.get("category", "General").strip() or "General"

    if not name:
        return "Item name is required", 400

    items.append({"id": next_id, "name": name, "category": category, "packed": False})
    next_id += 1
    return redirect("/")


@app.route("/toggle/<int:item_id>", methods=["POST"])
def toggle(item_id):
    for i in items:
        if i["id"] == item_id:
            i["packed"] = not i["packed"]
            return redirect("/")
    return "Item not found", 404


@app.route("/delete/<int:item_id>", methods=["POST"])
def delete(item_id):
    global items
    before = len(items)
    items = [i for i in items if i["id"] != item_id]
    if len(items) == before:
        return "Item not found", 404
    return redirect("/")


@app.route("/api/items")
def api_items():
    return jsonify(items)


@app.route("/health")
def health():
    return {"status": "ok", "commit": COMMIT}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
