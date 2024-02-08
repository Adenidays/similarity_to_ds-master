
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularRedocView

from chat.views import signup, user_login, main_page

urlpatterns = [
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),


    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('api/',include('userapp.urls')),
    path('chat/',include('chat.urls')),

    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('',main_page,name='main')
]
