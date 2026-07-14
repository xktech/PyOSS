import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from colorama import init, Fore, Style
from dotenv import load_dotenv

import core.config as config
from core.utils import new_window

un = config.username
load_dotenv()

def music():
    new_window(un)
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")

    print("ID:", CLIENT_ID)
    print("SECRET:", CLIENT_SECRET[:6] + "...")
    

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://127.0.0.1:8888/callback",
        scope="user-read-playback-state,user-modify-playback-state"
    ))

    def spotifySearch():
        song = input("Song name: ")

        results = sp.search(q=song, limit=5, type='track')

        print("\nResults:\n")

        for i, track in enumerate(results['tracks']['items'], start=1):
            name = track['name']
            artist = track['artists'][0]['name']

            print(f"{i}. {name} - {artist}")

    def playSong(song_name):

        results = sp.search(q=song_name, limit=1, type='track')

        tracks = results['tracks']['items']

        if not tracks:
            print("Song not found.")
            return

        track = tracks[0]
        uri = track['uri']

        devices = sp.devices()

        if not devices['devices']:
            print("No active Spotify device found. Please open spotify.")
            return

        device_id = devices['devices'][0]['id']

        sp.start_playback(device_id=device_id, uris=[uri])

        print(f"Now playing: {track['name']}")

    def get_active_device_id():
        devices = sp.devices()

        if not devices['devices']:
            return None

        for d in devices['devices']:
            if d['is_active']:
                return d['id']

        # nothing marked active — fall back to first device
        return devices['devices'][0]['id']

    while True:
        print("\n=== Spotify ===")
        print("1. Search for a song")
        print("2. Play a song")
        print("3. Pause")
        print("4. Resume")
        print("5. Skip")
        print("6. Exit")

        choice = input(">>> ")

        if choice == "1":
            spotifySearch()

        elif choice == "2":
            song_choice = input("Enter a song name: ")
            playSong(song_choice)

        elif choice == "3":
            device_id = get_active_device_id()
            if device_id is None:
                print("No active Spotify device found. Please open Spotify.")
            else:
                sp.pause_playback(device_id=device_id)
                print("Paused.")

        elif choice == "4":
            device_id = get_active_device_id()
            if device_id is None:
                print("No active Spotify device found. Please open Spotify.")
            else:
                sp.start_playback(device_id=device_id)
                print("Resumed.")

        elif choice == "5":
            sp.next_track()
            print("Skipped.")

        elif choice == "6":
            break