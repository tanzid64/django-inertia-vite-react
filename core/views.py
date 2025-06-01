from time import sleep
from django.shortcuts import render
from django.http import HttpResponse
from inertia import render as inertia_render


# Create your views here.
def index(request):
    return inertia_render(
        request,
        "index",
        props={"message": "Welcome to Inertia + Django + Vite + React!"},
    )


def about(request):
    sleep(2.5)
    return inertia_render(request, "about", props={"pageName": "About"})
