import toml
import serial

import init_electronic_device as IED

#params = {}
#with open("configuration.toml", 'r', encoding='utf-8') as fp:
#    params.update(toml.load(fp))
#    print(params)

def load_params(fname = "configuration.toml",param = ""):
    ### display toml file
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


        ### peripheral attributes (on/off)

        self.__periph_IR_analyzer = periph["IR_analyzer"]
        self.__periph_GPS = periph["GPS"]
        self.__periph_temperature_sensor = periph["temperature_sensor"]
        self.__periph_oxygen_sensor = periph["oxygen_sensor"]
        self.__periph_interface_box_chip = periph["interface_box_chip"]
        self.__periph_barometer_atmospheric = periph["barometer_atmospheric"]
        self.__barometer_equi = periph["barometer_equi"]
        self.__thermosalinometer = periph["thermosalinometer"]

        ### ir analyzer configurations attributes

        self.__ir_analyzer_active = ir_analyzer["active"]
        self.__ir_analyzer_serial_port = ir_analyzer["serial_port"]
        self.__ir_analyzer_baudrate = ir_analyzer["baudrate"]
        self.__ir_analyzer_data_bits = ir_analyzer["data_bits"]
        self.__ir_analyzer_stops_bits = ir_analyzer["stops_bits"]
        self.__ir_analyzer_parity = ir_analyzer["parity"]

        ### gps configurations attributes

        self.__gps_active = gps["active"]
        self.__gps_serial_port = gps["serial_port"]
        self.__gps_baudrate = gps["baudrate"]
        self.__gps_data_bits = gps["data_bits"]
        self.__gps_stops_bits = gps["stops_bits"]
        self.__gps_parity = gps["parity"]

        ### temperature sensor configurations attributes

        self.__temperature_sensor_active = temperature_sensor["active"]
        self.__temperature_sensor_serial_port = temperature_sensor["serial_port"]
        self.__temperature_sensor_baudrate = temperature_sensor["baudrate"]
        self.__temperature_sensor_data_bits = temperature_sensor["data_bits"]
        self.__temperature_sensor_stops_bits = temperature_sensor["stops_bits"]
        self.__temperature_sensor_parity = temperature_sensor["parity"]
        
        ### oxygen sensor configurations attributes

        self.__oxygen_sensor_active = oxygen_sensor["active"]
        self.__oxygen_sensor_serial_port = oxygen_sensor["serial_port"]
        self.__oxygen_sensor_baudrate = oxygen_sensor["baudrate"]
        self.__oxygen_sensor_data_bits = oxygen_sensor["data_bits"]
        self.__oxygen_sensor_stops_bits = oxygen_sensor["stops_bits"]
        self.__oxygen_sensor_parity = oxygen_sensor["parity"]

        ### interface box chip configurations attributes

        self.__interface_box_chip_active = interface_box_chip["active"]
        self.__interface_box_chip_serial_port = interface_box_chip["serial_port"]
        self.__interface_box_chip_baudrate = interface_box_chip["baudrate"]
        self.__interface_box_chip_data_bits = interface_box_chip["data_bits"]
        self.__interface_box_chip_stops_bits = interface_box_chip["stops_bits"]
        self.__interface_box_chip_parity = interface_box_chip["parity"]

        ### thermosalinometer configurations attributes

        self.__thermosalinometer_active = thermosalinometer["active"]
        self.__thermosalinometer_serial_port = thermosalinometer["serial_port"]
        self.__thermosalinometer_baudrate = thermosalinometer["baudrate"]
        self.__thermosalinometer_data_bits = thermosalinometer["data_bits"]
        self.__thermosalinometer_stops_bits = thermosalinometer["stops_bits"]
        self.__thermosalinometer_parity = thermosalinometer["parity"]

        ### getter peripheral

    def get_periph_IR_analyzer(self):
        return self.__periph_IR_analyzer

    def get_periph_GPS(self):
        return self.__periph_GPS

    def get_periph_temperature_sensor(self):
        return self.__periph_temperature_sensor

    def get_periph_oxygen_sensor(self):
        return self.__periph_oxygen_sensor

    def get_periph_interface_box_chip(self):
        return self.__periph_interface_box_chip

    def get_periph_barometer_atmospheric(self):
        return self.__periph_barometer_atmospheric

    def get_periph_barometer_equi(self):
        return self.__periph_barometer_equi

    def get_periph_thermosalinometer(self):
        return self.__periph_thermosalinometer

        ### getter ir analyzer

    def get_IR_analyzer_active(self):
        return self.__IR_analyzer_active

    def get_IR_analyzer_serial_port(self):
        return self.__IR_analyzer_serial_port

    def get_IR_analyzer_baudrate(self):
        return self.__IR_analyzer_baudrate

    def get_IR_analyzer_stops_bits(self):
        return self.__IR_analyzer_stops_bits

    def get_IR_analyzer_parity(self):
        return self.__IR_analyzer_parity

    def get_IR_analyser_bytesize(self):
        return self.__gps_IR_analyser

    ### getter GPS

    def get_gps_active(self):
        return self.__gps_active

    def get_gps_serial_port(self):
        return self.__gps_serial_port

    def get_gps_baudrate(self):
        return self.__gps_baudrate

    def get_gps_stops_bits(self):
        return self.__gps_stops_bits

    def get_gps_parity(self):
        return self.__gps_parity

    def get_gps_bytesize(self):
        return self.__gps_data_bits

    ### getter temperature sensor
    
    def get_temperature_sensor_active(self):
        return self.__temperature_sensor_active

    def get_temperature_sensor_serial_port(self):
        return self.__temperature_sensor_serial_port

    def get_temperature_sensor_baudrate(self):
        return self.__temperature_sensor_baudrate

    def get_temperature_sensor_stops_bits(self):
        return self.__temperature_sensor_stops_bits

    def get_temperature_sensor_parity(self):
        return self.__temperature_sensor_parity

    def get_temperature_sensor_bytesize(self):
        return self.__temperature_sensor_data_bits


    ### getter oxygen sensor

    def get_oxygen_sensor_active(self):
        return self.__oxygen_sensor_active

    def get_oxygen_sensor_serial_port(self):
        return self.__oxygen_sensor_serial_port

    def get_oxygen_sensor_baudrate(self):
        return self.__oxygen_sensor_baudrate

    def get_oxygen_sensor_stops_bits(self):
        return self.__oxygen_sensor_stops_bits

    def get_oxygen_sensor_parity(self):
        return self.__oxygen_sensor_parity
    
    def get_oxygen_sensor_bytesize(self):
        return self.__oxygen_sensor_data_bits

    ### getter interface box ship

    def get_interface_box_chip_active(self):
        return self.__interface_box_chip_active

    def get_interface_box_chip_serial_port(self):
        return self.__interface_box_chip_serial_port

    def get_interface_box_chip_baudrate(self):
        return self.__interface_box_chip_baudrate

    def get_interface_box_chip_stops_bits(self):
        return self.__interface_box_chip_stops_bits

    def get_interface_box_chip_parity(self):
        return self.__interface_box_chip_parity
    
    def get_interface_box_chip_bytesize(self):
        return self.__interface_box_chip_data_bits

    ### getter thermosalinometer

    def get_thermosalinometer_active(self):
        return self.__thermosalinometer_active

    def get_thermosalinometer_serial_port(self):
        return self.__thermosalinometer_serial_port

    def get_thermosalinometer_baudrate(self):
        return self.__thermosalinometer_baudrate

    def get_thermosalinometer_stops_bits(self):
        return self.__thermosalinometer_stops_bits

    def get_thermosalinometer_parity(self):
        return self.__thermosalinometer_parity

    def get_thermosalinometer_bytesize(self):
        return self.__thermosalinometer_data_bits
    
### class intances
time = config_time()

connec = config_elec_periph()

IED.init_time(time)

info = connec.get_periph_IR_analyzer()
print(info)
print(type(info))

IED.init_elec_device(connec)