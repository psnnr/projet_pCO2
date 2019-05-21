import serial

def init_time(cls):
    w = cls.get_t_mesure_atm_air()
    u = int(w)

def init_elec_device(cls):

    a = cls.get_gps_bytesize()
    print(a)
    print(type(str(a)))

    ser_GPS = serial.Serial(str(cls.get_gps_serial_port),
    baudrate=str(cls.get_gps_baudrate),
    parity=str(cls.get_gps_parity),
    stopbits=str(cls.get_gps_stops_bits),
    bytesize= serial.EIGHTBITS)
    #get_gps_bytesize)