from model import Model
from view import View, ChangerWidget
from pubsub import pub


class Controller:
    def __init__(self):
        self.model = Model()

        # set up the first frame which displays the current Model value
        self.view1 = View()
        self.view1.setMoney(self.model.myMoney)

        # set up the second frame which allows the user to modify the Model's value
        self.view2 = ChangerWidget()

        self.view1.Show()
        self.view2.Show()

        pub.subscribe(self.changeMoney, 'money_changing')

    def changeMoney(self, amount):
        if amount >= 0:
            self.model.addMoney(amount)
        else:
            self.model.removeMoney(-amount)
