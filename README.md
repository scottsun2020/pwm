# PWM

### PWM is useful for controlling the average power or amplitude delivered by an electrical signal. 

source:
https://www.youtube.com/watch?v=nXFoVSN3u-E

 The longer the switch is on, the higher the total power supplied to the load.


 The rectangular voltage pulses nonetheless result in a more and more smooth current waveform, as the switching frequency increases. The current waveform is the integral of the voltage waveform.

The main advantage of PWM is that power loss in the switching devices is very low. 

## PWM under Linux 

source: https://www.kernel.org/doc/html/v4.16/driver-api/miscellaneous.html#pulse-width-modulation-pwm


## 🔹 Option 1: Using /sys/class/pwm (PWM sysfs interface)

### Step 1 : Enable PWM overlay I tried GPIO PIN 18, but somehow, it does not work on the hardware PWM; I reconfigured GPIO PIN 12

```
[all]
dtoverlay=pwm-2chan,pin=12,func=4
```

reboot after adding the overlay in the config.txt

will see this show up ls /sys/class/pwm

```
pwmchip0
```

echo 0 | sudo tee export = Tell the kernel to make PWM channel 0 (GPIO12) available for use.

rivieh@raspberrypi:/sys/class/pwm/pwmchip0/pwm0 $ ls capture duty_cycle enable period polarity power uevent rivieh@raspberrypi:/sys/class/pwm/pwmchip0/pwm0 $ echo 1000000 | sudo tee period 1000000 
rivieh@raspberrypi:/sys/class/pwm/pwmchip0/pwm0 $ echo 500000 | sudo tee duty_cycle 500000 
rivieh@raspberrypi:/sys/class/pwm/pwmchip0/pwm0 $ echo 1 | sudo tee enable 1 
rivieh@raspberrypi:/sys/class/pwm/pwmchip0/pwm0 $ echo 0 | sudo tee enable 0 
rivieh@raspberrypi:/sys/class/pwm/pwmchip0/pwm0 $


### 🔹 Option 2: Using pigpio (easier in Python)


## After Reboot, need to export channel

```
rivieh@raspberrypi:~ $ ls /sys/class/pwm/pwmchip0/
device  export  npwm  power  subsystem  uevent  unexport
```

need to “export” channel 0 again:
```
cd /sys/class/pwm/pwmchip0
echo 0 | sudo tee export
/sys/class/pwm/pwmchip0 $ echo 0 | sudo tee export
0
rivieh@raspberrypi:/sys/class/pwm/pwmchip0 $ ls
device  export  npwm  power  pwm0  subsystem  uevent  unexport
rivieh@raspberrypi:/sys/class/pwm/pwmchip0 $ cd pwm0/
rivieh@raspberrypi:/sys/class/pwm/pwmchip0/pwm0 $ ls
capture  duty_cycle  enable  period  polarity  power  uevent

```

<img width="2380" height="1382" alt="Screenshot from 2025-09-23 15-10-18" src="https://github.com/user-attachments/assets/2670807a-197e-42e3-b358-9c16feeae67d" />



