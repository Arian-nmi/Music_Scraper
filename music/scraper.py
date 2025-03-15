import requests
from bs4 import BeautifulSoup
from music.models import Song


URL = "https://www.ahangimo.com/new_music"

def scraper():
    response = requests.get(URL)
    print("✅ Request status:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")
    songs = soup.select("div.musicItemBox")
    print(f"🎵 Number of songs found: {len(songs)}")

    for song in songs:
        title = song.select_one("h4").text.strip()
        artist = song.select("h4")[1].text.strip() if len(song.select("h4")) > 1 else "uncertain artist"
        img_tag = song.select_one("img")
        cover_url = img_tag["data-src"] if img_tag and "data-src" in img_tag.attrs else img_tag["src"] if img_tag else None
        link = "https://www.ahangimo.com" + song.select_one("a")["href"] if song.select_one("a") else None

        Song.objects.create(
            title=title,
            artist=artist,
            cover_url=cover_url,
            link=link
        )
        print(f"✅ Saved: {title} - {artist}")

scraper()