from django.urls import path, include

from funds import views

urlpatterns = [
    path('funds-list/', views.fundsList.as_view()),
    path('price-filter/', views.priceFilter),
]