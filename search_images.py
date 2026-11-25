import urllib.request
import json
import urllib.parse

def search_commons(query, limit=10):
    params = {
        'action': 'query',
        'format': 'json',
        'generator': 'search',
        'gsrsearch': f'{query} filetype:bitmap',
        'gsrnamespace': '6',
        'gsrlimit': str(limit),
        'prop': 'imageinfo',
        'iiprop': 'url|mime|size|extmetadata'
    }
    url = f"https://commons.wikimedia.org/w/api.php?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    results = []
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for k, v in pages.items():
                info = v.get('imageinfo', [{}])[0]
                results.append({
                    'title': v.get('title'),
                    'url': info.get('url'),
                    'mime': info.get('mime'),
                    'width': info.get('width'),
                    'height': info.get('height')
                })
    except Exception as e:
        print("Error:", e)
    return results

queries = [
    "carbon fiber composite manufacturing",
    "fiberglass composite",
    "wind tunnel model aerospace",
    "flight simulator cockpit",
    "radome antenna composite",
    "industrial quality inspection CMM metrology",
    "composite vacuum bagging",
    "aerospace composite component"
]

for q in queries:
    print(f"\n=== Query: {q} ===")
    res = search_commons(q, limit=4)
    for r in res:
        print(f"Title: {r['title']} | Dim: {r.get('width')}x{r.get('height')} | URL: {r.get('url')}")
