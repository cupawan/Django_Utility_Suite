import os
import praw
import os

class RedditData:
    def __init__(self):
        self.client_id= os.environ["RedditClientId"]
        self.client_secret= os.environ['RedditClientSecret']
        self.username = os.environ['RedditUsername']
        self.password = os.environ['RedditPassword']
        self.user_agent = os.environ['RedditUserAgent']

    def auth(self):
        reddit = praw.Reddit(client_id=self.client_id,
                             client_secret= self.client_secret,
                             username= self.username,
                             password= self.password,
                             user_agent= self.user_agent)
        reddit.read_only = True    
        return reddit
    
    def get_posts(self, sub, limit_posts, filterby):
        reddit = self.auth()
        subreddit = reddit.subreddit(sub)
        if filterby.lower() == 'top':
            posts = subreddit.top(limit=int(limit_posts))
        elif filterby.lower() == 'hot':
            posts = subreddit.hot(limit=int(limit_posts))
        elif filterby.lower() == 'new':
            posts = subreddit.new(limit=int(limit_posts))
        else:
            posts = subreddit.hot(limit=int(limit_posts))
        return posts


