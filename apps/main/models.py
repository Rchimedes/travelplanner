from django.db import models
from apps.login.models import User

class TripManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data["destination"]) < 3:
            errors["destination"] = "Please enter a destination with at least 3 characters"
        if len(post_data["plan"]) < 3:
            errors["plan"] = "Please enter more info on the plan"

        
        
        return errors
    def edit_validator(self, post_data):
        errors = {}

        if len(post_data["destination"]) < 3:
            errors["destination"] = "Please enter a destination"
        if len(post_data["plan"]) < 3:
            errors["plan"] = "Please enter more info on the plan"
        
        return errors

class Trip(models.Model):
    destination = models.CharField(max_length=50)
    plan = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="trips")
    userassigned = models.ForeignKey(User, related_name="tripsassigned")
    objects = TripManager()
