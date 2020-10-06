# encoding: utf-8
# module RPi._GPIO
# from /usr/lib/python2.7/dist-packages/RPi/_GPIO.arm-linux-gnueabihf.so
# by generator 1.145
""" GPIO functionality of a Raspberry Pi using Python """
# no imports

# Variables with simple values

BCM = 11

BOARD = 10
BOTH = 33

FALLING = 32

HARD_PWM = 43

HIGH = 1

I2C = 42

IN = 1

LOW = 0

OUT = 0

PUD_DOWN = 21
PUD_OFF = 20
PUD_UP = 22

RISING = 31

RPI_REVISION = 3

SERIAL = 40

SPI = 41

UNKNOWN = -1

# functions

def add_event_callback(*args, **kwargs): # real signature unknown
    """
    Add a callback for an event already defined using add_event_detect()
    channel      - either board pin number or BCM number depending on which mode is set.
    callback     - a callback function
    """
    pass

def add_event_detect(*args, **kwargs): # real signature unknown
    """
    Enable edge detection events for a particular GPIO channel.
    channel      - either board pin number or BCM number depending on which mode is set.
    edge         - RISING, FALLING or BOTH
    [callback]   - A callback function for the event (optional)
    [bouncetime] - Switch bounce timeout in ms for callback
    """
    pass

def cleanup(*args, **kwargs): # real signature unknown
    """
    Clean up by resetting all GPIO channels that have been used by this program to INPUT with no pullup/pulldown and no event detection
    [channel] - individual channel or list/tuple of channels to clean up.  Default - clean every channel that has been used.
    """
    pass

def event_detected(*args, **kwargs): # real signature unknown
    """
    Returns True if an edge has occured on a given GPIO.  You need to enable edge detection using add_event_detect() first.
    channel - either board pin number or BCM number depending on which mode is set.
    """
    pass

def getmode(*args, **kwargs): # real signature unknown
    """
    Get numbering mode used for channel numbers.
    Returns BOARD, BCM or None
    """
    pass

def gpio_function(*args, **kwargs): # real signature unknown
    """
    Return the current GPIO function (IN, OUT, PWM, SERIAL, I2C, SPI)
    channel - either board pin number or BCM number depending on which mode is set.
    """
    pass

def input(*args, **kwargs): # real signature unknown
    """
    Input from a GPIO channel.  Returns HIGH=1=True or LOW=0=False
    channel - either board pin number or BCM number depending on which mode is set.
    """
    pass

def output(*args, **kwargs): # real signature unknown
    """
    Output to a GPIO channel or list of channels
    channel - either board pin number or BCM number depending on which mode is set.
    value   - 0/1 or False/True or LOW/HIGH
    """
    pass

def remove_event_detect(*args, **kwargs): # real signature unknown
    """
    Remove edge detection for a particular GPIO channel
    channel - either board pin number or BCM number depending on which mode is set.
    """
    pass

def setmode(*args, **kwargs): # real signature unknown
    """
    Set up numbering mode to use for channels.
    BOARD - Use Raspberry Pi board numbers
    BCM   - Use Broadcom GPIO 00..nn numbers
    """
    pass

def setup(*args, **kwargs): # real signature unknown
    """
    Set up a GPIO channel or list of channels with a direction and (optional) pull/up down control
    channel        - either board pin number or BCM number depending on which mode is set.
    direction      - IN or OUT
    [pull_up_down] - PUD_OFF (default), PUD_UP or PUD_DOWN
    [initial]      - Initial value for an output channel
    """
    pass

def setwarnings(*args, **kwargs): # real signature unknown
    """ Enable or disable warning messages """
    pass

def wait_for_edge(*args, **kwargs): # real signature unknown
    """
    Wait for an edge.  Returns the channel number or None on timeout.
    channel      - either board pin number or BCM number depending on which mode is set.
    edge         - RISING, FALLING or BOTH
    [bouncetime] - time allowed between calls to allow for switchbounce
    [timeout]    - timeout in ms
    """
    pass

# classes

class PWM(object):
    """ Pulse Width Modulation class """
    def ChangeDutyCycle(self, *args, **kwargs): # real signature unknown
        """
        Change the duty cycle
        dutycycle - between 0.0 and 100.0
        """
        pass

    def ChangeFrequency(self, *args, **kwargs): # real signature unknown
        """
        Change the frequency
        frequency - frequency in Hz (freq > 1.0)
        """
        pass

    def start(self, *args, **kwargs): # real signature unknown
        """
        Start software PWM
        dutycycle - the duty cycle (0.0 to 100.0)
        """
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        """ Stop software PWM """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


# variables with complex values

RPI_INFO = {
    'MANUFACTURER': 'Sony',
    'P1_REVISION': 3,
    'PROCESSOR': 'BCM2835',
    'RAM': '512M',
    'REVISION': '9000c1',
    'TYPE': 'Unknown',
}

