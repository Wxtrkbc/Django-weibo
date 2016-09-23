#!/usr/bin/env python
# coding=utf-8


import pika

from weibo import settings
import json


class QueueService:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(settings.QUEUE_HOST))
        self.channel = self.connection.channel()
        self.user_new_weibo = []

    def publish_weibo(self, data):                  # 将微博发送到队列中去
        self.channel.queue_declare(queue='publish_weibo')
        self.channel.basic_publish(exchange='',
                                   routing_key='publish_weibo',
                                   body=json.dumps(data))
        print('P send {}'.format(data))


    # 返回用户微博列表的回掉函数
    def callback(self, ch, method, properties, body):
        print(" [x] Received %r" % (json.loads(body),))
        self.user_new_weibo.append(json.loads(body))


    # 根据用户id返回此用户队列里的微博
    def get_user_weibo(self, user_queue_id):

        self.channel.queue_declare(queue=user_queue_id)

        self.channel.basic_consume(self.callback,
                                   queue=user_queue_id,
                                   no_ack=True)

        self.channel.start_consuming()
        return self.user_new_weibo

    # 根据用户id返回此用户队列里的微博数量
    def get_uesr_weibo_counts(self, user_queue_id):
        queue_obj = self.channel.queue_declare(queue=user_queue_id)
        return queue_obj.method.message_count

    def close_queue(self):
        self.connection.close()