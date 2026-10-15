# Main entry for testing  our api

from app.main import app


def test_health():
    r = app.test_client().get("health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_pay_increments_metric():
    c = app.test_client()
    assert c.post("/pay").status_code == 201
    assert "app_payments_total 1" in c.get("/metrics").get_data(as_text=True)
