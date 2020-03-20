from django.shortcuts import render, redirect
from random import randint
from time import gmtime, strftime

track_gold = []

def index(request):
    total_gold = request.session.get('total_gold', 0)
    request.session['total_gold'] = total_gold

    context = {
        'total_gold' : total_gold,
        'track_gold' : reversed(track_gold)
    }
    return render(request, 'index.html', context)

def farm_click(request):
    farm_gold = randint(10, 20)
    request.session['total_gold'] = request.session['total_gold'] + farm_gold

    track_gold.insert(len(track_gold), f'Earned {farm_gold} gold from the Farm! {current_dt()}')
    print(track_gold)
    
    return redirect('/')

def cave_click(request):
    cave_gold = randint(5, 10)
    request.session['total_gold'] = request.session['total_gold'] + cave_gold

    track_gold.insert(len(track_gold), f'Earned {cave_gold} gold from the Cave! {current_dt()}')
    print(track_gold)
    
    return redirect('/')

def house_click(request):
    house_gold = randint(2, 5)
    request.session['total_gold'] = request.session['total_gold'] + house_gold

    track_gold.insert(len(track_gold), f'Earned {house_gold} gold from the House! {current_dt()}')
    print(track_gold)
    
    return redirect('/')

def casino_click(request):
    casino_gold = randint(-50, 50)
    request.session['total_gold'] = request.session['total_gold'] + casino_gold

    if casino_gold == 0:
        track_gold.insert(len(track_gold), f'Entered a casino and broke even with 0 gold... Pheww! {current_dt()}')
    elif casino_gold < 0:
        track_gold.insert(len(track_gold), f'Entered a casino and lost {casino_gold} gold... Ouch! {current_dt()}')
    else:
        track_gold.insert(len(track_gold), f'Entered a casino and won {casino_gold} gold!! Awesome! {current_dt()}')
    
    print(track_gold)
    
    return redirect('/')
    
def current_dt():
    print(strftime('%Y/%m/%d %I:%M %p', gmtime()))
    return strftime('%Y/%m/%d %I:%M %p', gmtime())

