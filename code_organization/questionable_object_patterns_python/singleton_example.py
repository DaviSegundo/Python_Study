class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# remove 'metaclass=Singleton' and test
class Logger(metaclass=Singleton):
    
    def log(self, msg):
        print(msg)


if __name__ == '__main__':
    logger = Logger()
    logger2 = Logger()

    if logger == logger2:
        print("Equal")
    else:
        print("Diff")

    logger.log("Davi")
    logger2.log("Segundo")