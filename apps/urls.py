from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import GroupReadOnlyViewSet, ServiceReadOnlyViewSet, PartnerReadOnlyViewSet, ClientCommentViewSet, \
    ArticleViewSet, CompaniesViewSet, QuestionViewSet, ShopViewSet, JobViewSet, AboutUsAPIView, \
    AppliedClientCreateApiView, ContactCreateApiView, ProfileCreateApiView, EmailCreateApiView, StatisticViewSet, \
    JobCategoryListAPIView

router = DefaultRouter()
router.register(r'group', GroupReadOnlyViewSet, basename='group')
router.register(r'service', ServiceReadOnlyViewSet, basename='service')
router.register(r'partner', PartnerReadOnlyViewSet, basename='partner')
router.register(r'client-comment', ClientCommentViewSet, basename='client-comment')
router.register(r'article', ArticleViewSet, basename='article')
router.register(r'companies', CompaniesViewSet, basename='companies')
router.register(r'question', QuestionViewSet, basename='question')
router.register(r'shop', ShopViewSet, basename='shop')
router.register(r'job', JobViewSet, basename='job')
router.register(r'statistic', StatisticViewSet, basename='statistic')

urlpatterns = [
    path('', include(router.urls)),
    path('about-us/', AboutUsAPIView.as_view(), name='about'),
    path('applied-client/', AppliedClientCreateApiView.as_view(), name='applied-client'),
    path('contact-create/', ContactCreateApiView.as_view(), name='contact-create'),
    path('candidate-create/', ProfileCreateApiView.as_view(), name='candidate-create'),
    path('email-create/', EmailCreateApiView.as_view(), name='email-create'),
    path('job-category/', JobCategoryListAPIView.as_view({'get': 'list'}), name='job-category'),
]
