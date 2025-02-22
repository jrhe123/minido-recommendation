from flask import Flask, jsonify, request

from recall.context import Context
from recall.service import recall_service

app = Flask("recall-service")


@app.route("/")
def get_anime():
    """
    RECOMMEND results
    """
    user_id = request.args.get("user_id", type=int)
    print(f"Calling user {user_id}...")

    context = Context(user_id=user_id)
    res = recall_service.anime_recall(context)
    return jsonify(res)


@app.route("/sim")
def get_sim_anime():
    """
    SIMILARITY results
    """
    anime_id = request.args.get("anime_id", type=int)
    if anime_id is None:
        return "bad anime id", 400

    context = Context(anime_id=anime_id)
    res = recall_service.similar_animes(context)
    return jsonify(res)
