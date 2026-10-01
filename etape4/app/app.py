# Compteur de visites : à chaque affichage, +1 dans Redis.
import os
import redis
from flask import Flask

app = Flask(__name__)
r = redis.Redis(host=os.environ.get("REDIS_HOST", "redis"), port=6379)
MESSAGE = os.environ.get("MESSAGE", "Bonjour")


@app.route("/")
def index():
    visites = r.incr("visites")
    return f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Compteur</title>
    <style>body{{font-family:system-ui,sans-serif;text-align:center;margin-top:5rem;color:#1e293b}}
    .n{{font-size:5rem;color:#4f46e5;font-weight:700}}</style></head>
    <body><h1>{MESSAGE}</h1><div class="n">{visites}</div><p>visite(s) enregistrée(s) dans Redis</p>
    <p><small>Rechargez la page pour incrémenter</small></p></body></html>"""
