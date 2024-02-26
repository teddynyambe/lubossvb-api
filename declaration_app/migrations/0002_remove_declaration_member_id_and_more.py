# Generated by Django 5.0.2 on 2024-02-24 21:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("declaration_app", "0001_initial"),
        ("member_app", "0008_alter_member_address_2"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="declaration",
            name="member_id",
        ),
        migrations.AddField(
            model_name="declaration",
            name="admin_fee_amount",
            field=models.DecimalField(
                decimal_places=2,
                default=0.0,
                help_text="Admin fee amount",
                max_digits=10,
            ),
        ),
        migrations.AddField(
            model_name="declaration",
            name="interest_amount",
            field=models.DecimalField(
                decimal_places=2,
                default=0.0,
                help_text="Interest fee amount",
                max_digits=10,
            ),
        ),
        migrations.AddField(
            model_name="declaration",
            name="is_deleted",
            field=models.BooleanField(
                default=False, help_text="Indicated the record is deleted"
            ),
        ),
        migrations.AddField(
            model_name="declaration",
            name="loan_repayment_amount",
            field=models.DecimalField(
                decimal_places=2,
                default=0.0,
                help_text="Loan repayment amount",
                max_digits=10,
            ),
        ),
        migrations.AddField(
            model_name="declaration",
            name="member",
            field=models.ForeignKey(
                help_text="The member this declaration belongs to",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="member_app.member",
            ),
        ),
        migrations.AddField(
            model_name="declaration",
            name="saving_amount",
            field=models.DecimalField(
                decimal_places=2, default=0.0, help_text="Saving amount", max_digits=10
            ),
        ),
        migrations.AddField(
            model_name="declaration",
            name="social_fund_amount",
            field=models.DecimalField(
                decimal_places=2,
                default=0.0,
                help_text="Social fund amount",
                max_digits=10,
            ),
            preserve_default=False,
        ),
    ]