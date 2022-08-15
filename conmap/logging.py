"""Defines the package-wide logger."""

from logging import DEBUG, INFO, FileHandler, Formatter, Logger, StreamHandler, getLogger


def get_logger(_name_: str) -> Logger:
    """Returns the package-wide logger."""

    # Configuring logger
    logger = getLogger(_name_)
    logger.setLevel(DEBUG)

    # Configuring file logging
    verbose_fh = FileHandler("conmap.log")
    verbose_fh.setLevel(DEBUG)

    # Configuring console logging
    console_fh = StreamHandler()
    console_fh.setLevel(INFO)

    # Configuring formatter
    formatter = Formatter("[%(asctime)s] %(name)s - %(levelname)s : %(message)s")
    verbose_fh.setFormatter(formatter)
    console_fh.setFormatter(formatter)

    # Adding hendlers
    logger.addHandler(verbose_fh)
    logger.addHandler(console_fh)

    return logger
