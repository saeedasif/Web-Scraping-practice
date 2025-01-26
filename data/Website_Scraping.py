import requests

url = 'https://www.timesofpakistan.com/pakistan/in-connection-with-comments-made-against-state-institutions-bhc-suspends-imrans-arrest-warrants/'

def fetchAndSave(url, path):
    req = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(req.text)
        
fetchAndSave(url, "data/index.html")
