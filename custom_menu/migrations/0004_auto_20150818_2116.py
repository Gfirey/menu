# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_menu', '0003_nodemodel_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('root_item', models.ForeignKey(null=True, verbose_name='root item', related_name='root_item', to='custom_menu.NodeModel', blank=True, editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='nodemodel',
            name='level',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nodemodel',
            name='menu',
            field=models.ForeignKey(null=True, verbose_name='menu', related_name='contained_items', to='custom_menu.Menu', blank=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nodemodel',
            name='url',
            field=models.CharField(blank=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='nodemodel',
            name='parent',
            field=models.ForeignKey(null=True, verbose_name='parent', to='custom_menu.NodeModel', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='nodemodel',
            name='title',
            field=models.CharField(max_length=80),
            preserve_default=True,
        ),
    ]
