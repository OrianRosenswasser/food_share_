# models.py
from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    password = models.CharField(max_length=255, default="default_password")
    email = models.EmailField(unique=True, default="default@example.com")

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    def get_food_posts_count(self):
        return self.foodpost_set.count()

    def get_food_requests_count(self):
        return self.foodrequest_set.count()

class FoodPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    posted_by = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='posts')
    expiration_date = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='food_posts/', null=True, blank=True)
    collection_point = models.CharField(max_length=255, null=False, default='Unknown')
    whatsapp_link = models.CharField(max_length=15, null=True, blank=True)    

    def __str__(self):
        return f"{self.title}"
    
class FoodRequest(models.Model):
    food_post = models.ForeignKey(FoodPost, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Request for {self.food_post} by {self.requested_by or 'Unknown'}"
    