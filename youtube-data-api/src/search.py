import os
from dotenv import load_dotenv

from googleapiclient.discovery import build

import scraping_livefans

# .envファイルのパスを指定して読み込む
dotenv_path = os.path.join(os.path.dirname(__file__), "../.env")
load_dotenv(dotenv_path)

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
YOUTUBE_API_KEY = os.getenv("YOUTUBE_DATA_API_KEY")

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_API_KEY)


def youtube_search(youtube, word):
    response = (
        youtube.search()
        .list(part="snippet", q=word, type="video", videoCategoryId="10")  # videoCategoryIdもstr型
        .execute()
    )
    print(type(response))  # <class 'dict'>
    # 検索結果のうち、最初の１件のタイトルと動画IDを返却
    for item in response.get("items", []):
        return item["snippet"]["title"], item["id"]["videoId"]

if __name__ == "__main__":
    URL = "https://www.livefans.jp/events/1643325"
    artistName, setlist = scraping_livefans.scraping_livefans(URL)
    print(artistName, setlist)

    for song in setlist:
        print(artistName, song)
        search_word = artistName + " " + song
        video_title, videoId = youtube_search(youtube, search_word)
        print(video_title, videoId)
