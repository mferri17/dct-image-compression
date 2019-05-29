from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

import os
import webui.utils as utils

# Create your views here.


def index(request, image=None, image_compress=None):
    return render(request, 'index.html')


def compress(request):
    try:
        # Trying to get POST data
        image = request.FILES['image']
        F = int(request.POST['F'])
        d = int(request.POST['d'])
        user = request.POST['user']
    except (KeyError):
        # Redisplay the form in case of error
        return render(request, 'index.html', {
            'image': image,
            'F': F,
            'd': d,
            'error_message': "You missed something.",
        })
    else:
        utils.compress_image(user, image, F, d)
        return redirect('index')


def get_user_images(request):
    user = request.GET['user']
    userpath = os.path.join('media', user)

    images = []

    for directory in os.listdir(userpath):
        for root, dirs, files in os.walk(os.path.join(userpath, directory)):
            for filename in files:
                imagepath = '/' + os.path.join(root, filename).replace('\\', '/')
                images.append(imagepath)

    return JsonResponse({'images': images})
