from django.db import models

class Organization(models.Model):
    id = 1
    name = models.CharField(max_length=120, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class zona(models.Model):
    organization = models.ForeignKey(
    'organizations.Organization',
    on_delete=models.CASCADE,
    related_name='zonas_organization',
    default = 1
    )
    name = models.CharField(max_length=120)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
