from hytest import *
from lib.api import GetInfo
import re
import traceback

class getBaidu:
    name = "获取百度网页的HTML源代码文本"
    def teststeps(self):
        global three
        STEP(1,'获取百度网页的HTML源代码文本')
        info = GetInfo.getBaidu()
        ret = info.content.decode('utf8')
        INFO(ret)
        p1 = re.compile(r'(id=lg.*)> </div> <form')
        for one in p1.findall(ret):
            p2 = re.compile(r'(h.*)')
            for two in p2.findall(one):
                STEP(2,'从获取的HTML源代码文本里，解析出id=lg的div标签里面的img标签')
                INFO(two)
                p3 = re.compile(r'(//.*) width')
                for three in p3.findall(two):
                    STEP(3, '返回此img标签上的src属性值')
                    INFO(three)
        STEP(4,'获取响应时间')
        responseTime = info.elapsed.total_seconds()
        INFO(responseTime)
        STEP(5,'断言：如果接口请求时间超过1秒钟，则Assert断言失败，'
               '如果接口返回值不等于"//www.baidu.com/img/bd_logo1.png"，则Assert断言失败')
        expected1 = '//www.baidu.com/img/bd_logo1.png'
        expected2 = 0.1
        try:
            CHECK_POINT('返回消息字体正确', expected2 == three)
            CHECK_POINT('返回消息体正确',expected1>responseTime)
        except Exception:
            #打印异常
            INFO(traceback.format_exc())





    