from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'home'),
    # path('', views.index, name = 'home')
]