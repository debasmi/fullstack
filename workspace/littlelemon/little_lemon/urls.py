#define URL route for index() view
from django.urls import path
from . import views


urlpatterns=[
    path('index/', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
   ]
