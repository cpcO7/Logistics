from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Model, CharField, ImageField, URLField, ForeignKey, CASCADE, EmailField, \
    TimeField
from django.db.models.fields import TextField, SmallIntegerField
from location_field.models.plain import PlainLocationField


class Statistic(Model):
    title = CharField("Title", max_length=255)
    value = CharField("Value", max_length=50)

    def __str__(self):
        return f"{self.value} {self.title}"


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
    first_name = CharField("First Name", max_length=255)
    last_name = CharField("Last Name", max_length=255)
    email = CharField("Email", max_length=255)
    phone_number = CharField("Phone Number", max_length=255)
    year_experience = SmallIntegerField("Experience")


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
    working_time = ForeignKey("apps.TimeManagement", CASCADE)
    image = ImageField("Image", upload_to='agent/')
    search = CharField("search", max_length=255, null=True, blank=True)
    location = PlainLocationField(based_fields=['search'], default='41.2994958, 69.2400734')


WEEK_DAYS = [
    ("mon-fri", "Monday - Friday"),
    ("mon-sat", "Monday - Saturday"),
    ("mon-sun", "Monday - Sunday"),
    ("sat-sun", "Saturday - Sunday"),
    ("sun", "Only Sunday"),
]

class AboutUs(Model):
    phone_number = CharField("Phone Number", max_length=255)
    email = EmailField("Email", max_length=255)
    address = CharField("Address", max_length=255)
    facebook = URLField("Facebook", null=True, blank=True)
    twitter = URLField("Twitter", null=True, blank=True)
    instagram = URLField("Instagram", null=True, blank=True)
    linkedin = URLField("LinkedIn", null=True, blank=True)
    telegram = URLField("Telegram", null=True, blank=True)

    work_day = CharField("Work Days", max_length=20, choices=WEEK_DAYS, default="mon-fri")
    work_hour_start = TimeField("Work Start Time", default="09:00")
    work_hour_end = TimeField("Work End Time", default="18:00")

    search = CharField("search", max_length=255, null=True, blank=True)
    location = PlainLocationField(based_fields=['search'], default='41.2994958, 69.2400734')

    class Meta:
        verbose_name_plural = "About Us"

    def __str__(self):
        return f"{self.phone_number}"