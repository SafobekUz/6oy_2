from django.http import HttpResponse


def on():
    a = 0
    while a < 10:
        return  f"{a} - Salom Dunyo"
        a = a + 1
def home(request):
    return HttpResponse(f"<h1>Salom dunyo</h1> {on()}")