from django.utils import timezone
from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d/')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
