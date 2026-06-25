import praw
import os
import time
from modules.utils import build_reply_with_items, parse_items_from_comment
from prawcore.exceptions import PrawcoreException

RECONNECT_DELAY = int(os.environ.get("RECONNECT_DELAY", 10))

def create_reddit_instance():
    return praw.Reddit(
        client_id=os.environ["REDDIT_CLIENT_ID"],
        client_secret=os.environ["REDDIT_SECRET"],
        password=os.environ["REDDIT_PASSWORD"],
        user_agent=os.environ["USER_AGENT"],
        username=os.environ["REDDIT_USERNAME"]
    )

def main():
    reddit = create_reddit_instance()
    running = True
    while running:
        try:
            print("Listening for comments...")
            for comment in reddit.subreddit(os.environ["SUBREDDITS"]).stream.comments(skip_existing=True):
                print(f"Rate limiting info: {reddit.auth.limits}")
                print(f"Comment received: {comment.body}")
                items_from_comment = parse_items_from_comment(comment.body)
                print(f"items from comment: {items_from_comment}")
                if len(items_from_comment) > 0:
                    if os.environ["SHOULD_REPLY"] == "true":
                        try:
                            reply = build_reply_with_items(items_from_comment)
                            if (len(reply) > 0):
                                comment.reply(reply)
                        except praw.exceptions.APIException as e:
                            print(e)
                            continue
                    else:
                        print("The bot is merely spectating subreddit traffic.")
                else:
                    print("No items, skipping...")
        except KeyboardInterrupt:
            logger.info('Shutting down...')
            running = False
        except PrawcoreException as e:
            print(f"Error: {e}")
            print(f"Reconnecting in {RECONNECT_DELAY} seconds...")
            time.sleep(RECONNECT_DELAY)

if __name__ == "__main__":
    main()
