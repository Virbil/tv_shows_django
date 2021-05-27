from django.db import models
import datetime as dt

class Show_Manager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data["title"]) < 1:
            errors["title"] = "Movie title must be at least 2 characters"
        
        if len(post_data["network"]) < 1:
            errors["network"] = "Movie network must be at least 2 characters"
        
        if len(post_data["description"]) > 0:
            if len(post_data["description"]) < 10:
                errors["description"] = "Movie description must be at least 10 characters"
        
        if len(post_data["release_date"]) < 1:
            errors["release_date"] = "Please select or enter a  release date"
        if post_data["release_date"].isalpha() == True:
            errors["release_date"] = "Release Date must be a valid date"
        if len(post_data["release_date"]) > 0:
            date_entered = dt.strptime(post_data["release_date"], "%m/%d/%Y")
            date_today = dt.today().strftime("%m/%d/%y")
            d3 = dt.strptime(date_today, "%m/%d/%Y")
            if date_entered > d3:
                errors["release_date"] = "Release Date must be in the past"

        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = Show_Manager()

    class Meta:
        ordering = ['title']