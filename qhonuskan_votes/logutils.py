import logging


def setup_loghandlers(level=None):
    # Setup logging for qhonuskan_votes if not already configured
    logger = logging.getLogger('qhonuskan_votes')
    if not logger.handlers:
        logging.config.dictConfig({
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "qhonuskan_votes": {
                    "format": "[%(levelname)s]%(asctime)s PID %(process)d: %(message)s",
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                },
            },
            "handlers": {
                "qhonuskan_votes": {
                    "level": "DEBUG",
                    "class": "logging.StreamHandler",
                    "formatter": "qhonuskan_votes"
                },
            },

            "loggers": {
                "qhonuskan_votes": {
                    "handlers": ["qhonuskan_votes"],
                    "level": level or "DEBUG",
                    "propagate": False,
                }
            }
        })
    return logger
