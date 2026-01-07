from django.db import models

# Create your models here.
class Contact(models.Model):
    # #Windsurf: Refactor | Explain
    
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)      # ✅ Fixed: max_length
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)       # ✅ Fixed: blank
    contact_date = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(null=True, blank=True)  # ✅ Fixed: for optional user
    
    # #Windsurf: Refactor | Explain | Generate Docstring
    
    def __str__(self):
        return self.name


    