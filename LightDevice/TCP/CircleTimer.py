# -*- coding: utf-8 -*-

from threading import Thread
from threading import Event

def Timer(*args, **kwargs):
    """Factory

    Timer call of seconds:

        t = Timer(10, f, args=[], kwargs={})
        t.start()
        t.cancel()     # stop

    """
    return _Timer(*args, **kwargs)

class _Timer(Thread):

    def __init__(self, interval, function, args=[], kwargs={}):
        Thread.__init__(self)
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.finished = Event()

    def cancel(self):
        """Stop"""
        self.finished.set()

    def run(self):
        self.finished.wait(self.interval)
        if not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
        self.finished.set()


# loop timer
class LoopTimer(_Timer):
    """Call a function after a specified number of seconds:


            t = LoopTimer(30.0, f, args=[], kwargs={})
            t.start()
            t.cancel()     # stop the timer's action if it's still waiting


    """
    def __init__(self, interval, function, args=[], kwargs={}):
        _Timer.__init__(self,interval, function, args, kwargs)


    def run(self):
        '''''self.finished.wait(self.interval)
        if not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
        self.finished.set()'''
        while True:
            self.finished.wait(self.interval)
            if self.finished.is_set():
                self.finished.set()
                break
            self.function(*self.args, **self.kwargs)


