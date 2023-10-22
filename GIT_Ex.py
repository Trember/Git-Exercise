class AnalogConvertor:
    def __init__(self, analog_volt):
        self.analog_volt = analog_volt

    def ToDigital(self):
        power_percentage = self.analog_volt/5
        if power_percentage == 1:
            return bin(2**10-1)[2:]
        return bin(int((2**10) * power_percentage))[2:].zfill(10)
    
    def set_digital_value(self, value):
        self.analog_volt = value
    
    def padded_bin(self,i, width):
        s = bin(i)
        return s[:2] + s[2:].zfill(width)

if __name__ == '__main__':
    convertor = AnalogConvertor(5)
    print(convertor.ToDigital())
    convertor.set_digital_value(1)
    print(convertor.ToDigital())

