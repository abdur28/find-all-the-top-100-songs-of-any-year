from bs4 import BeautifulSoup
import requests

year = input("what year? ")
month = input("what month? ")
date = input("what date? ")
URL = f"https://www.billboard.com/charts/hot-100/{year}-{month}-{date}"


response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
song_names = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
song_list = [song.getText().strip("\n\t") for song in song_names]

with open(f"{year}-{month}-{date}_playlist.txt", "w") as text:
    for songs in song_list:
        index = song_list.index(songs)
        text.write(f"{index + 1}) {songs}\n")

