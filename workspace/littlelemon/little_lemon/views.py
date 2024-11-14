from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

from rest_framework.decorators import api_view,permission_classes
from rest_framework import generics
from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer
from rest_framework import viewsets


# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset=Booking.objects.all()
    serializer_class= BookingSerializer
    
#view for authentication
'''@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message":"this view is protected"})'''