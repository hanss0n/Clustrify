# Clustrify

Clustrify allows Spotify users to group their playlists into clusters depending on the euclidian distance of the attributes of the songs. This allows for an easier way of identifying which tracks in a playlist may suit your taste, without the need for spending countless hours listening through every song manually. It does this via the use of the [Spotify Web API](https://developer.spotify.com/documentation/web-api/).


# How to use it
1.  Copy a spotify playlist url/uri, for instance: `https://open.spotify.com/playlist/1VAN3ouvQGhuGkgDdldSoi?si=oFsRrXV4T8avGKvKp9bInQ`

2. Paste the link into the Spotify list URI/URL field at the top

3. Press the Clustrify! button and wait for a few seconds

4. Profit!

![Example](https://i.imgur.com/SRGK9Up.png)

## Getting Started - Backend

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

In order to run this application, you will need python3 installed, as well as the following libraries:
* Flask - [installation link](https://pypi.org/project/Flask/)
* Flask_cors - [installation link](https://pypi.org/project/Flask-Cors/1.10.3/)
* Spotipy - [installation link](https://pypi.org/project/spotipy/)
* Scikit-learn - [installation link](https://pypi.org/project/scikit-learn/)
* Numpy - [installation link](https://pypi.org/project/numpy/)
* Pandas - [installation link](https://pypi.org/project/pandas/)

All of these can be installed via the package installer pip.

### Installing

#### Spotipy

In order for the requests to the Spotify API to be valid, you also need to set up an account on their developer website. You have to create a Spotify application, with a Spotify Client ID, as well as a Spotify Client Secret. Instructions for this can be found on this [link](https://developer.spotify.com/dashboard/). 

We use the Spotipy library to access the API, for which you will need to add both of these keys to your environment:
```
export SPOTIPY_CLIENT_ID=client_id_here
export SPOTIPY_CLIENT_SECRET=client_secret_here

// on Windows, use `SET` instead of `export`
```
**Note that it is SpotiPy with a P, not the regular F**

#### Setup `$PYTHONPATH`
We also have to setup the `PYTHONPATH` by adding the Clustrify directory to it: 
```
export PYTHONPATH=${PYTHONPATH}:${PWD}
```

## Getting Started - Frontend

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

In order to run this application, you will need to have `nodejs`, along with its package manager `npm`, installed.

### Installing
Make your way into the `web` folder and proceed with the following commands.

Install all the dependencies:
```
npm install
```

## Deployment

### Backend
Deploy the backend:
```
python3 clustrify/app/run.py
```
**Note that this should be ran in the top, Clustrify directory**


#### Demo
So, now that the Clustrify backend is up and running, let's make sure that it is working. In the file ``song_list_controller.py``, you can find all the endpoints that are defined. For simplicty's sake, let's do this via the use of `Postman`, an application that let's you make HTTP requests easily. 

Pick the `POST` option, and supply the adress for the backend. Both the IP-adress and port should have been made available to you in the terminal when you started up the application. Then click the `Body` header, followed by `text` (depending on version, it might be `raw`), and finally, choose `JSON`. In the textbox appearing below, enter:
```
{
    "list_uri": "playlist_uri",
    "num_clusters" : "5",
    "attributes": ["acousticness", "danceability", "energy", "instrumentalness", "speechiness"]
}
```

To get the ``playlist_uri``, you can open up `Spotify`, rightclick on a playlist, choose `Share` and finally `Copy Spotify URI`. It should take a form similar to `spotify:playlist:59ZbFPES4DQwEjBpWHzrtC`. 

If all of this is done correctly, you will receive a JSON response containing information of all the trakcs in the choosen playlist, as well as some information detailing which cluster it belongs to. 

### Frontend
Deploy the frontend:
```
npm run serve
```
**Note that this should be ran in the `web` directory**

#### Demo
Deploying the frontend will give you a url where you can view the application. Open you browser and open it up. On this page you will be able to try out the Clustrify application! Open up Spotify, and find one of your playlists. Rightclick it, choose `Share` followed by `Copy Spotify URI`. Paste the URI into the text field, and the press `Clustrify!`.

## Built With

* [Vue.js](https://vuejs.org/) - The web framework used
* [Amchart 4](https://www.amcharts.com/docs/v4/) - The library used to visualize the clusters
* [Axios](https://github.com/axios/axios) - The HTTP client used for handling API requests

## Authors

* **Björn Hansson** - [hanss0n](https://github.com/hanss0n)
* **Felix Luthman** - [felixlut](https://github.com/felixlut/)
