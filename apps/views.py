from django.template.loader import render_to_string
from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.models import Group, Service, Partner, ClientComment, Article, Companies, Question, Shop, Job, AboutUs, \
    AppliedClient, Contact, Email, Statistic, JobCategory, CompanyCategory
from apps.serializers import GroupModelSerializer, ServiceModelSerializer, PartnerSerializer, ClientCommentSerializer, \
    ArticleSerializer, CompaniesSerializer, QuestionSerializer, ShopSerializer, JobSerializer, AboutUsSerializer, \
    AppliedClientSerializer, ContactSerializer, ProfileSerializer, EmailSerializer, StatisticSerializer, \
    JobCategorySerializer, CompanyCategorySerializer
from apps.tasks import send_email
from root.settings import SERVER, WEBSITE


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
JobViewSet = create_viewset(Job, JobSerializer)
StatisticViewSet = create_viewset(Statistic, StatisticSerializer)
JobCategoryListAPIView = create_viewset(JobCategory, JobCategorySerializer)
CompanyCategoryListAPIView = create_viewset(CompanyCategory, CompanyCategorySerializer)

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
        msg = render_to_string('mail_template.html', context={'website': WEBSITE, 'server': SERVER})
        send_email.delay(email, msg, 'Kayili M Group LLC')
        return super().post(request, *args, **kwargs)
