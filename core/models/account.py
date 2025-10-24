# Best-practice custom user model for Django
from django.contrib.auth.models import AbstractUser
from django.db import models

__all__ = ['User', 'StudentProfile', 'BoothManagerProfile']

class User(AbstractUser):
	class Roles(models.TextChoices):
		STUDENT = 'student', 'Student'
		BOOTH_MANAGER = 'booth_manager', 'Booth Manager'
		SUPERUSER = 'superuser', 'Superuser'

	# first_name = models.CharField(max_length=150, blank=True)
	# last_name = models.CharField(max_length=150, blank=True)
	email = models.EmailField(unique=True, blank=False)
	role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.STUDENT)
	phone_number = models.CharField(max_length=20, blank=True, null=True)
	national_id = models.CharField(max_length=20, blank=True, null=True, unique=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['role']

	def is_student(self):
		return self.role == self.Roles.STUDENT

	def is_booth_manager(self):
		return self.role == self.Roles.BOOTH_MANAGER

	def is_superuser_role(self):
		return self.role == self.Roles.SUPERUSER

	def __str__(self):
		return f"{self.username} ({self.get_role_display()})"


class StudentProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
	student_code = models.CharField(max_length=32, unique=True)
	faculty = models.CharField(max_length=128)
	entrance_year = models.PositiveIntegerField()
	# Add more student-specific fields if needed

	def __str__(self):
		return f"StudentProfile: {self.user.username}"


class BoothManagerProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='booth_manager_profile')
	# Add booth manager-specific fields if needed

	def __str__(self):
		return f"BoothManagerProfile: {self.user.username}"
