import abc


class AbstractAxisModule(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def home(self, axis: str):
        pass

    @abc.abstractmethod
    def x_left(self, distance: float, speed: str):
        pass

    @abc.abstractmethod
    def x_right(self, distance: float, speed: str):
        pass

    @abc.abstractmethod
    def y_up(self, distance: float, speed: str):
        pass

    @abc.abstractmethod
    def y_down(self, distance: float, speed: str):
        pass

    @abc.abstractmethod
    def z_forward(self, distance: float, speed: str):
        pass

    @abc.abstractmethod
    def z_back(self, distance: float, speed: str):
        pass

    @abc.abstractmethod
    def yaw_left(self, distance: float, speed: str):
        pass

    @abc.abstractmethod
    def yaw_right(self, distance: float, speed: str):
        pass

    @abc.abstractmethod
    def pitch_up(self, distance: float, speed: str):
        pass

    @abc.abstractmethod
    def pitch_down(self, distance: float, speed: str):
        pass

    @abc.abstractmethod
    def stop(self, axis: str):
        pass

    @abc.abstractmethod
    def is_sensor_x_left(self):
        pass

    @abc.abstractmethod
    def is_sensor_x_org(self):
        pass

    @abc.abstractmethod
    def is_sensor_x_right(self):
        pass

    @abc.abstractmethod
    def is_sensor_x_move(self):
        pass

    @abc.abstractmethod
    def is_sensor_y_down(self):
        pass

    @abc.abstractmethod
    def is_sensor_y_org(self):
        pass

    @abc.abstractmethod
    def is_sensor_y_up(self):
        pass

    @abc.abstractmethod
    def is_sensor_y_move(self):
        pass

    @abc.abstractmethod
    def is_sensor_z_back(self):
        pass

    @abc.abstractmethod
    def is_sensor_z_org(self):
        pass

    @abc.abstractmethod
    def is_sensor_z_forward(self):
        pass

    @abc.abstractmethod
    def is_sensor_z_move(self):
        pass

    @abc.abstractmethod
    def is_sensor_yaw_left(self):
        pass

    @abc.abstractmethod
    def is_sensor_yaw_org(self):
        pass

    @abc.abstractmethod
    def is_sensor_yaw_right(self):
        pass

    @abc.abstractmethod
    def is_sensor_yaw_move(self):
        pass

    @abc.abstractmethod
    def is_sensor_pitch_down(self):
        pass

    @abc.abstractmethod
    def is_sensor_pitch_org(self):
        pass

    @abc.abstractmethod
    def is_sensor_pitch_up(self):
        pass

    @abc.abstractmethod
    def is_sensor_pitch_move(self):
        pass