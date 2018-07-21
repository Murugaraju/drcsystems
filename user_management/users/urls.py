#users/urls.py

from django.conf.urls import url
# from . import views
from .views import home, register

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^register/', register, name='register'),
    # url(r'^signup/', register, name='signup'),
    # url(r'^login/', register, name='login'),

]
