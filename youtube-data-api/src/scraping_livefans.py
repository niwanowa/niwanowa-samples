import requests
from bs4 import BeautifulSoup

# URLを指定
url = "https://www.livefans.jp/events/1643325"

# ページの内容を取得
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 'div'タグで'class'が'setBlock nopscr'の要素を抽出
parent_div = soup.find("div", class_="setBlock nopscr")

# 親要素が見つかった場合、その子要素の中からクラスが'ttl'の要素を取得
if parent_div:
    ttl_elements = parent_div.find_all(class_="ttl")
    for i, element in enumerate(ttl_elements, start=1):
        print(f"{i}. {element.text.strip()}")
else:
    print("'setBlock nopscr'クラスを持つdiv要素が見つかりませんでした。")
