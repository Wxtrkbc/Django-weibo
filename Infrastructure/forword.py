#!/usr/bin/env python
# coding=utf-8

from Service import queueService
from Infrastructure import redisOperate
import json

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weibo.settings")

import django
django.setup()
from Repository import models
from weibo import settings

class Forword:
    def __init__(self):
        self.queue_obj = queueService.QueueService()
        self.redis_obj = redisOperate.redisOperate(**settings.REDIS_CONNECT_DICT)
        self.listen_publish_queue()

    def save_weibo_db(self, weibo_data):
        print(type(weibo_data), weibo_data, '----')

        weibo_object = models.Weibo.objects.create(**weibo_data)

        print(weibo_object.id, '--1--')
        return weibo_object.id

    def push_followers(self,weibo_data, weibo_id):
        # 根据当前这条微博的用户id转发给在线关注该用户的好友
        weibo_data['weibo_id'] = weibo_id
        wb_user = models.UserProfile.objects.get(id=weibo_data.get('user_id'))
        print(wb_user.my_followers.select_related())
        for follower in list(wb_user.my_followers.select_related()):
            queue_name = str(follower.id)
            print(follower.id,'6666')
            # follower_is_active = self.redis_obj.r.get('active_user_{}'.format(follower.id))
            follower_is_active = self.redis_obj.r.get('active_user_2')
            print(follower_is_active,'-----')
            if follower_is_active:
                self.queue_obj.channel.queue_declare(queue=queue_name)
                self.queue_obj.channel.basic_publish(exchange='',
                                                 routing_key=queue_name,
                                                 body=json.dumps(weibo_data))

                print('push to{}.{}'.format(queue_name,weibo_data))

    def callback(self, ch, method, properties, body):
        print(" [x] Received %r" % (json.loads(str(body,encoding="utf-8"))))
        weibo_data = json.loads(str(body, encoding="utf-8"))
        weibo_id = self.save_weibo_db(weibo_data)
        self.push_followers(weibo_data, weibo_id)

    def listen_publish_queue(self):
        '''
         一旦收到微博，保存到数据库，推送关注者
        :return:
        '''
        self.queue_obj.channel.queue_declare(queue='publish_weibo')

        self.queue_obj.channel.basic_consume(self.callback,
                                   queue='publish_weibo',
                                   no_ack=True)

        self.queue_obj.channel.start_consuming()


forword = Forword()


