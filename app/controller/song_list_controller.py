from flask import Blueprint, request
from app.service.song_list_service import get_cluster_list_json
song_list = Blueprint('song_list', __name__)


@song_list.route("/spotify_list/", methods=["POST"])
def cluster_from_uri():
    return get_cluster_list_json(request.json)
