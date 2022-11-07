def divider():
    return {
        "type": "divider",
    }

def caption_block(message):
    return {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": message
        }
    }

def image_block(image_url, alt_text):
    return {
        "type": "image",
        "image_url": image_url,
        "alt_text": alt_text
    }

def build_post_body(message, blocks):
    return {
        "text": message,
        "blocks": blocks
    }
