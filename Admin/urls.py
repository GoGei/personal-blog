from django.conf.urls import url, include
from .views import handler401_view, handler404_view, handler500_view

urlpatterns = [
    url(r'^', include('urls')),
    url(r'', include('Admin.Home.urls')),
    url(r'^posts/', include('Admin.Posts.urls')),
    url(r'^contacts/', include('Admin.Contacts.urls')),
    url(r'^about/', include('Admin.About.urls')),
    url(r'^todo/', include('Admin.Todo.urls')),
]

handler401 = handler401_view
handler404 = handler404_view
handler500 = handler500_view
