from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")


def merry_christmas(request):

    #
    return  render(request,"圣诞树2.html")