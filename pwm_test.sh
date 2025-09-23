#!/bin/bash
# Simple PWM test on GPIO18 (pwmchip0, channel 0)

PWM_PATH=/sys/class/pwm/pwmchip0/pwm0

# Set frequency = 1 kHz (period = 1,000,000 ns)
echo 1000000 | sudo tee $PWM_PATH/period > /dev/null

# Enable PWM
echo 1 | sudo tee $PWM_PATH/enable > /dev/null

# Loop through 25%, 50%, 75% duty cycle
for duty in 250000 500000 750000; do
    echo $duty | sudo tee $PWM_PATH/duty_cycle > /dev/null
    echo "Duty cycle set to $((duty/10000)) %"
    sleep 3
done

# Turn off PWM
echo 0 | sudo tee $PWM_PATH/enable > /dev/null
echo "PWM disabled"
