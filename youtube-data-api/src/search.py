import os
from dotenv import load_dotenv

from googleapiclient.discovery import build

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
    for item in response.get("items", []):
        print(item["snippet"]["title"], item["id"]["videoId"])


search_word = "夜に駆ける"
youtube_search(youtube, search_word)
