# Generated by Django 2.0.5 on 2018-12-06 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StateLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('source_state', models.CharField(blank=True, db_index=True, default=None, max_length=255, null=True)),
                ('state', models.CharField(db_index=True, max_length=255, verbose_name='Target state')),
                ('transition', models.CharField(max_length=255)),
                ('object_id', models.UUIDField(db_index=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'get_latest_by': 'timestamp',
            },
        ),
    ]
