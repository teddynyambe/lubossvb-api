# Generated by Django 5.0.2 on 2024-02-24 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("member_app", "0007_alter_member_next_of_kin_nrc"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="address_2",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Address 2"
            ),
        ),
    ]
