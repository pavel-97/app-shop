from django.shortcuts import render
from django.views import View

# Create your views here.


class Region(View):
    def get(self, request):
        context = {
            'answer': ['Москва', 'Московская область', 'республика Алтай', 'Вологодская область']
        }
        return render(request, 'app/regions.html', context)

    def post(self, request):
        context = {
            'answer': 'Регион успешно создан.'
        }
        return render(request, 'app/regions.html', context)
