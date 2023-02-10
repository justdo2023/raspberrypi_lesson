import spidev
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def read_adc(channel):
    spi = spidev.SpiDev()
    spi.open(0,0)
    spi.max_speed_hz = 1260870
    r = spi.xfer2([4 | 2 | (channel>>2), (channel & 3) << 6, 0])
    adc = ((r[1] & 15) << 8) + r[2]
    spi.close()
    return adc

def map_value(x, in_min, in_max, out_min, out_max):
    return (((x - in_min) * (out_max - out_min)) / (in_max - in_min)) + out_min

def update_graph(i):
    reading = read_adc(1)
    water_percentage = map_value(reading, 4095, 1360, 0, 100)
    current_time = time.strftime("%Y/%m/%d %H:%M:%S")
    xs.append(current_time)
    ys.append(water_percentage)
    ax.clear()
    ax.plot(xs, ys)
    ax.set_title(f"Time: {current_time} - Measured Value: {round(water_percentage,2)}%")

fig, ax = plt.subplots()
xs = []
ys = []
ani = animation.FuncAnimation(fig, update_graph, interval=1000)
plt.show()
