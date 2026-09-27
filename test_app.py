from app import app, items


def client():
    app.config["TESTING"] = True
    items.clear()
    return app.test_client()

def test_health():
    res = client().get("/health")
    assert res.status_code == 200
    assert res.json["status"] == "ok"


def test_add_item_and_list():
    c = client()
    c.post("/add", data={"name": "Passport", "category": "Travel"})
    res = c.get("/api/items")
    assert len(res.json) == 1
    assert res.json[0]["name"] == "Passport"
    assert res.json[0]["packed"] is False


def test_toggle_marks_item_packed():
    c = client()
    c.post("/add", data={"name": "Charger", "category": "Electronics"})
    item_id = c.get("/api/items").json[0]["id"]
    c.post(f"/toggle/{item_id}")
    res = c.get("/api/items")
    assert res.json[0]["packed"] is True


def test_add_without_name_rejected():
    res = client().post("/add", data={"category": "Travel"})
    assert res.status_code == 400


def test_delete_item():
    c = client()
    c.post("/add", data={"name": "Shoes", "category": "Clothing"})
    item_id = c.get("/api/items").json[0]["id"]
    c.post(f"/delete/{item_id}")
    res = c.get("/api/items")
    assert len(res.json) == 0
