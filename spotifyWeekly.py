import spotipy
from spotipy.oauth2 import SpotifyOAuth

from flask import Flask, request, url_for, session, redirect

app = Flask(__name__)

app.config['SESSION_COOKIE_NAME'] = 'Spotify Cookie'
app.secret_key = 'xnxw83ijr921ed83513f'
TOKEN_INFO = 'token_info'

#Creating the home route
@app.route('/')
def login():
    auth_url = create_spotify_oauth().get_authorize_url()
    return redirect(auth_url)

# Redirect route
@app.route('/redirect')

# Save Discover weekly playlist route
@app.route('/saveDiscoverWeekly')



def create_spotify_oauth():
    return SpotifyOAuth( 
        client_id = "28a4021f82764dd480dc39ccc3b01bd6",
        client_secret = "2501136b78674124bc4199a75705a4da",
        redirect_uri = url_for('redirect'), _external = True,
        scope = 'user-library-read playlist-modify-public paylist-modify-private'
        )