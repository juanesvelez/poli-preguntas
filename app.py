from PySide2.QtWidgets import QApplication
from controllers.main_window import Jugador

if __name__ == "__main__":
    app = QApplication()
    window = Jugador()
    window.show()

    app.exec_()
    