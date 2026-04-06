from django.db import models

class Izoh(models.Model):
    matn = models.TextField()
    vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.matn[:30]