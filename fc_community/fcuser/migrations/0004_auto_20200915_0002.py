# Generated by Django 3.1.1 on 2020-09-14 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0003_auto_20200914_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcuser',
            name='useremail',
            field=models.EmailField(max_length=128, verbose_name='사용자 이메일'),
        ),
    ]