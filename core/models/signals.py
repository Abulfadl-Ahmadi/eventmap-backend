from django.db.models.signals import post_save
from django.dispatch import receiver
from .account import User, StudentProfile, BoothManagerProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == User.Roles.STUDENT:
            StudentProfile.objects.get_or_create(user=instance)
        elif instance.role == User.Roles.BOOTH_MANAGER:
            BoothManagerProfile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.role == User.Roles.STUDENT and hasattr(instance, 'student_profile'):
        instance.student_profile.save()
    elif instance.role == User.Roles.BOOTH_MANAGER and hasattr(instance, 'booth_manager_profile'):
        instance.booth_manager_profile.save()
