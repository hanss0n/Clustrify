from flask import Blueprint, request
from app.service.song_list_service import get_json_cluster_by_list_id
song_list = Blueprint('song_list', __name__)


@song_list.route("/spotify_list/<list_uri>", methods=["GET"])
def cluster_from_uri(list_uri):
    return get_json_cluster_by_list_id(list_uri)
