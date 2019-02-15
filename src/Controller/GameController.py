import cocos
from cocos.cocosnode import CocosNode
from cocos.layer import Layer
from pyglet.window import key

from Controller.NetBatController import NetBatController
from Controller.PlayerBatController import PlayerBatController
from Model.GameModel import GameModel
from Utils import Gamestate, Direction


class GameController(Layer):

    def __init__(self, model: GameModel):
        super(GameController, self).__init__()

        self.model = model
        self.delta = 0.16

        if not self.model.net:
            self.bat_controller = PlayerBatController()
            self.add(self.bat_controller)
        else:
            self.bat_controller = NetBatController(self.model)

        self.model.collision_manager.add(self.model.bat)
        self.model.collision_manager.add(self.model.ball)
        self.model.collision_manager.add(self.model.enemy)

        self.model.collision_manager.add(self.model.wall_left)
        self.model.collision_manager.add(self.model.wall_right)
        self.model.collision_manager.add(self.model.wall_top)
        self.model.collision_manager.add(self.model.wall_bottom)

        self.gamestate = Gamestate.RUNNING

    def update(self, delta: float):

        if self.model.gamestate == Gamestate.RUNNING:
            self.model.score += delta
            self.model.bat.update(delta)
            self.model.ball.update(delta)
            self.model.enemy.update(delta)

        self.bat_controller.update(delta)

        bat_collisions = self.model.collision_manager.objs_near(self.model.bat, 0.0001)

        if self.bat_controller.action_up:
            if not self.model.wall_top in bat_collisions:
                self.model.bat.move_bat(Direction.UP)
        if self.bat_controller.action_down:
            if not self.model.wall_bottom in bat_collisions:
                self.model.bat.move_bat(Direction.DOWN)

        ball_collisions = self.model.collision_manager.objs_near(self.model.ball, 0.0001)
        # print("ball_collisions: " + str(ball_collisions))
        if self.model.wall_top in ball_collisions or self.model.wall_bottom in ball_collisions:
            self.model.ball.flip_y_dir()
        if self.model.bat in ball_collisions or self.model.enemy in ball_collisions:
            self.model.ball.flip_x_dir()
        if self.model.wall_left in ball_collisions:
            self.on_game_end()
            pass
        if self.model.wall_right in ball_collisions:
            self.model.ball.flip_x_dir()
        # time.sleep(2)

    def on_game_end(self):
        print("on_game_end. time: " + str(self.model.score))
        self.gamestate = Gamestate.ENDED
        cocos.director.director.scene.end(self.model.score)

    def on_mouse_motion(self, x, y, dx, dy):
        pass
        # print("on_mouse_motion")
        # self.bat.position = x, y
