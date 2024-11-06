from django.shortcuts import render
from django.http import JsonResponse
from prawcore.exceptions import NotFound
from Scripts.RedditScript import RedditData
from Scripts.FormattingUtils import Formatter

def get_posts_view(request):
    if request.method == "GET":
        return render(request, 'RedditPostsAppTemplates/Index.html')
    elif request.method == "POST":
        subreddit = request.POST.get('subreddit')
        limit_posts = request.POST.get('limit')
        filterby = request.POST.get('filterby')
        reddit_data = RedditData()
        try:
            posts = reddit_data.get_posts(sub=subreddit,limit_posts = limit_posts, filterby = filterby)
            body = Formatter().redditPostsEmailFormatter(posts = posts)
        except NotFound:
            error_message = "Please correct your input (remove spaces from subreddit name if any). This subreddit might not exist."
            return render(request, 'MasterTemplates/ErrorPage.html', {'error_message': error_message})
        return render(request, 'RedditPostsAppTemplates/Results.html', {'posts': body})

