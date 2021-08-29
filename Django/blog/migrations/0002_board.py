# Generated by Django 3.2.5 on 2021-08-15 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('contents', models.TextField(max_length=1000, null=True)),
                ('image', models.FileField(upload_to='')),
                ('views', models.IntegerField(default=0)),
            ],
        ),
    ]