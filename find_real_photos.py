import urllib.request
import urllib.parse
import json

def search(query, limit=5):
    params = {
        'action': 'query',
        'format': 'json',
        'generator': 'search',
        'gsrsearch': f'{query} filetype:bitmap',
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
                results.append({
                    'title': v.get('title'),
                    'url': info.get('url'),
                    'mime': info.get('mime'),
                    'width': info.get('width', 0),
                    'height': info.get('height', 0)
                })
    except Exception as e:
        print(f"Error searching {query}:", e)
    return results

queries = {
    "radome": "radome radar antenna",
    "cmm_inspection": "coordinate measuring machine CMM inspection",
    "composite_vacuum": "vacuum bagging composite resin",
    "composite_weave": "carbon fiber cloth weave",
    "fiberglass_mould": "fiberglass molding mold",
    "cnc_enclosure": "CNC machine enclosure industrial",
    "automotive_composite": "composite car body automotive panel",
    "cleanroom_aerospace": "cleanroom aerospace manufacturing assembly"
}

for key, q in queries.items():
    print(f"\n=== {key} ({q}) ===")
    res = search(q, limit=5)
    for r in res:
        print(f"{r['title']} | {r['width']}x{r['height']} | {r['url']}")
