from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Olá, DevOps!"

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
import os

import redis
from flask import Flask

app = Flask(__name__)
r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)
import os

import redis
from flask import Flask

app = Flask(__name__)
r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)

@app.get("/")
def home():
    return "Olá, DevOps!"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/visitas")
def visitas():
    return {"visitas": r.incr("visitas")}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
@app.get("/")
def home():
    return "Olá, DevOps!"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/visitas")
def visitas():
    return {"visitas": r.incr("visitas")}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
