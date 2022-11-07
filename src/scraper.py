from instagrapi import Client

def get_client(session_id):
    cl = Client()
    cl.login_by_sessionid(session_id)

    return cl
