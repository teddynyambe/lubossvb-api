import uuid
from django.db import models

# An Account to track funds


class Account(models.Model):
    account_id = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False, help_text="Account ID")
    name = models.CharField(max_length=50)
