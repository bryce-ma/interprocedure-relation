import logging
from logging.config import dictConfig

logging_config = dict(
    version=1,
    formatters={
        'f': {'format':
              '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
    },
    handlers={
        'console': {'class': 'logging.StreamHandler',
                    'formatter': 'f',
                    'level': logging.DEBUG},
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': logging.DEBUG,
            'formatter': 'f',
            'filename': 'all.log',
            'mode': 'a',
            'maxBytes': 10485760,
            'backupCount': 5}
    },
    root={
        'handlers': ['console', 'file'],
        'level': logging.DEBUG,
    },
)

dictConfig(logging_config)
