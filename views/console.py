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