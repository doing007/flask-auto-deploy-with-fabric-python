"""Log messages
"""
__version__ = '0.1.0'
__author__ = 'Mohan <reddimohana@gmail.com>'

__all__ = [
    'info', 'debug', 'error',
    'warning', 'config'
]

import os
import errno

import time
import datetime

class Logger(object):
    """docstring for Logger."""
    def __init__(self, log_url = None):
        """docstring for Logger."""
        super(Logger, self).__init__()
        self.log_dir = os.getcwd() if log_url is None else log_url
        self.log_file = self._get_log_file()
        # self.debug = False

        # Print saying log file created this location


    def info(self, msg):
        self._log(msg, 'INFO')


    def error(self, msg):
        self._log(msg, 'ERROR')


    def warning(self, msg):
        self._log(msg, 'WARNING')


    def debug(self, msg):
        self._log(msg, 'DEBUG')


    def _log(self, msg, msg_type):
        msg = "[" + str(self._get_date_time()) + "]" + "[" + msg_type + "] " + msg
        color = self._colors(msg_type)
        end_c = self._colors('ENDC')
        print(color + msg + end_c)


    def _get_log_file(self):
        log_dir = self.log_dir + "/logs/"
        if not os.path.exists(log_dir):
            try:
                os.makedirs(log_dir)
                self.info("Log dir created at " + log_dir)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    self.error("No permissions to create Log dir at " + self.log_dir)
                # raise

        # return log_dir

    def _get_date_time(self):
        time_stamp = time.time()
        return datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M:%S')


    def config(self):
        mode = 'default Append'
        format = 'Log format, make a default one'
        pass


    def _colors(self, msg_type):
        colors = {
            'INFO': '\033[95m',
            'OKBLUE': '\033[94m',
            'OKGREEN': '\033[92m',
            'DEBUG': '\033[93m',
            'ERROR': '\033[91m',
            'WARNING': '\033[91m',
            'INFO': '\033[36m',
            'ENDC': '\033[0m',
            'BOLD': '\033[1m',
            'UNDERLINE': '\033[4m'
        }
        return colors[msg_type]
