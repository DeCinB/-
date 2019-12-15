# Generated by Django 2.2.7 on 2019-12-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0005_order_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='img',
            field=models.ImageField(default='default/staff.png', upload_to='staff', verbose_name='照片'),
        ),
        migrations.AddField(
            model_name='order',
            name='pay',
            field=models.BooleanField(default=False, verbose_name='付款状态'),
        ),
    ]
