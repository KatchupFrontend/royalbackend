from rest_framework import serializers
from . import models

class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = ['id','category', 'floortype', 'roomType','persons', 'address', 'apartmentPrice','apartmentImage','room1','room2','room3', 'description']

    def __init__(self, *args, **kwargs):
        super(RoomListSerializer, self).__init__(*args, **kwargs)
    
class RoomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = ['id','category', 'floortype', 'roomType', 'address', 'apartmentPrice','apartmentImage','room1','room2','room3', 'persons', 'description']


    def __init__(self, *args, **kwargs):
         super(RoomDetailSerializer, self).__init__(*args, **kwargs)
        

 
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['id','user', 'phone', 'fullname', 'email']

    def __init__(self, *args, **kwargs):
         super(CustomerSerializer, self).__init__(*args, **kwargs)
        

class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['id','user', 'phone', 'fullname', 'email']

    def __init__(self, *args, **kwargs):
         super(CustomerDetailSerializer, self).__init__(*args, **kwargs)
        

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['id','customer', 'date_booked']

    def __init__(self, *args, **kwargs):
        super(BookSerializer, self).__init__(*args, **kwargs)


class BookingDetailSerializer(serializers.ModelSerializer):
     class Meta:
         model = models.Bookings
         fields = ['id','room', 'booking', 'status']

     def __init__(self, *args, **kwargs):
          super(BookingDetailSerializer, self).__init__(*args, **kwargs)
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CampusCategory
        fields = ['id','campusname', 'campuslocation','campuslogo']


    def __init__(self, *args, **kwargs):
        super(CategorySerializer, self).__init__(*args, **kwargs)


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CampusCategory
        fields = ['id','campusname', 'campuslocation', 'campuslogo']

    def __init__(self, *args, **kwargs):
         super(CategoryDetailSerializer, self).__init__(*args, **kwargs)


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = ['booked_room','amount', 'date_created','ref','phone','email']

    def __init__(self, *args, **kwargs):
         super(PaymentSerializer, self).__init__(*args, **kwargs)
        

class PaymentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = ['id','booked_room','amount', 'date_created','ref','phone','email']

    def __init__(self, *args, **kwargs):
         super(PaymentDetailSerializer, self).__init__(*args, **kwargs)
    