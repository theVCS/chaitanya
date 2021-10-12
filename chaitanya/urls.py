from django.contrib import admin
from django.urls import path,include
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('home.urls')),
    path('home/',include('home.urls')),
    path('newsletters/',include('newsletters.urls')),
    path('blogs/',include('blog.urls')),
    path('contest/',include('contest.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
