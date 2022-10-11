from django.db import models

class Blogs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    data = models.DateField(auto_now=False)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
