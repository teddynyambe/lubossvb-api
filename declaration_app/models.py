import uuid
from django.db import models
from member_app.models import Member
from account_app.models import Account

# Create your models here.

# Declaration made by a member


class Declaration(models.Model):
    declaration_id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False, help_text="Globally Unique Identifier")
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    declaration_date = models.DateTimeField(
        auto_now_add=True, help_text="The date and time declaration made.")
    # saving_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Saving amount")
    # social_fund_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Social fund amount")
    # admin_fee_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Admin fee amount")
    # interest_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Interest fee amount")
    # loan_repayment_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Loan repayment amount")


# Transactions categorized by account affected by the transaction
class TransactionType(models.Model):
    transaction_type_id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, help_text="FK Transaction Type ID")
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    account = models.ForeignKey(Account, on_delete=models.CASCADE,
                                help_text="FK Account_ID affected by this transaction")


class TransactionTypeDeclaration(models.Model):
    declaration = models.ForeignKey(
        Declaration, null=False, on_delete=models.CASCADE, help_text="FK Declaration ID")
    transaction_type = models.ForeignKey(
        TransactionType, null=False, on_delete=models.CASCADE, help_text="FK transaction_type_id track")
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Amount for the transaction")


class Transaction(models.Model):
    transaction_id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True)
    transaction_date = models.DateTimeField(
        auto_now_add=True, help_text="Date payment made against the declaration")
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Total Amount of declared amount")
    declaration = models.ForeignKey(
        Declaration, null=False, on_delete=models.CASCADE, help_text="FK Declaration ID")
