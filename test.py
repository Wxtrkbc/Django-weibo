#!/usr/bin/env python
# coding=utf-8


# import os
# os.environ.update({"DJANGO_SETTINGS_MODULE": "weibo.settings"})

# import redis
#
# pool = redis.ConnectionPool(host='115.28.147.110', port=6379)
#
# r = redis.Redis(connection_pool=pool)
# r.set('k1','v1',ex=60)
#
# print(r.get('active_user_1'))

#
# from Repository import UserRespository
#
# r = UserRespository.UserRespository()
# r.fetch_all_by_uid(1)
# print(r)

from Infrastructure import redisOperate
from weibo import settings
redis_obj = redisOperate.redisOperate(**settings.REDIS_CONNECT_DICT)
ret = redis_obj.r.get('active_user_2')
print(ret)


