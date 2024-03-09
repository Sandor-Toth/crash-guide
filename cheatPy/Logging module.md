### Core Components of Python Logging

**Logger**: The main entry point to the logging system. It provides the interface through which applications can log messages.

**Logging Levels**: Define the severity of the messages to be logged. The default levels are DEBUG, INFO, WARNING, ERROR and CRITICAL.

**Formatter**: Specifies the format in which messages are logged, adding context such as time, module name, level, etc.

**Handler**: Responsible for sending logged messages to appropriate destinations such as console, files, email, etc.

### Basic Logging with the Root Logger

```
import logging

# Default logging level is WARNING
logging.warning("This is a warning message")
```

***Output:***

```
WARNING:root:This is a warning message
```

### Custom Logger with Different Levels and Handlers

```
import logging

# Create a custom logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)  # Set the logger's level

# Create a console handler and set its level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create a formatter and set it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(console_handler)

# Log messages
logger.debug("This is a debug message")
```

### File logging

```
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Now, log messages will also be written to 'app.log'
logger.info("This message goes to the console and the file")
```

### Advanced Configuration with Multiple Handlers

```
# Adding another handler for error messages only
error_file_handler = logging.FileHandler('error.log')
error_file_handler.setLevel(logging.ERROR)
error_file_handler.setFormatter(formatter)
logger.addHandler(error_file_handler)

# Error messages will go to both the console and 'error.log'
logger.error("This is an error message")
```

### Configuring Loggers Using a Configuration File

```
# logging_config.yaml
version: 1
formatters:
  simple:
    format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
handlers:
  console:
    class: logging.StreamHandler
    level: DEBUG
    formatter: simple
    stream: ext://sys.stdout
loggers:
  my_logger:
    level: DEBUG
    handlers: [console]
    propagate: no
```

```
import logging.config
import yaml

with open('logging_config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger('my_logger')
logger.debug("This is a debug message configured via YAML")
```
---