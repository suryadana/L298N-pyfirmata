MOTOR_A = 0
MOTOR_B = 1
HIGH = 1
LOW = 0


class Motor():
    def __init__(self, board, in1, in2, pwn):
        self.in1 = board.get_pin('d:{}:o'.format(in1))
        self.in2 = board.get_pin('d:{}:o'.format(in2))
        self.pwn = board.get_pin('d:{}:p'.format(pwn))


class L298N():
    def __init__(self, board, ena, in1, in2, in3, in4, enb):
        self.board = board

        self.motor = {
            0: Motor(board, in1, in2, ena),
            1: Motor(board, in3, in4, enb)
        }

    def drive_motor(self, motor_index, speed):
        self.motor[motor_index].pwn.write(speed)

    def drive_motors(self, speed):
        self.drive_motor(MOTOR_A, speed)
        self.drive_motor(MOTOR_B, speed)

    def setup_motor(self, motor_index, state1, state2):
        self.motor[motor_index].in1.write(state1)
        self.motor[motor_index].in2.write(state2)

    def setup_motors(self, state1, state2, state3, state4):
        self.setup_motor(MOTOR_A, state1, state2)
        self.setup_motor(MOTOR_B, state3, state4)

    def forward(self, speed, delay_time):
        self.setup_motors(HIGH, LOW, HIGH, LOW)
        self.drive_motors(speed)
        self.board.pass_time(delay_time)

    def backward(self, speed, delay_time):
        self.setup_motors(LOW, HIGH, LOW, HIGH)
        self.drive_motors(speed)
        self.board.pass_time(delay_time)

    def full_stop(self, delay_time):
        self.setup_motors(LOW, LOW, LOW, LOW)
        self.drive_motors(0)
        self.board(delay_time)

    def turn_left(self, speed, delay_time):
        self.setup_motors(HIGH, LOW, LOW, HIGH)
        self.drive_motors(speed)
        self.board.pass_time(delay_time)

    def turn_right(self, speed, delay_time):
        self.setup_motors(LOW, HIGH, HIGH, LOW)
        self.drive_motors(speed)
        self.board.pass_time(delay_time)
