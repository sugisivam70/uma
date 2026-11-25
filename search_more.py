import urllib.request
import urllib.parse
import json

def search(query, limit=5):
    params = {
        'action': 'query',
        'format': 'json',
        'generator': 'search',
        'gsrsearch': f'{query}',
        'gsrnamespace': '6',
        'gsrlimit': str(limit),
        'prop': 'imageinfo',
        'iiprop': 'url|mime|size'
    }
    url = f"https://commons.wikimedia.org/w/api.php?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    results = []
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for k, v in pages.items():
                info = v.get('imageinfo', [{}])[0]
                mime = info.get('mime', '')
                if 'image' in mime and 'svg' not in mime and 'pdf' not in mime:
                    results.append({
                        'title': v.get('title'),
                        'url': info.get('url'),
                        'mime': mime,
                        'width': info.get('width', 0),
                        'height': info.get('height', 0)
                    })
    except Exception as e:
        print(f"Error {query}:", e)
    return results

more_queries = {
    "carbon_fiber_fabric": "carbon fiber fabric",
    "composite_autoclave": "composite autoclave",
    "carbon_fiber_hood": "carbon fiber bonnet car",
    "composite_panel": "carbon fiber sheet",
    "cleanroom": "cleanroom aerospace manufacturing"
}

for k, q in more_queries.items():
    print(f"\n--- {k} ({q}) ---")
    res = search(q, limit=5)
    for r in res[:3]:
        print(f"  {r['title']} | {r['width']}x{r['height']} | {r['url']}")
