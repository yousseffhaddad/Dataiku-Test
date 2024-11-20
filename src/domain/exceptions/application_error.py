class ApplicationError(Exception):
    """
        A class used to represent application-level errors and provide detailed error messages.

        This class serves as a base exception for the application, allowing for customizable error
        messages that include a default message and an optional additional message for more context.
        ...

        Attributes
        ----------
        default_message : str
            The main error message that describes the nature of the error.
        additional_message : str
            Additional context or details about the error (optional).

        Methods
        -------
        get_message() -> str
            Returns a formatted error message combining the default message and the additional context.
        __str__() -> str
            Provides a string representation of the error message.
        """

    def __init__(self, default_message, additional_message=''):
        self.default_message = default_message
        self.additional_message = additional_message

    def __str__(self):
        return self.get_message()

    def get_message(self):
        return self.default_message if self.additional_message == '' else "{}: {}".format(self.default_message,self.additional_message)