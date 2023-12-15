from dataclasses import dataclass

@dataclass
class SpotifySong:
    id: str
    genre: str
    name: str
    artist_name: str
    valence: float
    energy: float