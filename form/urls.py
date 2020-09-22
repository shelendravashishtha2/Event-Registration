from django.urls import path
from .views import CheckView, OpenView, EventView, DownloadData, Blog

app_name = 'form'
urlpatterns = [
    path('', OpenView.as_view(), name='homepage'),
    path('reg', CheckView.as_view(), name='register'),
    path('eve', EventView.as_view(), name='event'),
    path('datadownload', DownloadData.as_view(), name='download'),
    path('blog', Blog.as_view(), name='blog'),
]
