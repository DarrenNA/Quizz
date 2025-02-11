# Generated by Django 4.0.4 on 2022-04-13 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0005_auto_20210512_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizzModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('theme', models.CharField(max_length=200)),
                ('niveau', models.IntegerField(max_length=200)),
                ('photo', models.ImageField(upload_to='images/resolution-definition.jpg')),
            ],
        ),
        migrations.AddField(
            model_name='quesmodel',
            name='quizz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Quiz.quizzmodel'),
        ),
    ]
