"""Various logging modules."""
import logging

import coloredlogs


def get_logger(log_to_console=True, log_to_file=True):
    """Initialize Python logger that outputs to file and console."""
    assert log_to_console or log_to_file

    logger = logging.getLogger("main_logger")
    logger.setLevel(logging.DEBUG)
    formatter = coloredlogs.ColoredFormatter(
        "%(asctime)s | %(filename)12s | %(levelname)8s | %(message)s"
    )

    if log_to_file:
        fh = logging.FileHandler("run.log")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    if log_to_console:
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    # Fix TensorFlow doubling logs
    # https://stackoverflow.com/questions/33662648/tensorflow-causes-logging-messages-to-double
    logger.propagate = False

    return logger
