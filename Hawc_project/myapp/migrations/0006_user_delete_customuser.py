# Generated by Django 4.2.5 on 2023-12-04 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_customuser_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('password1', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
