from algorithms import *
from controllers.simulator import Simulator

class ConsoleView:
    
    def __init__(self):
        self.rows = []
        self.events = []

    def __record(self, step: int, event):

        self.rows.append({
            "step": step,
            "page": event.page,
            "fault": event.page_fault,
            "removed": event.removed_page,
            "frames": event.frames
        })
        
        self.events.append(event)

    def __render(self):

        print("\nACESSO | PAGE | FAULT | REMOVED | FRAMES")
        print("-" * 50)

        for r in self.rows:
            print(
                f"{r['step']:>5} | "
                f"{r['page']:>4} | "
                f"{int(r['fault']):>5} | "
                f"{str(r['removed']):>7} | "
                f"{r['frames']}"
            )
    
    def __summary(self):

        faults = sum(r["fault"] for r in self.rows)
        hits = len(self.rows) - faults

        print("\nRESUMO")
        print("-" * 30)
        print(f"Total acessos: {len(self.rows)}")
        print(f"Page faults: {faults}")
        print(f"Hits: {hits}")
        print(f"Taxa de acerto: {hits / len(self.events):.2f}")

    def __run_simulation(self, algorithm_class, capacity: int, references: list[int]):
        algo = algorithm_class(capacity=capacity)
        simulator = Simulator(algo)
        events = simulator.run(references)

        for i, event in enumerate(events):
            self.__record(i + 1, event)

        self.__render()
        self.__summary()
        self.rows.clear()
        self.events.clear()

    def run(self, references):
        print("x*" * 20)
        print("Executando Simulação FCFS:")
        print("x*" * 20 + "\n")
        self.__run_simulation(FCFS, capacity=3, references=references)
        
        print("\n\n" + "x*" * 20)
        print("Executando Simulação LRU:")
        print("x*" * 20 + "\n")
        self.__run_simulation(LRU, capacity=3, references=references)

        print("\n\n" + "x*" * 20)
        print("Executando Simulação LFU:")
        print("x*" * 20 + "\n")
        self.__run_simulation(LFU, capacity=3, references=references)