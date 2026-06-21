from algorithms.fcfs import FCFS
from algorithms.lru import LRU
from controllers.simulator import Simulator
from views.console import ConsoleView
from time import sleep

def run_simulation(algorithm_class, capacity: int, references: list[int]):
    algo = algorithm_class(capacity=capacity)
    simulator = Simulator(algo)
    view = ConsoleView()
    events = simulator.run(references)

    for event in events:
        view.display(event)
        sleep(1)

def main():

    references = [1, 2, 3, 1, 4, 2, 5, 1]

    print("x*" * 20)
    print("Running FIFO Simulation:")
    print("x*" * 20 + "\n")
    run_simulation(FCFS, capacity=3, references=references)
    
    print("\n\n" + "x*" * 20)
    print("Running LRU Simulation:")
    print("x*" * 20 + "\n")
    run_simulation(LRU, capacity=3, references=references)


if __name__ == "__main__":
    main()