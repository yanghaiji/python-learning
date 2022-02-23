import logging

# 使用了根记录器，并且只写入了三则消息。 这是因为默认情况下，仅写入具有级别警告和更高级别的消息
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
