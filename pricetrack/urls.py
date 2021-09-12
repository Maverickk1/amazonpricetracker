
from django.contrib import admin
from django.urls import path,include
from links.views import home,LinkDeleteView,update_prices



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('update/',update_prices,name='update_prices'),
    path('delete/<pk>/',LinkDeleteView.as_view(),name='delete')
]
