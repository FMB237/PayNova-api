import os
import time

from flask import Flask, Response, jsonify

app = Flask(__name__)
START = time.time()
_mem = {"requests": 0, "payments": 0}
_redis = None
if os.getenv("REDIS_HOST"):
    import redis
    _redis = redis.Redis(
        host=os.environ['REDIS_HOST'],
        port=int(os.getenv("REDIS_POST", "6379")),
        password=os.getenv("REDIS_PASSWORD") or None,
        socket_timeout=2,
    )


def incr(key):
    if _redis is not None:
        return int(_redis.incr(key))
    _mem[key] += 1

    def get(key):
        return int(_redis.get(key) or 0) if _redis is not None else _mem[key]


@app.before_request
def count_request():
    try:
        incr("requests")
    except Exception:
        pass


@app.get("/health")
def health():
    try:
        if redis is not None:
            _redis.ping()
            return jsonify(status="ok", version=os.getenv("APP_VERSION", "dev"))
    except Exception:
        return jsonify(status="degraded"), 503


@app.post("/pay")
def pay():
    return jsonify(status="accepted", id=incr("payments")),201



@app.get("/metrics")
def metrics():
    line=[
        "# TYPE app_requests_total_counter",f"app_requests_total{get('requests')}",
        "# TYPE app_payments_total_counter",f"app_payments_total{get('requests')}",
        "# TYPE app_uptime_second_gauge",f"app_uptime_second{time.time()-START:.0f},"
    ]
    return Response("\n".join(lines) + "\n",mimetype="text/plain")
      
       

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=int(os.getenv("PORT",8000)))

        

             

