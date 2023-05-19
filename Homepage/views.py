from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Card

def index(request):
    cards = Card.objects.order_by('order')  # Retrieve cards ordered by 'order' field
    return render(request, 'index.html', {'cards': cards})

def update_card(request, card_id=None):
    if card_id:
        card = get_object_or_404(Card, id=card_id)
    else:
        card = Card()

    if request.method == 'POST':
        card.category = request.POST.get('category')
        card.title = request.POST.get('title')
        card.description = request.POST.get('description')
        card.link = request.POST.get('link')
        card.image = request.FILES.get('image')

        card.save()

        messages.success(request, f'Card saved successfully.')

        # Redirect
        return redirect('HomePage:index')

    # Render
    return render(request, 'update_card.html', {'card': card})


def carousel(request):
    cards = Card.objects.order_by('order')
    return render(request, 'carousel.html', {'cards': cards})

def success(request):
   return render(request, 'success.html')

def card_detail(request, card_id):
    
    card = Card.objects.get(id=card_id)  

    context = {
        'card': card,
    }

    return render(request, 'card_detail.html', context)

def delete_card(request):
    if request.method == 'POST':
        card_id = request.POST.get('card_id')
        card = Card.objects.filter(id=card_id).first()
        if card:
            card.delete()
            # Redirect 
            return redirect('HomePage:index')
        else:
            # Handle 
            return render(request, 'card_not_found.html')

    # Render 
    return render(request, 'delete_card.html')

def delete_all_cards(request):
    if request.method == 'POST':
        Card.objects.all().delete()
        # Redirect 
        return redirect('HomePage:index')

    # Render 
    return render(request, 'delete_all_cards.html')