class AnalogConvertor:
    def __init__(self, analog_volt,max_volt,bits):
        self.analog_volt = analog_volt
        self.max_volt = max_volt
        self.bits = bits

    def ToDigital(self):
        power_percentage = self.analog_volt/self.max_volt
        if power_percentage == 1:
            return bin(2**self.bits-1)[2:]
        return bin(int((2**self.bits) * power_percentage))[2:].zfill(self.bits)
    
    def set_digital_value(self, value):
        self.analog_volt = value

if __name__ == '__main__':
    convertor = AnalogConvertor(5,10,12)
    print(convertor.ToDigital())
    convertor.set_digital_value(2.5)
    print(convertor.ToDigital())

