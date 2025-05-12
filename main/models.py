from django.db import models
from datetime import timedelta, datetime
from django.contrib.auth.models import User
from skills.models import Tree
import pytz

class UserProfile(models.Model):
    exp = models.PositiveIntegerField(default=0)
    next_level_exp = models.PositiveIntegerField(default=100)
    level = models.PositiveIntegerField(default=1)
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    timezone = models.CharField(
        max_length=32,
        choices=[(tz, tz) for tz in pytz.common_timezones],
        default='UTC'
    )
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    def level_up(self):
        while self.exp >= self.level * 100:
            self.exp -= self.level * 100
            self.level += 1
            self.next_level_exp = self.level * 100

    def level_down(self):
        while self.exp < 0 and self.level > 1:
            self.level -= 1
            
            self.exp += self.level * 100 
            self.next_level_exp = self.level * 100

    def save(self, *args, **kwargs):
        if self.exp < 0:
            self.exp = 0
        if self.level < 1:
            self.level = 1
            self.exp = 0
        return super().save(*args, **kwargs)
        

class Habit(models.Model):
    name = models.CharField(max_length=255, default="default_habit")
    exp_reward = models.PositiveBigIntegerField()
    time_required = models.PositiveBigIntegerField()
    difficulty = models.SmallIntegerField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    id = models.AutoField(primary_key=True)
    streak = models.PositiveBigIntegerField(default=0, editable=False)
    reset_time = models.TimeField(null=True)
    needs_reset = models.BooleanField(default=False)
    skills = models.ManyToManyField(Tree, null=True)


    def get_exp(self):
        return self.time_required * self.difficulty

    def save(self, *args, **kwargs):
        self.exp_reward = self.get_exp()
        habit = super().save(*args, **kwargs)

        return habit

class Quest(models.Model):
    name = models.CharField(max_length=255, default="default_habit")
    exp_reward = models.PositiveBigIntegerField()
    time_required = models.PositiveBigIntegerField()
    difficulty = models.PositiveSmallIntegerField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    id = models.AutoField(primary_key=True)
    def get_exp(self):
        return self.time_required * self.difficulty

    def save(self, *args, **kwargs):
        self.exp_reward = self.get_exp()
        

        return super().save(*args, **kwargs)
