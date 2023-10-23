
from django.db import models

from accounts.models import User


class Note(models.Model):
    note_text = models.CharField(max_length=500)
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.User
