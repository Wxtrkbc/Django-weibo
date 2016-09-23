#!/usr/bin/env python
# coding=utf-8
import redis

class redisOperate:
    def __init__(self, **conn):
        self.pool = redis.ConnectionPool(**conn)
        self.r = redis.Redis(connection_pool=self.pool)