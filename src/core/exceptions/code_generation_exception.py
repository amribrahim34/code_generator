class CodeGenerationException(Exception):
    """
    Custom exception class for code generation errors.
    """

    def __init__(self, message: str, details: dict = None):
        """
        Initialize the CodeGenerationException.

        Args:
            message (str): The error message.
            details (dict, optional): Additional details about the error. Defaults to None.
        """
        self.message = message
        self.details = details or {}
        super().__init__(self.message)

    def __str__(self):
        """
        String representation of the exception.

        Returns:
            str: A formatted string containing the error message and details.
        """
        error_str = f"CodeGenerationException: {self.message}"
        if self.details:
            error_str += "\nDetails:"
            for key, value in self.details.items():
                error_str += f"\n  {key}: {value}"
        return error_str

    def to_dict(self):
        """
        Convert the exception to a dictionary.

        Returns:
            dict: A dictionary representation of the exception.
        """
        return {
            "error": "CodeGenerationException",
            "message": self.message,
            "details": self.details
        }