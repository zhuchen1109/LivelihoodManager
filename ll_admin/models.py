# coding=utf-8
from django.db import models

TYPE = (
    (0, u"无"),
    (1, u"咨询"),
    (2, u"建议"),
)

# Create your models here.
class CardDetail(models.Model):

    # 信件编号
    cardId = models.CharField(primary_key=True, max_length=30)
    # 信件标题
    title = models.CharField(default='', max_length=100)
    # 信件类型 咨询：1 建议：2
    type = models.SmallIntegerField(default=0, choices=TYPE)
    # 信件来源
    source = models.CharField(default='', max_length=30)
    # 答复单位
    reply = models.CharField(default='', max_length=30)
    # 人气
    hotCount = models.IntegerField(default=0)
    # 回复时间
    replyDate = models.DateTimeField()
    # 请求参数
    isSearchPassWord = models.CharField(default='', max_length=40)
    # 请求参数
    tag = models.CharField(default='', max_length=40)
    # 来信时间
    createTime = models.DateTimeField()
    # 信件内容
    content = models.TextField(default='')
    # 回复内容
    replyContent = models.TextField(default='')

    def card_id(self):
        return self.cardId
    card_id.short_description = '编号'
    card_id.admin_order_field = 'cardId'

    def card_title(self):
        return self.title
    card_title.short_description = '标题'
    card_title.admin_order_field = 'title'

    def reply_unit(self):
        return self.reply
    reply_unit.short_description = '答复单位'
    reply_unit.admin_order_field = 'reply'

    def hot_count(self):
        return self.hotCount
    hot_count.short_description = '人气'
    hot_count.admin_order_field = 'hotCount'

    def card_source(self):
        return self.source
    card_source.short_description = '信件来源'
    card_source.admin_order_field = 'source'

    def reply_date(self):
        return self.replyDate.strftime('%Y-%m-%d')
    reply_date.short_description = '回复时间'
    reply_date.admin_order_field = 'replyDate'

    # 指定详情页的标题
    def __str__(self):
        if len(self.title) > 25:
            return self.title[:25] + '...'
        else:
            return self.title

    class Meta:
        db_table = 'll_card_detail'
        verbose_name = u"合肥直通车"
        verbose_name_plural = verbose_name

class RegisterUser(models.Model):
    # userid
    userId = models.AutoField(primary_key=True)
    # 姓名
    name = models.CharField(default='', max_length=30)
    # 年龄
    age = models.IntegerField(default=0)
    # 手机号
    phone = models.CharField(default='', max_length=30)
    # 微信号
    wechat = models.CharField(default='', max_length=50)
    # 芝麻分
    score = models.IntegerField(default=0)
    # 银行卡号
    bankNum = models.CharField(default='', max_length=30)
    # 银行地址
    bank = models.CharField(default='', max_length=30)
    # 身份证号
    card = models.CharField(default='', max_length=30)
    # 地址
    address = models.CharField(default='', max_length=100)
    # 配偶
    wife = models.CharField(default='', max_length=20)
    # 配偶电话
    wifePhone = models.CharField(default='', max_length=30)
    # 父亲
    father = models.CharField(default='', max_length=20)
    # 父亲电话
    fatherPhone = models.CharField(default='', max_length=30)
    # 母亲
    mother = models.CharField(default='', max_length=20)
    # 母亲电话
    motherPhone = models.CharField(default='', max_length=30)
    # 同事
    workmate = models.CharField(default='', max_length=20)
    # 同事电话
    workmatePhone = models.CharField(default='', max_length=30)
    # 朋友
    friend = models.CharField(default='', max_length=20)
    # 朋友电话
    friendPhone = models.CharField(default='', max_length=30)
    # 公司名称
    workUnit = models.CharField(default='', max_length=40)
    # 职位
    work = models.CharField(default='', max_length=20)
    # 单位电话
    unitPhone = models.CharField(default='', max_length=30)
    # 单位地址
    workAddress = models.CharField(default='', max_length=100)
    # 社保
    socialSecurity = models.CharField(default='', max_length=30)
    # 注册时间
    createTime = models.DateTimeField(auto_now_add=True)
    # 更新时间
    updateTime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'register_user'
        verbose_name = u"金融注册用户"
        verbose_name_plural = verbose_name
