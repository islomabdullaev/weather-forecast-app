from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=24)
    degree = models.FloatField(default=0.0)
    main = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)