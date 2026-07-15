import sys

def main():

    if len(sys.argv) > 1 and sys.argv[1] == "gui":
        from views.gui import GUIView
        view = GUIView()
        view.run([1, 2, 3, 1, 4, 2, 5, 1])
    else:
        from views.console import ConsoleView
        view = ConsoleView()
        view.run([1, 2, 3, 1, 4, 2, 5, 1])

if __name__ == "__main__":
    main()