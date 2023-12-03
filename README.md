# Spotify Playlist Manager
## Overview

Welcome to the Spotify Playlist Manager repository! This Python script allows you to efficiently manage your Spotify playlists and create new playlists based on specified music styles. Whether you want to organize your existing playlists or discover new music based on your mood, this tool has you covered.
## Features

- Playlist Management: Easily add, remove, and update songs in your existing Spotify playlists.
- Create Playlists by Style: Generate new playlists based on predefined music styles such as "happy," "energetic," or "chill."
- User-Friendly: Simple command-line interface for a seamless user experience.
- Spotify API Integration: Utilizes the Spotify API for smooth interaction with your Spotify account.

# Getting Started

To use this Spotify Playlist Manager, follow these steps:

1. Clone the Repository:

```bash
git clone https://github.com/your-username/spotify-playlist-manager.git
cd spotify-playlist-manager
```
2. Install Dependencies:

```bash
pip install -r requirements.txt
```
3. Set Up Spotify API:

Create a Spotify Developer account and register a new application to obtain API credentials.
Set the enviroment variables for the Spotify API client_id and client_secret.
```bash
    export client_id=your_client_id
    export client_secret=your_client_secret
```


4. Run the Script:

```bash
    python playlist_manager.py
```
## Usage

The _playlist_manager.py_ script provides a set of commands to manage your Spotify playlists:

    add: Add tracks to a specified playlist.
    remove: Remove tracks from a specified playlist.
    update: Update the details of a specified playlist.
    create: Create a new playlist based on a predefined music style.

Example:

```bash
python playlist_manager.py create sad
```
This will generate a new playlist with songs categorized as "sad."
## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit pull requests. Contributions and suggestions are always welcome!
License

This project is licensed under the MIT License - see the LICENSE file for details.
## Acknowledgments

Special thanks to the Spotify API for making it possible to interact with Spotify programmatically.

Happy listening! 🎶