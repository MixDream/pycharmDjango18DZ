from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View

# Функциональное представление
def functional_view(request):
    return render(request, 'second_task/func_template.html')

# Классовое представление
class ClassBasedView(View):
    def get(self, request):
        return render(request, 'second_task/class_template.html')
