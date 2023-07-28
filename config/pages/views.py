from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest

from django.http import Http404
from pages.models import Event, BannerImage, Consert, UZ, RU, EN

from pages.translation_data import ARGUMENTS

LANGUAGES = (UZ, RU, EN)
LANGUAGE_ITEM = 'language-item-347rgw43g23e37rtg3qb6re3g2egrq347'



def get_language_static(language: str):
    _dict = {}
    _dict['active'] = {
        'image': f'images/{language}.jpg',
        'code': language
    }
    _dict['deactive'] = []
    for i in LANGUAGES:
        if i != language:
            _dict['deactive'].append({
                'image': f'images/{i}.jpg',
                'url': i
            })
    return _dict



def index(request: WSGIRequest):
    language = request.COOKIES.get(LANGUAGE_ITEM, 'uz')
    if language in LANGUAGES:
        return redirect('_language_choices_page', language=language)
    else:
        return redirect('_language_choices_page', language='uz')


def language_choices_page(request: WSGIRequest, language):
    if not (language in LANGUAGES):
        raise Http404

    context = {
        'banners': BannerImage.objects.all(),
        'conserts': Consert.objects.filter(language=language),
        'events': Event.objects.filter(language=language),
        'language': get_language_static(language),
        'data': ARGUMENTS[language]
    }


    response = render(request, 'index.html', context)
    response.set_cookie(LANGUAGE_ITEM, language)
    return response