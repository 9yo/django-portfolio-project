from backend import settings
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def render_static_files(request, filename=''):
    if 'css' in filename:
        return render(request, "{}/css/{}".format(settings.TEMPLATES[0]['DIRS'][0], filename), content_type='text/css')
    elif 'js' in filename:
        return render(request, "{}/js/{}".format(settings.TEMPLATES[0]['DIRS'][0], filename), content_type='application/javascript')
