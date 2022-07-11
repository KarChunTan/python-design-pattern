class Singleton:
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton('default', 0)
        return Singleton.__instance

    def __init__(self, name: str, age: int) -> None:
        if Singleton.__instance is not None:
            raise Exception("Singleton cannot be instantiated more than once!")
        self.name = name
        self.age = age
        Singleton.__instance = self

if __name__ == '__main__':
    a = Singleton('mike', 30)
    print(a)

    b = Singleton.get_instance()
    print(b)

    if id(a) == id(b):
        print('Shared object')
