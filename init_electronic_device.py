import serial

def init_time(cls):
    u = cls.get_t_mesure_atm_air()
    print(u)

def init_elec_device(cls):


    ser_GPS = serial.Serial(cls.gps["serial_port"],
    baudrate=cls.gps["baudrate"],
    parity=cls.gps["parity"],
    stopbits=cls.gps["stops_bits"],
    bytesize= serial.)
