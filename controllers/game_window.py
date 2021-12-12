# Impotar librerias de PySide2
from PySide2.QtCore import Qt, QCoreApplication
from PySide2.QtWidgets import QWidget, QMessageBox
from views.game_window import GameForm

# Importar json para obtener la informacion
# de los archivos de preguntas
import json

# Definimos clase PoliPreguntas
class PoliPreguntas(QWidget, GameForm):

    # Contructor de la clase, recibe parametro de la instancia padre
    def __init__(self, parent=None, jugador=None, age=None, dif=None):
        # Permite llamar metodos/funciones de las clases padre
        super().__init__(parent)
        # Llamar función que construye los componente graficos del GameForm
        self.setupUi(self)
        # Separamos las ventanas de los forms
        self.setWindowFlag(Qt.Window)

        # Definición de varibles de instancia
        self.cat_actual = ""
        self.dificultad = dif
        self.jugador_name = jugador
        self.jugador_age = age
        self.q_no = 0
        self.correct = 0
        self.data_size = 0

        # Envio de valores nombre, edad y nivel de dificultad del jugador hacia el GameForm
        self.lbl_jugador.setText(QCoreApplication.translate("GameForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">" \
            + self.jugador_name + "</span></p></body></html>", None))
        self.lbl_edad.setText(QCoreApplication.translate("GameForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">" \
            + str(self.jugador_age) + " años / " + self.dificultad + "</span></p></body></html>", None))

        # Vinculación de metodo con el evento de los botones
        self.btn_cat_historia.clicked.connect(self.cargar_historia)
        self.btn_cat_geografia.clicked.connect(self.cargar_geografia)
        self.btn_cat_matematicas.clicked.connect(self.cargar_matematicas)
        self.btn_cat_cultura.clicked.connect(self.cargar_cultura)
        self.btn_cat_ingles.clicked.connect(self.cargar_ingles)
        #self.btn_about.clicked.connect(self.cargar_about)
        self.btn_next.clicked.connect(self.next_question)
        self.btn_about.clicked.connect(self.about)

    def cargar_historia(self):
        # Cargue Categoria
        self.cat_actual = "Historia"
        # Inicializar componentes del GameForm
        self.inicializar("preguntas_historia")
        # Visualizar preguntas en el GameForm
        self.display_question()
        # Visualizar opciones en el GameForm
        self.display_options()

    def cargar_geografia(self):
        # Cargue Categoria
        self.cat_actual = "Geografía"
        # Inicializar componentes del GameForm
        self.inicializar("preguntas_geografia")
        # Visualizar preguntas en el GameForm
        self.display_question()
        # Visualizar opciones en el GameForm
        self.display_options() 

    def cargar_matematicas(self):
        # Cargue Categoria
        self.cat_actual = "Matemáticas"
        # Inicializar componentes del GameForm
        self.inicializar("preguntas_matematicas")
        # Visualizar preguntas en el GameForm
        self.display_question()
        # Visualizar opciones en el GameForm
        self.display_options() 

    def cargar_cultura(self):
        # Cargue Categoria
        self.cat_actual = "Cultura General"
        # Inicializar componentes del GameForm
        self.inicializar("preguntas_cultura")
        # Visualizar preguntas en el GameForm
        self.display_question()
        # Visualizar opciones en el GameForm
        self.display_options()  

    def cargar_ingles(self):
        # Cargue Categoria
        self.cat_actual = "Inglés"
        # Inicializar componentes del GameForm
        self.inicializar("preguntas_ingles")
        # Visualizar preguntas en el GameForm
        self.display_question()
        # Visualizar opciones en el GameForm
        self.display_options() 

    # ######################################### Metodo inicializar ########################################
    # Este método iniciliza los componentes graficos del tablero dew acuerdo con la categoria seleccionada
    def inicializar(self, banco):
        # Componentes Enable
        self.btn_next.setVisible(True)
        self.opt_respuesta_1.setVisible(True)
        self.opt_respuesta_2.setVisible(True)
        self.opt_respuesta_3.setVisible(True)
        self.opt_respuesta_4.setVisible(True)

        # Fondo imagen tablero preguntas
        self.frame_jugador.setStyleSheet(u"image: url(./assets/img/fondo_tablero.png);")

         # Envio de valores categoria hacia el GameForm
        self.lbl_categoria.setText(QCoreApplication.translate("GameForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">" \
               + self.cat_actual + "</span></p></body></html>", None))
        
        """ Obtenemos la data del archivo preguntas.json;
        para evitar que los acentos no se vean afectados
        debemos configurar la codificacion UTF-8
        """
        with open('./data_config/' + banco + '.json', encoding="utf-8") as f:
                data = json.load(f)

        # Iniciamos las preguntas, opciones y respuestas
        self.question = (data['question_' + self.dificultad ])
        self.options = (data['options_' + self.dificultad ])
        self.answer = (data['answer_' + self.dificultad ])

        # Numero de preguntas total en preguntas.json
        self.data_size = len(self.question)

    # ######################################### Metodo display_question ########################################
    # Este método muestra la pregunta actual en la pantalla
    def display_question(self):
        # Envio de valores categoria hacia el GameForm
        self.lbl_pregunta.setText(QCoreApplication.translate("GameForm", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:16pt;\">" \
            + self.question[self.q_no] + "</span></p></body></html>", None))

    # ######################################### Metodo display_options ###########################################
    # Este metodo anula la seleccion de la opcion en pantalla
    # Tambien es usado para mostrar las opciones disponibles
    def display_options(self):
        # Deseleccion de opciones
        self.opt_respuesta_0.setChecked(True)
        self.opt_respuesta_1.setChecked(False)
        self.opt_respuesta_2.setChecked(False)
        self.opt_respuesta_3.setChecked(False)
        self.opt_respuesta_4.setChecked(False)
        
        # Deseleccion de opciones
        self.opt_respuesta_1.setText(QCoreApplication.translate("GameForm", u"" + str(self.options[self.q_no][0]), None))
        self.opt_respuesta_2.setText(QCoreApplication.translate("GameForm", u"" + str(self.options[self.q_no][1]), None))
        self.opt_respuesta_3.setText(QCoreApplication.translate("GameForm", u"" + str(self.options[self.q_no][2]), None))
        self.opt_respuesta_4.setText(QCoreApplication.translate("GameForm", u"" + str(self.options[self.q_no][3]), None))

    # ######################################### Metodo next_btn ####################################################
    # Este método se utiliza para verificar la respuesta de la
    # pregunta actual llamando al metodo check_ans
    # Si la pregunta es correcta, aumenta el contador en 1 y pasará a la siguiente pregunta.
    # Si es la última pregunta, llamara al metodo display_result el cual mostrara
    # el resultado.
    def next_question(self):
        # Validación selección respuesta
        if self.opt_respuesta_0.isChecked():
            QMessageBox.critical(self, "Poli-Preguntas Game", "Debes seleccionar una respuesta valida!")
        else:
            # Comprueba si la respuesta es correcta.
            if self.check_ans():
                # Si la respuesta es correcta, incrementa la correcta en 1
                self.correct += 1

            # Pasa a la siguiente pregunta incrementando el contador q_no
            self.q_no += 1

            # Comprueba si el tamaño de q_no es igual al tamaño de las preguntas en preguntas.json
            if self.q_no == self.data_size:
                # Si ha finalizado las preguntas en el preguntas.json muestra el resultado
                self.display_result()

            else:
                # Muestra la siguiente pregunta
                self.display_question()
                self.display_options()
            
    # ####################################### Metodo check_ans #####################################################
    # Este metodo verifica la respuesta
    # Despues de hacer clic
    def check_ans(self):
        # Variable para almacenar el indice del RadioButton seleccionado.
        val_res = 0

        # Captura númeral seleccionado
        if self.opt_respuesta_1.isChecked():
            val_res = 1
        if self.opt_respuesta_2.isChecked():
            val_res = 2
        if self.opt_respuesta_3.isChecked():
            val_res = 3
        if self.opt_respuesta_4.isChecked():
            val_res = 4
        
        # Comprueba si la opcion selecciona es correcta
        if val_res == self.answer[self.q_no]:
            # Si la opcion es correcta retorna True
            return True

    # ################################### Metodo display_result ########################################################
    # Este método se usa para mostrar el resultado.
    # Tambien cuenta el número de respuestas correctas e incorrectas
    # y al final muestra un cuadro con el resultado
    def display_result(self):
        # Calculo de preguntas incorrectas
        wrong_count = self.data_size - self.correct
        # Calculo de porcentaje
        score = int(self.correct / self.data_size * 100)

        # Impresion de resultados
        reply = QMessageBox.question(self, "Poli-Preguntas Game", "Felicitaciones!!!\nEn " + self.cat_actual + " tú porcentaje de aciertos es del " \
            + str(score) + "%\nRespuestas correctas: "  + str(self.correct) \
            + "\nRespuestas incorrectas: "+ str(wrong_count) +"\n¿Quieres seguir jugando?", QMessageBox.Yes, QMessageBox.No)

        # Validación usuario continua juego
        if reply == QMessageBox.Yes:
            # Reestablecer tablero
            self.frame_jugador.setStyleSheet(u"image: url(./assets/img/fondo_tablero_inicio.png);")
            self.lbl_categoria.setText(QCoreApplication.translate("GameForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\"></span></p></body></html>", None))
            self.lbl_pregunta.setText(QCoreApplication.translate("GameForm", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:16pt;\"></span></p></body></html>", None))
            
            # Restablecer opciones
            self.btn_next.setVisible(False)
            self.opt_respuesta_1.setVisible(False)
            self.opt_respuesta_2.setVisible(False)
            self.opt_respuesta_3.setVisible(False)
            self.opt_respuesta_4.setVisible(False)
            self.opt_respuesta_0.setVisible(False)
            self.opt_respuesta_0.setChecked(True)
            
            # Restablecer contadores
            self.q_no = 0
            self.correct = 0
            self.data_size = 0
        else:
            # Cerrar ventana game
            self.destroy()
    
     # ################################### Metodo about ########################################################
    # Este método se usa para mostrar el acerca de
    def about(self):
        QMessageBox.information(self, "Poli-Preguntas Game", "Poli-Preguntas” es un juego interactivo de preguntas y respuestas de selección múltiple presentadas al jugador en diversas categorías tales como Historia," \
            "Geografía, Matemáticas y Cultura General.\nMediante la captura de un nombre de usuario, el jugador podrá acumular puntos a medida que conteste de manera acertada las preguntas," \
            "al mismo tiempo que fomenta y estimula el aprendizaje de algunas áreas fundamentales en el desarrollo académico de una manera simple y lúdica (Prior, 2020).\n\n" \
            "Este juego es una herramienta educativa e instrumento para medir conocimientos integrales de una persona.\n\n“Poli-Preguntas” implica interacción digital para" \
            "desarrollar agilidad de respuesta, competitividad sana, búsqueda del conocimiento. El juego esta desarrollado en el lenguaje de programación Python en su" \
            "versión 3.10.0 con framework de interfaces gráficas Qt de PySide2 y manejo de datos con persistencia en archivos de configuración JSon.")