# Decorator practice

def decorator_function(function):

    def wrapper(*args, **kwargs):
        print('executed before ', function.__name__)
        result = function(*args, **kwargs)
        print('executed after ', function.__name__)
        return result

    return wrapper


@decorator_function
def test_function(text):
    print(text)

test_function('How about that!')
test_function('Again already?')
