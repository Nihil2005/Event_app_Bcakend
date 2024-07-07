from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='events/images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
