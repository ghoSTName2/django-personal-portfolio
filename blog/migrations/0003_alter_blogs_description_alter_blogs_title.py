# Generated by Django 4.0.3 on 2022-09-30 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogs_delete_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
