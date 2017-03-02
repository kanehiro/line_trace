__author__ = 'kanehiro'
import ev3dev.ev3 as ev3
from time import sleep

class LineTrace:
    THRESHOLD = 50
    # tested values 150 - 100,400 - 200,200 - 100
    POWER_BIG = 200
    POWER_SMALL = POWER_BIG - 100
    def __init__(self):
        self.m_right = ev3.LargeMotor('outC'); assert self.m_right.connected
        self.m_left = ev3.LargeMotor('outB'); assert self.m_left.connected
        self.cs = ev3.ColorSensor('in2'); assert self.cs.connected
    def line_trace(self):
        while self.cs.value() >= self.THRESHOLD:
            self.m_right.run_forever(speed_sp = self.POWER_BIG)
            self.m_left.run_forever(speed_sp = self.POWER_SMALL)
        while self.cs.value() < self.THRESHOLD:
            self.m_right.run_forever(speed_sp = self.POWER_SMALL)
            self.m_left.run_forever(speed_sp = self.POWER_BIG)
    def stop(self):
        self.m_right.stop()
        self.m_left.stop()
