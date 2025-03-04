from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")
def test(request):
    return HttpResponse("<h1>Welcome to test url</h1>")