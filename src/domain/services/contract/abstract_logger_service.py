import logging
from abc import ABC, ABCMeta,abstractmethod


class AbstractLoggerService(ABC):
    """
        An abstract base class that defines the structure for logger services used in the application.

        This class uses the `ABC` module to enforce that subclasses must implement a method for retrieving a logger instance. The logger instance is intended for logging application events, errors, and debug information. Subclasses will implement the `get_logger` method to return an appropriate logger instance (e.g., a `logging.Logger`).

        ...

        Methods
        -------
        get_logger() -> logging
            An abstract method that must be implemented by any subclass. It retrieves and returns a logger instance to be used for logging in the application.
        """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_logger(self) -> logging: raise NotImplementedError