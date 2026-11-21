class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')


class ToyotaCar(Car):
    def run(self):
        print('fast')


class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        super().__init__(model)
        self.enable_auto_run = enable_auto_run
    def run(self):
        print('super fast')
    def auto_run(self):
        print('auto run')


car = Car()
car.run()

toyota_car = ToyotaCar()
toyota_car.run()

print('###############')
tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()