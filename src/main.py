from scraper import *
from slacker import *
from state import *

import requests
import json
import time
import os

workdir = os.getenv('WORKDIR', '/mnt/host')
config = json.load(open(f'{workdir}/config.json', 'r'))
state_file = f'{workdir}/state.txt' 

seen_ids = get_state(state_file)
client = get_client(config['session'])

print("hello :)")

while 1:
    for pair in config['maps']:
        collection = client.collection_medias(pair['collection_id'])
        webhook_url = pair['webhook']
        print(f"Processing {pair['collection_id']}")

        for media in collection:
            if media.code in seen_ids:
                continue

            if media.media_type == 8: # album
                thumbnails = list(map(lambda x: str(x.thumbnail_url), media.resources))
            elif media.media_type in [1, 2]: # single pic/video
                thumbnails = [str(media.thumbnail_url)]

            url = f"https://www.instagram.com/p/{media.code}/"
            username = media.user.username
            fullname = media.user.full_name
            caption = media.caption_text

            caption = f"{username} ({fullname}): {caption}\n{url}"
            print(caption)

            blocks = []
            blocks.append(caption_block(caption))
            for img in thumbnails:
                blocks.append(divider())
                blocks.append(image_block(img, "yeet"))

            post_body = build_post_body(caption, blocks)
            requests.post(webhook_url, json=post_body)

            seen_ids.append(media.code)
            put_state(state_file, seen_ids)

            time.sleep(1)

    print("Nap time!")
    time.sleep(600)
