from django.conf.urls import url, include
from .views import handler401_view, handler404_view, handler500_view

urlpatterns = [
    url(r'', include('Admin.Home.urls')),
    url(r'^', include('urls')),
]

handler401 = handler401_view
handler404 = handler404_view
handler500 = handler500_view