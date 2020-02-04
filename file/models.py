from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import SET_NULL


class File(models.Model):
    name = models.CharField(max_length=50, unique=True)
    file = models.FileField(upload_to='files/')
    uploaded_by = models.ForeignKey(get_user_model(), on_delete=SET_NULL, null=True)
    downloads = models.IntegerField(default=0)
