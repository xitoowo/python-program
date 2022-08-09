class Singleton:
    __instance = None  # ссылка на экземпляр класса

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, data):
        self.data = data

    def __del__(self):
        Singleton.__instance = None


pt = Singleton('hello')
py = Singleton('world')
print(pt.data)  # world
print(py.data)  # world
print(id(pt), id(py))  # 1124466355984 1124466355984
