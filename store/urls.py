from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static 
from restaurant_project import settings

from . import views

app_name="store"
urlpatterns = [
    path('list/', views.list, name="list"),
    path('<food_id>/', views.order, name='order'),
    #path('search/', views.search),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)