# Generated by Django 5.0.2 on 2024-02-15 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("member_app", "0002_alter_member_member_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="member",
            name="account_number",
            field=models.CharField(
                default="111111111", max_length=20, verbose_name="Account Number"
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="address_1",
            field=models.CharField(
                default="Need Address here.", max_length=50, verbose_name="Address 1"
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="address_2",
            field=models.CharField(max_length=50, null=True, verbose_name="Address 2"),
        ),
        migrations.AddField(
            model_name="member",
            name="bank_name",
            field=models.CharField(
                default="data needed", max_length=50, verbose_name="Bank name"
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="branch_address",
            field=models.CharField(
                default="data needed", max_length=20, verbose_name="Branch address"
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="branch_code",
            field=models.CharField(
                default=101, max_length=3, verbose_name="Branch code"
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="branch_name",
            field=models.CharField(
                default="data needed", max_length=50, verbose_name="Branch name"
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="country",
            field=models.CharField(
                default="Zambia", max_length=20, verbose_name="Country"
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="member_mobile",
            field=models.CharField(default="260977760473", max_length=12),
        ),
        migrations.AddField(
            model_name="member",
            name="next_of_kin_fullname",
            field=models.CharField(
                default="data needed",
                max_length=30,
                verbose_name="Next of Kin (Fullname)",
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="next_of_kin_mobile",
            field=models.CharField(
                default="data needed", max_length=12, verbose_name="Next of kin mobile"
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="nrc",
            field=models.CharField(default="data needed", max_length=11),
        ),
        migrations.AddField(
            model_name="member",
            name="province",
            field=models.CharField(
                default="Lusaka", max_length=20, verbose_name="Province/State"
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="role",
            field=models.CharField(
                choices=[("Admin", "Admin"), ("Fin", "Fin"), ("Member", "Member")],
                default="Member",
                max_length=10,
                verbose_name="Role",
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="town",
            field=models.CharField(
                default="data needed", max_length=20, verbose_name="Town"
            ),
        ),
    ]