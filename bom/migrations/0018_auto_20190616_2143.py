# Generated by Django 2.2 on 2019-06-16 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bom', '0017_auto_20190616_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assemblysubparts',
            name='assembly',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bom.Assembly'),
        ),
        migrations.AlterField(
            model_name='assemblysubparts',
            name='subpart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bom.Subpart'),
        ),
    ]