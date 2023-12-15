from modules import SpotifyAPI 

class PlaylistManager:
    def __init__(self):
        self.spotify_api = SpotifyAPI()

    def init(self):
        self.spotify_api.get_music_recommandation()

    def create_playlist(self, name, description=''):
        if self.__check_initialisation():
            print(f'Create playlist with name: {name}')
        

    def update_playlist(self, name):
        if self.__check_initialisation():
            print(f'Update playlist {name}')

    def add_to_playlist(self, name):
        if self.__check_initialisation():
            print(f'Add songs to playlist {name}')

    def remove_playlist(self, name):
        if self.__check_initialisation():
            print(f'Remove playlist {name}')

            

    def __check_initialisation(self):
        print("Initialisation need to be firstly executed...")
        return False
    