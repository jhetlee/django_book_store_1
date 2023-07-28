from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) #validators
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True ,null=False, db_index=True)

    #slugify the title for slug field # can now be deleted because of BookAdmin class on admin because it is prepopulated with slug format
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)#format title to "harry-potter-1"
        super().save(*args, **kwargs)#save the slugify title to slug field

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])

    #methods
    def __str__(self):
        return f"{self.title} ({self.rating})"