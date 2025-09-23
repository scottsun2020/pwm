import time

PWM_PATH = "/sys/class/pwm/pwmchip0/pwm0"

def write_pwm(filename, value):
    with open(f"{PWM_PATH}/{filename}", "w") as f:
        f.write(str(value))

def main():
    # Set frequency = 1 kHz (period = 1,000,000 ns)
    write_pwm("period", 1000000)

    # Enable PWM
    write_pwm("enable", 1)

    duty = 500000  # 50% duty cycle (half of 1,000,000 ns)
    loops = 60 // 3  # Run for 1 minute in 3-second steps

    for i in range(loops):
        write_pwm("duty_cycle", duty)
        print(f"[{i+1}/{loops}] Duty cycle set to 50%")
        time.sleep(3)

    # Disable PWM after 1 minute
    write_pwm("enable", 0)
    print("PWM disabled after 1 minute")

if __name__ == "__main__":
    main()

