from rest_framework import serializers
from .models import Habit, UserProfile

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = [
            'name',
            'time_required',
            'difficulty',
            'reset_time',
            'completed',
            'id'

        ]

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

