from django.shortcuts import render


def translate_text(request):
    return render(request, 'StravaRunWidgetAppTemplates/Index.html')
