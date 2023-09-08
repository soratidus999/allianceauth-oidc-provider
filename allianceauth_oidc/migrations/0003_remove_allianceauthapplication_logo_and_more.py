# Generated by Django 4.2.4 on 2023-09-08 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allianceauth_oidc', '0002_alter_allianceauthapplication_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allianceauthapplication',
            name='logo',
        ),
        migrations.AddField(
            model_name='allianceauthapplication',
            name='debug_mode',
            field=models.BooleanField(
                default=False, help_text='Prints token-post request to logging for debuging purposes. These logs are at the Warning Level.'),
        ),
        migrations.AddField(
            model_name='allianceauthapplication',
            name='logo_url',
            field=models.TextField(
                blank=True, help_text='Url to the Applications Icon (128x128), can be a local static file or a full URL', max_length=1024, null=True),
        ),
    ]
