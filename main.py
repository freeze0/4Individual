class BeeElephant(object):
    def __init__(self, b, e):
        self.bee = b
        self.elephant = e

    def fly(self):
        if self.bee >= self.elephant:
            return True
        else:
            return False

    def trumpet(self):
        if self.bee <= self.elephant:
            return "tu-tu-doo-doo"
        else:
            return "wzzzzz"

    def eat(self, meal, value):
        if meal == 'nectar':
            elvalue = self.elephant - value
            bevalue = self.bee + value
            self.elephant = elvalue if elvalue > 0 else 1
            self.bee += bevalue if bevalue < 100 else 100
        elif meal == 'grass':
            elvalue = self.elephant + value
            bevalue = self.bee - value
            self.elephant = elvalue
            self.bee = bevalue
            self.elephant = elvalue if elvalue < 100 else 100
            self.bee = bevalue if bevalue > 0 else 1
        else:
            return 'dont eat this'

    def get_parts(self):
        return self.elephant, self.bee


be1 = BeeElephant(4, 5)
print(be1.fly(), '|', be1.trumpet(), '|', be1.eat('meat', 1), '|', be1.eat('nectar', 10), be1.get_parts(), '|',
      be1.eat('grass', 100), be1.get_parts())
