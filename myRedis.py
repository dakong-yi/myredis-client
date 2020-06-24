# -*- coding: utf-8 -*-

import redis


class myRedis(object):
    def testConnect(self, host, port, decode=True):
        try:
            r = redis.Redis(host=host, port=port, decode_responses=decode)
            if r.ping():
                return '连接成功'
            else:
                return '连接失败'
        except:
            return '连接失败'

