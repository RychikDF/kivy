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

        try: txa4 = int(self.text_input_a4.text)
        except ValueError: txa4 = 0
        try: txb4 = int(self.text_input_b4.text)
        except ValueError: txb4 = 0
        try: txc4 = int(self.text_input_c4.text)
        except ValueError: txc4 = 0

        try: txa5 = int(self.text_input_a5.text)
        except ValueError: txa5 = 0
        try: txb5 = int(self.text_input_b5.text)
        except ValueError: txb5 = 0
        try: txc5 = int(self.text_input_c5.text)
        except ValueError: txc5 = 0

        try: txa6 = int(self.text_input_a6.text)
        except ValueError: txa6 = 0
        try: txb6 = int(self.text_input_b6.text)
        except ValueError: txb6 = 0
        try: txc6 = int(self.text_input_c6.text)
        except ValueError: txc6 = 0

        try: txa7 = int(self.text_input_a7.text)
        except ValueError: txa7 = 0
        try: txb7 = int(self.text_input_b7.text)
        except ValueError: txb7 = 0
        try: txc7 = int(self.text_input_c7.text)
        except ValueError: txc7 = 0

        try: txa8 = int(self.text_input_a8.text)
        except ValueError: txa8 = 0
        try: txb8 = int(self.text_input_b8.text)
        except ValueError: txb8 = 0
        try: txc8 = int(self.text_input_c8.text)
        except ValueError: txc8 = 0

        try: txa9 = int(self.text_input_a9.text)
        except ValueError: txa9 = 0
        try: txb9 = int(self.text_input_b9.text)
        except ValueError: txb9 = 0
        try: txc9 = int(self.text_input_c9.text)
        except ValueError: txc9 = 0

        try: txa10 = int(self.text_input_a10.text)
        except ValueError: txa10 = 0
        try: txb10 = int(self.text_input_b10.text)
        except ValueError: txb10 = 0
        try: txc10 = int(self.text_input_c10.text)
        except ValueError: txc10 = 0


        # Проверка отсутсвия цыфр в соседней колонке для вычета их
        # из подчетов

        if (txa1 <= 0 and txb1 > 0) or (txa1 > 0 and txb1 <= 0):
            txa1, txb1 = 0, 0
        if (txa2 <= 0 and txb2 > 0) or (txa2 > 0 and txb2 <= 0):
            txa2, txb2 = 0, 0
        if (txa3 <= 0 and txb3 > 0) or (txa3 > 0 and txb3 <= 0):
            txa3, txb3 = 0, 0
        if (txa4 <= 0 and txb4 > 0) or (txa4 > 0 and txb4 <= 0):
            txa4, txb4 = 0, 0
        if (txa5 <= 0 and txb5 > 0) or (txa5 > 0 and txb5 <= 0):
            txa5, txb5 = 0, 0
        if (txa6 <= 0 and txb6 > 0) or (txa6 > 0 and txb6 <= 0):
            txa6, txb6 = 0, 0
        if (txa7 <= 0 and txb7 > 0) or (txa7 > 0 and txb7 <= 0):
            txa7, txb7 = 0, 0
        if (txa8 <= 0 and txb8 > 0) or (txa8 > 0 and txb8 <= 0):
            txa8, txb2 = 0, 0
        if (txa9 <= 0 and txb9 > 0) or (txa9 > 0 and txb9 <= 0):
            txa9, txb9 = 0, 0
        if (txa10 <= 0 and txb10 > 0) or (txa10 > 0 and txb10 <= 0):
            txa10, txb10 = 0, 0


        tx1 = txa1 + txa2 + txa3 + txa4 + txa5 + \
              txa6 + txa7 + txa8 + txa9 + txa10
        tx2 = txb1 + txb2 + txb3 + txb4 + txb5 + \
              txb6 + txb7 + txb8 + txb9 + txb10
        tx3 = txc1 + txc2 + txc3 + txc4 + txc5 + \
              txc6 + txc7 + txc8 + txc9 + txc10

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
        self.text_input_a4.text = ""
        self.text_input_a5.text = ""
        self.text_input_a6.text = ""
        self.text_input_a7.text = ""
        self.text_input_a8.text = ""
        self.text_input_a9.text = ""
        self.text_input_a10.text = ""

        self.text_input_b1.text = ""
        self.text_input_b2.text = ""
        self.text_input_b3.text = ""
        self.text_input_b4.text = ""
        self.text_input_b5.text = ""
        self.text_input_b6.text = ""
        self.text_input_b7.text = ""
        self.text_input_b8.text = ""
        self.text_input_b9.text = ""
        self.text_input_b10.text = ""

        self.text_input_c1.text = ""
        self.text_input_c2.text = ""
        self.text_input_c3.text = ""
        self.text_input_c4.text = ""
        self.text_input_c5.text = ""
        self.text_input_c6.text = ""
        self.text_input_c7.text = ""
        self.text_input_c8.text = ""
        self.text_input_c9.text = ""
        self.text_input_c10.text = ""


class MyApp(App):
    def build(self):
        return Container()


if __name__ == "__main__":
    MyApp().run()