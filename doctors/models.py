from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    description = models.TextField(blank=True)  # longer bio/description, no artificial length limit
    phone = models.CharField(max_length=20, default='00000000', blank=True)
    email = models.EmailField(unique=True)  # EmailField doesn’t need max_length, defaults to 254
    is_mvp = models.BooleanField(default=False)  # mark as featured doctor
    hire_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
