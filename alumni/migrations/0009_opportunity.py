# Generated by Django 3.2.12 on 2025-02-04 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alumni', '0008_auto_20250203_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('location', models.CharField(choices=[('Remote', 'Remote'), ('On-Site', 'On-Site'), ('Hybrid', 'Hybrid')], default='On-Site', max_length=100)),
                ('opportunity_type', models.CharField(choices=[('Job', 'Job'), ('Internship', 'Internship'), ('Scholarship', 'Scholarship'), ('Fellowship', 'Fellowship'), ('Research', 'Research'), ('Other', 'Other')], default='Job', max_length=50)),
                ('description', models.TextField()),
                ('application_link', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
