from domain.services.contract.abstract_logger_service import AbstractLoggerService
import logging

class LoggerService (AbstractLoggerService):
    """
    A class used to create and configure custom logger

    Attributes
    ----------
    _logger : logging.Logger
        Logger instance configured to write logs to a file with a specific format and level.

    Methods
    -------
    get_logger() -> logging.Logger
        Retrieves the configured logger instance for use in logging messages.
    """

    def __init__(self):

        # creating base logger
        self._logger = logging.getLogger("C3PO - Algorithm")
        self._logger.propagate = False
        self._logger.setLevel(logging.DEBUG)

        # Prevent duplicate log entries if the logger already has handlers
        if not self._logger.hasHandlers():
            # Create a file handler
            file_handler = logging.FileHandler("./logs/app.log", mode="a", encoding="utf-8")
            file_handler.setLevel(logging.DEBUG)

            # Create a formatter
            formatter = logging.Formatter(
                "{asctime} - {levelname} - {message}",
                style="{",
                datefmt="%Y-%m-%d %H:%M"
            )
            file_handler.setFormatter(formatter)

            # Add the handler to the logger
            self._logger.addHandler(file_handler)

    def get_logger(self)-> logging.Logger:
        return self._logger