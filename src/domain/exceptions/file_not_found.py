from domain.exceptions.application_error import ApplicationError


class JsonFileNotFound(ApplicationError):
    """
        A class used to represent an exception when a required JSON file is not found.

        This class extends the ApplicationError base class to provide specific error
        handling and messaging for scenarios where a JSON file is missing or cannot be located.

        ...

        Attributes
        ----------
        default_message : str
            The main error message indicating that a JSON file was not found (inherited from ApplicationError).
        additional_message : str
            Additional context or details about the error, including the file path if provided (inherited from ApplicationError).

        Methods
        -------
        Inherits all methods from ApplicationError:
        get_message() -> str
            Returns a formatted error message combining the default message and the additional context.
        __str__() -> str
            Provides a string representation of the error message.
        """

    def __init__(self, additional_message: str = '', file_path: str = None):
        super().__init__('Json File Not Found ', additional_message + ' {}'.format(file_path))
