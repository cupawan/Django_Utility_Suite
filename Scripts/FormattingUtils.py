
class Formatter:
    def __init__(self):
        pass

    def redditPostsEmailFormatter(self,posts):
        body = ''''''
        for post in posts:
            post_body = ''
            post_body += f'<div><strong>{post.author}</strong></div>\n'
            if post.is_video:
                post_body += f'<p><h3>{post.title} [VIDEO]</h3></p>\n'
            else:
                post_body += f'<p><h3>{post.title}</h3></p>\n'        
            if post.selftext:
                post_body += f'<p>{post.selftext}</p>\n'
            if hasattr(post, 'preview') and 'images' in post.preview:
                all_images = [x['source'] for x in post.preview['images']]
                for image in all_images:
                    post_body += f'<img src="{image["url"]}" alt="Post Image" style="max-width: 100%; height: auto;">\n'
            post_body += f'<p>Upvotes: {post.ups} Comments: {post.num_comments}</p>'        
            if post.is_video:
                post_body += f"<br><a class='watch-video-btn' href='https://reddit.com{post.permalink}'> Watch Video</a>"
            else:
                post_body += f"<br><a class='watch-video-btn' href='https://reddit.com{post.permalink}'> See on Reddit</a>"        
            post_body += '</div>\n'
            post_body += "<hr>"
            body += post_body
        body += "<p>Wishing you a wonderful day!</p>"
        return body
