from __future__ import annotations
import logging
from dataclasses import dataclass, field
from threading import Lock, Condition
from typing import TYPE_CHECKING
from constants import ForkState

if TYPE_CHECKING:
    from philosophers import Philosopher

logger = logging.getLogger(__name__)


@dataclass
class Fork:
    id: int
    _owner: Philosopher = field(init=False,
                                default=None)
    state: ForkState = field(init=False,
                             default=ForkState.DIRTY)
    lock: Lock = field(init=False,
                       default_factory=Lock)
    condition: Condition = field(init=False,
                                 default_factory=Condition)

    def request(self, philosopher: Philosopher):
        if self._owner == philosopher:
            with self.lock:
                message = f'{philosopher} already owns a {self}, he is washing it'
                logger.info(message)
                print(message)
                self.state = ForkState.CLEAN
                return

        if self.state is ForkState.DIRTY:
            with self.lock:
                message = f'{philosopher} receiving the dirty {self} from {self._owner}, and washing it'
                logger.info(message)
                print(message)
                self.state = ForkState.CLEAN
                self._owner = philosopher
            return

        if self.state is ForkState.CLEAN:
            with self.condition:
                message = f'{philosopher} is waiting for {self._owner} to get his {self}'
                logger.info(message)
                print(message)
                self.condition.wait()

                with self.lock:
                    message = f'{philosopher} receiving {self} and washing it'
                    logger.info(message)
                    print(message)
                    self._owner = philosopher
                    self.state = ForkState.CLEAN

    def done(self):
        with self.lock:
            self.state = ForkState.DIRTY

        with self.condition:
            self.condition.notify_all()

    def __repr__(self) -> str:
        return f'Fork {self.id}'
