import uuid
from django.db import models
from account_app.models import Account
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from constants import Role


class Member(models.Model):
    # Account details
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    member_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    role = models.CharField(
        _("Role"), max_length=10, choices=Role.choices, default=Role.MEMBER)
    # Personal Details
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    account_id = models.ForeignKey(
        Account, on_delete=models.CASCADE, null=True, blank=True)
    nrc = models.CharField(max_length=11)
    member_mobile = models.CharField(max_length=12)
    address_1 = models.CharField(
        _("Address 1"), max_length=50, null=False)
    address_2 = models.CharField(
        _("Address 2"), max_length=50, null=True, blank=True)
    town = models.CharField(_("Town"), max_length=20)
    province = models.CharField(
        _("Province/State"), max_length=20)
    country = models.CharField(_("Country"), max_length=20)
    # Bank details
    bank_name = models.CharField(
        _("Bank name"), max_length=50)
    branch_name = models.CharField(
        _("Branch name"), max_length=50)
    branch_code = models.CharField(_("Branch code"), max_length=3)
    account_number = models.CharField(
        _("Account Number"), max_length=20, null=False)
    branch_address = models.CharField(
        _("Branch address"), max_length=20)
    # Next of Kin
    next_of_kin_fullname = models.CharField(
        _("Next of Kin (Fullname)"), max_length=30)
    next_of_kin_nrc = models.CharField(
        _("Next of Kin (NRC)"), max_length=11)
    next_of_kin_mobile = models.CharField(
        _("Next of kin mobile"), max_length=12)

    def __str__(self):
        return self.first_name + " " + self.last_name
