class ConsoleView:

    def display(self, event):

        print(f"Página acessada: {event.page}")

        if event.page_fault:
            print("Page fault: SIM")
        else:
            print("Page fault: NÃO")

        if event.removed_page is not None:
            print(f"Página removida: {event.removed_page}")

        print(f"Frames: {event.frames}")

        print("-" * 40)
    
    def __init__(self):
        self.rows = []
        self.events = []

    def record(self, step: int, event):

        self.rows.append({
            "step": step,
            "page": event.page,
            "fault": event.page_fault,
            "removed": event.removed_page,
            "frames": event.frames
        })
        
        self.events.append(event)

    def render(self):

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
    
    def summary(self):

        faults = sum(r["fault"] for r in self.rows)
        hits = len(self.rows) - faults

        print("\nRESUMO")
        print("-" * 30)
        print(f"Total acessos: {len(self.rows)}")
        print(f"Page faults: {faults}")
        print(f"Hits: {hits}")
        print(f"Taxa de acerto: {hits / len(self.events):.2f}")
