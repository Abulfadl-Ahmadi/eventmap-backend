from rest_framework import routers
from rest_framework_nested import routers as nested_routers

from .views.account import UserViewSet, StudentProfileViewSet, BoothManagerProfileViewSet
from .views.booth import BoothViewSet, BoothEventViewSet, RatingViewSet, ContestSettingViewSet, ContestWinnerViewSet
from .views.content import BoothResourceViewSet, PhotoSubmissionViewSet, PhotoSubmissionAuditViewSet
from .views.login import LoginAPIView
from .views.register import RegisterAPIView
from .views.account import CurrentUserAPIView



router = routers.DefaultRouter()
# Booth must be registered before nested router
router.register(r'booths', BoothViewSet, basename='booths')

router.register(r'events', BoothEventViewSet, basename='booth-events')
# Nested routers for booth
booth_router = nested_routers.NestedDefaultRouter(router, r'booths', lookup='booth')
booth_router.register(r'ratings', RatingViewSet, basename='booth-ratings')
booth_router.register(r'resources', BoothResourceViewSet, basename='booth-resources')
booth_router.register(r'photos', PhotoSubmissionViewSet, basename='booth-photos')

# Account
router.register(r'users', UserViewSet)
router.register(r'student-profiles', StudentProfileViewSet)
router.register(r'booth-manager-profiles', BoothManagerProfileViewSet)

# Other Booth endpoints
router.register(r'contest-settings', ContestSettingViewSet)
router.register(r'contest-winners', ContestWinnerViewSet)

# Content
router.register(r'photo-submission-audits', PhotoSubmissionAuditViewSet)

urlpatterns = router.urls + booth_router.urls

# Login endpoint
from django.urls import path
urlpatterns += [
	path('auth/login/', LoginAPIView.as_view(), name='login'),
	path('auth/register/', RegisterAPIView.as_view(), name='register'),
    path('auth/me/', CurrentUserAPIView.as_view(), name='current-user'),
]
