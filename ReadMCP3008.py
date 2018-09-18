import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 500000
spi.mode = 0b11


def Read1Chan(n):
    # read SPI data from the MCP3008, 8 channels in total
    if n > 7 or n < 0:
        return -1
    r = spi.xfer2([1, 8 + n << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

def Aread (channel):
    output = Read1Chan(channel)
    return output
