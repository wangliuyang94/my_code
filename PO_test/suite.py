import unittest
import HTMLTestRunner
import time


# 找到用例。 defaultTestLoader 是用来配置默认加载的用例的，discover是用来找用例的
file_dir = './page_case/'
suite = unittest.defaultTestLoader.discover(start_dir=file_dir, pattern='*test.py')

now = time.strftime('%Y-%m-%d %H-%M-%S')
report_name = '测试报告名称'
report_title = '测试报告标题'
report_desc = '测试报告描述'

# 创建一个文本,HTML是二进制的，所以要用wb。verbosity后面可以设置0、1、2，代表报告的详细程度，2是最详细
with open('./report/HTML_{}_report.html'.format(now), 'wb') as f:
    HTMLTestRunner.HTMLTestRunner(stream=f,
                                  verbosity=2,
                                  title=report_title,
                                  description=report_desc).run(suite)