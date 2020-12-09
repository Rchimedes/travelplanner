from django.db import models
from django.core.validators import validate_email

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data["first_name"]) < 1:
            errors["first_name"] = "Please enter a first name"
        elif len(post_data["first_name"]) < 2:
            errors["first_name"] = "Please enter a first name with at least 2 letters"
        if len(post_data["last_name"]) < 1:
            errors["last_name"] = "Please enter a last name"
        elif len(post_data["last_name"]) < 2:
            errors["last_name"] = "Please enter a last name with at least 2 letters"
        if len(post_data["email"]) < 1:
            errors["email"] = "Please provide an email address"
        elif len(post_data["email"]) < 4:
            errors["email"] = "Please provide a valid email address"
        if len(post_data["password"]) < 8:
            errors["password"] = "Please provide a password with at least 8 characters"
        if post_data["password"] != post_data["confirm_password"]:
            errors["password"] = "Your passwords don't match sucka!"
        try:
            validate_email(post_data["email"])
        except:
            errors["email"] = "Please enter a valid email"
        
        return errors
    def login_validator(self, post_data):
        errors = {}

        if len(post_data["email"]) < 1:
            errors["email"] = "Please provide an email address and/or password"
        elif len(post_data["email"]) < 1:
            errors["email"] = "Please provide an email address and/or password"
        
        if len(post_data["password"]) < 1:
            errors["password"] = "Please enter a password"
        try:
            validate_email(post_data["email"])
        except:
            errors["email"] = "Please enter a valid email"
        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

