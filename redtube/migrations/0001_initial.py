# Generated by Django 3.1.2 on 2020-10-31 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pornstar',
            fields=[
                ('pornstar_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('link', models.URLField()),
                ('small_thumb_url', models.URLField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('videos', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('astrology', models.CharField(blank=True, max_length=20, null=True)),
                ('height', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('weight', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('rank', models.PositiveIntegerField(blank=True, null=True)),
                ('subscribers', models.PositiveIntegerField(blank=True, null=True)),
                ('views', models.PositiveIntegerField(blank=True, null=True)),
                ('ethnicity', models.CharField(blank=True, max_length=20, null=True)),
                ('hair_color', models.CharField(blank=True, max_length=20, null=True)),
                ('cup_size', models.CharField(blank=True, max_length=5, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('years_active', models.CharField(blank=True, max_length=50, null=True)),
                ('birth_place', models.CharField(blank=True, max_length=200, null=True)),
                ('tattoos', models.CharField(blank=True, max_length=300, null=True)),
                ('piercings', models.CharField(blank=True, max_length=300, null=True)),
                ('measurements', models.CharField(blank=True, max_length=40, null=True)),
                ('background', models.CharField(blank=True, max_length=40, null=True)),
                ('breast_type', models.CharField(blank=True, max_length=20, null=True)),
                ('performer_aka', models.CharField(blank=True, max_length=200, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('video_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('link', models.URLField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('views', models.PositiveIntegerField()),
                ('like_prc', models.PositiveSmallIntegerField()),
                ('duration_sec', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Similar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similar_to', models.PositiveIntegerField()),
                ('pornstar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redtube.pornstar')),
            ],
        ),
        migrations.CreateModel(
            name='PornstarVideos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pornstar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redtube.pornstar')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redtube.video')),
            ],
        ),
    ]
