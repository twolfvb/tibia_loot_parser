from django.shortcuts import render

# Create your views here.

def loot_landing(request):
    return render(request, 'loot_parser/loot_landing.html')