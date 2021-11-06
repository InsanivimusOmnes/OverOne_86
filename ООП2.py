# 14.7
class BigHouse:
    def __init__(self, flats):
        self.flats = flats

    def watchman(self):
        print(f'To hire the watchman')

# 14.8
class BeautyShopMixin:
    def __init__(self, open_time, close_time):
        self.open_time = open_time
        self.close_time = close_time

    def manicure(self):
        pass

    def haircut(self):
        pass

    def shop_working(self, now_time):
        if now_time < self.open_time or now_time > self.close_time:
            print(f'The shop is closed')
        else:
            print(f'The shop is open')

# 14.9
class House(BeautyShopMixin):
    def __init__(self, open_time, close_time):
        super(House, self).__init__(open_time, close_time)

if __name__ == '__main__':
    hws = House(10, 22)
    print(hws.__dict__)
    hws.shop_working(13)

