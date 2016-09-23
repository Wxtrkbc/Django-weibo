#!/usr/bin/env python
# coding=utf-8
from django.contrib.auth import authenticate,login
from weibo import settings
import os
from Service import responseService
from Infrastructure import redisOperate

class UserService:

    def __init__(self,UserRespository):
        self.UserRespository = UserRespository

    def login(self, request, username, password):
        user = authenticate(username=username, password=password)
        rep = responseService.RESPONSE
        if user is not None:
            rep['status'] = True
            login(request, user)
            rep['data']['user_id'] = request.user.id
            print('login-user-id.{}'.format())
            user_dir = '{}/{}'.format(settings.USER_HOME_FILE, request.user.id)
            if not os.path.exists(user_dir):
                os.mkdir(user_dir)              # 创建一个用户的家目录以用户的nid为名

            # 往redis里面 将注册的用户id存到redis里面
                redis_obj = redisOperate.redisOperate(**settings.REDIS_CONNECT_DICT)
                redis_obj.r.set('active_user_{}'.format(request.user.id), request.user.id, ex=3600*24)
        else:
            rep['message'] = '用户名或密码错误'
        return rep

    def fetch_all_by_uid(self,uid):
        rep = responseService.RESPONSE
        ret = self.UserRespository.fetch_all_by_uid(uid)
        if ret:
            print(ret,type(ret))
            rep['status'] = True
            rep['data'] = ret
        else:
            rep['message'] = '该用户不存在'
        return rep
