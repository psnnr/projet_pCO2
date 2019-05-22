import serial

class serial_connexion(cls):

    def __init__(self,cls):
        self.serial_gps = ser_interface_box_chip = serial.Serial(str(cls.get_interface_box_chip_serial_port()),
        baudrate=int(cls.get_interface_box_chip_baudrate()),
        parity=eval("serial." +(cls.get_interface_box_chip_parity())),
        stopbits=eval("serial."+(cls.get_interface_box_chip_stops_bits())),
        bytesize = eval("serial."+ cls.get_interface_box_chip_bytesize()))

u = serial_connexion()


def init_time(cls):
    w = cls.get_t_mesure_atm_air()
    u = int(w)

def init_elec_device(cls):


    ### initialisation interface box chip

    ser_interface_box_chip = serial.Serial(str(cls.get_interface_box_chip_serial_port()),
    baudrate=int(cls.get_interface_box_chip_baudrate()),
    parity=eval("serial." +(cls.get_interface_box_chip_parity())),
    stopbits=eval("serial."+(cls.get_interface_box_chip_stops_bits())),
    bytesize = eval("serial."+ cls.get_interface_box_chip_bytesize()))

    ### initialisation GPS

    ser_GPS = serial.Serial(str(cls.get_gps_serial_port()),
    baudrate=int(cls.get_gps_baudrate()),
    parity=eval("serial." +(cls.get_gps_parity())),
    stopbits=eval("serial."+(cls.get_gps_stops_bits())),
    bytesize = eval("serial."+ cls.get_gps_bytesize()))

    ### initialisation oxygen sensor

    ser_oxygen = serial.Serial(str(cls.get_oxygen_sensor_serial_port()),
    baudrate=int(cls.get_oxygen_sensor_baudrate()),
    parity=eval("serial." +(cls.get_oxygen_sensor_parity())),
    stopbits=eval("serial."+(cls.get_oxygen_sensor_stops_bits())),
    bytesize = eval("serial."+ cls.get_oxygen_sensor_bytesize()))

    ### initialisation temperature sensor

    ser_temperature = serial.Serial(str(cls.get_temperature_sensor_serial_port()),
    baudrate=int(cls.get_temperature_sensor_baudrate()),
    parity=eval("serial." +(cls.get_temperature_sensor_parity())),
    stopbits=eval("serial."+(cls.get_temperature_sensor_stops_bits())),
    bytesize = eval("serial."+ cls.get_temperature_sensor_bytesize()))

    ### initialisation IR Licor

    ser_IR_analyzer = serial.Serial(str(cls.get_IR_analyzer_serial_port()),
    baudrate=int(cls.get_IR_analyzer_baudrate()),
    parity=eval("serial." +(cls.get_IR_analyzer_parity())),
    stopbits=eval("serial."+(cls.get_IR_analyzer_stops_bits())),
    bytesize = eval("serial."+ cls.get_IR_analyzer_bytesize()))


