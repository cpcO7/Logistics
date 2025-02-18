from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from drf_spectacular.utils import extend_schema_field

from apps.models import Group, Service, Partner, ClientComment, Article, Companies, Question, Shop, \
    Job, TimeManagement, AboutUs, AppliedClient, Contact, Candidate, Email, Statistic, JobCategory


# Creating dynamic serializer classes means that you can combine the same views
def create_serializer(model_class):
    class Meta:
        model = model_class
        fields = '__all__'

    serializer_name = f"{model_class.__name__}Serializer"
    attrs = {"Meta": Meta}

    return type(serializer_name, (ModelSerializer,), attrs)


GroupModelSerializer = create_serializer(Group)
ServiceModelSerializer = create_serializer(Service)
PartnerSerializer = create_serializer(Partner)
ClientCommentSerializer = create_serializer(ClientComment)
ArticleSerializer = create_serializer(Article)
CompaniesSerializer = create_serializer(Companies)
QuestionSerializer = create_serializer(Question)
ShopSerializer = create_serializer(Shop)
AboutUsSerializer = create_serializer(AboutUs)
AppliedClientSerializer = create_serializer(AppliedClient)
ContactSerializer = create_serializer(Contact)
ProfileSerializer = create_serializer(Candidate)
EmailSerializer = create_serializer(Email)
StatisticSerializer = create_serializer(Statistic)


class JobSerializer(ModelSerializer):
    working_time = SerializerMethodField()

    def get_working_time(self, obj):
        return obj.working_time.working_time

    class Meta:
        model = Job
        fields = '__all__'


class JobCategorySerializer(ModelSerializer):
    jobs = JobSerializer(many=True, read_only=True)

    class Meta:
        model = JobCategory
        fields = '__all__'
