# encoding: utf-8
# module gi._gi
# from /usr/lib/python3/dist-packages/gi/_gi.cpython-35m-arm-linux-gnueabihf.so
# by generator 1.145
# no doc

# imports
import _gobject as _gobject # <module '_gobject'>
import _glib as _glib # <module '_glib'>
import gi as __gi
import gobject as __gobject


from .type import type

class FunctionInfoFlags(type):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    IS_CONSTRUCTOR = 2
    IS_GETTER = 4
    IS_METHOD = 1
    IS_SETTER = 8
    THROWS = 32
    WRAPS_VFUNC = 16


