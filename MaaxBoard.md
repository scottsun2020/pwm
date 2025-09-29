# Set up MaaxBoard

## test UART 

### Step 1. Identify which UART to use

On MaaXBoard 40-pin header:

Pin 8 = UART1_TXD

Pin 10 = UART1_RXD

Pin 6 = GND

So you can connect a USB-UART dongle from your laptop → MaaXBoard:

Dongle TX → MaaXBoard Pin 10 (RX)

Dongle RX → MaaXBoard Pin 8 (TX)

Dongle GND → MaaXBoard Pin 6 (GND)

### Step 2.Plug in the TTL232RG → it will appear as a serial device, e.g.

```
ls /dev/ttyUSB*
```

```
screen /dev/ttyUSB0 115200
```

```
minicom -D /dev/ttyUSB0 -b 115200
```

### Step 3. Get IP address 

```
ip addr
```
