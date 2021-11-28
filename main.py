# importanos tkinter
from tkinter import *

# importamos el cuadro de mensajes como "mb" desde tkinter
from tkinter import messagebox as mb

# importamos json para obtener la informacion
# de nuestro archivos de preguntas
import json

# Clase que define los componentes de la interfaz

class PoliPreguntas:

    # Este es el primer método que se llama cuando
    # Se inicializa un nuevo objeto de la clase. Este método
    # establece el contador de preguntas en 0 e inicializa todos los
    # otros métodos para mostrar el contenido del juego.
    def __init__(self):

        # establecer el número de pregunta en 0
        self.q_no = 0

        # Asignaremos las funciones para mostrarlas mas tarde
        self.display_title()
        self.display_question()

        # opt_selected espera un valor entero
        # para seleccionar la pregunta.
        self.opt_selected = IntVar()

        # Muestra el boton de radio para la pregunta actual
        # y se usa para mostrar las respuestas de la pregunta
        self.opts = self.radio_buttons()

        # Muestra las opciones de respuesta de las preguntas
        self.display_options()

        # Muestra los botones salir y siguiente.
        self.buttons()

        # Numero de preguntas total en preguntas.json
        self.data_size = len(question)

        # Contador preguntas correctas
        self.correct = 0

# ################################### Metodo display_result ########################################################

    # Este método se usa para mostrar el resultado.
    # Tambien cuenta el número de respuestas correctas e incorrectas
    # y al final muestra un cuadro con el resultado
    def display_result(self):

        # Calculo de preguntas incorrectas
        wrong_count = self.data_size - self.correct
        correct = f"Correctas: {self.correct}"
        wrong = f"Incorrectas: {wrong_count}"

        # Calculo de preguntas correctas
        score = int(self.correct / self.data_size * 100)
        result = f"Puntuación: {score}%"

        # Muestra un mensaje con el resultado
        mb.showinfo("Resultado", f"{result}\n{correct}\n{wrong}")

# ####################################### Metodo check_ans #####################################################

    # Este metodo verifica la respuesta
    # despues de hacer clic
    def check_ans(self, q_no):

        # Comprueba si la opcion selecciona es correcta
        if self.opt_selected.get() == answer[q_no]:
            # si la opcion es correcta retorna True
            return True
# ######################################### Metodo next_btn ####################################################

    # Este método se utiliza para verificar la respuesta de la
    # pregunta actual llamando al metodo check_ans
    # si la pregunta es correcta, aumenta el contador en 1 y pasará a la siguiente pregunta.
    # Si es la última pregunta, llamara al metodo display_result el cual mostrara
    # el resultado.
    def next_btn(self):

        # Comprueba si la respuesta es correcta.
        if self.check_ans(self.q_no):
            # si la respuesta es correcta, incrementa la correcta en 1
            self.correct += 1

        # Pasa a la siguiente pregunta incrementando el contador q_no
        self.q_no += 1

        # comprueba si el tamaño de q_no es igual al tamaño de las preguntas en preguntas.json
        if self.q_no == self.data_size:

            # Si ha finalizado las preguntas en el preguntas.json muestra el resultado
            self.display_result()

            # Destryue la GUI
            gui.destroy()
        else:
            # Muestra la siguiente pregunta
            self.display_question()
            self.display_options()

# ################################# Metodo buttons ######################################################

    # Este metodo muestra dos botones en pantalla
    # El primero es el boton next_button el cual pasa
    # a la siguiente pregunta. Tiene propiedades como
    # tamaño, color y texto.
    # El segundo es el boton de salida el cual se utiliza
    # para "destruir" la GUI sin finalizar el juego
    def buttons(self):

        # el Boton "next_button" da paso a la siguiente pregunta
        next_button = Button(gui, text="Siguiente", command=self.next_btn,
                             width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))

        # Ubicacion del boton "siguiente" en pantalla
        next_button.place(x=350, y=380)

        # El boton quit_button es usuado para quitar el juego
        quit_button = Button(gui, text="Salir", command=gui.destroy,
                             width=5, bg="black", fg="white", font=("ariel", 16, " bold"))

        # Ubicacion del boton "salir" en pantalla
        quit_button.place(x=700, y=50)

# ######################################### Metodo display_options ###########################################

    # Este metodo anula la seleccion de la opcion en pantalla
    # Tambien es usado para mostrar las opciones disponibles
    def display_options(self):
        val = 0

        # deseleccion de opciones
        self.opt_selected.set(0)

        # Recorremos las opciones que seran mostradas
        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

# ######################################### Metodo display_question ########################################

    # Este método muestra la pregunta actual en la pantalla
    def display_question(self):

        # Propiedades de la pregunta para mostrar en pantalla
        q_no = Label(gui, text=question[self.q_no], width=60,
                     font=('ariel', 16, 'bold'), anchor='w')

        # Ubicacion de las preguntas en pantalla
        q_no.place(x=70, y=100)

# ####################################### Metodo display_title #############################################

    # Metodo usado para mostrar el titulo del juego
    def display_title(self):

        # El titulo del juego
        title = Label(gui, text="POLI PREGUNTAS",
                      width=50, bg="green", fg="white", font=("ariel", 20, "bold"))

        # Ubicacion del titulo
        title.place(x=0, y=2)

# ################################ Metodo radio_buttons ##############################################

    # ESTE METODO SE ENCUENTA EN CONSTRUCCION PARA MEJORAR LA INTERFAZ

    # Este metodo muestra los botones de radio para seleccionar la pregunta
    # Tambien devuelve una lista que se usara para agregar las opciones de pregunta

    def radio_buttons(self):

        # Inicializa una lista con opciones vacias
        q_list = []

        # Posicion de la primera opcion
        y_pos = 150

        # Agregando las opciones de la lista creada
        while len(q_list) < 4:
            # Configuracion del radio boton
            radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 14))

            # Agregando el boton de la lista
            q_list.append(radio_btn)

            # Ubicacion del boton
            radio_btn.place(x=100, y=y_pos)

            # Incrementando la posicion y-axis por 40
            y_pos += 40

        # Retorno de los radio boton
        return q_list


# Creacion de la ventana de la GUI
gui = Tk()

# Configuracion del tamaño de la interfaz
gui.geometry("800x450")

# Configuracion del titulo de la ventana
gui.title("Poli Preguntas")

# Obtenemos la data del archivo preguntas.json
# Para evitar que los acentos no se vean afectados
# debemos configurar la codificacion UTF-8
with open('preguntas.json', encoding="utf-8") as f:
    data = json.load(f)

# Iniciamos las preguntas, opciones y respuestas
question = (data['question'])
options = (data['options'])
answer = (data['answer'])

# Creamos un objeto de la clase PoliPreguntas
poliPreguntas = PoliPreguntas()

# Iniciamos la interfaz
gui.mainloop()