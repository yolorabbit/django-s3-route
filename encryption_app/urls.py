from django.urls import path
from .views import upload_and_encrypt_file

urlpatterns = [
   path('upload/', upload_and_encrypt_file, name='upload_and_encrypt_file'),
]
