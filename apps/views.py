from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.models import Group, Service, Partner, ClientComment, Article, Companies, Question, Shop, Agent, AboutUs, \
    AppliedClient, Contact, Email, Statistic
from apps.serializers import GroupModelSerializer, ServiceModelSerializer, PartnerSerializer, ClientCommentSerializer, \
    ArticleSerializer, CompaniesSerializer, QuestionSerializer, ShopSerializer, AgentSerializer, AboutUsSerializer, \
    AppliedClientSerializer, ContactSerializer, ProfileSerializer, EmailSerializer, StatisticSerializer
from apps.tasks import send_email


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
StatisticViewSet = create_viewset(Statistic, StatisticSerializer)

@extend_schema(responses={200: AboutUsSerializer})
class AboutUsAPIView(APIView):
    pagination_class = None
    def get(self, request):
        about_us = AboutUs.objects.first()
        if about_us:
            serializer = AboutUsSerializer(about_us)
            return Response(serializer.data)
        return Response({"detail": "About us not found"})


class AppliedClientCreateApiView(CreateAPIView):
    model = AppliedClient
    serializer_class = AppliedClientSerializer

class ContactCreateApiView(CreateAPIView):
    model = Contact
    serializer_class = ContactSerializer

class ProfileCreateApiView(CreateAPIView):
    model = Partner
    serializer_class = ProfileSerializer

class EmailCreateApiView(CreateAPIView):
    model = Email
    serializer_class = EmailSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        send_email.delay(email, 'Successfully sent email')
        return super().post(request, *args, **kwargs)

