# coding=utf-8

from models import *
import xadmin
import xadmin.filters
from xadmin import views
from xadmin.plugins.batch import BatchChangeAction

@xadmin.sites.register(views.website.IndexView)
class MainDashboard(object):
    widgets = [
        [
            {"type": "html", "title": "", "content": "<h3>关心城市生活身边事，倾听市民最真实需求！</h3>"},
            {"type": "chart", "model": "ll_admin.carddetail", "chart": "reply_count"},
        ],
        [
            {"type": "list", "model": "ll_admin.carddetail", "params": {"o": "-replyDate"}},
        ]
    ]

# 设置主题选择
@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

# 全局设置
@xadmin.sites.register(views.CommAdminView)
class GlobalSetting(object):
    site_title = '政府直通车' # 设置后台标题
    site_footer = '发呆网络' # 设置页脚
    global_search_models = [CardDetail,] # 全局搜索定制
    global_models_icon = {
        CardDetail: "fa fa-cloud",
    } # 设置每个应用在菜单里的小图标
    menu_style = 'default'  # 'accordion' # 设置菜单展现方式

@xadmin.sites.register(CardDetail)
class cardDetailAdmin(object):

    # 自定义字段
    def open_web(self, instance):
        return """<a href="http://www.hf12345.gov.cn/" target="_blank">Open</a>"""
    open_web.short_description = "源站"
    open_web.allow_tags = True
    open_web.is_column = True

    # listdisplay设置要显示在列表中的字段
    list_display = ['card_id', 'card_title', 'reply_unit', 'hot_count', 'card_source', 'reply_date', 'open_web']

    # 设置字段的链接
    list_display_links = ['card_id', 'card_title']

    # raw_id_fields = ("idc",)
    # style_fields = {"system": "radio-inline"}

    # 设置添加item表单样式
    # wizard_form_list = [
    #     ("第一步", ("title", "type", "replyDate")),
    #     ("第二步", ("reply", "hotCount", "source")),
    #     ("第三步", ("content", "replyContent"))
    # ]

    # 只可读不可编辑的字段
    # readonly_fields = ['cardId']

    # 设置每页显示多少条记录，默认是100条
    list_per_page = 20

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-replyDate',)

    # 设置在列表页可编辑
    list_editable = ['card_title']

    # 定义导出数据格式
    # list_export = {'json', 'xml', 'xls', 'xlsx', 'csv'}

    # 过滤器
    list_filter = [
        'cardId', 'title', 'content', 'replyContent', 'createTime', 'replyDate',
        # ('type', xadmin.filters.MultiSelectFieldListFilter,),
    ]
    # 页面左下角 快速筛选列表
    list_quick_filter = ["type", {"field": "replyDate", "limit": 10}]
    # 搜索字段
    search_fields = ('cardId', 'title', 'content', 'replyContent')
    # 详细时间分层筛选　
    date_hierarchy = 'replyDate'
    relfield_style = "fk-select"

    # 设置内置标签
    show_bookmarks = True
    list_bookmarks = [{
        "title": "西子曼城",
        "query": {"title": ""},
        "order": ("-replyDate",),
        "cols": ("cardId", "title", "hotCount"),
        "search": "西子曼城",
    }]

    # 显示详情
    show_detail_fields = ("card_title")

    # 在编辑表单页会增加按钮，将当前表单保存会新一条数据
    save_as = True

    # 按数学公式计算指定字段
    aggregate_fields = {"replyDate": "min", "hotCount": "max"}

    # 增加布局方式：网格
    grid_layouts = ("table", "thumbnails")

    # 自定义表单样式
    # form_layout = []

    # 记录操作
    reversion_enable = True

    # action操作 可自定义
    actions = [BatchChangeAction, ]
    batch_fields = ("title", "reply", "hotCount")

    # 设置刷新时间规则
    refresh_times = (3, 5, 10)

    data_charts = {
        # "host_service_type_counts": {
        #     'title': u"Host service type count", "x-field": "replyDate",
        #     "y-field": ("cardId",),
        #     "option": {
        #      "series": {"bars": {"align": "center", "barWidth": 0.8, 'show': True}},
        #      "xaxis": {"aggregate": "count", "mode": "categories"},
        #     },
        # },
        # "per_month": {
        #     'title': u"Monthly Users", "x-field": "_chart_month", "y-field": ("cardId",),
        #     "option": {
        #       "series": {"bars": {"align": "center", "barWidth": 0.8, 'show': True}},
        #       "xaxis": {"aggregate": "count", "mode": "categories"},
        #     },
        # },
        "reply_count": {
            'title': u"各个部门回复数", "x-field": "reply", "y-field": ("cardId",), "order": ('-replyDate',),
            "option": {
                "series": {"bars": {"align": "center", "barWidth": 0.8, 'show': True}},
                "xaxis": {"aggregate": "count", "mode": "categories"},
            },
        },
    }

    def _chart_month(self, obj):
        return obj.replyDate.strftime("%m.%d")

    Fieldset = (
        'title', 'content'
        #('base', {'fields': ('title')}),
        #["other", {'fields': ('content', 'replyContent')}]
    )

    # Fieldset = (
    #     ['Main', {
    #         'fields': ('title', 'cardId'),
    #     }],
    #     ['Advance', {
    #         'classes': ('collapse',),  # CSS
    #         'fields': ('content',),
    #     }]
    # )

    actions_on_top = True
    actions_on_bottom = True

    # def get_queryset(self, request):
    #     """函数作用：使当前登录的用户只能看到自己负责的服务器"""
    #     qs = super(MachineInfoAdmin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=UserInfo.objects.filter(user_name=request.user))

    #数据保存时进行一些额外的操作
    # def save_model(self, request, obj, form, change):
    # def delete_model(self, request, obj):
    # common.DeLog.objects.create(**data)  # 创建日志
    # def get_readonly_fields(self, request, obj=None):
    # def change_view(self, request, object_id, form_url='', extra_context=None):

