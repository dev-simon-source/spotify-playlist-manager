import os
import tekore as tk
import pandas as pd
from tqdm import tqdm, trange
import time

from custom_types import SpotifySong

DATABASE_NAME = 'results/arousal_dataset.csv'

class SpotifyAPI:
    def __init__(self):
        self.token = self.__auth__()
        

    def __auth__(self):
        client_id  = os.environ.get('client_id')
        secret_key = os.environ.get('client_secret')
        token = tk.request_client_token(client_id, secret_key)
        return tk.Spotify(token)

    def get_music_recommandation(self,retries=3):
        self.__set_song_database()
        
        self.spotify_songs = []

        try:
            genres = self.token.recommendation_genre_seeds()

            # Get recommendation for each genre
            t = trange(len(genres), desc="Processing")

            for idx, genre in enumerate(genres, start=1):
                t.set_description(f"Processing {genre}")
                self.__get_songs_for_genre(genre)
                t.update(1)

            t.close()

        except Exception as e:
            print(f"Error getting recommendations: {e}")
            if retries > 0:
                print(f"Retrying in 30 seconds... ({retries} retries left)")
                time.sleep(30)
                return self.get_music_recommandation(retries=retries-1)
            else:
                print("Max retries reached. Unable to fetch song data.")
        finally:
            self.__safe_result(self.spotify_songs)


    def __check_song_exists(self, track_id):
        # Check if the track ID is already in the set
        if track_id in self.unique_ids:
            return True
        else:
            self.unique_ids.add(track_id)
            return False

    def __set_song_database(self):
        try:
            self.existing_df = pd.read_csv(DATABASE_NAME)
            self.unique_ids = set(self.existing_df["id"].tolist())
        except FileNotFoundError:
            self.existing_df = pd.DataFrame()
            self.unique_ids = set()

    def __get_song_data(self, track_id, retries=3):
        try:
            if not self.__check_song_exists(track_id):
                # print(f"Collecting data for song with ID: {track_id}")
                self.track_meta = self.token.track(track_id)
                self.track_features = self.token.track_audio_features(track_id)
                return True
            else:
                print("Track already exists in the database...")
        except Exception as e:
            print(e)
            if retries > 0:
                print(f"Retrying in 30 seconds... ({retries} retries left)")
                time.sleep(30)
                return self.__get_song_data(track_id, retries=retries-1)
            else:
                print("Max retries reached. Unable to fetch song data.")
        return False

    def __get_songs_for_genre(self, genre):
        recs = self.token.recommendations(genres=[genre], limit=10)
        recs = eval(recs.json().replace("null", "-999").replace("false", "False").replace("true", "True"))["tracks"]

        for track in recs:
            if self.__get_song_data(track["id"]):
                song = SpotifySong(id=track["id"], genre=genre, name=self.track_meta.name, artist_name=self.track_meta.album.artists[0].name, valence=self.track_features.valence, energy=self.track_features.energy)
                self.spotify_songs.append(song)
    
    def __safe_result(self, spotify_songs):
        songs_dict_list = [vars(song) for song in spotify_songs]

        # Convert the list of dictionaries to a Pandas DataFrame
        new_df = pd.DataFrame(songs_dict_list)

        # Concatenate new data with existing data
        combined_df = pd.concat([self.existing_df, new_df])

        # Drop duplicates
        combined_df.drop_duplicates(subset="id", keep="first", inplace=True)

        # Save to CSV
        combined_df.to_csv(DATABASE_NAME, index=False)