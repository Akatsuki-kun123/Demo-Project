# Generated by Django 3.1 on 2022-06-02 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_answer_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='result_kanji_text',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
    ]
