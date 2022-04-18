# Generated by Django 4.0.4 on 2022-04-18 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='질문')),
                ('category', models.CharField(choices=[(0, '일반'), (1, '계정'), (2, '기타')], default=0, max_length=2)),
                ('answer', models.TextField(verbose_name='답변')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('modifier', models.CharField(max_length=20, unique=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('Writer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
