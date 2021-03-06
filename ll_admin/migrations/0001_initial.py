# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-09 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardDetail',
            fields=[
                ('cardId', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('title', models.CharField(default=b'', max_length=100)),
                ('type', models.SmallIntegerField(choices=[(0, '\u65e0'), (1, '\u54a8\u8be2'), (2, '\u5efa\u8bae')], default=0)),
                ('source', models.CharField(default=b'', max_length=30)),
                ('reply', models.CharField(default=b'', max_length=30)),
                ('hotCount', models.IntegerField(default=0)),
                ('replyDate', models.DateTimeField()),
                ('isSearchPassWord', models.CharField(default=b'', max_length=40)),
                ('tag', models.CharField(default=b'', max_length=40)),
                ('createTime', models.DateTimeField()),
                ('content', models.TextField(default=b'')),
                ('replyContent', models.TextField(default=b'')),
            ],
            options={
                'db_table': 'll_card_detail',
                'verbose_name': '\u5408\u80a5\u76f4\u901a\u8f66',
                'verbose_name_plural': '\u5408\u80a5\u76f4\u901a\u8f66',
            },
        ),
        migrations.CreateModel(
            name='RegisterUser',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=b'', max_length=30)),
                ('age', models.IntegerField(default=0)),
                ('phone', models.IntegerField(default=0)),
                ('wechat', models.CharField(default=b'', max_length=50)),
                ('score', models.IntegerField(default=0)),
                ('bankNum', models.IntegerField(default=20)),
                ('bank', models.CharField(default=b'', max_length=30)),
                ('card', models.CharField(default=b'', max_length=30)),
                ('address', models.CharField(default=b'', max_length=100)),
                ('wife', models.CharField(default=b'', max_length=20)),
                ('wifePhone', models.IntegerField(default=0)),
                ('father', models.CharField(default=b'', max_length=20)),
                ('fatherPhone', models.IntegerField(default=0)),
                ('mother', models.CharField(default=b'', max_length=20)),
                ('motherPhone', models.IntegerField(default=0)),
                ('workmate', models.CharField(default=b'', max_length=20)),
                ('workmatePhone', models.IntegerField(default=0)),
                ('friend', models.CharField(default=b'', max_length=20)),
                ('friendPhone', models.IntegerField(default=0)),
                ('workUnit', models.CharField(default=b'', max_length=40)),
                ('work', models.CharField(default=b'', max_length=20)),
                ('unitPhone', models.IntegerField(default=0)),
                ('workAddress', models.CharField(default=b'', max_length=100)),
                ('socialSecurity', models.CharField(default=b'', max_length=30)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'register_user',
                'verbose_name': '\u91d1\u878d\u6ce8\u518c\u7528\u6237',
                'verbose_name_plural': '\u91d1\u878d\u6ce8\u518c\u7528\u6237',
            },
        ),
    ]
