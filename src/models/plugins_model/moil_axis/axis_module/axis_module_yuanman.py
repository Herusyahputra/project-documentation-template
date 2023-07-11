import time

import serial
from serial.tools.list_ports import comports

from .abstract_axis_module import AbstractAxisModule


class AxisModuleYuanman(AbstractAxisModule):

    def __init__(self):
        # Arduino Serial Port & Baud
        self.arduino_com_port = "COM4"
        self.arduino_baud_rate = 115200

        # CRUX Serial Port & Baud
        self.crux_com_port = "COM3"
        self.crux_baud_rate = 9600

        # isOpen
        self.is_serial_crux_open = False
        self.is_serial_arduino_open = False
        # Serial Object
        self.serial_arduino = None
        self.serial_crux = None
        # Speed String Conversion
        self.speed_dict = {
            "speed0": "0",
            "speed1": "1",
            "speed2": "2",
            "speed3": "3",
            "speed4": "4",
            "speed5": "5",
            "speed6": "6",
            "speed7": "7",
            "speed8": "8",
            "speed9": "9",
        }

        # Axis String Conversion
        self.axis_dict = {"pitch": "1", "yaw": "2", "x": "3", "y": "4", "z": "5"}
        # FRP Direction String Conversion
        self.crux_direction_dict = {"cw": "0", "ccw": "1"}
        self.arduino_direction_dict = {"cw": "1", "ccw": "0"}
        # Response Mode String Conversion
        self.response_method_dict = {"completed": "0", "quick": "1"}
        # Connect Serial
        self.connect_serial()

    def home(self, axis: str):
        axis = axis.lower()
        return self.org(axis)
    
    def new_home(self,axis:str):
        is_axis_cw = False
        self.frp(axis,7,"cw")
        while True:
            status = self.status(axis+"_org")
            if status[1]:
                if not is_axis_cw:
                    self.stop(axis)
                    break
                if is_axis_cw:
                    time.sleep(3)
                    self.frp(axis,7,"cw")
                    is_axis_cw = False
            status = self.status(axis+"_cw")
            if status[1]:
                if not is_axis_cw:
                    is_axis_cw = True
                    self.frp(axis,7,"ccw")

        return 0

    def x_left(self, distance: float, speed: str):
        amount = int(distance / 0.002)
        amount = amount * 2
        speed = speed.lower()
        if speed == "high":
            speed_int = 7
        elif speed == "mid":
            speed_int = 5
        elif speed == "low":
            speed_int = 3
        else:
            speed_int = 3

        return self.rps("x", speed_int, amount)

    def x_right(self, distance: float, speed: str):
        amount = int(distance / 0.002)
        amount = amount * 2
        speed = speed.lower()
        if speed == "high":
            speed_int = 7
        elif speed == "mid":
            speed_int = 5
        elif speed == "low":
            speed_int = 3
        else:
            speed_int = 3

        return self.rps("x", speed_int, -amount)

    def y_up(self, distance: float, speed: str):
        amount = int(distance / 0.002)
        amount = amount * 2
        speed = speed.lower()
        if speed == "high":
            speed_int = 7
        elif speed == "mid":
            speed_int = 5
        elif speed == "low":
            speed_int = 3
        else:
            speed_int = 3

        return self.rps("y", speed_int, -amount)

    def y_down(self, distance: float, speed: str):
        amount = int(distance / 0.002)
        amount = amount * 2
        speed = speed.lower()
        if speed == "high":
            speed_int = 7
        elif speed == "mid":
            speed_int = 5
        elif speed == "low":
            speed_int = 3
        else:
            speed_int = 3

        return self.rps("y", speed_int, amount)

    def z_forward(self, distance: float, speed: str):
        amount = int(distance / 0.005)
        amount = amount * 2
        speed = speed.lower()
        if speed == "high":
            speed_int = 7
        elif speed == "mid":
            speed_int = 5
        elif speed == "low":
            speed_int = 3
        else:
            speed_int = 3

        return self.rps("z", speed_int, -amount)

    def z_back(self, distance: float, speed: str):
        amount = int(distance / 0.005)
        amount = amount *2
        speed = speed.lower()
        if speed == "high":
            speed_int = 7
        elif speed == "mid":
            speed_int = 5
        elif speed == "low":
            speed_int = 3
        else:
            speed_int = 3

        return self.rps("z", speed_int, amount)

    def yaw_right(self, distance: float, speed: str):
        amount = int(distance / 0.00067)
        speed = speed.lower()
        if speed == "high":
            speed_int = 7
        elif speed == "mid":
            speed_int = 5
        elif speed == "low":
            speed_int = 3
        else:
            speed_int = 3

        return self.rps("yaw", speed_int, -amount)

    def yaw_left(self, distance: float, speed: str):
        amount = int(distance / 0.00067)
        speed = speed.lower()
        if speed == "high":
            speed_int = 7
        elif speed == "mid":
            speed_int = 5
        elif speed == "low":
            speed_int = 3
        else:
            speed_int = 3

        return self.rps("yaw", speed_int, amount)

    def pitch_down(self, distance: float, speed: str):
        amount = int(distance / 0.00084)
        speed = speed.lower()
        if speed == "high":
            speed_int = 7
        elif speed == "mid":
            speed_int = 5
        elif speed == "low":
            speed_int = 3
        else:
            speed_int = 3

        return self.rps("pitch", speed_int, amount)

    def pitch_up(self, distance: float, speed: str):
        amount = int(distance / 0.00084)
        speed = speed.lower()
        if speed == "high":
            speed_int = 7
        elif speed == "mid":
            speed_int = 5
        elif speed == "low":
            speed_int = 3
        else:
            speed_int = 3

        return self.rps("pitch", speed_int, -amount)

    def stop(self, axis: str):
        axis = axis.lower()
        return self.stp(axis)

    def is_sensor_x_left(self):
        check,data = self.status("x_cw")
        if isinstance(check,bool):
            if check:
                if data == '0':
                    return True
                else:
                    return False
            else:
                return data
        elif isinstance(check,str):
            return check
        return "ERROR"

    def is_sensor_x_org(self):
        check,data = self.status("x_org")
        if isinstance(check,bool):
            if check:
                if data == '0':
                    return True
                else:
                    return False
            else:
                return data
        elif isinstance(check,str):
            return check
        return "ERROR"

    def is_sensor_x_right(self):
        check,data = self.status("x_ccw")
        if isinstance(check,bool):
            if check:
                if data == '0':
                    return True
                else:
                    return False
            else:
                return data
        elif isinstance(check,str):
            return check
        return "ERROR"

    def is_sensor_x_move(self):
        check,data = self.status("x")
        if isinstance(check,bool):
            if check:
                if data == '1':
                    return True
                else:
                    return False
            else:
                return data
        elif isinstance(check,str):
            return check
        return "ERROR"

    def is_sensor_y_down(self):
        check,data = self.status("y_cw")
        if isinstance(check,bool):
            if check:
                if data == '0':
                    return True
                else:
                    return False
            else:
                return data
        elif isinstance(check,str):
            return check
        return "ERROR"

    def is_sensor_y_org(self):
        check,data = self.status("y_org")
        if isinstance(check,bool):
            if check:
                if data == '0':
                    return True
                else:
                    return False
            else:
                return data
        elif isinstance(check,str):
            return check
        return "ERROR"

    def is_sensor_y_up(self):
        check,data = self.status("y_ccw")
        if isinstance(check,bool):
            if check:
                if data == '0':
                    return True
                else:
                    return False
            else:
                return data
        elif isinstance(check,str):
            return check
        return "ERROR"

    def is_sensor_y_move(self):
        check,data = self.status("y")
        if isinstance(check,bool):
            if check:
                if data == '1':
                    return True
                else:
                    return False
            else:
                return data
        elif isinstance(check,str):
            return check
        return "ERROR"

    def is_sensor_z_back(self):
        check,data = self.status("z_cw")
        if isinstance(check,bool):
            if check:
                if data == '0':
                    return True
                else:
                    return False
            else:
                return data
        elif isinstance(check,str):
            return check
        return "ERROR"

    def is_sensor_z_org(self):
        check,data = self.status("z_org")
        if isinstance(check,bool):
            if check:
                if data == '0':
                    return True
                else:
                    return False
            else:
                return data
        elif isinstance(check,str):
            return check
        return "ERROR"

    def is_sensor_z_forward(self):
        check,data = self.status("z_ccw")
        if isinstance(check,bool):
            if check:
                if data == '0':
                    return True
                else:
                    return False
            else:
                return data
        elif isinstance(check,str):
            return check
        return "ERROR"

    def is_sensor_z_move(self):
        check,data = self.status("z")
        if isinstance(check,bool):
            if check:
                if data == '1':
                    return True
                else:
                    return False
            else:
                return data
        elif isinstance(check,str):
            return check
        return "ERROR"

    def is_sensor_yaw_left(self):
        check,data = self.status("yaw_cw")
        if isinstance(check,bool):
            if check:
                if data == '1':
                    return True
                else:
                    return False
            else:
                return data
        elif isinstance(check,str):
            return check
        return "ERROR"

    def is_sensor_yaw_org(self):
        check,data = self.status("yaw_org")
        if isinstance(check,bool):
            if check:
                if data == '1':
                    return True
                else:
                    return False
            else:
                return data
        elif isinstance(check,str):
            return check
        return "ERROR"

    def is_sensor_yaw_right(self):
        check,data = self.status("yaw_ccw")
        if isinstance(check,bool):
            if check:
                if data == '1':
                    return True
                else:
                    return False
            else:
                return data
        elif isinstance(check,str):
            return check
        return "ERROR"

    def is_sensor_yaw_move(self):
        check,data = self.status("yaw")
        if isinstance(check,bool):
            if check:
                if data == '1':
                    return True
                else:
                    return False
            else:
                return data
        elif isinstance(check,str):
            return check
        return "ERROR"

    def is_sensor_pitch_down(self):
        check,data = self.status("pitch_cw")
        if isinstance(check,bool):
            if check:
                if data == '1':
                    return True
                else:
                    return False
            else:
                return data
        elif isinstance(check,str):
            return check
        return "ERROR"

    def is_sensor_pitch_org(self):
        check,data = self.status("pitch_org")
        if isinstance(check,bool):
            if check:
                if data == '1':
                    return True
                else:
                    return False
            else:
                return data
        elif isinstance(check,str):
            return check
        return "ERROR"

    def is_sensor_pitch_up(self):
        check,data = self.status("pitch_ccw")
        if isinstance(check,bool):
            if check:
                if data == '1':
                    return True
                else:
                    return False
            else:
                return data
        elif isinstance(check,str):
            return check
        return "ERROR"

    def is_sensor_pitch_move(self):
        check,data = self.status("pitch")
        if isinstance(check,bool):
            if check:
                if data == '1':
                    return True
                else:
                    return False
            else:
                return data
        elif isinstance(check,str):
            return check
        return "ERROR"

    def set_crux_com_port(self, com_port):
        self.crux_com_port = com_port
        print("AxisModule.set_crux_com_prot(): Set CRUX Comport:", self.crux_com_port)

    # Set Comport of ARDUINO
    def set_arduino_com_port(self, com_port):
        self.arduino_com_port = com_port
        print(
            "AxisModule.set_crux_com_port(): Set ARDUINO Comport:",
            self.arduino_com_port,
        )

    # Create serial object of "ARDUINO" and "CRUX" at same time
    def connect_serial(self):

        ports = [p.device for p in comports()]
        # Check Serial Port
        if self.crux_com_port not in ports:
            return "CRUX Serial connect error: " + self.crux_com_port + " is not found"

        if self.arduino_com_port not in ports:
            return (
                    "ARDUINO Serial connect error: "
                    + self.arduino_com_port
                    + " is not found"
            )

        try:
            print(
                "AxisModule.connect_serial(): Connect CRUX Serial: "
                + self.crux_com_port
                + ", "
                + str(self.crux_baud_rate)
            )
            self.serial_crux = serial.Serial(self.crux_com_port, self.crux_baud_rate)
        except serial.SerialException as e:
            print("AxisModule.connect_serial(): CRUX_SerialException: " + str(e))
            return "CRUX Serial connect error: \n\n" + str(e)

        try:
            print(
                "AxisModule.connect_serial(): Connect ARDUINO Serial: "
                + self.arduino_com_port
                + ", "
                + str(self.arduino_baud_rate)
            )
            self.serial_arduino = serial.Serial(
                self.arduino_com_port, self.arduino_baud_rate
            )
        except serial.SerialException as e:
            print("AxisModule.connect_serial(): ARDUINO_SerialException: " + str(e))
            return "ARDUINO Serial connect error: \n\n" + str(e)
        time.sleep(0.1)

        self.is_serial_crux_open = True
        self.is_serial_arduino_open = True

        time.sleep(0.81)
        return "Connect Successes"

    # Close serial port of "ARDUINO" and "CRUX" at same time
    def close_serial(self):

        if self.is_serial_crux_open and self.is_serial_arduino_open:
            print(
                "AxisModule.close_serial(): Close ARDUINO Serial: "
                + self.arduino_com_port
            )
            self.serial_arduino.close()

            print("AxisModule.close_serial(): Close CRUX Serial: " + self.crux_com_port)
            self.serial_crux.close()

            self.is_serial_crux_open = False
            self.is_serial_arduino_open = False

        else:
            print("AxisModule.close_serial: !!!ERROR!!! Serial Port is not open")

    # When send HEX format command to serial
    # This method must be told which "stage_type" is to be used to send the command
    def send_command_to_serial(self, string_command):
        if string_command.startswith("STX"):
            string_command = string_command[3:]

        # Convert string command to b'\x02<Command>\r\n'
        serial_command = self.convert_command_to_hex(string_command)

        # Check which comport must be use to send command
        result, return_value = self.check_stage_type(string_command)

        if not result:
            error_msg = return_value
            return False, error_msg

        else:
            stage_type = return_value

        if self.is_serial_crux_open and self.is_serial_arduino_open:

            if stage_type == "CRUX":
                try:
                    self.serial_crux.flushInput()
                    print(
                        "AxisModule.send_command_to_serial(): Send Command to CRUX: "
                        + str(serial_command)
                    )
                    self.serial_crux.write(serial_command)
                    time.sleep(0.1)
                    return_from_serial = self.serial_crux.readline(self.serial_crux.in_waiting)
                    print(
                        "AxisModule.send_command_to_serial(): Return value from Serial is [ "
                        + str(return_from_serial)
                        + "]"
                    )
                    print(
                        "AxisModule.send_command_to_serial(): Return String value from Serial is [ "
                        + str(return_from_serial.decode())
                        + "]"
                    )
                    time.sleep(0.1)

                except Exception as e:
                    print(e)
                    return False, str(e)

                return True, return_from_serial

            elif stage_type == "ARDUINO":
                try:
                    self.serial_arduino.flushInput()
                    print(
                        "AxisModule.send_command_to_serial(): Send Command to ARDUINO: "
                        + str(serial_command)
                    )

                    self.serial_arduino.write(serial_command)
                    time.sleep(0.01)

                    return_from_serial = self.serial_arduino.read(
                        self.serial_arduino.in_waiting
                    )
                    print(
                        "AxisModule.send_command_to_serial(): Return Bytes value from Serial is [ "
                        + str(return_from_serial)
                        + " ]"
                    )
                    print(
                        "AxisModule.send_command_to_serial(): Return String value from Serial is [ "
                        + str(return_from_serial.decode())
                        + " ]"
                    )
                    time.sleep(0.01)

                except Exception as e:
                    print(e)
                    return False, str(e)
                return True, return_from_serial

            else:
                print(
                    'AxisModule.send_command_to_serial: !!!ERROR!!! stage_type is not "CRUX" or "ARDUINO"'
                )
                return False, 'AxisModule.send_command_to_serial: !!!ERROR!!! stage_type is not "CRUX" or "ARDUINO"'

        else:
            print(
                "AxisModule.send_command_to_serial: !!!ERROR!!! Serial Port is not open"
            )
            return False, "AxisModule.send_command_to_serial: !!!ERROR!!! Serial Port is not open"

    # Convert command to HEX format
    # err msg don't need
    @staticmethod
    def convert_command_to_hex(command_without_header):
        if command_without_header.startswith("STX"):
            command_without_header = command_without_header[3:]
        final_hex_command = b"\x02"
        final_hex_command += command_without_header.encode("UTF-8")
        final_hex_command += b"\r\n"
        return final_hex_command

    # Check stage_type by axis_num
    # axis_num = 1 or 2 --> return stage_type = "CRUX"
    # axis_num = 3 or 4 or 5 or 6 --> return stage_type = "ARDUINO"
    # err msg ok
    @staticmethod
    def check_stage_type(string_command):
        axis_num = string_command[3]
        print("AxisModule.check_stage_type(): axis_num = " + axis_num)

        if axis_num in ["1", "2"]:
            print('AxisModule.check_stage_type(): StageType is "CRUX"')
            return True, "CRUX"

        elif axis_num in ["3", "4", "5", "6"]:
            print('AxisModule.check_stage_type(): StageType is "ARDUINO"')
            return True, "ARDUINO"

        else:
            print(
                'AxisModule.check_stage_type(): !!!ERROR!!! axis_num is not in "1~6" '
            )
            return False, 'AxisModule.check_stage_type(): !!!ERROR!!! axis_num is not in "1~6" '

    # Axis Controller API
    """~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ [API START] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

    # ORG: Origin Return Drive
    def org(self, axis: str):
        time.sleep(0.05)

        axis_num = str(self.axis_dict[axis])

        print("[ Origin Return Drive: Axis-" + str(axis) + " ]")

        if axis in ['yaw', 'pitch']:
            # Ex: command = "ORG2/7/0"
            command = ("ORG" + axis_num + "/7/0")
        elif axis in ['x', 'y', 'z']:
            # Ex: command = "ORG4/8"
            command = ("ORG" + axis_num + "/8/0")

        return self.send_command_to_serial(command)

    # FRP: Free Rotation Drive
    def frp(self, axis: str, speed: int, direction: str):
        time.sleep(0.05)

        print("[ Free Rotation Driver: Axis-" + str(axis) + " ]")

        if axis in ["yaw", "pitch"]:
            moving_direction = self.crux_direction_dict[direction]
        elif axis in ["x", "y", "z"]:
            moving_direction = self.arduino_direction_dict[direction]

        # Ex: command = "FRP3/8/ccw"
        command = "FRP" + str(self.axis_dict[axis]) + "/" + str(speed) + "/" + str(moving_direction)

        return self.send_command_to_serial(command)

    # STP: Motor Stop
    def stp(self, axis: str):
        print("[ Motor Stop: Axis-" + str(axis) + " ]")

        # Ex: command = "STP5/0"
        command = "STP" + str(self.axis_dict[axis]) + "/0"

        return self.send_command_to_serial(command)

    # RDP: Read Present Position
    def rdp(self, axis: str):
        time.sleep(0.05)

        print("[ Read Present Position: Axis-" + str(axis) + " ]")

        # Ex: command = "RDP5"
        command = "RDP" + str(self.axis_dict[axis])

        if axis in ['yaw', 'pitch']:
            check, result = self.send_command_to_serial(command)
            print('[result]', result)
            if check:
                coordinate = result.decode(encoding='ascii')[7:]
                return check, coordinate
            else:
                return check, result
        elif axis in ['x', 'y', 'z']:
            check, result = self.send_command_to_serial(command)
            print('[result]', result)
            if check:
                coordinate = result.decode(encoding='ascii')[6:]
                return check, coordinate
            else:
                return check, result

    # WRP: Write Present Position
    def wrp(self, axis: str, amount: int):
        time.sleep(0.05)

        print("[ Write Present Position: Axis-" + str(axis) + " ]")

        if axis in ['pitch', 'yaw']:

            if -8388607 < amount or amount < 8388607:
                return False, 'amount over limit'

            # Ex: command = "WRP1/-576700"
            command = "WRP" + str(self.axis_dict[axis]) + "/" + str(amount)

        elif axis in ['x', 'y', 'z']:

            if 200000 < amount or amount < 9800000:
                return False, 'amount over limit'
            # Ex: command = "WRP5/7379745"
            if amount >= 0:
                command = "WRP" + str(self.axis_dict[axis]) + "/" + str(amount).zfill(8)
            elif amount < 0:
                command = "WRP" + str(self.axis_dict[axis]) + "/" + str(amount).zfill(9)

        return self.send_command_to_serial(command)

    # RPS: Relative Position Drive
    def rps(self, axis: str, speed: int, amount: int):
        time.sleep(0.05)

        print("[ Relative Position Drive: Axis-" + str(axis) + " ]")

        if axis in ['pitch', 'yaw']:

            if amount < -16777215 or 16777215 < amount:
                return False, 'amount over limit'

            # Ex: command = "RPS1/7/-576700/5"
            command = "RPS" + str(self.axis_dict[axis]) + "/" + str(speed) + "/" + str(amount) + "/0"

        elif axis in ['x', 'y', 'z']:
            print(axis, amount, speed)
            if -195000 > amount or amount > 195000:
                return False, 'amount over limit'

            # Ex: command = "RPS5/7/379745/0"
            if amount >= 0:
                command = "RPS" + str(self.axis_dict[axis]) + "/" + str(speed) + "/" + str(amount).zfill(8) + "/0"
            else:
                command = "RPS" + str(self.axis_dict[axis]) + "/" + str(speed) + "/" + str(amount).zfill(9) + "/0"

        return self.send_command_to_serial(command)

    # STR: Read Status
    def status(self, sensor: str):
        time.sleep(0.05)

        print("[ Read Status: Axis-" + sensor + " ]")

        if sensor.startswith('pitch'):

            # Ex: command = "STR1"
            check, result = self.send_command_to_serial("STR1")
            if not check:
                return check, result

            stage_status = result.decode(encoding='ascii')
            if sensor == "pitch":
                return check, stage_status[7]
            elif sensor == "pitch_org":
                return check, stage_status[11]
            elif sensor == "pitch_ccw":
                return check, stage_status[13]
            elif sensor == "pitch_cw":
                return check, stage_status[15]

        elif sensor.startswith('yaw'):

            # Ex: command = "STR2"
            check, result = self.send_command_to_serial("STR2")
            if not check:
                return check, result

            stage_status = result.decode(encoding='ascii')

            if sensor == "yaw":
                return check, stage_status[7]
            if sensor == "yaw_org":
                return check, stage_status[11]
            elif sensor == "yaw_ccw":
                return check, stage_status[13]
            elif sensor == "yaw_cw":
                return check, stage_status[15]

        elif sensor.startswith('x') or sensor.startswith('y') or sensor.startswith('z'):

            # Ex: command = "STR6"
            check, result = self.send_command_to_serial("STR6")
            if not check:
                return check, result

            stage_status = result.decode(encoding='ascii')
            if sensor == "x":
                return check, stage_status[7]
            elif sensor == "y":
                return check, stage_status[8]
            elif sensor == "z":
                return check, stage_status[9]
            elif sensor == "x_cw":
                return check, stage_status[10]
            elif sensor == "x_org":
                return check, stage_status[11]
            elif sensor == "x_ccw":
                return check, stage_status[12]
            elif sensor == "y_cw":
                return check, stage_status[13]
            elif sensor == "y_org":
                return check, stage_status[14]
            elif sensor == "y_ccw":
                return check, stage_status[15]
            elif sensor == "z_cw":
                return check, stage_status[16]
            elif sensor == "z_org":
                return check, stage_status[17]
            elif sensor == "z_ccw":
                return check, stage_status[18]

        else:
            print(
                "AxisModule.str: !!!ERROR!!! Sensor argument wrong"
            )

            return 'ERROR'

    # Send Command by typing
    def send(self, command: str):
        return self.send_command_to_serial(command)
