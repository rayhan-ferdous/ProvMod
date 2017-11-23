# version 1.2.3
import logging

# use with locals()

# debug level messages
formatter_debug = logging.Formatter(
    'time: %(asctime)s, file: %(filename)s, func: %(funcName)s, level: %(levelname)s, line: %(lineno)d, module: %(module)s, msecs: %(msecs)d, msg: %(message)s, logger: %(name)s, path: %(pathname)s, procID: %(process)d, proc: %(processName)s, threadID: %(thread)d, thread: %(threadName)s' + '\n*********')

# informatin level messages
formatter_info = logging.Formatter(
    'time: %(asctime)s, msecs: %(msecs)d, msg: %(message)s' + '\n~~~~~~~~~')
formatter_info_start = logging.Formatter(
    'time: %(asctime)s, file: %(filename)s, func: %(funcName)s, level: %(levelname)s, module: %(module)s, msecs: %(msecs)d, msg: %(message)s, logger: %(name)s' + '\n---')
formatter_info_end = logging.Formatter(
    'time: %(asctime)s, file: %(filename)s, func: %(funcName)s, level: %(levelname)s, module: %(module)s, msecs: %(msecs)d, msg: %(message)s, logger: %(name)s' + '\n---------')

# warning
formatter_warn = logging.Formatter(
    'time: %(asctime)s, file: %(filename)s, func: %(funcName)s, level: %(levelname)s, line: %(lineno)d, module: %(module)s, msecs: %(msecs)d, msg: %(message)s, logger: %(name)s, path: %(pathname)s' + '\n!!!!!!!!!')

# error with locals()
formatter_error = logging.Formatter(
    'time: %(asctime)s, file: %(filename)s, func: %(funcName)s, level: %(levelname)s, line: %(lineno)d, module: %(module)s, msecs: %(msecs)d, msg: %(message)s, logger: %(name)s, path: %(pathname)s, procID: %(process)d, proc: %(processName)s, threadID: %(thread)d, thread: %(threadName)s' + '\nXXXXXXXXX')

# fatal error with locals()
formatter_fatal = logging.Formatter(
    'time: %(asctime)s, file: %(filename)s, func: %(funcName)s, level: %(levelname)s, line: %(lineno)d, module: %(module)s, msecs: %(msecs)d, msg: %(message)s, logger: %(name)s, path: %(pathname)s, procID: %(process)d, proc: %(processName)s, threadID: %(thread)d, thread: %(threadName)s' + '\n$$$$$$$$$')


# info config
def logger_info(name, log_file, level=logging.INFO):
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter_info)

    logger = logging.getLogger(name + '-INFO')
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def logger_info_start(name, log_file, level=logging.INFO):
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter_info_start)

    logger = logging.getLogger(name + '-INFOST')
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def logger_info_end(name, log_file, level=logging.INFO):
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter_info_end)

    logger = logging.getLogger(name + '-INFOND')
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# debug config
def logger_debug(name, log_file, level=logging.DEBUG):
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter_debug)

    logger = logging.getLogger(name + '-DEBUG')
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# warn config
def logger_warn(name, log_file, level=logging.WARNING):
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter_warn)

    logger = logging.getLogger(name + '-WARN')
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# error config
def logger_error(name, log_file, level=logging.ERROR):
    # type: (object, object, object) -> object
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter_error)

    logger = logging.getLogger(name + '-ERROR')
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# fatal config
def logger_fatal(name, log_file, level=logging.CRITICAL):
    # type: (object, object, object) -> object
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter_fatal)

    logger = logging.getLogger(name + '-FATAL')
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger