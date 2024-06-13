from django.urls import path
from .views import upload_file, process_file

urlpatterns = [
    path('', upload_file, name='upload_file'),
    path('process/', process_file, name='process_file'),
]
