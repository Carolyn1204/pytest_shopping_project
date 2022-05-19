import datetime
import logging
import os
from common import util
from config import global_parameters as gp
from config import path


class LogUtil:
    def __init__(self):
        log_name = "mylog_" + util.current_time() + ".log"
        self.log_file = os.path.join(path.log_dir, log_name)


    def setMSG(self, level, msg):
        logger = logging.getLogger('shopping-online')
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh = logging.FileHandler(self.log_file)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        if level == 'debug':
            logger.debug(msg)
        elif level == 'info':
            logger.info(msg)
        elif level == 'warning':
            logger.warning(msg)
        elif level == 'error':
            logger.error(msg)

        logger.removeHandler(fh)
        fh.close()

    def debug(self, msg):
        self.setMSG('debug', msg)

    def info(self, msg):
        self.setMSG('info', msg)

    def warning(self, msg):
        self.setMSG('warning', msg)

    def error(self, msg):
        self.setMSG('error', msg)


if __name__ == '__main__':
    l = LogUtil()
    l.info('test!')

