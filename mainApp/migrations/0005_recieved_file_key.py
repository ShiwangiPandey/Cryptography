# Generated by Django 4.0.4 on 2022-07-02 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_recieved_file_alter_dfile_dtext_alter_efile_etext'),
    ]

    operations = [
        migrations.AddField(
            model_name='recieved_file',
            name='key',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]