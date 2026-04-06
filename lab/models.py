from django.db import models

class Comment(models.Model):
    text = models.TextField()  # Izoh matni
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:20]
    