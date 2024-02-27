from django.db import models


class Game(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_state = models.JSONField()
    who_won = models.CharField(max_length=1, null=True)
