# Generated by Django 4.0 on 2022-09-01 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cdnProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=20)),
                ('country', models.CharField(blank=True, max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_En', models.CharField(default=None, max_length=20)),
                ('title_Fa', models.CharField(default=None, max_length=20)),
                ('URL', models.URLField()),
                ('IP', models.CharField(default=None, max_length=30)),
                ('location', models.CharField(default=None, max_length=3)),
                ('cdn_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_api.cdnprovider')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default=None, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_api.site')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_api.subject')),
            ],
        ),
        migrations.AddField(
            model_name='site',
            name='subject',
            field=models.ManyToManyField(through='web_api.SubjectSite', to='web_api.Subject'),
        ),
        migrations.CreateModel(
            name='QualityOfService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jitter', models.DecimalField(decimal_places=4, max_digits=19)),
                ('delay', models.DecimalField(decimal_places=4, max_digits=19)),
                ('load_time', models.DecimalField(decimal_places=4, max_digits=19)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_api.site')),
            ],
        ),
    ]