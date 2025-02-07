from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Model, CharField, ImageField, URLField, ForeignKey, CASCADE, TextChoices
from django.db.models.fields import TextField, SmallIntegerField, IntegerField


class Statistic(Model):
    title = CharField("Title", max_length=255)
    value = CharField("Value", max_length=50)  # Example: "700+", "9,000+", "100%"
    description = TextField()

    def __str__(self):
        return f"{self.value} {self.title}"


class CentralBlock(Model):
    title = CharField("Title", max_length=255)
    description = TextField("Description")

    def __str__(self):
        return self.title


class CompanyInfo(Model):
    founded_year = IntegerField("Founded Year")
    description = TextField("Description")

    def __str__(self):
        return f"Established in {self.founded_year}"


class Group(Model):
    description = TextField("Text")
    image = ImageField("Image", upload_to='companies/')


class Service(Model):
    title = CharField("Title", max_length=255)
    description = TextField("Description")
    image = ImageField("Image", upload_to='service/')


class Partner(Model):
    title = CharField("Title", max_length=255)
    text = TextField("Text")


class PartnersImage(Model):
    partner = ForeignKey('apps.Partner', CASCADE)
    image = ImageField("Image", upload_to='partner/')


class ClientComment(Model):
    first_name = CharField("First Name", max_length=100)
    job = CharField("Job", max_length=100)
    comment_title = CharField("Comment Title", max_length=255)
    comment = TextField("Comment")
    image = ImageField("Image", upload_to='client/')
    rating = SmallIntegerField("Rating", validators=[MinValueValidator(0), MaxValueValidator(5)])


class Article(Model):
    title = CharField("Title", max_length=255, null=True, blank=True)
    description = TextField("Description")
    image = ImageField("Image", upload_to='article/')


class AppliedClient(Model):
    first_name = CharField("First_Name", max_length=255)
    last_name = CharField("Last_Name", max_length=255)
    email = CharField("Email", max_length=255)
    phone_number = CharField("Phone_Number", max_length=255)
    year_experience = IntegerField("Experience")


class Companies(Model):
    name = CharField("Name", max_length=255, null=True, blank=True)
    image = ImageField("Image", upload_to='companies/')
    url = URLField("Url", max_length=255, blank=True, null=True)

class Question(Model):
    title = CharField("Title", max_length=255)
    body = TextField("Body")

class Answer(Model):
    title = CharField("Title", max_length=255)
    body = TextField("Body")
    question = ForeignKey("apps.Question", CASCADE)

class Shop(Model):
    title = CharField("Title", max_length=255, null=True, blank=True)
    description = TextField("Description")
    image = ImageField("Image", upload_to='shop/')

class TimeManagement(Model):
    working_time = CharField("Value", max_length=255, help_text="Full or Part Time and more")

class Agent(Model):
    first_name = CharField("First Name", max_length=255, null=True, blank=True)
    last_name = CharField("Last Name", max_length=255, null=True, blank=True)
    email = CharField("Email", max_length=255, null=True, blank=True)
    job = CharField("Job", max_length=255, null=True, blank=True)
    address = CharField("Address", max_length=255, null=True, blank=True)
    long = CharField("Longitude", max_length=255, null=True, blank=True)
    lat = CharField("Latitude", max_length=255, null=True, blank=True)
    working_time = ForeignKey("apps.TimeManagement", CASCADE)
    image = ImageField("Image", upload_to='agent/')


class AboutUs(Model):
    phone_number = CharField("Phone Number", max_length=255)
    email = CharField("Email", max_length=255)
    address = CharField("Address", max_length=255)
    long = CharField("Longitude", max_length=255, null=True, blank=True)
    lat = CharField("Latitude", max_length=255, null=True, blank=True)
    facebook = URLField("Facebook", null=True, blank=True)
    twitter = URLField("Twitter", null=True, blank=True)
    instagram = URLField("Instagram", null=True, blank=True)
    linkedin = URLField("LinkedIn", null=True, blank=True)
    telegram = URLField("Telegram", null=True, blank=True)

    class Meta:
        verbose_name_plural = "About Us"

    def __str__(self):
        return f"+{self.phone_number}"