# Set up MaaxBoard

## Flash SD and Prepare a USB

### 1.Download the Yocto Lite image

### 2.Flash the Yocto Lite image to SD card
```
sudo dd if=MaaXBoard-Yocto-Lite-<date>.wic of=/dev/sdX bs=4M status=progress conv=fsync
```

### 3. Set Up Wifi connection 

Check if wifi interface exists
```
ip link
```
Turn interface UP
```
ip link set wlan0 up
```
Scan for wifi signals:
```
iwlist wlan0 scan | grep SSID
```
Create WPA config file with your wifi username and passwor
```
wpa_passphrase "YourNetworkSSID" "YourPassword" > /etc/wpa_supplicant.conf
```
Connect Wifi
```
wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf
```
Get an IP via DHCP and verify
```
udhcpc -i wlan0
ip addr show wlan0
ping -c 3 google.com
```
### 4. Retrieve IP and SSH connection


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

![IMG_8270](https://github.com/user-attachments/assets/a8d515c9-9014-4374-a9a2-fbe3f5e88f03)

![IMG_8269](https://github.com/user-attachments/assets/ed0122d4-97e2-407b-a3ed-2beac41ef984)


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
