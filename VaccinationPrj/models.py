from django.db import models
from django.contrib.auth.models import User

class Vaccine(models.Model):
    VACCINE_TYPES = [
        ('PF', 'Pfizer'),
        ('MD', 'Moderna'),
        ('AZ', 'AstraZeneca'),
        ('JJ', 'Johnson & Johnson'),
    ]

    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vaccine_type = models.CharField(max_length=2, choices=VACCINE_TYPES)
    date_of_vaccination = models.DateField()
    dosage = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.username} - {self.vaccine_type} - {self.date_of_vaccination}'
    