from pyfirmata import Arduino
from l289n import L298N


def main():
    board = Arduino('/dev/ttyACM0')
    # Initial pin
    ena = 11
    enb = 10
    in1 = 7
    in2 = 6
    in3 = 5
    in4 = 4
    motor = L298N(board, ena, in1, in2, in3, in4, enb)
    # Forward with speed 70%
    motor.forward(0.7)


if __name__ == '__main__':
    main()
