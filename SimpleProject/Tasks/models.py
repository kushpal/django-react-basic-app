from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class JsonFileUpload(models.Model):
    data = models.JSONField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        """."""
        managed = True
        db_table = "json_file_upload_table"
        ordering = ["-pk"]
