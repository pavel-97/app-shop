from django.shortcuts import render
from django.views import View
from . import models
import random
import time

# Create your views here.


class Advertisement(View):
    def get(self, request):
        t1 = time.time()
        res = models.Advertisement.objects.all()
        print(time.time()-t1)
        objs = models.Advertisement.objects.all()
        obj = list(objs)[random.randint(0, len(objs) - 1)]
        context = {
            'objs': objs,
            'obj':obj
        }
        return render(request, 'app/index.html', context)
