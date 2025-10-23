from rest_framework import routers
from .views.account import UserViewSet, StudentProfileViewSet, BoothManagerProfileViewSet
from .views.booth import BoothViewSet, BoothEventViewSet, RatingViewSet, ContestSettingViewSet, ContestWinnerViewSet
from .views.content import BoothResourceViewSet, PhotoSubmissionViewSet, PhotoSubmissionAuditViewSet

router = routers.DefaultRouter()

# Account
router.register(r'users', UserViewSet)
router.register(r'student-profiles', StudentProfileViewSet)
router.register(r'booth-manager-profiles', BoothManagerProfileViewSet)

# Booth
router.register(r'booths', BoothViewSet)
router.register(r'booth-events', BoothEventViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'contest-settings', ContestSettingViewSet)
router.register(r'contest-winners', ContestWinnerViewSet)

# Content
router.register(r'booth-resources', BoothResourceViewSet)
router.register(r'photo-submissions', PhotoSubmissionViewSet)
router.register(r'photo-submission-audits', PhotoSubmissionAuditViewSet)

urlpatterns = router.urls
