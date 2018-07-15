# dojo/views.py

import os
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


def mysum(request, numbers):
    # request : HttpRequest
    # numbers = "1/2/12/13/112312/13123/...."
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    print(numbers)
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요'.format(name, age))


def post_list1(request):
    name = '공유'
    return HttpResponse('''

    '''.format(name=name))


def post_list2(request):
    name = '공유'
    return render(request, 'dojo/post_list.html', {'name': name})


def post_list3(request):
    return JsonResponse({
        'message': '안녕, 파이썬&장고',
        'items': ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
    }, json_dumps_params={'ensure_ascii': False})

def excel_download(request):
    filepath = '/Users/fullyalive/Project/project_blog/blog/examplefile.xlsx'
    # filepath = os.path.join(settings.BASE_DIR, 'examplefile.xlsx')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel') 
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
