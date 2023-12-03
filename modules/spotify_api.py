import os
import tekore as tk
import pandas as pd
from tqdm import tqdm

class SpotifyAPI:
    def __init__(self):
        self.token = self.__auth__()
        

    def __auth__(self):
        client_id  = os.environ.get('client_id')
        secret_key = os.environ.get('client_secret')
        token = tk.request_client_token(client_id, secret_key)
        return tk.Spotify(token)

    def get_music_recommandation(self):
        genres = self.token.recommendation_genre_seeds()

        data_dict = {
            "id":[], 
            "genre":[], 
            "track_name":[], 
            "artist_name":[],
            "valence":[],     # <-- this is our psychological value
            "energy":[]       # <-- this too 
        }
        
        
        # Get recommendation for each genre
        for genre in tqdm(genres):
            
            recs = self.token.recommendations(genres = [genre], limit = 100)
            recs = eval(recs.json().replace("null", "-999").replace("false", "False").replace("true", "True"))["tracks"]
            
            for track in recs:
                data_dict["id"].append(track["id"])
                data_dict["genre"].append(genre)
                track_meta = self.token.track(track["id"])
                data_dict["track_name"].append(track_meta.name)
                data_dict["artist_name"].append(track_meta.album.artists[0].name)
                track_features = self.token.track_audio_features(track["id"])
                data_dict["valence"].append(track_features.valence)
                data_dict["energy"].append(track_features.energy)



        # Store data in pandas dataframe
        df = pd.DataFrame(data_dict)

        # Drop duplicates
        df.drop_duplicates(subset = "id", keep = "first", inplace = True)
        df.to_csv("arousal_dataset.csv", index = False)