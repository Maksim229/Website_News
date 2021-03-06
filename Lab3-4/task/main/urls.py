from django.urls import path
from .views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about', About.as_view()),
    path('news', views.read),
    path('contacts', Contacts.as_view()),
    path('signup', RegisterView.as_view()),
    path('signin', LoginView.as_view()),
    path('create', views.create),
    path('logout', views.logout_user),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
