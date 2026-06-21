from algorithms.fcfs import FCFS
from algorithms.lfu import LFU
from algorithms.lru import LRU
from controllers.simulator import Simulator
from views.console import ConsoleView

def run_simulation(algorithm_class, capacity: int, references: list[int]):
    algo = algorithm_class(capacity=capacity)
    simulator = Simulator(algo)
    view = ConsoleView()
    events = simulator.run(references)

    for i, event in enumerate(events):
        view.record(i + 1, event)

    view.render()
    view.summary()

def main():

    references = [1, 2, 3, 1, 4, 2, 5, 1]

    print("x*" * 20)
    print("Executando Simulação FIFO:")
    print("x*" * 20 + "\n")
    run_simulation(FCFS, capacity=3, references=references)
    
    print("\n\n" + "x*" * 20)
    print("Executando Simulação LRU:")
    print("x*" * 20 + "\n")
    run_simulation(LRU, capacity=3, references=references)

    print("\n\n" + "x*" * 20)
    print("Executando Simulação LFU:")
    print("x*" * 20 + "\n")
    run_simulation(LFU, capacity=3, references=references)


if __name__ == "__main__":
    main()