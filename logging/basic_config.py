import logging

"""
basicConfig()配置根记录器。 它通过使用默认格式化程序创建流处理程序来为日志系统进行基本配置。
如果没有为根记录器定义处理程序，则debug()，info()，warning()，error()和critical()自动调用basicConfig()。
"""
logging.basicConfig(filename='test.log', format='%(filename)s: %(message)s',
                    level=logging.DEBUG)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
