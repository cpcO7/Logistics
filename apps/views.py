from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.models import Group, Service, Partner, ClientComment, Article, Companies, Question, Shop, Agent, AboutUs
from apps.serializers import GroupModelSerializer, ServiceModelSerializer, PartnerSerializer, ClientCommentSerializer, \
    ArticleSerializer, CompaniesSerializer, QuestionSerializer, ShopSerializer, AgentSerializer, AboutUsSerializer


# Creating dynamic view classes means that you can combine the same views
def create_viewset(model_class, serializer_class):
    viewset_name = f"{model_class.__name__}ViewSet"

    return type(viewset_name, (ReadOnlyModelViewSet,), {
        "queryset": model_class.objects.order_by('id'),
        "serializer_class": serializer_class
    })


GroupReadOnlyViewSet = create_viewset(Group, GroupModelSerializer)
ServiceReadOnlyViewSet = create_viewset(Service, ServiceModelSerializer)
PartnerReadOnlyViewSet = create_viewset(Partner, PartnerSerializer)
ClientCommentViewSet = create_viewset(ClientComment, ClientCommentSerializer)
ArticleViewSet = create_viewset(Article, ArticleSerializer)
CompaniesViewSet = create_viewset(Companies, CompaniesSerializer)
QuestionViewSet = create_viewset(Question, QuestionSerializer)
ShopViewSet = create_viewset(Shop, ShopSerializer)
AgentViewSet = create_viewset(Agent, AgentSerializer)

@extend_schema(responses={200: AboutUsSerializer})
class AboutUsAPIView(APIView):
    pagination_class = None
    def get(self, request):
        about_us = AboutUs.objects.first()
        if about_us:
            serializer = AboutUsSerializer(about_us)
            return Response(serializer.data)
        return Response({"detail": "About us not found"})

