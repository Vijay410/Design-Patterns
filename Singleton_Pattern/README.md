## Singleton Logger with Thread Safetyr.

### Introduction
This demonstrates the implementation of a thread-safe Singleton pattern using a metaclass in Python. 
It includes a Singleton logger class that ensures only one instance of the logger is created, 
providing a centralized logging mechanism for multi-threaded environments.

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

## Application of Singleton Design Pattern
      1. **Logging** : In many application, its mandatory to have an single , centralized logging mechanism to collect and retrive the log messages. Using Using a Singleton logger ensures that all parts of the application write to the same log.

      2. **Configuration Management:**
          A Singleton configuration manager allows consistent access to configuration
          data throughout the application.
          
      3.** Database Connections:** : Managing database connections can be resource-intensive.
      Using a Singleton database connection manager ensures that only one connection 
      -pool is maintained, reducing overhead and managing connections efficiently.

      4. **Caching**: Caching mechanisms can be implemented as Singletons to ensure 
      that there is a single cache storage that is 
      accessed and updated consistently across the application. 
        
      5.**Event Handling**: Event handling systems, such as event dispatchers 
      or message queues, can be implemented as Singletons to ensure 
      -consistent event propagation and handling across the application.
      
      6.Service Locator: A service locator that provides access to 
      various services in an application can be implemented as a Singleton 
      -to ensure there is a single access point for retrieving services
