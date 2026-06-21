class Simulator:

    def __init__(self, algorithm):
        self.algorithm = algorithm

    def step(self, page: int):

        return self.algorithm.access(page)

    def run(self, references: list[int]):

        events = []

        for page in references:
            events.append(self.step(page))

        return events