# Question 12

#Suppose you're building a logging library for a web application that needs to keep track of all requests and responses.
#You want to use the Singleton pattern to ensure that there's only one instance of the logger class throughout the application.


class Logger:
    _instance = None

    def __new__(cls):
        # Singleton implementation using __new__
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
            # Additional setup for the logger can be done here
        return cls._instance

    def log(self, message):
        # Log the message (implementation details can be added here)
        print(f"Logging: {message}")

#  Testing the Example to verify if it's running well
# logger1 = Logger()
# logger1.log("Request received")
#
# logger2 = Logger()
# logger2.log("Response sent")
#
# # Both logger1 and logger2 point to the same instance
# print(logger1 is logger2)  # Output: True