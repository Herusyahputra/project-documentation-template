import requests
from .axis_module.abstract_axis_module import AbstractAxisModule


class AxisHTTPClient(AbstractAxisModule):
    def __init__(self, url: str = "http://127.0.0.1:8000/"):
        self.url = url

    def home(self, axis: str):
        payload = {'axis': axis}
        url = self.url + "home"
        r = requests.get(url, params=payload)
        data = r.json()
        return data["message"]

    def x_left(self, distance: float, speed: str):
        payload = {'distance': distance, 'speed': speed}
        url = self.url + "x_left"
        r = requests.get(url, params=payload)
        data = r.json()
        return data["message"]

    def x_right(self, distance: float, speed: str):
        payload = {'distance': distance, 'speed': speed}
        url = self.url + "x_right"
        r = requests.get(url, params=payload)
        data = r.json()
        return data["message"]

    def y_up(self, distance: float, speed: str):
        payload = {'distance': distance, 'speed': speed}
        url = self.url + "y_up"
        r = requests.get(url, params=payload)
        data = r.json()
        return data["message"]

    def y_down(self, distance: float, speed: str):
        payload = {'distance': distance, 'speed': speed}
        url = self.url + "y_down"
        r = requests.get(url, params=payload)
        data = r.json()
        return data["message"]

    def z_forward(self, distance: float, speed: str):
        payload = {'distance': distance, 'speed': speed}
        url = self.url + "z_forward"
        r = requests.get(url, params=payload)
        data = r.json()
        return data["message"]

    def z_back(self, distance: float, speed: str):
        payload = {'distance': distance, 'speed': speed}
        url = self.url + "z_back"
        r = requests.get(url, params=payload)
        data = r.json()
        return data["message"]

    def yaw_left(self, distance: float, speed: str):
        payload = {'distance': distance, 'speed': speed}
        url = self.url + "yaw_left"
        r = requests.get(url, params=payload)
        data = r.json()
        return data["message"]

    def yaw_right(self, distance: float, speed: str):
        payload = {'distance': distance, 'speed': speed}
        url = self.url + "yaw_right"
        r = requests.get(url, params=payload)
        data = r.json()
        return data["message"]

    def pitch_up(self, distance: float, speed: str):
        payload = {'distance': distance, 'speed': speed}
        url = self.url + "pitch_up"
        r = requests.get(url, params=payload)
        data = r.json()
        return data["message"]

    def pitch_down(self, distance: float, speed: str):
        payload = {'distance': distance, 'speed': speed}
        url = self.url + "pitch_down"
        r = requests.get(url, params=payload)
        data = r.json()
        return data["message"]

    def stop(self, axis: str):
        payload = {'axis': axis}
        url = self.url + "stop"
        r = requests.get(url, params=payload)
        data = r.json()
        return data["message"]

    def is_sensor_x_left(self):
        url = self.url + "is_sensor_x_left"
        r = requests.get(url)
        data = r.json()
        return data["message"]

    def is_sensor_x_org(self):
        url = self.url + "is_sensor_x_org"
        r = requests.get(url)
        data = r.json()
        return data["message"]

    def is_sensor_x_right(self):
        url = self.url + "is_sensor_x_right"
        r = requests.get(url)
        data = r.json()
        return data["message"]

    def is_sensor_x_move(self):
        url = self.url + "is_sensor_x_move"
        r = requests.get(url)
        data = r.json()
        return data["message"]

    def is_sensor_y_down(self):
        url = self.url + "is_sensor_y_down"
        r = requests.get(url)
        data = r.json()
        return data["message"]

    def is_sensor_y_org(self):
        url = self.url + "is_sensor_y_org"
        r = requests.get(url)
        data = r.json()
        return data["message"]

    def is_sensor_y_up(self):
        url = self.url + "is_sensor_y_up"
        r = requests.get(url)
        data = r.json()
        return data["message"]

    def is_sensor_y_move(self):
        url = self.url + "is_sensor_y_move"
        r = requests.get(url)
        data = r.json()
        return data["message"]

    def is_sensor_z_back(self):
        url = self.url + "is_sensor_z_back"
        r = requests.get(url)
        data = r.json()
        return data["message"]

    def is_sensor_z_org(self):
        url = self.url + "is_sensor_z_org"
        r = requests.get(url)
        data = r.json()
        return data["message"]

    def is_sensor_z_forward(self):
        url = self.url + "is_sensor_z_forward"
        r = requests.get(url)
        data = r.json()
        return data["message"]

    def is_sensor_z_move(self):
        url = self.url + "is_sensor_z_move"
        r = requests.get(url)
        data = r.json()
        return data["message"]

    def is_sensor_yaw_left(self):
        url = self.url + "is_sensor_yaw_left"
        r = requests.get(url)
        data = r.json()
        return data["message"]

    def is_sensor_yaw_org(self):
        url = self.url + "is_sensor_yaw_org"
        r = requests.get(url)
        data = r.json()
        return data["message"]

    def is_sensor_yaw_right(self):
        url = self.url + "is_sensor_yaw_right"
        r = requests.get(url)
        data = r.json()
        return data["message"]

    def is_sensor_yaw_move(self):
        url = self.url + "is_sensor_yaw_move"
        r = requests.get(url)
        data = r.json()
        return data["message"]

    def is_sensor_pitch_down(self):
        url = self.url + "is_sensor_pitch_down"
        r = requests.get(url)
        data = r.json()
        return data["message"]

    def is_sensor_pitch_org(self):
        url = self.url + "is_sensor_pitch_org"
        r = requests.get(url)
        data = r.json()
        return data["message"]

    def is_sensor_pitch_up(self):
        url = self.url + "is_sensor_pitch_up"
        r = requests.get(url)
        data = r.json()
        return data["message"]

    def is_sensor_pitch_move(self):
        url = self.url + "is_sensor_pitch_move"
        r = requests.get(url)
        data = r.json()
        return data["message"]
