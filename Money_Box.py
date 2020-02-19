class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.count1 = 0
        self.capacity = capacity
    def can_add(self, v):
    # True, если можно добавить v монет, False иначе
        if self.capacity - self.count1 >= v:
            return True
        else:
            return False
    def add(self, v):
    # положить v монет в копилку
        if MoneyBox.can_add(self, v):
            self.count1 += v

x=MoneyBox(100) # создаем объект класса monebox
x.add(15) # к объекту класса х применили метод add класса manebox
print(x.count1)
x.add(100)
print(x.count1)
x.can_add(15)
# проверка commit
