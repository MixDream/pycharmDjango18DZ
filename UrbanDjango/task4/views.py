from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
def platform(request):
    return render(request, 'third_task/platform.html')
def games(request):
    games_list = {
        'game1': 'Atomic Heart',
        'game2': 'Cyberpunk 2077',
        'game3': 'PayDay 2',
    }
    return render(request, 'third_task/games.html', {'games': games_list})
def cart(request):
    return render(request, 'third_task/cart.html')
# Create your views here.
