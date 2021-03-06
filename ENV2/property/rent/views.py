from django.shortcuts import render, loader
from django.http import HttpResponse

from .models import Location, Property, Room, Transaction, Leasedetails
from django.db.models import Count, Avg
from django.core import serializers

# Create your views here.

def index(request):
    latest_question_list = Location.objects.order_by('-location_name')[:5]
    template = loader.get_template('rent/property.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def create(request):
    return HttpResponse("create")

def property(request):
    location = Location.objects.all();
    room = Room.objects.all();
    property = Property.objects.all();
    #property_details = Property.objects.values('property_id','property_name','property_location_id' ).annotate(num_room=Count('room')).order_by('property_id')
    property_details = Property.objects.all().annotate(num_room=Count('room')).order_by('property_id')
    string_data = []#serializers.serialize('json', property_details)
    #room_count = Room.objects.all().values('room_property').annotate(num_room=Count('room_property')).order_by('room_property')
    print(property_details)
    return render(request,'rent/property.html',{'location':location,'room':room,'property':property, 'room_count':property_details, 'string_data':string_data})

def property_details(request, property_id):
    room = Room.objects.filter(room_property_id=property_id)
    lease_details = Leasedetails.objects.filter(lease_room__in=room)
    print(lease_details.filter(lease_tenant=3))
    string_data = serializers.serialize('json',lease_details)
    return render(request,'rent/property_details.html',{'room':room,'lease_details':lease_details,'string_data':string_data})

def transaction_list(request):
    transaction = Transaction.objects.all()
    return render(request,'rent/transaction.html',{'transaction_list':transaction})

def room_details(request, room_id):
    room = Room.objects.get(room_id=room_id)
    return render(request,'rent/room_details.html',{'room_details':room})
    
