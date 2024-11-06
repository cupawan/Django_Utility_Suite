import git
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def update_server_view(request):
    if request.method == 'POST':
        try:
            repo = git.Repo('/home/cupawan/django_utility_suite')
            repo.git.stash("save")
            origin = repo.remotes.origin
            origin.pull()
            return JsonResponse({'message': 'Updated PythonAnywhere successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Wrong event type'}, status=400)

def homepage_view(request):
    if request.method == 'GET':
        return render(request, 'MasterTemplates/Home.html')