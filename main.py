# main.py

from assignment_9 import FileOperations, MathOperations, StringOperations, CustomException

# File Operations
file_op = FileOperations("example.txt")
content = file_op.read_file()
print("File Content:", content)

write_status = file_op.write_file("Hello, World!")
print(write_status)

# Math Operations
sqrt_result = MathOperations.square_root(16)
print("Square Root:", sqrt_result)

power_result = MathOperations.power(2, 3)
print("Power:", power_result)

# String Operations
split_result = StringOperations.split_string("Hello, World!")
print("Split Result:", split_result)

# Custom Exception
try:
    raise CustomException("This is a custom exception.")
except CustomException as e:
    print("Exception:", str(e))
