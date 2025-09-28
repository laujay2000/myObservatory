import logging
import logging.handlers
import os
class Logger:

    @staticmethod
    def init_log_config(logger_name,filename,when='midnight',interval=1,backup_count=30):#每天的午夜产生一个信息

        log_dir = os.path.dirname(filename)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # 创建日志器对象
        logger = logging.getLogger(logger_name)

        logger.setLevel(logging.DEBUG)
        #logging.DEBUG  调试级别
        #logging.INFO   信息级别
        #logging.WARNING  警告级别
        #logging.ERROR  错误级别
        #logging.CRITICAL  严重错误级别

        # 创建处理器对象
        #控制台对象
        st = logging.StreamHandler()
        # 文件对象
        fh = logging.handlers.TimedRotatingFileHandler(filename,
                                                       when=when,
                                                       interval=interval,
                                                       backupCount=backup_count,
                                                       encoding='utf-8')
        #日志格式信息
        fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"

        formatter = logging.Formatter(fmt)

        #给处理器设置日志格式信息
        st.setFormatter(formatter)
        fh.setFormatter(formatter)

        # 将处理器添加到日志器中
        logger.addHandler(st)
        logger.addHandler(fh)
        return logger

if __name__ == '__main__':
    logger = Logger.init_log_config(__name__,'../log/logs.log')
    logger.debug('我是一个日志级别的信息')
