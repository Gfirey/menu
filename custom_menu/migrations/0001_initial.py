# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NodeModel',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('parent', models.ForeignKey(related_name='children', null=True, to='custom_menu.NodeModel', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
