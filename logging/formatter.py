import logging

logger = logging.getLogger('dev')
logger.setLevel(logging.INFO)
# 创建文件记录
fileHandler = logging.FileHandler('test.log')
fileHandler.setLevel(logging.INFO)
# 创建console输出
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)
# 格式化
formatter = logging.Formatter('%(asctime)s  %(name)s  %(levelname)s: %(message)s')
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)
logger.info('information message')
