from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#created a many to one realtion between Blog and User -> one user can have many Blogs and vice versa not true
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.description[:5]}'
    

