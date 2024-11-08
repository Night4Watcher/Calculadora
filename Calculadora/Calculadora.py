import reflex as rx
# ESTILOS DE LOS CONTENIDOS DE LA PAGINA

estilo_general = {
    
}

estilo_botones = {
    
}

estilo_texto = {
    
}

class calculadora(rx.State):
    resultado: int = 0
    numero_mostrado: str = "0"
    numero_1: int = 0
    numero_2: int = 0
    operador: int = 0
    texto_ayuda: str = ""
    
    def añadir_numero_1(self):
        if self.numero_mostrado == "0":
            self.numero_mostrado = "1"
        else:
            self.numero_mostrado += "1"
    
    def añadir_numero_2(self):
        if self.numero_mostrado == "0":
            self.numero_mostrado = "2"
        else:
            self.numero_mostrado += "2"
    
    def añadir_numero_3(self):
        if self.numero_mostrado == "0":
            self.numero_mostrado = "3"
        else:
            self.numero_mostrado += "3"
    
    def añadir_numero_4(self):
        if self.numero_mostrado == "0":
            self.numero_mostrado = "4"
        else:
            self.numero_mostrado += "4"
            
    def añadir_numero_5(self):
        if self.numero_mostrado == "0":
            self.numero_mostrado = "5"
        else:
            self.numero_mostrado += "5"
            
    def añadir_numero_6(self):
        if self.numero_mostrado == "0":
            self.numero_mostrado = "6"
        else:
            self.numero_mostrado += "6"
            
    def añadir_numero_7(self):
        if self.numero_mostrado == "0":
            self.numero_mostrado = "7"
        else:
            self.numero_mostrado += "7"
            
    def añadir_numero_8(self):
        if self.numero_mostrado == "0":
            self.numero_mostrado = "8"
        else:
            self.numero_mostrado += "8"
            
    def añadir_numero_9(self):
        if self.numero_mostrado == "0":
            self.numero_mostrado = "9"
        else:
            self.numero_mostrado += "9"
            
    def añadir_numero_0(self):
        self.numero_mostrado += "0"
        
    def vaciar_texto(self):
        self.numero_mostrado = "0"    
    
    def sumar(self):
        if self.numero_mostrado != "0":
            self.numero_1 = int(self.numero_mostrado)
            self.numero_mostrado = "0"
        self.operador = 1
        self.texto_ayuda = ""
    
    def resta(self):
        if self.numero_mostrado != "0":
            self.numero_1 = int(self.numero_mostrado)
            self.numero_mostrado = "0"
        self.operador = 2
        self.texto_ayuda = ""
    
    def multiplicar(self):
        if self.numero_mostrado != "0":
            self.numero_1 = int(self.numero_mostrado)
            self.numero_mostrado = "0"
        self.operador = 3
        self.texto_ayuda = ""
    
    def dividir(self):
        if self.numero_mostrado != "0":
            self.numero_1 = int(self.numero_mostrado)
            self.numero_mostrado = "0"
        self.operador = 4
        self.texto_ayuda = ""
    
    def resolver(self):
        if self.numero_mostrado != "0":
            self.numero_2 = int(self.numero_mostrado)
        match (self.operador):
            case 0:
                self.texto_ayuda = "No has seleccionado ningun operador"
            case 1:
                self.resultado = self.numero_1 + self.numero_2
                self.numero_mostrado = str(self.resultado)
                self.operador = 0
            case 2:
                self.resultado = self.numero_1 - self.numero_2
                self.numero_mostrado = str(self.resultado)
                self.operador = 0
            case 3:
                self.resultado = self.numero_1 * self.numero_2
                self.numero_mostrado = str(self.resultado)
                self.operador = 0
            case 4:
                self.resultado = int(self.numero_1 / self.numero_2)
                self.numero_mostrado = str(self.resultado)
                self.operador = 0

@rx.page(title= "Calculadora", route= "/")
def index():
    return (
        rx.vstack(
            rx.text(
                calculadora.texto_ayuda
            ),
            rx.hstack(
                rx.text(
                    calculadora.numero_mostrado
                )
            ),
            # MUESTRA AL USUARIO LOS NUMEROS 1, 2 Y 3 Y EL BORRADO DEL NUMERO QUE SE MUESTRE EN LA PANTALLA
            rx.hstack(
                rx.button(
                    "1",
                    on_click= calculadora.añadir_numero_1
                ),
                rx.button(
                    "2",
                    on_click= calculadora.añadir_numero_2
                ),
                rx.button(
                    "3",
                    on_click= calculadora.añadir_numero_3
                ),
                rx.button(
                    "AC",
                    on_click= calculadora.vaciar_texto
                )
            ),
            # MUESTRA AL USUARIO LOS NUMEROS 4, 5 Y 6 Y LA OPCION DE SUMAR NUMEROS
            rx.hstack(
                rx.button(
                    "4",
                    on_click=calculadora.añadir_numero_4
                ),
                rx.button(
                    "5",
                    on_click=calculadora.añadir_numero_5
                ),
                rx.button(
                    "6",
                    on_click=calculadora.añadir_numero_6
                ),
                rx.button(
                    "+",
                    on_click=calculadora.sumar
                )
            ),
            # MUESTRA AL USUARIO LOS NUMEROS 7, 8 Y 9 Y LA OPCION DE RESTAR NUMEROS
            rx.hstack(
                rx.button(
                    "7",
                    on_click=calculadora.añadir_numero_7
                ),
                rx.button(
                    "8",
                    on_click=calculadora.añadir_numero_8
                ),
                rx.button(
                    "9",
                    on_click=calculadora.añadir_numero_9
                ),
                rx.button(
                    "-",
                    on_click=calculadora.resta
                )
            ),
            rx.hstack(
                rx.button(
                    "0",
                    on_click=calculadora.añadir_numero_0
                ),
                rx.button(
                    "X",
                    on_click=calculadora.multiplicar
                ),
                rx.button(
                    "/",
                    on_click=calculadora.dividir
                ),
                rx.button(
                    "=",
                    on_click=calculadora.resolver
                )
            )
        )
    )

app = rx.App()
