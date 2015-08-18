# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_menu', '0004_auto_20150818_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='NodeExt',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('selected_patterns', models.TextField(blank=True)),
                ('node', models.OneToOneField(to='custom_menu.NodeModel', related_name='ext')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
