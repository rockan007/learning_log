from django.db import models

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add= True)

    def __str__(self) -> str:
        """Return a string respresentation of the model"""
        return self.text

