# Generated by Django 3.2.12 on 2022-04-11 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0003_quizmodel_totalques'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quesmodel',
            old_name='question',
            new_name='ques',
        ),
        migrations.DeleteModel(
            name='QuizModel',
        ),
    ]