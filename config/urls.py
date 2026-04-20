from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', include('apps.profiles.urls')),
    path('blog/', include('apps.blogs.urls')),
    path('events/', include('apps.events.urls')),
    path('inbox/', include('apps.messages_app.urls')),
    path('catch-log/', include('apps.catches.urls')),
    path('goals/', include('apps.goals.urls')),
    path('gear/', include('apps.gear.urls')),
    path('regulations/', include('apps.regulations.urls')),
    path('fish-species/', include('apps.fish.urls')),
    path('spots/', include('apps.spots.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
