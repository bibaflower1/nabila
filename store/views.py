from django.shortcuts import HttpResponse, render, get_object_or_404
from .forms import ContactForm
from .models import Food, Contact, Booking
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

# Create your views here.

def index(request):
    #request foods
    foods=Food.objects.filter(available=True).order_by('-created_at')[:12]
    #then format the request.
    #note that we don't use food['title] anymore but food.title
    #because it's now an attribute
    formatted_foods=["<li>{}</li>".format(food.title) for food in foods]
    message="""<ul>{}</ul>""".format("\n".join(formatted_foods))

    template=loader.get_template('store/index.html')
    context={
        'foods':foods
    }
    return render(request, 'store/index.html', context)


def list(request):

    #request foods
    foods=Food.objects.filter(available=True).order_by('-created_at')[:12]
    #then format the request.
    #note that we don't use food['title] anymore but food.title
    #because it's now an attribute
    formatted_foods=["<li>{}</li>".format(food.title) for food in foods]
    message="""<ul>{}</ul>""".format("\n".join(formatted_foods))

    template=loader.get_template('store/list.html')
    context={
        'foods':foods
    }
    return render(request, 'store/list.html', context)



def order(request, food_id):
    food=get_object_or_404(Food, id=food_id)
    #food=Food.objects.filter(available=True)
    #context={
        #'food':food,
        #'title':foods.title,
        #'description':foods.description,
        #'price':foods.price,
        #'picture':foods.picture
    #}

    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            address=form.cleaned_data['address']
            contact=Contact.objects.filter(name=name)
            try:
                contact=Contact.objects.get(name=name)
            except Contact.DoesNotExist:
                contact=Contact.objects.create(
                    name=name,
                    address=address
                )
            food=get_object_or_404(Food, pk=food_id)
            booking=Booking.objects.create(
                contact=contact,
                food=food
            )

            food.available=False
            food.save()
            context={
                'title':food.title
                        
            }

            return render(request, 'store/confirm.html', context)
    form=ContactForm()
    context={
        'form':form,
        'food':food
    }   
    return render(request, 'store/order.html', context)
