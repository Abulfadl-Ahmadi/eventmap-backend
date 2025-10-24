from django.db import models

__all__ = ['Booth', 'BoothEvent', 'Rating', 'ContestSetting', 'ContestWinner']

class Booth(models.Model):
    name = models.TextField()
    community_name = models.TextField()
    description = models.TextField(blank=True, null=True)
    x_coordinate = models.IntegerField(default=0)
    y_coordinate = models.IntegerField(default=0)
    svg_x = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    svg_y = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    region_type = models.CharField(max_length=50, default='rectangle')
    region_data = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class BoothEvent(models.Model):
    booth_id = models.ForeignKey(Booth, on_delete=models.CASCADE, related_name='events')
    event_name = models.TextField()
    event_description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(end_time__gt=models.F('start_time')), name='valid_time_range')
        ]

    def __str__(self):
        return f"{self.event_name} @ {self.booth}"
    

class Rating(models.Model):
    booth_id = models.ForeignKey(Booth, on_delete=models.CASCADE, related_name='ratings')
    student_number = models.CharField(max_length=64)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(rating__gte=1) & models.Q(rating__lte=5), name='rating_range'),
            models.UniqueConstraint(fields=['booth', 'student_number'], name='unique_booth_student')
        ]

    def __str__(self):
        return f"{self.booth} - {self.student_number}: {self.rating}"


class ContestSetting(models.Model):
    contest_name = models.TextField()
    contest_description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    max_photos_per_student = models.IntegerField(default=3)
    max_photos_per_booth_id = models.IntegerField(default=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'contest_settings'

    def __str__(self):
        return self.contest_name


class ContestWinner(models.Model):
    WINNER_TYPES = [
        ('booth', 'Booth'),
        ('individual', 'Individual')
    ]

    winner_type = models.CharField(max_length=20, choices=WINNER_TYPES)
    booth_id = models.ForeignKey(Booth, on_delete=models.SET_NULL, null=True, blank=True)
    student_number = models.CharField(max_length=64, blank=True, null=True)
    photo_submission = models.ForeignKey('PhotoSubmission', on_delete=models.SET_NULL, null=True, blank=True)
    position = models.IntegerField()
    prize_description = models.TextField(blank=True, null=True)
    announced_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'contest_winners'

    def __str__(self):
        return f"{self.winner_type} - {self.position}"



