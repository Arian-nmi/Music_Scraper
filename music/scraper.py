import requests
from bs4 import BeautifulSoup
from .models import Song

def fetch_latest_songs():
    url = 'https://hitseda.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    songs = []
    for item in soup.select('article.vip_posts'):
        title = item.select_one('h2').text.strip()
        link = item.select_one('a.vip_ulinks')['href']
        img = item.select_one('figure img')['src']
        category = item.select_one('p').text.strip()

        # Add to database
        song, created = Song.objects.get_or_create(
            title=title,
            defaults={
                      'link': link,
                      'img': img,
                      'category': category
                      }
        )
        if created:
            songs.append(song)
    return songs
