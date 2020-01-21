if __name__ == '__main__':
    def debug(f):
        def new_function(a, b):
            print("Function add() called!")
            return f(a, b)

        return new_function


    @debug
    def add(a, b):
        return a + b


    print(add(7, 5))