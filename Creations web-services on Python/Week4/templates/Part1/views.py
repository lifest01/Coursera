from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


@csrf_exempt
def echo(request):
    if 'HTTP_X_PRINT_STATEMENT' in request.META:
        header = request.META['HTTP_X_PRINT_STATEMENT']
    else:
        header = 'empty'
    if request.method == 'GET':
        data = {
            'method': 'get',
            # 'param_name': list(request.GET.keys())[0],
            # 'param_value': list(request.GET.values())[0],
            'items': list(request.GET.items()),
            'header': header,
            # 'meta': request.META
        }
        return render(request, 'echo.html', context=data)

    elif request.method == 'POST':
        data = {
            'method': 'post',
            'items': list(request.POST.items()),
            'header': header,
            # 'meta': request.META
        }
        return render(request, 'echo.html', context=data)

    # ['HTTP_X_PRINT_STATEMENT']
    # if request.method == 'GET':
    #     param_name = list(request.GET.keys())[0]
    #     param_value = list(request.GET.values())[0]
    #     return HttpResponse(f'get {param_name}:{param_value} statement is empty\n{request.META.HTTP_X_Print_Statement}')
    # elif request.method == 'POST':
    #     param_name = list(request.POST.keys())[0]
    #     param_value = list(request.POST.values())[0]
    #     return HttpResponse(f'get {param_name}:{param_value} statement is empty')


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })
