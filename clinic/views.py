from django.shortcuts import render
from django.http import HttpResponse

# function based view:
def Home(request):
    # http reponse simply sends back HTML -- very basic
    context = {
        'html': 'Front page'
    }
    return render(request,'home.html', context)

def nope_403(request):
    # http reponse simply sends back HTML -- very basic
    # return HttpResponse('<a href="/quote/">quote</a><br><a href="/html/dt">DateTime</a><br><a href="/html/">Greeting</a><br>')
    context = {
        'html': 'You don\'t have access to this function.  Contact the adminstrator.'
    }
    return render(request,'home.html', context)

def Aesspode(request):
    raise Exception('▐▓▒░ ͶΔͲΞ ░▒▓▌ there has been an intentional exception to demonstrate the capability of the exception-catching middleware.  \n A user went to url: /aesspoded-evrahdang/')
    return HttpResponse()