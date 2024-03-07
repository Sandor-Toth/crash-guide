import logging.config
# pip install PyYAML
import yaml
from datetime import datetime

# Read YAML config file
with open('cheatPy/logging_config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger_debug = logging.getLogger('my_application_logger')

# This message is written to the app.log file
logger_debug.error("This is an error message.")
logger_debug.info("This is an information message.")
logger_debug.debug("This is a debug message.")

logger_info = logging.getLogger('my_other_logger')

logger_info.error("This is an error message.")
logger_info.info("This is an information message.")
# These messages are not included as they are not at INFO level
logger_info.debug("This is a debug message.(1)")
logger_info.debug("This is a debug message.(2)")



# Dynamically generate the log filename with the current date
log_filename = datetime.now().strftime("my_app_log_%Y-%m-%d.log")

# Logging configuration dictionary
log_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'filename': log_filename,  # Dynamically set filename
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout',  # Standard output (console)
        },
    },
    'loggers': {
        'my_application': {
            'level': 'DEBUG',
            'handlers': ['file_handler', 'console'],
            'propagate': False,
        },
    },
}

# Apply the configuration
logging.config.dictConfig(log_config)

# Instantiate and use the logger
logger = logging.getLogger('my_application')
logger.debug('This is a debug message.')
logger.info('This is an info message.')
