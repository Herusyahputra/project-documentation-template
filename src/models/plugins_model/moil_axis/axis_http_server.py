from fastapi import FastAPI
from .axis_module.axis_module_yuanman import AxisModuleYuanman
from .axis_module.axis_module_yingda import AxisModuleYingDa

axis_http_server_ip = "192.168.113.56"


class AxisHttpServer(FastAPI):
    def __init__(self, module):
        super().__init__(title="AxisHttpServer")

        @self.get("/close_serial")
        def close_serial():
            return {"message": module.close_serial()}

        @self.get("/home")
        def home(axis: str):
            return {"message": module.home(axis)}

        @self.get("/new_home")
        def new_home(axis: str):
            return {"message": module.new_home(axis)}

        @self.get("/x_left")
        def x_left(distance: float, speed: str):
            return {"message": module.x_left(distance, speed)}

        @self.get("/x_right")
        def x_right(distance: float, speed: str):
            return {"message": module.x_right(distance, speed)}

        @self.get("/y_up")
        def y_up(distance: float, speed: str):
            return {"message": module.y_up(distance, speed)}

        @self.get("/y_down")
        def y_down(distance: float, speed: str):
            return {"message": module.y_down(distance, speed)}

        @self.get("/z_forward")
        def z_forward(distance: float, speed: str):
            return {"message": module.z_forward(distance, speed)}

        @self.get("/z_back")
        def z_back(distance: float, speed: str):
            return {"message": module.z_back(distance, speed)}

        @self.get("/yaw_left")
        def yaw_left(distance: float, speed: str):
            return {"message": module.yaw_left(distance, speed)}

        @self.get("/yaw_right")
        def yaw_right(distance: float, speed: str):
            return {"message": module.yaw_right(distance, speed)}

        @self.get("/pitch_up")
        def pitch_up(distance: float, speed: str):
            return {"message": module.pitch_up(distance, speed)}

        @self.get("/pitch_down")
        def pitch_down(distance: float, speed: str):
            return {"message": module.pitch_down(distance, speed)}

        @self.get("/stop")
        def stop(axis: str):
            return {"message": module.stop(axis)}

        @self.get("/is_sensor_x_left")
        def is_sensor_x_left():
            return {"message": module.is_sensor_x_left()}

        @self.get("/is_sensor_x_org")
        def is_sensor_x_org():
            return {"message": module.is_sensor_x_org()}

        @self.get("/is_sensor_x_right")
        def is_sensor_x_right():
            return {"message": module.is_sensor_x_right()}

        @self.get("/is_sensor_x_move")
        def is_sensor_x_move():
            return {"message": module.is_sensor_x_move()}

        @self.get("/is_sensor_y_down")
        def is_sensor_y_down():
            return {"message": module.is_sensor_y_down()}

        @self.get("/is_sensor_y_org")
        def is_sensor_y_org():
            return {"message": module.is_sensor_y_org()}

        @self.get("/is_sensor_y_up")
        def is_sensor_y_up():
            return {"message": module.is_sensor_y_up()}

        @self.get("/is_sensor_y_move")
        def is_sensor_y_move():
            return {"message": module.is_sensor_y_move()}

        @self.get("/is_sensor_z_back")
        def is_sensor_z_back():
            return {"message": module.is_sensor_z_back()}

        @self.get("/is_sensor_z_org")
        def is_sensor_z_org():
            return {"message": module.is_sensor_z_org()}

        @self.get("/is_sensor_z_forward")
        def is_sensor_z_forward():
            return {"message": module.is_sensor_z_forward()}

        @self.get("/is_sensor_z_move")
        def is_sensor_z_move():
            return {"message": module.is_sensor_z_move()}

        @self.get("/is_sensor_yaw_left")
        def is_sensor_yaw_left():
            return {"message": module.is_sensor_yaw_left()}

        @self.get("/is_sensor_yaw_org")
        def is_sensor_yaw_org():
            return {"message": module.is_sensor_yaw_org()}

        @self.get("/is_sensor_yaw_right")
        def is_sensor_yaw_right():
            return {"message": module.is_sensor_yaw_right()}

        @self.get("/is_sensor_yaw_move")
        def is_sensor_yaw_move():
            return {"message": module.is_sensor_yaw_move()}

        @self.get("/is_sensor_pitch_down")
        def is_sensor_pitch_down():
            return {"message": module.is_sensor_pitch_down()}

        @self.get("/is_sensor_pitch_org")
        def is_sensor_pitch_org():
            return {"message": module.is_sensor_pitch_org()}

        @self.get("/is_sensor_pitch_up")
        def is_sensor_pitch_up():
            return {"message": module.is_sensor_pitch_up()}

        @self.get("/is_sensor_pitch_move")
        def is_sensor_pitch_move():
            return {"message": module.is_sensor_pitch_move()}

# try:
#     import uvicorn
#     from .axis_module.axis_module_yuanman import AxisModuleYuanman
#     from .axis_module.axis_module_yingda import AxisModuleYingDa
#
#     app = AxisHttpServer(AxisModuleYuanman())
#
#     uvicorn.run(app, host=axis_http_server_ip, port=8000, log_level="info")
#
# except:
#     print(f"Cant make a connection to this Ip Address: '{axis_http_server_ip}' for stage panel server")
