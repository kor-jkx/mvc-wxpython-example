from pubsub import pub


class Model:
    def __init__(self):
        self.myMoney = 0

    def addMoney(self, value):
        self.myMoney += value
        # now tell anyone who cares that the value has been changed
        pub.sendMessage("money_changed", money=self.myMoney)

    def removeMoney(self, value):
        self.myMoney -= value
        # now tell anyone who cares that the value has been changed
        pub.sendMessage("money_changed", money=self.myMoney)
