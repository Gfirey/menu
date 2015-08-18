# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_menu', '0002_remove_nodemodel_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodemodel',
            name='parent',
            field=models.ForeignKey(null=True, to='custom_menu.NodeModel', blank=True, related_name='children'),
            preserve_default=True,
        ),
    ]
