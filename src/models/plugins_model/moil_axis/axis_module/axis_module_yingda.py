from distutils import bcppcompiler
import re
import time

import serial
from serial.tools.list_ports import comports

from .abstract_axis_module import AbstractAxisModule
import logging
from datetime import datetime


class AxisModuleYingDa(AbstractAxisModule):

    def __init__(self,
                 comport_yaw,
                 comport_pitch,
                 comport_x,
                 comport_y,
                 comport_z):

        self.comport_yaw = comport_yaw
        self.comport_pitch = comport_pitch
        self.comport_x = comport_x
        self.comport_y = comport_y
        self.comport_z = comport_z

        self.baudrate_yaw = 9600
        self.baudrate_pitch = 9600
        self.baudrate_x = 9600
        self.baudrate_y = 9600
        self.baudrate_z = 9600

        self.set_log_file_format()

        self.set_comport()

        # speed dict
        self.speed_z = {
            'Low': 500,
            'Mid': 1500,
            'High': 2500
        }
        self.speed_4axis = {
            'Low': 100,
            'Mid': 300,
            'High': 500
        }

        # isOpen
        self.is_serial_x_open = False
        self.is_serial_y_open = False
        self.is_serial_z_open = False
        self.is_serial_yaw_open = False
        self.is_serial_pitch_open = False

        # Serial Object
        self.serial_x = None
        self.serial_y = None
        self.serial_z = None
        self.serial_yaw = None
        self.serial_pitch = None

        # Connect Serial
        self.connect_serial()

        self.target_serial = None

    def set_log_file_format(self):
        # Example: now=2022-05-30 09:59:52.592
        # Formatting
        now = str(datetime.now()).split('.')[0].replace("-", "").replace(":", "").replace(" ", "-")
        # Example: now=20220530-095952

        filename = 'AxisYingDa_' + str(now) + '.log'
        print(filename)
        logging.basicConfig(format='%(levelname)s - '
                                   '%(asctime)s - YingDa - '
                                   '%(message)s - '
                                   '%(filename)s - '
                                   '%(funcName)s - '
                                   '%(lineno)d',
                            filename=filename,
                            encoding='utf-8',
                            level=logging.DEBUG)

    def set_comport(self):

        # [ Yaw ] Serial Port & Baud
        yaw_com_baud = str((self.comport_yaw, self.baudrate_yaw))
        logging.info('Yaw com, baud: ' + str(yaw_com_baud))

        # [ Pitch ] Serial Port & Baud
        pitch_com_baud = str((self.comport_pitch, self.baudrate_pitch))
        logging.info('Pitch com, baud: ' + str(pitch_com_baud))

        # [ X ] Serial Port & Baud
        x_com_baud = str((self.comport_x, self.baudrate_x))
        logging.info('X com, baud: ' + str(x_com_baud))

        # [ Y ] Serial Port & Baud
        y_com_baud = str((self.comport_y, self.baudrate_y))
        logging.info('Y com, baud: ' + str(y_com_baud))

        # [ Z ] Serial Port & Baud
        z_com_baud = str((self.comport_z, self.baudrate_z))
        logging.info('Z com, baud: ' + str(z_com_baud))


    # Create serial object of "ARDUINO" and "CRUX" at same time
    def connect_serial(self):

        logging.info('Connect Serial')
        ports = [p.device for p in comports()]

        # Check Serial Port
        if self.comport_x not in ports:
            err_msg = '!!!ERROR!!! connect_serial(): Serial port not found X: ' + self.comport_x
            logging.error(err_msg)
            print(err_msg)
            return err_msg

        if self.comport_y not in ports:
            err_msg = '!!!ERROR!!! connect_serial(): Serial port not found Y: ' + self.comport_y
            logging.error(err_msg)
            print(err_msg)
            return err_msg

        if self.comport_z not in ports:
            err_msg = '!!!ERROR!!! connect_serial(): Serial port not found Z: ' + self.comport_z
            logging.error(err_msg)
            print(err_msg)
            return err_msg

        if self.comport_yaw not in ports:
            err_msg = '!!!ERROR!!! connect_serial(): Serial port not found Yaw: ' + self.comport_yaw
            logging.error(err_msg)
            print(err_msg)
            return err_msg

        if self.comport_pitch not in ports:
            err_msg = '!!!ERROR!!! connect_serial(): Serial port not found Pitch: ' + self.comport_pitch
            logging.error(err_msg)
            print(err_msg)
            return err_msg

        # Connect Serial X
        try:
            logging.info('Serial X Connecting')
            self.serial_x = serial.Serial(self.comport_x, self.baudrate_x)
        except serial.SerialException as e:
            logging.error('X Serial connect error: \n\n" + str(e)')
            return "X Serial connect error: \n\n" + str(e)
        logging.info('Serial X Connected')

        # Connect Serial Y
        try:
            logging.info('Serial Y Connecting')
            self.serial_y = serial.Serial(self.comport_y, self.baudrate_y)
        except serial.SerialException as e:
            logging.error('Y Serial connect error: \n\n" + str(e)')
            return "Y Serial connect error: \n\n" + str(e)
        logging.info('Serial Y Connected')

        # Connect Serial Z
        try:
            logging.info('Serial Z Connecting')
            self.serial_z = serial.Serial(self.comport_z, self.baudrate_z)
        except serial.SerialException as e:
            logging.error('Z Serial connect error: \n\n" + str(e)')
            return "Z Serial connect error: \n\n" + str(e)
        logging.info('Serial Z Connected')

        # Connect Serial Yaw
        try:
            logging.info('Serial Yaw Connecting')
            self.serial_yaw = serial.Serial(self.comport_yaw, self.baudrate_yaw)
        except serial.SerialException as e:
            logging.error('Yaw Serial connect error: \n\n" + str(e)')
            return "Yaw Serial connect error: \n\n" + str(e)
        logging.info('Serial Yaw Connected')

        # Connect Serial Pitch
        try:
            logging.info('Serial Pitch Connecting')
            self.serial_pitch = serial.Serial(self.comport_pitch, self.baudrate_pitch)
        except serial.SerialException as e:
            logging.error('Pitch Serial connect error: \n\n" + str(e)')
            return "Pitch Serial connect error: \n\n" + str(e)
        logging.info('Serial Pitch Connected')

        time.sleep(0.1)

        self.is_serial_x_open = True
        self.is_serial_y_open = True
        self.is_serial_z_open = True
        self.is_serial_yaw_open = True
        self.is_serial_pitch_open = True

        time.sleep(0.81)
        return 'Successes'

    # Close serial port of "ARDUINO" and "CRUX" at same time
    def close_serial(self):

        if self.is_serial_x_open and \
                self.is_serial_y_open and \
                self.is_serial_z_open and \
                self.is_serial_yaw_open and \
                self.is_serial_pitch_open:

            self.serial_x.close()
            logging.info('Close X Serial')

            self.serial_y.close()
            logging.info('Close Y Serial')

            self.serial_z.close()
            logging.info('Close Z Serial')

            self.serial_yaw.close()
            logging.info('Close Yaw Serial')

            self.serial_pitch.close()
            logging.info('Close Pitch Serial')

            self.is_serial_x_open = False
            self.is_serial_y_open = False
            self.is_serial_z_open = False
            self.is_serial_yaw_open = False
            self.is_serial_pitch_open = False

        else:
            logging.error('Serial Port is not open')
            print("!!!ERROR!!! close_serial: Serial Port is not open")

    # Send command to serial
    def send_command_to_serial(self, command, axis):

        time.sleep(0.1)
        if self.is_serial_x_open and \
                self.is_serial_y_open and \
                self.is_serial_z_open and \
                self.is_serial_yaw_open and \
                self.is_serial_pitch_open:

            self.target_serial = self.__get_target_serial(axis)

            try:
                # Clean serial buffer
                self.target_serial.flushInput()

                # Send command to serial
                self.target_serial.write(str.encode(command + '\r\n'))
                time.sleep(0.1)

                # Read serial return
                serial_return = self.target_serial.read(self.target_serial.in_waiting)
                print('[Serial Return] ' + command)
                print(str(serial_return.decode()))
                time.sleep(0.1)

            except Exception as e:
                print(e)
                logging.error(str(e))

                return False, str(e)

            return True, serial_return

        else:
            print(
                '!!!ERROR!!! send_command_to_serial(): Serial Port is not open'
            )
            logging.error('Serial Port is not open')
            return False, "!!!ERROR!!! Serial Port is not open"

    def __get_target_serial(self, axis):
        if axis == 'x':
            return self.serial_x

        elif axis == 'y':
            return self.serial_y

        elif axis == 'z':
            return self.serial_z

        elif axis == 'yaw':
            return self.serial_yaw

        elif axis == 'pitch':
            return self.serial_pitch

        else:
            print('!!!ERROR!!! Axis_name is wrong: ', axis)
            logging.error( 'Axis_name is wrong: ' + axis)

    def home(self, axis: str):

        logging.info('Home_' + axis)
        command = 'VH=300'
        self.send_command_to_serial(command, axis)
        command = 'SAVE C'
        self.send_command_to_serial(command, axis)

        self.send_command_to_serial('H', axis)

    def x_left(self, distance: float, speed: str):

        speed = self.speed_4axis[speed]
        command = 'VM='+str(speed)
        self.send_command_to_serial(command, 'x')
        command = 'SAVE C'
        self.send_command_to_serial(command, 'x')

        self.send_command_to_serial('MR -' + str(distance), 'x')

    def x_right(self, distance: float, speed: str):

        speed = self.speed_4axis[speed]
        command = 'VM='+str(speed)
        self.send_command_to_serial(command, 'x')
        command = 'SAVE C'
        self.send_command_to_serial(command, 'x')

        self.send_command_to_serial('MR ' + str(distance), 'x')

    def y_up(self, distance: float, speed: str):

        speed = self.speed_4axis[speed]
        command = 'VM='+str(speed)
        self.send_command_to_serial(command, 'y')
        command = 'SAVE C'
        self.send_command_to_serial(command, 'y')

        self.send_command_to_serial('MR ' + str(distance), 'y')

    def y_down(self, distance: float, speed: str):

        speed = self.speed_4axis[speed]
        command = 'VM='+str(speed)
        self.send_command_to_serial(command, 'y')
        command = 'SAVE C'
        self.send_command_to_serial(command, 'y')

        self.send_command_to_serial('MR -' + str(distance), 'y')

    def z_forward(self, distance: float, speed: str):

        speed = self.speed_z[speed]
        command = 'VM='+str(speed)
        self.send_command_to_serial(command, 'z')
        command = 'SAVE C'
        self.send_command_to_serial(command, 'z')

        self.send_command_to_serial('MR ' + str(distance), 'z')

    def z_back(self, distance: float, speed: str):

        speed = self.speed_z[speed]
        command = 'VM='+str(speed)
        self.send_command_to_serial(command, 'z')
        command = 'SAVE C'
        self.send_command_to_serial(command, 'z')

        self.send_command_to_serial('MR -' + str(distance), 'z')

    def yaw_right(self, distance: float, speed: str):

        speed = self.speed_4axis[speed]
        command = 'VM='+str(speed)
        self.send_command_to_serial(command, 'yaw')
        command = 'SAVE C'
        self.send_command_to_serial(command, 'yaw')

        self.send_command_to_serial('MR -' + str(distance), 'yaw')

    def yaw_left(self, distance: float, speed: str):

        speed = self.speed_4axis[speed]
        command = 'VM='+str(speed)
        self.send_command_to_serial(command, 'yaw')
        command = 'SAVE C'
        self.send_command_to_serial(command, 'yaw')

        self.send_command_to_serial('MR ' + str(distance), 'yaw')

    def pitch_down(self, distance: float, speed: str):

        speed = self.speed_4axis[speed]
        command = 'VM='+str(speed)
        self.send_command_to_serial(command, 'pitch')
        command = 'SAVE C'
        self.send_command_to_serial(command, 'pitch')

        self.send_command_to_serial('MR ' + str(distance), 'pitch')

    def pitch_up(self, distance: float, speed: str):

        speed = self.speed_4axis[speed]
        command = 'VM='+str(speed)
        self.send_command_to_serial(command, 'pitch')
        command = 'SAVE C'
        self.send_command_to_serial(command, 'pitch')

        self.send_command_to_serial('MR -' + str(distance), 'pitch')

    def stop(self, axis: str):

        self.send_command_to_serial('STOP', axis)

    def is_sensor_x_left(self):

        value = self.send_command_to_serial('?IN3', "x")
        if value[0]:
            value = value[1].decode()[-3]
            # value = value[:]
            # value = value.decode()
            if value == '1':
                return True
            else:
                return False

    def is_sensor_x_org(self):
        value = self.send_command_to_serial('?IN1', "x")
        if value[0]:
            value = value[1].decode()[-3]
            # value = value[:]
            # value = value.decode()
            if value == '1':
                return True
            else:
                return False

    def is_sensor_x_right(self):
        value = self.send_command_to_serial('?IN2', "x")
        if value[0]:
            value = value[1].decode()[-3]
            # value = value[:]
            # value = value.decode()
            if value == '1':
                return True
            else:
                return False

    def is_sensor_x_move(self):

        value = self.send_command_to_serial('?ST', "x")
        if value[0]:
            value = value[1].decode()[-3]
            # value = value[:]
            # value = value.decode()
            if value == 'D':
                return True
            else:
                return False

    def is_sensor_y_down(self):

        value = self.send_command_to_serial('?IN3', "y")
        if value[0]:
            value = value[1].decode()[-3]
            # value = value[:]
            # value = value.decode()
            if value == '1':
                return True
            else:
                return False

    def is_sensor_y_org(self):

        value = self.send_command_to_serial('?IN1', "y")
        if value[0]:
            value = value[1].decode()[-3]
            # value = value[:]
            # value = value.decode()
            if value == '1':
                return True
            else:
                return False

    def is_sensor_y_up(self):

        value = self.send_command_to_serial('?IN2', "y")
        if value[0]:
            value = value[1].decode()[-3]
            # value = value[:]
            # value = value.decode()
            if value == '1':
                return True
            else:
                return False

    def is_sensor_y_move(self):

        value = self.send_command_to_serial('?ST', "y")
        if value[0]:
            value = value[1].decode()[-3]
            # value = value[:]
            # value = value.decode()
            if value == 'D':
                return True
            else:
                return False

    def is_sensor_z_back(self):

        value = self.send_command_to_serial('?IN1', "z")
        if value[0]:
            value = value[1].decode()[-3]
            # value = value[:]
            # value = value.decode()
            if value == '1':
                return True
            else:
                return False

    def is_sensor_z_org(self):
        return False

    def is_sensor_z_forward(self):

        value = self.send_command_to_serial('?IN2', "z")
        if value[0]:
            value = value[1].decode()[-3]
            # value = value[:]
            # value = value.decode()
            if value == '1':
                return True
            else:
                return False

    def is_sensor_z_move(self):

        value = self.send_command_to_serial('?ST', "z")
        if value[0]:
            value = value[1].decode()[-3]
            # value = value[:]
            # value = value.decode()
            if value == 'D':
                return True
            else:
                return False

    def is_sensor_yaw_left(self):

        value = self.send_command_to_serial('?IN3', "yaw")
        if value[0]:
            value = value[1].decode()[-3]
            # value = value[:]
            # value = value.decode()
            if value == '1':
                return True
            else:
                return False

    def is_sensor_yaw_org(self):

        value = self.send_command_to_serial('?IN1', "yaw")
        if value[0]:
            value = value[1].decode()[-3]
            # value = value[:]
            # value = value.decode()
            if value == '1':
                return True
            else:
                return False

    def is_sensor_yaw_right(self):

        value = self.send_command_to_serial('?IN2', "yaw")
        if value[0]:
            value = value[1].decode()[-3]
            # value = value[:]
            # value = value.decode()
            if value == '1':
                return True
            else:
                return False

    def is_sensor_yaw_move(self):

        value = self.send_command_to_serial('?ST', "yaw")
        if value[0]:
            value = value[1].decode()[-3]
            # value = value[:]
            # value = value.decode()
            if value == 'D':
                return True
            else:
                return False

    def is_sensor_pitch_down(self):

        value = self.send_command_to_serial('?IN2', "pitch")
        if value[0]:
            value = value[1].decode()[-3]
            # value = value[:]
            # value = value.decode()
            if value == '1':
                return True
            else:
                return False

    def is_sensor_pitch_org(self):

        value = self.send_command_to_serial('?IN1', "pitch")
        if value[0]:
            value = value[1].decode()[-3]
            # value = value[:]
            # value = value.decode()
            if value == '1':
                return True
            else:
                return False

    def is_sensor_pitch_up(self):

        value = self.send_command_to_serial('?IN3', "pitch")
        if value[0]:
            value = value[1].decode()[-3]
            # value = value[:]
            # value = value.decode()
            if value == '1':
                return True
            else:
                return False

    def is_sensor_pitch_move(self):

        value = self.send_command_to_serial('?ST', "pitch")
        if value[0]:
            value = value[1].decode()[-3]
            # value = value[:]
            # value = value.decode()
            if value == 'D':
                return True
            else:
                return False


if __name__ == '__main__':
    axis_controller = AxisModuleYingDa()
    # axis_controller.home("x")
    axis_controller.is_sensor_pitch_up()
    axis_controller.is_sensor_pitch_down()

    axis_controller.pitch_up(20, 'mid')
    while axis_controller.is_sensor_pitch_move():
        time.sleep(0.5)
    axis_controller.is_sensor_pitch_up()
    axis_controller.is_sensor_pitch_down()

    axis_controller.pitch_down(20, 'mid')
    while axis_controller.is_sensor_pitch_move():
        time.sleep(0.5)
    axis_controller.is_sensor_pitch_up()
    axis_controller.is_sensor_pitch_down()
