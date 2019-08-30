import os, traceback,re
import sys
import logging

def createlogger(name):
    """Create a logger named specified name with the level set in config file."""
    logger = logging.getLogger(name)
    logger.setLevel("DEBUG")
    ch = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s.%(msecs)03d: [%(levelname)s] [%(name)s] [%(funcName)s] %(message)s',
        '%y%m%d %H:%M:%S')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

def create_folder():
    log_path = os.environ.get("LOG_PATH")
    if log_path is None:
        log_path =  sys.path[0][sys.path[0].find(':')+1:] + '\\results'
    if not os.path.exists(log_path):
        logger.debug("log_path not exsit")
        os.makedirs(log_path)
    if not os.path.exists(log_path):
        return None
    return log_path


def log_traceback(traceback):
    """print traceback information with the log style.

    """
    str_list = traceback.split("\n")
    for s in str_list:
        logger.warning(s)


logger = createlogger("COMMON")