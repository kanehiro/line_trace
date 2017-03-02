import ev3dev.ev3 as ev3
from time import sleep

from classed_line_trace import LineTrace

ts = ev3.TouchSensor('in3')

lt = LineTrace()
while not (ts.value()):
    lt.line_trace()
lt.stop()
