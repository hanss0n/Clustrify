from flask import Flask
from flask_cors import CORS
from app.controller.song_list_controller import song_list

app = Flask(__name__)
CORS(app)
app.register_blueprint(song_list)

if __name__ == '__main__':
    app.run()
