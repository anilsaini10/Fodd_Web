# Generated by Django 2.1.7 on 2019-04-19 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0004_auto_20190419_0137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addsubcategory',
            fields=[
                ('subcatid', models.AutoField(primary_key=True, serialize=False)),
                ('subcatnm', models.CharField(max_length=50)),
                ('catnm', models.CharField(max_length=50)),
                ('subcatdisc', models.CharField(max_length=1000)),
                ('subcaticon', models.CharField(max_length=100)),
                ('subcatprice', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Addsubcat',
        ),
    ]
