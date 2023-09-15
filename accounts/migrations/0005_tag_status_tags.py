# Generated by Django 4.1.4 on 2023-09-05 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_status_products_status_requester_alter_status_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='status',
            name='tags',
            field=models.ManyToManyField(to='accounts.tag'),
        ),
    ]
