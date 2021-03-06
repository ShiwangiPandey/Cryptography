# Generated by Django 4.0.5 on 2022-06-28 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_alter_dfile_dtext_alter_efile_etext'),
    ]

    operations = [
        migrations.CreateModel(
            name='recieved_file',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(default=None, null=True, upload_to='Files/')),
            ],
        ),
        migrations.AlterField(
            model_name='dfile',
            name='dtext',
            field=models.FileField(default=None, null=True, upload_to='dec_files/'),
        ),
        migrations.AlterField(
            model_name='efile',
            name='etext',
            field=models.FileField(default=None, null=True, upload_to='enc_files/'),
        ),
    ]
