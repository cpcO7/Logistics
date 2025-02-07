from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import GroupReadOnlyViewSet, ServiceReadOnlyViewSet, PartnerReadOnlyViewSet, ClientCommentViewSet, \
    ArticleViewSet, CompaniesViewSet, QuestionViewSet, ShopViewSet, AgentViewSet, AboutUsAPIView

router = DefaultRouter()
router.register(r'group', GroupReadOnlyViewSet, basename='group')
router.register(r'service', ServiceReadOnlyViewSet, basename='service')
router.register(r'partner', PartnerReadOnlyViewSet, basename='partner')
router.register(r'client-comment', ClientCommentViewSet, basename='client-comment')
router.register(r'article', ArticleViewSet, basename='article')
router.register(r'companies', CompaniesViewSet, basename='companies')
router.register(r'question', QuestionViewSet, basename='question')
router.register(r'shop', ShopViewSet, basename='shop')
router.register(r'agent', AgentViewSet, basename='agent')

urlpatterns = [
    path('', include(router.urls)),
    path('about-us/', AboutUsAPIView.as_view(), name='about'),
]
