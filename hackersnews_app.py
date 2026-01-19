import requests
import time

# Top　Stories（Up to 500） 最後に.jsonをつけないと取得できない。
response_top = requests.get("https://hacker-news.firebaseio.com//v0/topstories.json")

# Top　StoriesのIDをリスト形式にする
topstory_id_list = response_top.text.replace("[", "").replace("]", "").split(",")

# ID毎にタイトルとリンクを取得し出力する。（３０件）
for id in topstory_id_list[:30]:
    response_item = requests.get(f"https://hacker-news.firebaseio.com//v0/item/{id}.json").json()
    item_title = response_item["title"]
    item_link = response_item["url"]
    if len(item_link) != 0:
        print(f'{{"title": "{item_title}", "link": "{item_link}"}}')
    else:
        print(f'{{"title": "{item_title}", "link": "None"}}')
    time.sleep(1)

# 出力例
# {"title": "PYX: The next step in Python packaging", "link": "https://astral.sh/pyx"}
# {
#     "title": "Nginx introduces native support for ACME protocol",
#     "link": "https://blog.nginx.org/blog/native-support-for-acme-protocol",
# }
# {
#     "title": "FFmpeg 8.0 adds Whisper support",
#     "link": "https://code.ffmpeg.org/FFmpeg/FFmpeg/commit/13ce36fef98a3f4e6d8360c24d6b8434cbb8869b",
# }
# {"title": "OCaml as my primary language", "link": "https://xvw.lol/en/articles/why-ocaml.html"}
# {"title": "Pebble Time 2* Design Reveal", "link": "https://ericmigi.com/blog/pebble-time-2-design-reveal/"}
