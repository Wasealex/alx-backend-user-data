#!/usr/bin/env python3
"""a module that contains hashing password
using bycryt
"""
import bcrypt


def hash_password(password):
    """hashing password
    args [password]
    to return byte of password
    """
    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Return the hashed password as a byte string
    return hashed_password


def is_valid(hashed_password, password):
    """Validate if the provided password matches the hashed password.
        Args:
            hashed_password (bytes): The hashed password.
            password (str): The password to validate.
        Returns:
            bool: True if the password matches the hashed password,
            False otherwise.
    """
    # Validate the password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
