
# --- Imports ---
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models.account import User, StudentProfile, BoothManagerProfile
from .models.booth import Booth, BoothEvent, Rating, ContestSetting, ContestWinner
from .models.content import BoothResource, PhotoSubmission, PhotoSubmissionAudit

# --- User/Admin ---

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'student_code', 'faculty', 'entrance_year')
	search_fields = ('user__username', 'student_code', 'faculty')
	autocomplete_fields = ('user',)

@admin.register(BoothManagerProfile)
class BoothManagerProfileAdmin(admin.ModelAdmin):
	list_display = ('user',)
	search_fields = ('user__username',)
	autocomplete_fields = ('user',)

# --- Booth ---
@admin.register(Booth)
class BoothAdmin(admin.ModelAdmin):
	list_display = ('name', 'community_name', 'region_type', 'created_at')
	search_fields = ('name', 'community_name')
	list_filter = ('region_type',)
	readonly_fields = ('created_at', 'updated_at')

@admin.register(BoothEvent)
class BoothEventAdmin(admin.ModelAdmin):
	list_display = ('event_name', 'booth', 'start_time', 'end_time')
	search_fields = ('event_name', 'booth__name')
	list_filter = ('start_time', 'end_time')
	autocomplete_fields = ('booth',)
	readonly_fields = ('created_at', 'updated_at')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
	list_display = ('booth', 'student_number', 'rating', 'created_at')
	search_fields = ('booth__name', 'student_number')
	list_filter = ('rating',)
	autocomplete_fields = ('booth',)
	readonly_fields = ('created_at',)

@admin.register(ContestSetting)
class ContestSettingAdmin(admin.ModelAdmin):
	list_display = ('contest_name', 'start_date', 'end_date', 'is_active')
	search_fields = ('contest_name',)
	list_filter = ('is_active',)
	readonly_fields = ('created_at', 'updated_at')

@admin.register(ContestWinner)
class ContestWinnerAdmin(admin.ModelAdmin):
	list_display = ('winner_type', 'booth', 'student_number', 'position', 'announced_at')
	search_fields = ('winner_type', 'booth__name', 'student_number')
	list_filter = ('winner_type',)
	autocomplete_fields = ('booth', 'photo_submission')
	readonly_fields = ('announced_at', 'created_at')

# --- Content ---
@admin.register(BoothResource)
class BoothResourceAdmin(admin.ModelAdmin):
	list_display = ('file_name', 'booth', 'file_type', 'file_size', 'created_at')
	search_fields = ('file_name', 'booth__name')
	list_filter = ('file_type',)
	autocomplete_fields = ('booth',)
	readonly_fields = ('created_at',)

@admin.register(PhotoSubmission)
class PhotoSubmissionAdmin(admin.ModelAdmin):
	list_display = ('photo_filename', 'student_number', 'booth', 'moderation_status', 'created_at')
	search_fields = ('photo_filename', 'student_number', 'booth__name')
	list_filter = ('moderation_status', 'created_at')
	autocomplete_fields = ('booth', 'moderated_by')
	readonly_fields = ('created_at', 'updated_at', 'submission_timestamp')

@admin.register(PhotoSubmissionAudit)
class PhotoSubmissionAuditAdmin(admin.ModelAdmin):
	list_display = ('submission', 'action', 'old_status', 'new_status', 'moderated_by', 'created_at')
	search_fields = ('submission__id', 'action', 'moderated_by__username')
	list_filter = ('action', 'created_at')
	autocomplete_fields = ('submission', 'moderated_by')
	readonly_fields = ('created_at',)

@admin.register(User)
class UserAdmin(BaseUserAdmin):
	fieldsets = BaseUserAdmin.fieldsets + (
		('Additional Info', {'fields': ('role', 'phone_number', 'national_id')}),
	)
	list_display = BaseUserAdmin.list_display + ('role', 'phone_number', 'national_id')
	search_fields = BaseUserAdmin.search_fields + ('phone_number', 'national_id')

