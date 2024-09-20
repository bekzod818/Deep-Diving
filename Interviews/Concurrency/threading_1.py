import urllib.request as ur
from concurrent.futures import ThreadPoolExecutor

datas = []


def get_from(url):
    print("Opening url: ", url)
    connection = ur.urlopen(url)
    data = connection.read()
    datas.append({"url": url, "data": data})


urls = [
    "https://python.org",
    "https://docs.python.org/",
    "https://wikipedia.org",
    "https://imdb.com",
]

with ThreadPoolExecutor() as ex:
    for url in urls:
        ex.submit(get_from, url)

# let's just look at the beginning of each data stream
# as this could be a lot of data
arr = [{"data": data["data"][:200], "url": data["url"]} for data in datas]
print(arr, len(arr))
