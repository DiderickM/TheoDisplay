# encoding: utf-8
# module rgbmatrix.core
# from /usr/local/lib/python2.7/dist-packages/rgbmatrix/core.so
# by generator 1.145
# no doc

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import PIL.Image as Image # /usr/lib/python2.7/dist-packages/PIL/Image.pyc

# functions

def __pyx_unpickle_Canvas(*args, **kwargs): # real signature unknown
    pass

# classes

class Canvas(object):
    # no doc
    def SetImage(self, *args, **kwargs): # real signature unknown
        pass

    def SetPixelsPillow(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is ''


class FrameCanvas(Canvas):
    # no doc
    def Clear(self, *args, **kwargs): # real signature unknown
        pass

    def Fill(self, *args, **kwargs): # real signature unknown
        pass

    def SetPixel(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    brightness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pwmBits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class RGBMatrix(Canvas):
    # no doc
    def Clear(self, *args, **kwargs): # real signature unknown
        pass

    def CreateFrameCanvas(self, *args, **kwargs): # real signature unknown
        pass

    def Fill(self, *args, **kwargs): # real signature unknown
        pass

    def SetPixel(self, *args, **kwargs): # real signature unknown
        pass

    def SwapOnVSync(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    brightness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    luminanceCorrect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pwmBits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class RGBMatrixOptions(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    brightness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    chain_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    daemon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    disable_hardware_pulsing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drop_privileges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gpio_slowdown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hardware_mapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    inverse_colors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    led_rgb_sequence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    multiplexing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parallel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pixel_mapper_config = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pwm_bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pwm_dither_bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pwm_lsb_nanoseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row_address_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    show_refresh_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

__test__ = {}

