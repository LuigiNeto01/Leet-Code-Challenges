from __future__ import annotations
import threading

class DiningPhilosophers:
    def __init__(self):
        # One lock per fork to ensure mutual exclusion
        self.forks = [threading.Lock() for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        # Each philosopher's left fork index = philosopher id
        # right fork index = (id + 1) % 5
        left_fork = philosopher
        right_fork = (philosopher + 1) % 5

        # Deadlock prevention: philosopher #4 picks right fork first.
        # This breaks the circular wait condition.
        if philosopher == 4:
            # Acquire right fork, then left fork; but call pickLeftFork first
            with self.forks[right_fork]:
                with self.forks[left_fork]:
                    pickLeftFork()
                    pickRightFork()
                    eat()
                    putLeftFork()
                    putRightFork()
        else:
            # Normal order: left fork first, then right fork
            with self.forks[left_fork]:
                with self.forks[right_fork]:
                    pickLeftFork()
                    pickRightFork()
                    eat()
                    putLeftFork()
                    putRightFork()