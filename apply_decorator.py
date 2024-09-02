def apply_decorator(func):
    def decorator_func():
        # Print a message before calling the function
        print("Decorator Applied")
        func()
    return decorator_func

# Example usage
if __name__ == "__main__":
    @apply_decorator
    def say_hello():
        print("Hello, world!")

    say_hello()
