from PIL import Image
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Model, CharField, ImageField, URLField, ForeignKey, CASCADE, EmailField, \
    TimeField, DateTimeField, FileField
from django.db.models.fields import TextField, SmallIntegerField
from django_ckeditor_5.fields import CKEditor5Field
from location_field.models.plain import PlainLocationField


def validate_image_size(image):
    max_size = 10 * 1024 * 1024  # 10MB
    if image.size > max_size:
        raise ValidationError("❌ Image size must be less than 10 MB!")


class Statistic(Model):
    title = CharField("Title", max_length=255)
    value = CharField("Value", max_length=50)

    def __str__(self):
        return f"{self.title}  --  {self.value}"


class Group(Model):
    description = TextField("Text")
    image = ImageField("Image", upload_to='companies/')

    def __str__(self):
        return self.description


class Service(Model):
    title = CharField("Title", max_length=255)
    description = TextField("Description")
    image = ImageField("Image", upload_to='service/')

    def __str__(self):
        return self.title


class Partner(Model):
    title = CharField("Title", max_length=255)
    text = TextField("Text")
    image = ImageField("Image", upload_to='partners/')

    def __str__(self):
        return self.title

    def clean(self):
        if self.image:
            validate_image_size(self.image)

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Partner"

class ClientComment(Model):
    first_name = CharField("First Name", max_length=100)
    job = CharField("Job", max_length=100)
    comment_title = CharField("Comment Title", max_length=255)
    comment = TextField("Comment")
    image = ImageField("Image", upload_to='client/')
    rating = SmallIntegerField("Rating", validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.first_name} {self.job}"


class Article(Model):
    title = CharField("Title", max_length=255, null=True, blank=True)
    description = CKEditor5Field("Description")
    image = ImageField("Image", upload_to='article/')

    def __str__(self):
        if hasattr(self, 'title'):
            return self.title

        return (self.description[:20] + "...") if len(self.description) > 20 else self.description


class AppliedClient(Model):
    first_name = CharField("First Name", max_length=255)
    last_name = CharField("Last Name", max_length=255)
    email = CharField("Email", max_length=255)
    phone_number = CharField("Phone Number", max_length=255)
    year_experience = SmallIntegerField("Experience")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Companies(Model):
    name = CharField("Name", max_length=255, null=True, blank=True)
    image = FileField("Image", upload_to='companies/')
    url = URLField("Url", max_length=255, blank=True, null=True)

    def __str__(self):
        if hasattr(self, 'name'):
            return f"{self.name}"

    class Meta:
        verbose_name_plural = "Companies"


class Question(Model):
    question = CharField("Question", max_length=255)
    answer = TextField("Answer")

    def __str__(self):
        return self.question


class Shop(Model):
    title = CharField("Title", max_length=255, null=True, blank=True)
    description = TextField("Description")
    image = ImageField("Image", upload_to='shop/')

    def __str__(self):
        return self.title


class TimeManagement(Model):
    working_time = CharField("Value", max_length=255, help_text="Full or Part Time and more")

    def __str__(self):
        return self.working_time


class Agent(Model):
    first_name = CharField("First Name", max_length=255, null=True, blank=True)
    last_name = CharField("Last Name", max_length=255, null=True, blank=True)
    email = CharField("Email", max_length=255, null=True, blank=True)
    job = CharField("Job", max_length=255)
    address = CharField("Address", max_length=255, null=True, blank=True)
    working_time = ForeignKey("apps.TimeManagement", CASCADE)
    image = ImageField("Image", upload_to='agent/')
    search = CharField("search", max_length=255, null=True, blank=True)
    location = PlainLocationField(based_fields=['search'], default='41.2994958, 69.2400734')

    def __str__(self):
        return self.job


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


class Contact(Model):
    first_name = CharField("First Name", max_length=255, null=True, blank=True)
    last_name = CharField("Last Name", max_length=255, null=True, blank=True)
    email = EmailField("Email", max_length=255, null=True, blank=True)
    website = URLField("Website", max_length=255, null=True, blank=True)
    theme = CharField("Theme", max_length=255, null=True, blank=True)
    comment = TextField("Comment")
    phone_number = CharField("Phone Number", max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.email}"


class Candidate(Model):
    first_name = CharField("First Name", max_length=255)
    last_name = CharField("Last Name", max_length=255)
    birthday = DateTimeField("Birthday")
    country = CharField("Country", max_length=255, null=True, blank=True)
    city = CharField("City", max_length=255, null=True, blank=True)
    itin = CharField("ITIN", max_length=255, null=True, blank=True)

    def __str__(self):
        return self.first_name


class Email(Model):
    email = EmailField("Email", max_length=255)

    def __str__(self):
        return self.email
