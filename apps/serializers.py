from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from drf_spectacular.utils import extend_schema_field

from apps.models import Group, Service, Partner, PartnersImage, ClientComment, Article, Companies, Question, Shop, \
    Agent, TimeManagement, AboutUs, Answer, AppliedClient


# Creating dynamic serializer classes means that you can combine the same views
def create_serializer(model_class, sub_model_class=None, sub_field=None):
    class Meta:
        model = model_class
        fields = '__all__'

    serializer_name = f"{model_class.__name__}Serializer"
    attrs = {"Meta": Meta}

    if sub_model_class and sub_field:
        related_serializer_name = f"{sub_model_class.__name__}Serializer"

        class RelatedSerializer(ModelSerializer):
            class Meta:
                model = sub_model_class
                fields = '__all__'

        is_many = sub_field.endswith("s")
        if is_many:
            attrs[sub_field] = RelatedSerializer(many=is_many, read_only=True)
        else:
            method_name = f'get_{sub_field}'

            @extend_schema_field(str)
            def get_related_field(self, obj):
                related_obj = getattr(obj, sub_field, None)
                return related_obj.working_time if related_obj else None

            attrs[method_name] = get_related_field  # Adding dynamic method
            attrs[sub_field] = SerializerMethodField(method_name=method_name)
    return type(serializer_name, (ModelSerializer,), attrs)


GroupModelSerializer = create_serializer(Group)
ServiceModelSerializer = create_serializer(Service)
PartnerSerializer = create_serializer(Partner, PartnersImage, "images")
ClientCommentSerializer = create_serializer(ClientComment)
ArticleSerializer = create_serializer(Article)
CompaniesSerializer = create_serializer(Companies)
QuestionSerializer = create_serializer(Question, Answer, "answer")
ShopSerializer = create_serializer(Shop)
AgentSerializer = create_serializer(Agent, TimeManagement, "working_time")
AboutUsSerializer = create_serializer(AboutUs)
AppliedClientSerializer = create_serializer(AppliedClient)