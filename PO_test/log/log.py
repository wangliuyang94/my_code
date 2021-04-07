import logging
import time
import os


class DemoLog:

    def log(self):

        # 创建一个日志器
        logger = logging.getLogger("logger")

        # 给日志器设置日志输出的最低等级,低于这个等级的信息，会被忽略
        logger.setLevel(logging.DEBUG)

        # 判断是否已经添加过处理器
        if not logger.handlers:

            # 创建输出到控制台的处理器，再创建一个文件处理器
            sh = logging.StreamHandler()

            # 存放日志的路径不能写绝对路径或者相对路径，因为别的地方的函数调用的时候会找不到位置。这里用到os模块的方法，把这个log包的地址给固定了
            log_path1 = os.path.dirname(os.path.abspath(__file__))
            log_path2 = "/log_data/{}_log".format(time.strftime("%Y_%m_%d", time.localtime()))
            log_path = log_path1 + log_path2
            fh = logging.FileHandler(filename=log_path, encoding="utf-8")

            # 创建一个格式器
            formator = logging.Formatter(fmt="%(asctime)s %(filename)s %(levelname)s %(message)s", datefmt="%Y/%m/%d/%X")

            # 给输出到控制台的处理器加一个格式器，格式器里面已经设置好了格式。再把文件处理器也加上格式器
            sh.setFormatter(formator)
            fh.setFormatter(formator)

            # 给日志器加一个处理器，这个处理器已经设置好了格式器，格式器也设置好了格式，所以现在日志器也已经设置好了格式。再把文件处理器也加到日志器里
            logger.addHandler(sh)
            logger.addHandler(fh)

            # logger.debug('debug信息')
            # logger.info('info信息')
            # logger.warning('warning信息')
            # logger.error('error信息')
            # logger.critical('critical信息')

        return logger


if __name__ == '__main__':
    log = DemoLog()
    log.log().debug('这里是文字内容')
