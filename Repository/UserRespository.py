#!/usr/bin/env python
# coding=utf-8

from .import models

class UserRespository:

    def fetch_all_by_uid(self, uid):
        ret = models.UserProfile.objects.filter(id=uid).values('name', 'brief', 'head_img',)
        obj = models.UserProfile.objects.filter(id=uid)
        # follower = obj[0].related_name_set.
        # print(follower)
        return ret[0]