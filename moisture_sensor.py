import spidev
import time

#Setup SPI
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1260870

#Read ADC value
def analog_read_3208(channel):
    r = spi.xfer2([4 | 2 |(channel>>2), (channel &3) << 6,0])    
    adc_out = ((r[1]&15) << 8) + r[2]
    return adc_out


#Covert ADC value to percent value
def map(x, in_min, in_max, out_min, out_max):
    out_val = (((x - in_min) * (out_max - out_min)) / (in_max - in_min)) + out_min
    return out_val

#Read moisture sensor value
try:
    while True:
        print(time.strftime("%Y/%m/%d %H:%M:%S"))
        reading = analog_read_3208(1)
        print(type(reading))
        voltage = reading * 3.3 / 4096
        print("MCP3208: Reading=%d\tVoltage=%f" % (reading, voltage)) 

        Water_Percentage = map(reading, 4095, 2137, 0, 100)
        print("Water%%: %0.1f\n" % (Water_Percentage))
        time.sleep(2)


except RuntimeError:
    pass