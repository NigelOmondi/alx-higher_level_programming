#!/usr/bin/python3


def raise_exception_msg(message=""):
    """Raises a NameError exception with the specified message.

    Args:
        message (str): The message to include in the exception.

    Raises:
        NameError: Always raises a NameError exception.
    """
    raise NameError(message)
