from django.db import models
from datetime import timedelta

class Habit(models.Model):
    name = models.CharField(max_length=255, default="default_habit")
    exp_reward = models.PositiveBigIntegerField()
    time_required = models.TimeField()
    difficulty = models.PositiveSmallIntegerField()
    completed = models.BooleanField()
    id = models.AutoField(primary_key=True)
    streak = models.PositiveBigIntegerField(null=True)
    def get_exp(self):
        total_minutes = self.time_required.hour * 60 + self.time_required.minute
        return total_minutes * self.difficulty

    def save(self, *args, **kwargs):
        self.exp_reward = self.get_exp()
        return super().save(*args, **kwargs)
