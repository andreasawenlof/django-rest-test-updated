"""
This module defines the Post model.
"""
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    This class defines the Post model.
    """
    image_filter_choices = [
        ('_1977', '1977'), ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'), ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'), ('normal', 'Normal'),
        ('nashville', 'Nashville'), ('rise', 'Rise'),
        ('toaster', 'Toaster'), ('valencia', 'Valencia'),
        ('walden', 'Walden'), ('xpro2', 'X-pro II')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_wwzdvo', blank=True)

    image_filter = models.CharField(
        max_length=32,
        choices=image_filter_choices,
        default='normal',
    )

    class Meta:
        """
        This class defines metadata for the Post model.
        """
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.pk} {self.title}'
