class MyCustomError(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise MyCustomError("This is a custom error !!!")
except MyCustomError as e:
    print("Error message: ", e.message)