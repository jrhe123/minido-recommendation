from flask import Flask, jsonify, request

from rank.context import Context
from rank.service import rank_service

app = Flask("rank-service")


@app.route("/")
def get_anime():
    user_id = request.args.get("user_id", type=int)
    context = Context(user_id=user_id)

    animes = rank_service.anime_rank(context)
    print(f"Got {len(animes)} rank items")

    return jsonify(animes)
