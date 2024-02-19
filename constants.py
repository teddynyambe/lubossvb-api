from django.db import models


class Role(models.TextChoices):
    ADMIN = "Admin", "Admin"
    FIN = 'Fin', "Fin"
    MEMBER = "Member", "Member"
