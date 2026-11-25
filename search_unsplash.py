import urllib.request
import json
import re

def search_unsplash_source(term):
    # Unsplash search HTML scrape for direct photo URLs
    url = f"https://unsplash.com/napi/search/photos?query={urllib.parse.quote(term)}&per_page=10"
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    })
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            results = []
            for item in data.get('results', []):
                urls = item.get('urls', {})
                results.append({
                    'id': item.get('id'),
                    'alt': item.get('alt_description'),
                    'raw': urls.get('raw'),
                    'regular': urls.get('regular'),
                    'small': urls.get('small')
                })
            return results
    except Exception as e:
        print(f"Error fetching Unsplash for {term}:", e)
        return []

terms = [
    "carbon fiber texture",
    "aerospace engineering",
    "factory workshop industrial",
    "manufacturing machine",
    "quality control laboratory",
    "fiberglass"
]

for t in terms:
    res = search_unsplash_source(t)
    print(f"\n=== Unsplash: {t} (found {len(res)}) ===")
    for r in res[:3]:
        print(r['id'], "|", r['alt'], "|", r['regular'])
