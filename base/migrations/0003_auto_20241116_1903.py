# Generated by Django 3.1.12 on 2024-11-16 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20241115_1217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='mobile_number',
            new_name='mobile_no',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='email',
        ),
        migrations.AddField(
            model_name='employee',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='email_id',
            field=models.EmailField(default='example@example.com', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
