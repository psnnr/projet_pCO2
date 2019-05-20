import toml
import serial

import init_electronic_device as IED

#params = {}
#with open("configuration.toml", 'r', encoding='utf-8') as fp:
#    params.update(toml.load(fp))
#    print(params)

def load_params(fname = "configuration.toml",param = ""):
    params = {}
    with open(fname, 'r', encoding='utf-8') as fp:
        params.update(toml.load(fp))


class config_time():
    ### contain all configured time for all cycles

    #def __init__(self):
    #    self.t_rinsing_azote = 180
    #    self.t_rinsing_low_standard = 180
    #    self.t_rinsing_med_standard = 180
    #    self.t_rinsing_high_standard = 180
    #    self.t_rinsing_atm_air = 240
    #    self.t_rinsing_sea_water = 600
    
    def __init__(self, file = "configuration.toml"):
        parsed_toml = toml.load(file,_dict = dict)
        time = parsed_toml['time']
        self.__t_rinsing_azote = time['rinsing_azote_cycle']
        self.__t_rinsing_low_standard = time['rinsing_low_standard']
        self.__t_rinsing_med_standard = time['rinsing_medium_standard']
        self.__t_rinsing_high_standard = time['rinsing_high_standard']
        self.__t_rinsing_atm_air = time['rinsing_atmospheric_air']
        self.__t_rinsing_sea_water = time['rinsing_sea_water']

        self.__t_mesure_azote = time['mesure_azote_cycle']
        self.__t_mesure_low_standard = time['mesure_low_standard']
        self.__t_mesure_med_standard = time['mesure_medium_standard']
        self.__t_mesure_high_standard = time['mesure_high_standard']
        self.__t_mesure_atm_air = time['mesure_atmospheric_air']
        self.__t_mesure_sea_water = time['mesure_sea_water']

    ### getters

    def get_t_rinsing_azote(self):
        return self.__t_rinsing_azote

    def get_t_rinsing_low_standard(self):
        return self.__t_rinsing_low_standard

    def get_t_rinsing_med_standard(self):
        return self.__t_rinsing_med_standard

    def get_t_rinsing_high_standard(self):
        return self.__t_rinsing_high_standard

    def get_t_rinsing_atm_air(self):
        return self.__t_rinsing_atm_air

    def get_t_rinsing_sea_water(self):
        return self.__t_rinsing_sea_water

    def get_t_mesure_azote(self):
        return self.__t_mesure_azote

    def get_t_mesure_low_standard(self):
        return self.__t_mesure_low_standard

    def get_t_mesure_med_standard(self):
        return self.__t_mesure_med_standard

    def get_t_mesure_high_standard(self):
        return self.__t_mesure_high_standard

    def get_t_mesure_atm_air(self):
        return self.__t_mesure_atm_air

    def get_t_mesure_sea_water(self):
        return self.__t_mesure_sea_water



class config_elec_periph():

    ### contain all inforation about electronical device connexion

    def __init__(self, file = "configuration.toml"):
        parsed_toml = toml.load(file,_dict = dict)
        periph = parsed_toml['peripheral']
        ir_analyzer = parsed_toml['IR_analyzer']
        gps = parsed_toml['GPS']
        temperature_sensor = parsed_toml['temperature_sensor']
        oxygen_sensor = parsed_toml['oxygen_sensor']
        interface_box_chip = parsed_toml['interface_box_chip']
        thermosalinometer = parsed_toml['thermosalinometer']


        self.periph = periph
        self.ir_analyzer = ir_analyzer
        self.gps = gps
        self.temperature_sensor = temperature_sensor
        self.oxygen_sensor = oxygen_sensor
        self.interface_box_chip = interface_box_chip
        self.thermosalinometer = thermosalinometer

    def get_periph(self):
        return self.periph

    def get_ir_analyzer(self):
        return self.ir_analyzer

    def get_gps_serial_port():
        return self.gps["serial_port"]

    def get_gps_baudrate():
        return self.gps["baudrate"]

    def get_gps_parity():
        return self.gps["parity"]

    def get_gps_stops_bits():
        return self.gps["stops_bits"]
    
    def get_gps_bytesize():
        return self.gps["bytesize"]





def init_elec_device(cls):

    #ser_GPS = serial.Serial(str(cls.get_gps_serial_port),
    #baudrate=str(cls.get_gps_baudrate),
    #parity=str(cls.get_gps_parity),
    #stopbits=str(cls.get_gps_stops_bits),
    #bytesize= int(str(cls.get_gps_bytesize)))

    a = cls.get_gps_baudrate
    print(a)

### class intances
time = config_time()

connec = config_elec_periph()

IED.init_time(time)

#info = connec.get_periph()
#print(info)

init_elec_device(connec)

#init_elec_device(connec)