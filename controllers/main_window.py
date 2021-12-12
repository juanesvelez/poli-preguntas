from PySide2.QtWidgets import QWidget
from views.main_window import LoginRegisterForm

# Definimos clase PoliPreguntas
class Jugador(QWidget, LoginRegisterForm):
    # Contructor de la clase
    def __init__(self):
        # Permite llamar metodos/funciones de las clases padre
        super().__init__()
        # Llamar función que construye los componente graficos del LoginRegisterForm
        self.setupUi(self)

        # Definición e inicilización de variables de instancia
        self.dificultad = ""
        self.jugador_name = ""
        self.jugador_age = 0

        # Vinculación de metodo con el evento del boton btn_jugar
        self.btn_jugar.clicked.connect(self.cargar_juego)

    def check_age(self):
        # Captura de valores nombre y edad jugador del LoginRegisterForm
        self.jugador_name = self.txt_jugador.text()
        self.jugador_age = int(self.txt_edad.text())

        # Calculo nivel de dificultad de la partida
        if self.jugador_age <= 16:
            self.dificultad = "Básico"

        if self.jugador_age > 16 and self.jugador_age <= 28:
            self.dificultad = "Intermedio"
            
        if self.jugador_age > 28:
            self.dificultad = "Difícil"

    def cargar_juego(self):
        # Validar dificultad vrs. edad
        self.check_age()
        # Importar la clase del form game
        from controllers.game_window import PoliPreguntas
        # Variable que almacena el objeto del form game, recibe parametro la instancia de la clase padre
        window = PoliPreguntas(self, self.jugador_name, self.jugador_age, self.dificultad)
        # Evento mostrar nuevo form game
        window.show()
        # Cerrar ventana Register
        self.destroy()
