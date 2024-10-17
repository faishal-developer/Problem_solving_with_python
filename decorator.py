def timer(func):
    def inner():
        print("kdjfdkjdk")
        func()
        print("dkfjdkf")
    
    return func

# decorator
@timer
def get_factorial():
    print('factorial starting')

get_factorial()

