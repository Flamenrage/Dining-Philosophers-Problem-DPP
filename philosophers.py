from __future__ import annotations
import threading
import time
from random import uniform
import logging
from typing import Tuple
from forks import Fork
from constants import PhilosopherState


logger = logging.getLogger(__name__)


class Philosopher(threading.Thread):
    ENOUGH_DINNER_COUNT = 1
    LOWER_BOUND = 1.2
    UPPER_BOUND = 5.0


    def __init__(self, id: int, forks: Tuple[Fork, Fork]) -> None:
        threading.Thread.__init__(self)
        self.id = id
        self.state = PhilosopherState.THINKING
        self.forks = forks
        self.full = 0

    def run(self):
        while self.full < self.ENOUGH_DINNER_COUNT:
            self.eat()
            self.full += 1
            self.think()
        message = f'{self} is satisfied with food'
        logger.info(message)
        print(message)
        return

    def eat(self):
        message = f'{self} is starving, attempting to eat some food'
        logger.info(message)
        print(message)
        for fork in self.forks:
            fork.request(self)

        self.state = PhilosopherState.EATING
        message = f'{self} is having dinner'
        logger.info(message)
        print(message)
        time.sleep(uniform(self.LOWER_BOUND, self.UPPER_BOUND))

    def think(self):
        message = f'{self} is done eating, putting down his forks'
        logger.info(message)
        print(message)
        for fork in self.forks:
            fork.done()

        self.state = PhilosopherState.THINKING
        time.sleep(uniform(self.LOWER_BOUND, self.UPPER_BOUND))

    def __repr__(self) -> str:
        return f'Philosopher {self.id}'
