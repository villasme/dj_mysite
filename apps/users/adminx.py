#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
@author: ljt
@license: Apache Licence
@file: adminx.py
@time: 2019/03/14
@contact: liujiantongvip@163.com
@site:
@software: PyCharm

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

import xadmin
from xadmin import views


class ManageAdmin(views.CommAdminView):
    site_title = "我的服务"
    site_footer = "这是我的版权"


xadmin.site.register(views.CommAdminView, ManageAdmin)