# Spotify_API_Automated_Playlist_PythonProject
This code is a Flask application that allows users to authenticate with their Spotify account and save their Discover Weekly playlist as a new playlist called "Saved Weekly".

Libraries Used
The following libraries are imported for this code:

1.os: For accessing environment variables.
2.time: For handling time-related operations.
3.spotipy: A lightweight Python library for the Spotify Web API.
4.SpotifyOAuth: For handling the Spotify authentication process.
5.Flask: A micro web framework for building the application.
6.request: For handling HTTP requests.
7.url_for: For generating URLs.
8.session: For storing user session data.
9.redirect: For redirecting users to different routes.


Application Setup

The Flask app is initialized.
The session cookie name is set to 'Spotify Cookie'.
A random secret key is set to sign the cookie.
The key for the token info in the session dictionary is defined as TOKEN_INFO.


ROUTES

1.Route: '/'
This route handles the initial login process.
The user is redirected to the Spotify authorization URL to grant access to the application.


2.Route: '/redirect'

This route handles the redirect URI after the user authorizes the application.
The session is cleared to start a new session.
The authorization code is obtained from the request parameters.
The authorization code is exchanged for an access token and refresh token using SpotifyOAuth.
The token info is saved in the session.
The user is redirected to the 'save_discover_weekly' route.


3.Route: '/saveDiscoverWeekly'

This route saves the Discover Weekly playlist as a new playlist called "Saved Weekly".
It first checks if the user is logged in by getting the token info from the session.
If the token info is not found, the user is redirected to the login route.
A Spotify instance is created using the access token.
The user ID is retrieved from the Spotify instance.
The user's playlists are fetched.
The Discover Weekly and Saved Weekly playlists are identified.
If the Discover Weekly playlist is not found, an error message is returned.
If the Saved Weekly playlist is not found, a new playlist with the name "Saved Weekly" is created.
The tracks from the Discover Weekly playlist are extracted.
The tracks are added to the Saved Weekly playlist using the Spotify API.
A success message is returned.


Function: get_token()

This function retrieves the token info from the session.
If the token info is not found, the user is redirected to the login route.
If the token is expired, it is refreshed using SpotifyOAuth.
The token info is returned.


Function: create_spotify_oauth()

This function creates a SpotifyOAuth instance with the necessary parameters for authentication.
Usage
Run the Flask application using app.run(debug=True).
Access the application in a web browser.
You will be redirected to the Spotify login page.
Log in with your Spotify account credentials.
After authorization, you will be redirected to the 'saveDiscoverWeekly' route.
The Discover Weekly playlist will be saved as a new playlist called "Saved Weekly".
You will see a success message.



Make sure to provide your Spotify Client ID and Client Secret as environment variables or update the code accordingly.

Note: This code is for educational purposes and should comply with Spotify's terms of service and policies.