# Generated by Django 4.2.7 on 2023-11-22 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mentor', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(choices=[('thenth', '10'), ('eleventh', '11'), ('towelveth', '12')], max_length=9)),
                ('member_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
                ('mentor_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to='mentor.mentor')),
            ],
        ),
    ]
