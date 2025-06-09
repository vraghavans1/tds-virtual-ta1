import json
import os
import re

SRC = 'downloaded_threads/discourse_posts.json'
OUT_DIR = 'downloaded_threads'

with open(SRC, 'r', encoding='utf-8') as f:
    posts = json.load(f)

def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

topics = {}
for p in posts:
    tid = p['topic_id']
    topic = topics.setdefault(tid, {
        'id': tid,
        'title': p['topic_title'],
        'slug': slugify(p['topic_title']),
        'post_stream': {'posts': []}
    })
    topic['post_stream']['posts'].append({
        'id': p['post_id'],
        'post_number': p['post_number'],
        'username': p['author'],
        'created_at': p['created_at'],
        'like_count': p['like_count'],
        'cooked': p['content']
    })

for tid, data in topics.items():
    out_file = os.path.join(OUT_DIR, f'topic_{tid}.json')
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
print(f'Created {len(topics)} topic files in {OUT_DIR}')
