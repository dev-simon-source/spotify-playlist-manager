import tekore as tk

def authorize():
    CLIENT_ID = 'ENTER YOUR CLIENT ID HERE'
    CLIENT_SECRET = 'ENTER YOUR CLIENT SECRET HERE'
    app_token = tk.request_client_token(CLIENT_ID, CLIENT_SECRET)
    return tk.Spotify(app_token)