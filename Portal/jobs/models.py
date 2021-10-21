from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.first_name


JOB_TYPE = (
    ('Part Time', 'Part Time'),
    ('Full Time', 'Full Time'),
    ('Freelance', 'Freelancer'),
)

CATEGORY = (
    ('Web Design', 'Web Design'),
    ('Graphic Design', 'Graphic Design'),
    ('Web Developing', 'Web Developing'),
    ('Software Engineering', 'Software Engineering'),
    ('HR', 'HR'),
    ('Marketing', 'Marketing'),
)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Any', 'Any'),
)


class JobListing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, editable=False, blank=True)
    title = models.CharField(max_length=100, verbose_name='Titulo del Puesto')
    company_name = models.CharField(max_length=200,default="Istmo Center",verbose_name="Compañia")
    employment_status = models.CharField(choices=JOB_TYPE, max_length=10, verbose_name="Tipo de contrato")
    vacancy = models.CharField(max_length=10, null=True,verbose_name="Vacantes")
    gender = models.CharField(choices=GENDER, max_length=30, null=True, verbose_name="Genero")
    category = models.CharField(choices=CATEGORY, max_length=30,verbose_name="Categoria")
    description = models.TextField(verbose_name="Descripción")
    responsibilities = models.TextField(verbose_name="responsabilidades")
    experience = models.CharField(max_length=100,verbose_name="Experiencia")
    job_location = models.CharField(max_length=120,verbose_name="Provincia")
    Salary = models.CharField(max_length=100, null=True, blank=True,verbose_name="Salario")
    image = models.ImageField(blank=True, upload_to='media', null=True)
    application_deadline = models.DateTimeField(verbose_name="Fecha limite")
    published_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("jobs:job-single", args=[self.id])


class ApplyJob(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    file = models.FileField(null=True)

    def __str__(self):
        return self.name
