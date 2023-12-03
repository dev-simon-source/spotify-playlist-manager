from modules import SpotifyAPI 

class PlaylistManager:
    def __init__(self):
        self.spotify_api = SpotifyAPI()

    def create_playlist(self, name, description=''):
        print(f'Create playlist with name: {name}')
        self.spotify_api.get_music_recommandation()

    def update_playlist(self, name):
        print(f'Update playlist {name}')

    def add_to_playlist(self, name):
        print(f'Add songs to playlist {name}')

    def remove_playlist(self, name):
        print(f'Remove playlist {name}')

    