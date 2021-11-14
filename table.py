import logging
from typing import List

from philosophers import Philosopher

from forks import Fork

logger = logging.getLogger(__name__)


class Table:
    PHILOSOPHERS_COUNT = 5

    def dinner_starting(self):
        message = f'There are {self.PHILOSOPHERS_COUNT} philosophers gathered for a dinner'
        logger.info(message)
        print(message)
        forks = self._create_forks(self.PHILOSOPHERS_COUNT)
        philosophers = self._create_philosophers(
            self.PHILOSOPHERS_COUNT, forks
        )
        for philosopher in philosophers:
            philosopher.start()

    @staticmethod
    def _create_forks(number_of_philosophers: int) -> List[Fork]:
        return [Fork(i) for i in range(number_of_philosophers)]

    @staticmethod
    def _create_philosophers(
        number_of_philosophers: int, forks: List[Fork]
    ):
        philosophers = []

        for philosopher_number in range(number_of_philosophers):
            neighbor_forks = (
                forks[philosopher_number % number_of_philosophers],
                forks[(philosopher_number + 1) % number_of_philosophers]
            )
            philosopher = Philosopher(philosopher_number, neighbor_forks)

            # Передача вилки другому философу, если она свободна
            for fork in neighbor_forks:
                if not fork._owner:
                    fork._owner = philosopher
            philosophers.append(philosopher)

        return philosophers
