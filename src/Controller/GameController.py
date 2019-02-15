import cocos
from cocos.cocosnode import CocosNode
from cocos.layer import Layer
from pyglet.window import key

from Model.GameModel import GameModel
from Utils import Gamestate, Direction


class GameController(Layer):

    def __init__(self, model: GameModel):
        super(GameController, self).__init__()

        self.model = model
        self.delta = 0.16
        self.is_event_handler = True
        self.keys_pressed = []

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

        bat_collisions = self.model.collision_manager.objs_near(self.model.bat, 0.0001)

        if self.model.net is not None:
            net_in = (self.model.bat.y, self.model.ball.x, self.model.ball.y)
            # print("net_in: " + str(net_in))
            net_out = self.model.net.activate(net_in)
            # print("net_out: " + str(net_out))
        else:
            # print("net is None")
            pass

        #todo: batController classes
        if key.W in self.keys_pressed:
            if not self.model.wall_top in bat_collisions:
                self.model.bat.move_bat(Direction.UP)
        if key.S in self.keys_pressed:
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

    def on_key_press(self, key, modifiers):
        print("on_key_press")
        self.keys_pressed.append(key)

    def on_key_release(self, key, modifiers):
        if key in self.keys_pressed:
            self.keys_pressed.remove(key)

    def on_mouse_motion(self, x, y, dx, dy):
        pass
        # print("on_mouse_motion")
        # self.bat.position = x, y
