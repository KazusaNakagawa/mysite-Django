from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

if __name__ == '__main__':
    # check path
    print('=' * 50)
    print(urlpatterns[0])
    print(urlpatterns[1])
    print(urlpatterns[2])
    print('=' * 50)
    print(urlpatterns, '\n')
    print('settings.FILE_CHARSET:', settings.FILE_CHARSET)
    print('settings.MEDIA_URL:', settings.MEDIA_URL)
    print('settings.MEDIA_ROOT:', settings.MEDIA_ROOT, '\n')
