# ig_to_slack

I use a private Slack instance as something like a combination of Evernote, Pinterest, and an RSS feed. Instagram is a big source of content similar to Pinterest for me, so `ig_to_slack` acts as the glue between my saved collections and Slack. It runs indefinitely in the background and uses a simple text file to store state to dedupe.

You can map one Slack webhook per saved collection.

```json
{
    "session": "<your instagram session>",
    "maps": [
        {
            "collection_id": "179857097930",
            "webhook": "https://hooks.slack.com/services/XXX/YYY/ZZZ"
        },
        {
            "collection_id": "179388819981",
            "webhook": "https://hooks.slack.com/services/XXX/YYY/ZZZ"
        },
        {
            "collection_id": "17885084890568297",
            "webhook": "https://hooks.slack.com/services/XXX/YYY/ZZZ"
        }
    ]
}
```

1. Build: `docker build -t instanotify .`
2. Run: `docker run -v /path/to/dir/holding/configs:/mnt/host --rm -it instanotify:latest`
3. Develop: `WORKDIR=/path/to/same/dir/ python3 src/main.py`
