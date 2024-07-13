import threading
import logging

class SingletonMeta(type):
    """
    Metaclass for creating thread-safe Singleton classes.

    This metaclass ensures that only one instance of a class is created,
    even in a multi-threaded environment.

    Attributes:
        _instances (dict): Dictionary to store instances of Singleton classes.
        _lock (threading.Lock): Lock object for thread safety during instance creation.
    """

    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        """
        Call method override to create or retrieve the Singleton instance.

        Args:
            cls (type): Class being instantiated.
            *args: Positional arguments for initializing the instance.
            **kwargs: Keyword arguments for initializing the instance.

        Returns:
            object: The Singleton instance of the class.
        """
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

    

class Logger(metaclass=SingletonMeta):
    """
    Singleton class for logging messages.

    This class ensures that only one instance of the logger is created,
    providing a centralized logging mechanism.

    Attributes:
        logger (logging.Logger): Logger instance for logging messages.
    """

    def __init__(self):
        """
        Initializes the logger instance if it doesn't exist.

        Sets up a StreamHandler with a specified logging format and level.
        """
        self.logger = logging.getLogger("SingletonLogger")
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.INFO)

    def log(self, message, level=logging.INFO):
        """
        Logs a message at the specified logging level.

        Args:
            message (str): Message to be logged.
            level (int): Logging level (default: logging.INFO).
                        Valid levels are logging.INFO, logging.ERROR,
                        logging.WARNING, logging.DEBUG.
        """

        logging_methods = {
            logging.INFO: self.logger.info,
            logging.ERROR: self.logger.error,
            logging.WARNING: self.logger.warning,
            logging.DEBUG: self.logger.debug
        }
        print('11111111111',level,message)
        log_method = logging_methods.get(level, self.logger.info)
        log_method(message)

        
# Testing the Logger Singleton with multiple threads
def test_logger():
    """
    Simulates logging messages using the Logger Singleton instance.
    """
    logger_1 = Logger()
    logger_2 = Logger()
    print(f"Logger ID 1: {id(logger_1)}")
    print(f"Logger ID 2 : {id(logger_2)}")
    logger_1.log("This is a log message.")

threads = []
for i in range(10):
    thread = threading.Thread(target=test_logger)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