@xadmin.sites.register(RegisterUser)
class registerUserAdmin(object):

    # listdisplay设置要显示在列表中的字段
    list_display = ['userId', 'name', 'age', 'phone', 'wechat', 'score']

    # 设置字段的链接
    list_display_links = ['userId', 'name']

    # 设置每页显示多少条记录，默认是100条
    list_per_page = 20

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-updateTime',)

    # 设置在列表页可编辑
    list_editable = ['name']

    # 定义导出数据格式
    # list_export = {'json', 'xml', 'xls', 'xlsx', 'csv'}

    # 过滤器
    list_filter = [
        'userId', 'name', 'phone',
        # ('type', xadmin.filters.MultiSelectFieldListFilter,),
    ]
    # 页面左下角 快速筛选列表
    #list_quick_filter = ["type", {"field": "replyDate", "limit": 10}]
    # 搜索字段
    search_fields = ('userId', 'name', 'phone', 'wechat')
    # 详细时间分层筛选　
    #date_hierarchy = 'replyDate'
    #relfield_style = "fk-select"

    # 设置内置标签
    show_bookmarks = True
    # list_bookmarks = [{
    #     "title": "西子曼城",
    #     "query": {"title": ""},
    #     "order": ("-replyDate",),
    #     "cols": ("userId", "title", "hotCount"),
    #     "search": "西子曼城",
    # }]

    # 显示详情
    show_detail_fields = ("name")

    # 在编辑表单页会增加按钮，将当前表单保存会新一条数据
    save_as = True

    # 按数学公式计算指定字段
    #aggregate_fields = {"replyDate": "min", "hotCount": "max"}

    # 增加布局方式：网格
    grid_layouts = ("table", "thumbnails")

    # 自定义表单样式
    # form_layout = []

    # 记录操作
    reversion_enable = True

    # action操作 可自定义
    #actions = [BatchChangeAction, ]
    #batch_fields = ("title", "reply", "hotCount")

    # 设置刷新时间规则
    refresh_times = (3, 5, 10)

    # data_charts = {
    #     # "host_service_type_counts": {
    #     #     'title': u"Host service type count", "x-field": "replyDate",
    #     #     "y-field": ("cardId",),
    #     #     "option": {
    #     #      "series": {"bars": {"align": "center", "barWidth": 0.8, 'show': True}},
    #     #      "xaxis": {"aggregate": "count", "mode": "categories"},
    #     #     },
    #     # },
    #     # "per_month": {
    #     #     'title': u"Monthly Users", "x-field": "_chart_month", "y-field": ("cardId",),
    #     #     "option": {
    #     #       "series": {"bars": {"align": "center", "barWidth": 0.8, 'show': True}},
    #     #       "xaxis": {"aggregate": "count", "mode": "categories"},
    #     #     },
    #     # },
    #     "reply_count": {
    #         'title': u"各个部门回复数", "x-field": "reply", "y-field": ("cardId",), "order": ('-replyDate',),
    #         "option": {
    #             "series": {"bars": {"align": "center", "barWidth": 0.8, 'show': True}},
    #             "xaxis": {"aggregate": "count", "mode": "categories"},
    #         },
    #     },
    # }

    # def _chart_month(self, obj):
    #     return obj.replyDate.strftime("%m.%d")

    # Fieldset = (
    #     'title', 'content'
    #     #('base', {'fields': ('title')}),
    #     #["other", {'fields': ('content', 'replyContent')}]
    # )

    # Fieldset = (
    #     ['Main', {
    #         'fields': ('title', 'cardId'),
    #     }],
    #     ['Advance', {
    #         'classes': ('collapse',),  # CSS
    #         'fields': ('content',),
    #     }]
    # )

    #actions_on_top = True
    #actions_on_bottom = True

    # def get_queryset(self, request):
    #     """函数作用：使当前登录的用户只能看到自己负责的服务器"""
    #     qs = super(MachineInfoAdmin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=UserInfo.objects.filter(user_name=request.user))

    #数据保存时进行一些额外的操作
    # def save_model(self, request, obj, form, change):
    # def delete_model(self, request, obj):
    # common.DeLog.objects.create(**data)  # 创建日志
    # def get_readonly_fields(self, request, obj=None):
    # def change_view(self, request, object_id, form_url='', extra_context=None):