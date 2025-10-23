from rest_framework import routers
from rest_framework_nested import routers as nested_routers

from .views.account import UserViewSet, StudentProfileViewSet, BoothManagerProfileViewSet
from .views.booth import BoothViewSet, BoothEventViewSet, RatingViewSet, ContestSettingViewSet, ContestWinnerViewSet
from .views.content import BoothResourceViewSet, PhotoSubmissionViewSet, PhotoSubmissionAuditViewSet
from .views.login import LoginAPIView
from .views.register import RegisterAPIView


router = routers.DefaultRouter()
booth_router = nested_routers.NestedDefaultRouter(router, r'booths', lookup='booth')
booth_router.register(r'events', BoothEventViewSet, basename='booth-events')
booth_router.register(r'ratings', RatingViewSet, basename='booth-ratings')
booth_router.register(r'resources', BoothResourceViewSet, basename='booth-resources')
booth_router.register(r'photos', PhotoSubmissionViewSet, basename='booth-photos')

# Account
router.register(r'users', UserViewSet)
router.register(r'student-profiles', StudentProfileViewSet)
router.register(r'booth-manager-profiles', BoothManagerProfileViewSet)

# Booth
router.register(r'booths', BoothViewSet)
# router.register(r'booth-events', BoothEventViewSet)
# router.register(r'ratings', RatingViewSet)
router.register(r'contest-settings', ContestSettingViewSet)
router.register(r'contest-winners', ContestWinnerViewSet)

# Content
# router.register(r'booth-resources', BoothResourceViewSet)
# router.register(r'photo-submissions', PhotoSubmissionViewSet)
router.register(r'photo-submission-audits', PhotoSubmissionAuditViewSet)

urlpatterns = router.urls + booth_router.urls

# Login endpoint
from django.urls import path
urlpatterns += [
	path('login/', LoginAPIView.as_view(), name='login'),
	path('register/', RegisterAPIView.as_view(), name='register'),
]
