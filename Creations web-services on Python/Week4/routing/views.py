from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_http_methods, require_POST


@require_http_methods(['GET', 'PUT', 'POST'])
def simple_route(request, something=None):
    if request.method == 'GET' and something == None:
        return HttpResponse(content='', status=200)
    elif request.method in ['POST', 'PUT']:
        return HttpResponse(status=405)
    else:
        return HttpResponse(status=404)

@csrf_exempt
def slug_route(request, telo):
    # if telo != None:
    return HttpResponse(telo)
    # else:
    #     return HttpResponse(status=404)

@csrf_exempt
def sum_route(request, num1, num2):
    if num1 != None and num2 != None:
        return HttpResponse(int(num1) + int(num2))
    else:
        return HttpResponse(status=404)


@require_http_methods(['GET'])
def sum_get_method(request):
    if request.GET.get('a') != None and request.GET.get('b') != None:
        num_a = request.GET.get('a')
        num_b = request.GET.get('b')
        if check_num(num_a) == True and check_num(num_b) == True:
            result = str(int(num_a) + int(num_b))
            return HttpResponse(content=result, status=200)
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=400)


@require_http_methods(['POST'])
@csrf_exempt
def sum_post_method(request):
    if request.POST.get('a') != None and request.POST.get('b') != None:
        num_a = request.POST.get('a')
        num_b = request.POST.get('b')
        if check_num(num_a) and check_num(num_b):
            return HttpResponse(str(int(num_a) + int(num_b)))
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=400)


def check_num(num):
    if num[0] in ('-', '+'):
        return num[1:].isdigit()
    return num.isdigit()
