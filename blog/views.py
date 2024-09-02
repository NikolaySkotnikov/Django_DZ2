from django.shortcuts import HttpResponse

CATEGORIES = {
        1: "Чилл территории Python",
        2: "Django, сложно, но можно!",
        3: "Flask, бегите, глупцы!",
    }


def blog_catalog(request):
    return HttpResponse('Тут будет блог')


def category_list(request):
    result = ('<h1>Категории</h1>'
              '<ol>')
    for i, j in zip(CATEGORIES.values(), CATEGORIES.keys()):
        result += f'<li><a href="{j}">{i}</a></li>'
    result += '</ol>'
    return HttpResponse(result)


def category_detail(request, cat_id):
    if cat_id in CATEGORIES.keys():
        return HttpResponse(f'Подробная информация о категории: {CATEGORIES[cat_id]}')
    else:
        return HttpResponse('404 - Категория не найдена', status=404)
