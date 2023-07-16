# operations.py

import math

class FileOperations:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def read_file(self):
        try:
            with open(self.file_name, 'r') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            return "File not found."
        except IOError:
            return "Error reading the file."
    
    def write_file(self, content):
        try:
            with open(self.file_name, 'w') as file:
                file.write(content)
            return "File written successfully."
        except IOError:
            return "Error writing to the file."

class MathOperations:
    @staticmethod
    def square_root(num):
        return math.sqrt(num)
    
    @staticmethod
    def power(base, exponent):
        return math.pow(base, exponent)

class StringOperations:
    @staticmethod
    def split_string(text, delimiter=' '):
        return text.split(delimiter)

class CustomException(Exception):
    pass
