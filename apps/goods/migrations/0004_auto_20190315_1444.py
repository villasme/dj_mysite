# Generated by Django 2.1.7 on 2019-03-15 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20190315_1421'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodbrand',
            options={'verbose_name': '品牌', 'verbose_name_plural': '品牌'},
        ),
        migrations.AlterField(
            model_name='goodbrand',
            name='image',
            field=models.ImageField(max_length=200, upload_to='brand', verbose_name='品牌LOGO'),
        ),
    ]
