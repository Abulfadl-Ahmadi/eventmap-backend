
from django.db import models
from django.conf import settings

__all__ = ['BoothResource', 'PhotoSubmission', 'PhotoSubmissionAudit']

class BoothResource(models.Model):
    booth = models.ForeignKey('Booth', on_delete=models.CASCADE, related_name='resources')
    file_name = models.TextField()
    file_url = models.TextField()
    file_type = models.CharField(max_length=128)
    file_size = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'booth_resources'

    def __str__(self):
        return f"{self.file_name} ({self.booth})"
    

class PhotoSubmission(models.Model):
    MODERATION_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    student_number = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=32)
    booth = models.ForeignKey('Booth', on_delete=models.CASCADE, related_name='photos')
    photo_url = models.TextField()
    photo_filename = models.TextField()
    photo_size = models.IntegerField()
    submission_timestamp = models.DateTimeField(auto_now_add=True)
    moderation_status = models.CharField(max_length=20, choices=MODERATION_CHOICES, default='pending')
    moderation_notes = models.TextField(blank=True, null=True)
    moderated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    moderated_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'photo_submissions'

    def __str__(self):
        return f"Photo {self.photo_filename} by {self.student_number}"


class PhotoSubmissionAudit(models.Model):
    submission = models.ForeignKey(PhotoSubmission, on_delete=models.CASCADE, related_name='audits')
    action = models.TextField()  # insert, update, delete, moderate
    old_status = models.TextField(blank=True, null=True)
    new_status = models.TextField(blank=True, null=True)
    moderated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    moderation_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'photo_submission_audit'

    def __str__(self):
        return f"Audit {self.action} for {self.submission_id}"