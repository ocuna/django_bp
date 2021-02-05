from django.contrib import admin
from django.urls import path
from clinic.views import Home,nope_403,Aesspode

# need to get the ability to import sub-application urls
from django.conf.urls import include

urlpatterns = [
    path('',Home),
    path('nvaadmin/', admin.site.urls),
    # get the projet urls
    path('',include('mysql_clinic.urls')),
    path('aesspoded-evrahdang/', Aesspode),
    # Primarilly used by the mysql_CBV package
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/403', nope_403)
]

