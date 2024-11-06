from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import git

def update_server_view(request):
    if request.method == 'POST':
        try:
            repo = git.Repo('/home/cupawan/django_utility_suite')
            origin = repo.remotes.origin
            origin.pull()
            return JsonResponse({'message': 'Updated PythonAnywhere successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Wrong event type'}, status=400)
