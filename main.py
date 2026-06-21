from algorithms.fifo import FIFO
from controllers.simulator import Simulator
from views.console import ConsoleView
from time import sleep


def main():

    references = [1, 2, 3, 1, 4, 2, 5, 1]

    fifo = FIFO(capacity=3)

    simulator = Simulator(fifo)

    view = ConsoleView()

    events = simulator.run(references)

    for event in events:
        view.display(event)
        sleep(1)


if __name__ == "__main__":
    main()