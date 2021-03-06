import datetime
import os

import mongoengine

mongoengine.connect(
    't66y',
    alias='t66y',
    username=os.environ.get('T66Y_NAME'),
    password=os.environ.get('T66Y_PASSWD'))


class Articles(mongoengine.Document):
    """Articls，数据保存模型"""
    url = mongoengine.StringField(unique=True)
    title = mongoengine.StringField()
    author = mongoengine.StringField()
    post_date = mongoengine.DateTimeField(default=datetime.datetime.now())
    post_date_str = mongoengine.StringField()
    content = mongoengine.StringField()
    content_no_tag = mongoengine.StringField()
    is_jieba = mongoengine.BooleanField(default=False)
    top_key = mongoengine.ListField(default=[])

    meta = {'db_alias': 't66y', 'indexes': ['url']}


class AnalysisResults(mongoengine.Document):
    """保持分析的数据"""
    date = mongoengine.StringField(unique=True)
    count = mongoengine.IntField(default=0)

    meta = {'db_alias': 't66y', 'indexes': ['date']}