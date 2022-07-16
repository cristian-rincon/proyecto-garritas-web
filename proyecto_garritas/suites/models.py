from django.db import models
from django.urls import reverse

# Create your models here.


class Suite(models.Model):
    """
    Model representing a Suite, which is a room that can be rented.
    """

    name = models.CharField(
        max_length=200, help_text="Enter a suite name (e.g. 'A', 'B', 'C', etc.)"
    )
    description = models.TextField(
        max_length=1000, help_text="Enter a description of the suite"
    )
    price = models.IntegerField(help_text="Enter the price of the suite")
    photo = models.ImageField(
        upload_to="suites/photos", blank=True, help_text="Upload a photo of the suite"
    )
    available = models.BooleanField(default=True, help_text="Is the suite available?")

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this suite.
        """
        return reverse("suites:suite-detail", args=[str(self.id)])
