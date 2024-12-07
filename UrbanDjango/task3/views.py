from django.shortcuts import render

def platform_view(request):
    return render(request, 'third_task/platform.html')

def games_view(request):
    games = [
        {'name': 'Atomic Heart'},
        {'name': 'Cyberpunk 2077'},
        {'name': 'PayDay 2'},
    ]
    return render(request, 'third_task/games.html', {'games': games})

def cart_view(request):
    return render(request, 'third_task/cart.html')
