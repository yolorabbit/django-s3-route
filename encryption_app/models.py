from django.db import models

# Create your models here.

class EncryptedFile(models.Model):
    file_name = models.CharField(max_length = 255)
    upload_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
    	return self.file_name
