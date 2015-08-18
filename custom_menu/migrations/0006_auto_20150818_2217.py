# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_menu', '0005_nodeext'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nodeext',
            name='node',
        ),
        migrations.DeleteModel(
            name='NodeExt',
        ),
    ]
