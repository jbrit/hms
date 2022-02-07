from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class BaseModel(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class NamedBaseModel(BaseModel):
    name = models.CharField(max_length=200)

    class Meta:
        abstract = True


class Organization(NamedBaseModel):
    description = models.TextField()
    services = models.TextField()


class Equipment(NamedBaseModel):
    pass


class Patient(NamedBaseModel):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    pass


class Referral(BaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class Incident(BaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    description = models.TextField()
