from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from crawler import views as crawler_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^profile/$', crawler_views.profile),
    url(r'^getProfile$', crawler_views.get_profile, name='getProfile'),
    url(r'^getNumberOfTopSkills$', crawler_views.get_number_of_top_skills, name='getNumberOfTopSkills')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
