if __name__ == '__main__':
    def debug(f):
        def new_function(a, b):
            print("Function called!")
            return f(a, b)

        return new_function


    @debug
    def add(a, b):
        return a + b

    @debug
    def multi(a,b):
        return a*b


    print(add(7, 5))
    print(multi(2,3))

    def milog(f):
        def new_function(x):
            print("Function called!")
            fx = f(x)
            print("Hacer el log de objeto guardado")
            return fx

        return new_function

    @milog
    def salva(x):
        print("Objeto guardado")
        return x

    print(salva(7))




    class MyDecorator:
        def __init__(self, function):
            self.function = function

        def __call__(self):
            # We can add some code
            # before function call

            self.function()

            # We can also add some code
            # after function call.


    # adding decorator to the class
    @MyDecorator
    def function():
        print("Algo")


    function()


    class MyDecorator:
        def __init__(self, function):
            self.function = function

        def __call__(self, *args, **kwargs):
            # We can add some code
            # before function call

            self.function(*args, **kwargs)

            # We can also add some code
            # after function call.


    # adding decorator to the class
    @MyDecorator
    def function(name, message='Hello'):
        print("{}, {}".format(message, name))


    function("Algo", "hello")


    def decorator_function_with_arguments(arg1, arg2, arg3):
        def wrap(f):
            print("Inside wrap()")

            def wrapped_f(*args):
                print("Inside wrapped_f()")
                print("Decorator arguments:", arg1, arg2, arg3)
                f(*args)
                print("After f(*args)")

            return wrapped_f

        return wrap


    @decorator_function_with_arguments("hello", "world", 42)
    def sayHello(a1, a2, a3, a4):
        print('sayHello arguments:', a1, a2, a3, a4)


    print("After decoration")

    print("Preparing to call sayHello()")
    sayHello("say", "hello", "argument", "list")
    print("after first sayHello() call")
    sayHello("a", "different", "set of", "arguments")
    print("after second sayHello() call")


    def singleton(cls):
        instances = {}

        def getinstance():
            if cls not in instances:
                print("Instancia no Encontrada")
                instances[cls] = cls()
            else:
                print("Instancia Encontrada")
            return instances[cls]

        return getinstance


    @singleton
    class MyClass:
        def __init__(self):
            self.prop = ''

    c = MyClass()
    c.prop ="Hola"
    c = MyClass()
    print(c.prop)

    import functools
    import logging


    def create_logger():
        # Creates a log object and returns it

        logger = logging.getLogger("example_logger")
        logger.setLevel(logging.INFO)

        # create the log file handler
        fh = logging.FileHandler("./test.log")

        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)

        # add handler to logger object
        logger.addHandler(fh)
        return logger


    def exception(function):
        #A decorator that wraps the passed in function and logs exceptions should one occur
    

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            logger = create_logger()
            try:
                return function(*args, **kwargs)
            except:
                # log the exception
                err = "There was an exception in  "
                err += function.__name__
                logger.exception(err)
                print("salta dentro")
                # re-raise the exception
                raise

        return wrapper


    @exception
    def zero_divide():
        1 / 0

    try:
        zero_divide();
    except:
        print("Fallo fuera")
        
