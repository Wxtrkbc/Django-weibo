#!/usr/bin/env python
# coding=utf-8

from .import models


class UserRespository:

    def fetch_all_by_uid(self, uid):
        ret = models.UserProfile.objects.filter(id=uid).values('name', 'brief', 'head_img',)
        ret = list(ret)
        obj = models.UserProfile.objects.get(id=uid)

        try:
            ret[0]['followers'] = len(obj.follow_list)  # 关注的人
        except Exception as e:
            ret[0]['followers'] = 0
        try:
            ret[0]['followerd'] = len(obj.my_followers.select_related()) #粉丝数
        except Exception as e:
            ret[0]['followerd'] = 0

        return ret[0]