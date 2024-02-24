import requests
from bs4 import BeautifulSoup

# URLを指定
URL = "https://www.livefans.jp/events/1643325"


def scraping_livefans(url):
    setlist = []
    # ページの内容を取得
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    artistName = soup.find("h4", class_="artistName2").text.strip()
    print(artistName)

    # 'div'タグで'class'が'setBlock nopscr'の要素を抽出
    parent_div = soup.find("div", class_="setBlock nopscr")

    # 親要素が見つかった場合、その子要素の中からクラスが'ttl'の要素を取得
    if parent_div:
        ttl_elements = parent_div.find_all(class_="ttl")
        for i, element in enumerate(ttl_elements, start=1):
            # elementの中からaタグのテキストを取得
            a_tag = element.find("a").text
            setlist.append(a_tag)
    else:
        raise Exception("指定した要素が見つかりませんでした。")

    return artistName, setlist


if __name__ == "__main__":
    setlist = scraping_livefans(URL)
    print(setlist)
