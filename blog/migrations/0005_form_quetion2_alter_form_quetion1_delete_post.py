# Generated by Django 4.2.3 on 2023-09-20 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_form_post_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='quetion2',
            field=models.IntegerField(choices=[('select1', 'a.more outgoing, think out loud or'), ('select2', 'b.more reserved, think to yourself')], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='form',
            name='quetion1',
            field=models.IntegerField(choices=[('select1', 'a.expend energy, enjoy groups or'), ('select2', 'b.conserve energy, enjoy one-on-one')]),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
