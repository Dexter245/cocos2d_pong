from Controller.BatController import BatController


class NetBatController(BatController):

    def __init__(self, model):
        super(NetBatController, self).__init__()

        self.model = model

    def update(self, delta: float):
        net_in = (self.model.bat.y, self.model.ball.x, self.model.ball.y)
        print("net_in: " + str(net_in))
        net_out = self.model.net.activate(net_in)
        print("net_out: " + str(net_out))

        index_max = net_out.index(max(net_out))
        print("index_max: " + str(index_max))
        self.action_up = False
        self.action_down = False
        if index_max == 1:
            self.action_up = True
        elif index_max == 2:
            self.action_down = True
