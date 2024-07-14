## Singleton Logger with Thread Safetyr.

### Introduction
This project demonstrates the implementation of a thread-safe Singleton pattern using a metaclass in Python. 
It includes a Singleton logger class that ensures only one instance of the logger is created, 
providing a centralized logging mechanism for multi-threaded environments.

Usage
#### SingletonMeta Metaclass

**Purpose**: Ensures thread-safe creation of Singleton instances.
Attributes:
**_instances**: Dictionary storing instances of Singleton classes.
**_lock**: Threading lock for ensuring thread safety during instance creation.
Methods:
__call__(cls, *args, **kwargs): Override method to create or retrieve Singleton instances.
Logger Singleton Class

**Purpose**: Provides a centralized logging mechanism with a Singleton instance.
Attributes:
**logger**: logging.Logger instance for logging messages.
**Methods**:
__init__(): Initializes the logger instance with a StreamHandler.
log(message, level=logging.INFO): Logs a message at a specified logging level.****
