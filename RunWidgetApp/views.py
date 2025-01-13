from django.shortcuts import render
from django.http import JsonResponse
from Scripts.GarminConnectUtils import GarminUtils


def get_strava_frames(request):
    return render(request, 'RunWidgetAppTemplates/Index.html')

def get_garmin_run_ids(request):
    try:
        utils = GarminUtils()
        run_ids = utils.getRunId()
        return JsonResponse(run_ids, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)