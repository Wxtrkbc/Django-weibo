#!/usr/bin/env python
# coding=utf-8
from django.shortcuts import render, HttpResponse
import time
import json

from Service import queueService


def publish_wb(request):
    ret = request.GET.get('data', {
        'user_id': 1,
        'text': 'haha',
        'date': time.time()
    })
    print(ret)

    queue_obj = queueService.QueueService()
    queue_obj.publish_weibo(ret)  # 将消息发送到队列中去
    queue_obj.close_queue()  # 关闭连接
    return HttpResponse({'status': True, 'data': 'ret'})  # 直接返回前端成功信息


# 返回用户队列里的微博
def get_user_weibos(request, user_queue_id):
    queue_obj = queueService.QueueService()
    user_weibo_list = queue_obj.get_user_weibo(user_queue_id)
    return HttpResponse(json.dumps({'user_weibo_list': user_weibo_list}))


# 返回用户队列里的微博数量
def get_user_weibos_count(request, user_queue_id):
    queue_obj = queueService.QueueService()
    user_weibo_count = queue_obj.get_uesr_weibo_counts(user_queue_id)
    return HttpResponse(json.dumps({'user_weibo_count': user_weibo_count}))
