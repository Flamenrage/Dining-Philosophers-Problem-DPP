import logging
from table import Table

logging.basicConfig(filename="sample.log",
    level = logging.INFO, format = '%(asctime)s %(message)s'
)

def start():
    print("Logging to the file sample.log")
    dining_table = Table()
    dining_table.dinner_starting()


def init():
    if __name__ == "__main__":
        start()


init()
