from __future__ import annotations
import threading

class FooBar:
    """
    Synchronizes two threads so that they alternately print "foo" and "bar".
    Uses two events to signal the order: foo then bar, repeated n times.
    """
    def __init__(self, n):
        self.n = n
        # Event for foo's turn; initially set so foo runs first.
        self.foo_event = threading.Event()
        self.foo_event.set()
        # Event for bar's turn; initially cleared so bar waits.
        self.bar_event = threading.Event()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # Wait for permission to print foo.
            self.foo_event.wait()
            # Clear the event so foo won't run again until bar signals.
            self.foo_event.clear()
            printFoo()
            # Allow bar to proceed.
            self.bar_event.set()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # Wait for permission to print bar.
            self.bar_event.wait()
            # Clear so bar won't run again until foo signals.
            self.bar_event.clear()
            printBar()
            # Signal foo to print the next "foo".
            self.foo_event.set()