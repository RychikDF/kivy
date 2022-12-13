from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


def get_calc(a, b, c):  # обработка результата
    if a > 1 and b > 1 and c >= 1:
        window1 = str(((a*2) + (b*2)) * c)
        window2 = str(c * 4)
        window3 = str((c * 4) * 2)

    elif a > 1 and b > 1 and c < 1:
        window1 = str((a * 2) + (b * 2))
        window2, window3 = str("0"), str("0")

    elif a < 1 and b < 1 and c < 1:
        window1, window2, window3 = str("0"), str("0"), str("0")

    elif a < 1 or b < 1 and c >= 1:
        window1, window2, window3 = str("0"), str("0"), str("0")

    elif a < 1 or b < 1 and c < 1:
        window1, window2, window3 = str("0"), str("0"), str("0")

    return {"window1": window1, "window2": window2, "window3": window3}


class Container(BoxLayout):

    def sbor(self): #Сбор и отправка данных


        try: txa1 = int(self.text_input_a1.text)
        except ValueError: txa1 = 0
        try: txb1 = int(self.text_input_b1.text)
        except ValueError: txb1 = 0
        try: txc1 = int(self.text_input_c1.text)
        except ValueError: txc1 = 0


        try: txa2 = int(self.text_input_a2.text)
        except ValueError: txa2 = 0
        try: txb2 = int(self.text_input_b2.text)
        except ValueError: txb2 = 0
        try: txc2 = int(self.text_input_c2.text)
        except ValueError: txc2 = 0


        try: txa3 = int(self.text_input_a3.text)
        except ValueError: txa3 = 0
        try: txb3 = int(self.text_input_b3.text)
        except ValueError: txb3 = 0
        try: txc3 = int(self.text_input_c3.text)
        except ValueError: txc3 = 0


        # Проверка отсутсвия цыфр в соседней колонке для вычета их
        # из подчетов

        if (txa1 <= 0 and txb1 > 0) or (txa1 > 0 and txb1 <= 0):
            txa1, txb1 = 0, 0
        if (txa2 <= 0 and txb2 > 0) or (txa1 > 0 and txb2 <= 0):
            txa2, txb2 = 0, 0
        if (txa3 <= 0 and txb3 > 0) or (txa3 > 0 and txb3 <= 0):
            txa3, txb3 = 0, 0


        tx1 = txa1 + txa2 + txa3
        tx2 = txb1 + txb2 + txb3
        tx3 = txc1 + txc2 + txc3

        sbor_win = get_calc(tx1,tx2,tx3)
        self.window1.text = sbor_win.get("window1") + " мм"
        self.window2.text = sbor_win.get("window2") + " шт."
        self.window3.text = sbor_win.get("window3") + " шт."

    def Clear(self): # Замена символов в полях
        self.window1.text = "мм"
        self.window2.text = "шт."
        self.window3.text = "шт."

        self.text_input_a1.text = ""
        self.text_input_a2.text = ""
        self.text_input_a3.text = ""

        self.text_input_b1.text = ""
        self.text_input_b2.text = ""
        self.text_input_b3.text = ""

        self.text_input_c1.text = ""
        self.text_input_c2.text = ""
        self.text_input_c3.text = ""


class MyApp(App):
    def build(self):
        return Container()


if __name__ == "__main__":
    MyApp().run()