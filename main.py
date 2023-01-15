from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
import locale
import collections
#Window.size = (720, 1280) # Примерный экран смартфона
Window.size = (480, 853)
locale.setlocale(locale.LC_ALL, '')

def get_calc(a, b, c):  # обработка результата
    if a > 1 and b > 1 and c >= 1:
        window1 = (((a*2) + (b*2)) * c)
        window2 = (c * 4)
        window3 = ((c * 4) * 2)
    elif a > 1 and b > 1 and c < 1:
        window1 = (a) + (b)
        window2, window3 = (0), (0)

    elif a < 1 and b < 1 and c < 1:
        window1, window2, window3 = (0), (0), (0)

    elif a < 1 or b < 1 and c >= 1:
        window1, window2, window3 = (0), (0), (0)

    elif a < 1 or b < 1 and c < 1:
        window1, window2, window3 = (0), (0), (0)

    return {"window1": window1, "window2": window2, "window3": window3}



class Container(BoxLayout):


    def sbor(self): #Сбор и отправка данных

        try: window_a_1 = int(self.text_input_a1.text)
        except ValueError: window_a_1 = 0
        try: window_b_1 = int(self.text_input_b1.text)
        except ValueError: window_b_1 = 0
        try: window_c_1 = int(self.text_input_c1.text)
        except ValueError: window_c_1 = 0

        try: window_a_2 = int(self.text_input_a2.text)
        except ValueError: window_a_2 = 0
        try: window_b_2 = int(self.text_input_b2.text)
        except ValueError: window_b_2 = 0
        try: window_c_2 = int(self.text_input_c2.text)
        except ValueError: window_c_2 = 0

        try: window_a_3 = int(self.text_input_a3.text)
        except ValueError: window_a_3 = 0
        try: window_b_3 = int(self.text_input_b3.text)
        except ValueError: window_b_3 = 0
        try: window_c_3 = int(self.text_input_c3.text)
        except ValueError: window_c_3 = 0

        try: window_a_4 = int(self.text_input_a4.text)
        except ValueError: window_a_4 = 0
        try: window_b_4 = int(self.text_input_b4.text)
        except ValueError: window_b_4 = 0
        try: window_c_4 = int(self.text_input_c4.text)
        except ValueError: window_c_4 = 0

        try: window_a_5 = int(self.text_input_a5.text)
        except ValueError: window_a_5 = 0
        try: window_b_5 = int(self.text_input_b5.text)
        except ValueError: window_b_5 = 0
        try: window_c_5 = int(self.text_input_c5.text)
        except ValueError: window_c_5 = 0

        try: window_a_6 = int(self.text_input_a6.text)
        except ValueError: window_a_6 = 0
        try: window_b_6 = int(self.text_input_b6.text)
        except ValueError: window_b_6 = 0
        try: window_c_6 = int(self.text_input_c6.text)
        except ValueError: window_c_6 = 0

        try: window_a_7 = int(self.text_input_a7.text)
        except ValueError: window_a_7 = 0
        try: window_b_7 = int(self.text_input_b7.text)
        except ValueError: window_b_7 = 0
        try: window_c_7 = int(self.text_input_c7.text)
        except ValueError: window_c_7 = 0

        try: window_a_8 = int(self.text_input_a8.text)
        except ValueError: window_a_8 = 0
        try: window_b_8 = int(self.text_input_b8.text)
        except ValueError: window_b_8 = 0
        try: window_c_8 = int(self.text_input_c8.text)
        except ValueError: window_c_8 = 0

        try: window_a_9 = int(self.text_input_a9.text)
        except ValueError: window_a_9 = 0
        try: window_b_9 = int(self.text_input_b9.text)
        except ValueError: window_b_9 = 0
        try: window_c_9 = int(self.text_input_c9.text)
        except ValueError: window_c_9 = 0

        try: window_a_10 = int(self.text_input_a10.text)
        except ValueError: window_a_10 = 0
        try: window_b_10 = int(self.text_input_b10.text)
        except ValueError: window_b_10 = 0
        try: window_c_10 = int(self.text_input_c10.text)
        except ValueError: window_c_10 = 0


        # Проверка отсутсвия цыфр в соседней колонке для вычета их
        # из подчетов

        if (window_a_1 <= 0 and window_b_1 > 0) or (window_a_1 > 0 and window_b_1 <= 0):
            window_a_1, window_b_1 = 0, 0
        if (window_a_2 <= 0 and window_b_2 > 0) or (window_a_2 > 0 and window_b_2 <= 0):
            window_a_2, window_b_2 = 0, 0
        if (window_a_3 <= 0 and window_b_3 > 0) or (window_a_3 > 0 and window_b_3 <= 0):
            window_a_3, window_b_3 = 0, 0
        if (window_a_4 <= 0 and window_b_4 > 0) or (window_a_4 > 0 and window_b_4 <= 0):
            window_a_4, window_b_4 = 0, 0
        if (window_a_5 <= 0 and window_b_5 > 0) or (window_a_5 > 0 and window_b_5 <= 0):
            window_a_5, window_b_5 = 0, 0
        if (window_a_6 <= 0 and window_b_6 > 0) or (window_a_6 > 0 and window_b_6 <= 0):
            window_a_6, window_b_6 = 0, 0
        if (window_a_7 <= 0 and window_b_7 > 0) or (window_a_7 > 0 and window_b_7 <= 0):
            window_a_7, window_b_7 = 0, 0
        if (window_a_8 <= 0 and window_b_8 > 0) or (window_a_8 > 0 and window_b_8 <= 0):
            window_a_8, window_b_8 = 0, 0
        if (window_a_9 <= 0 and window_b_9 > 0) or (window_a_9 > 0 and window_b_9 <= 0):
            window_a_9, window_b_9 = 0, 0
        if (window_a_10 <= 0 and window_b_10 > 0) or (window_a_10 > 0 and window_b_10 <= 0):
            window_a_10, window_b_10 = 0, 0


         #СОбераем списки
        sbor_win1 = get_calc(window_a_1, window_b_1, window_c_1)
        sbor_win2 = get_calc(window_a_2, window_b_2, window_c_2)
        sbor_win3 = get_calc(window_a_3, window_b_3, window_c_3)
        sbor_win4 = get_calc(window_a_4, window_b_4, window_c_4)
        sbor_win5 = get_calc(window_a_5, window_b_5, window_c_5)
        sbor_win6 = get_calc(window_a_6, window_b_6, window_c_6)
        sbor_win7 = get_calc(window_a_7, window_b_7, window_c_7)
        sbor_win8 = get_calc(window_a_8, window_b_8, window_c_8)
        sbor_win9 = get_calc(window_a_9, window_b_9, window_c_9)
        sbor_win10 = get_calc(window_a_10, window_b_10, window_c_10)
         #создаем доп список
        sbor_win = collections.Counter()
         #загружаем все в один список
        sbor_win.update(sbor_win1)
        sbor_win.update(sbor_win2)
        sbor_win.update(sbor_win3)
        sbor_win.update(sbor_win4)
        sbor_win.update(sbor_win5)
        sbor_win.update(sbor_win6)
        sbor_win.update(sbor_win7)
        sbor_win.update(sbor_win8)
        sbor_win.update(sbor_win9)
        sbor_win.update(sbor_win10)


        print(sbor_win)

         #выводим на экран

        """Разделитель текста, 1 234 567 890 """
        wind = locale.format_string('%d', sbor_win.get("window1"), grouping=True)


        self.window_l1.text = str(wind) + " мм"
        self.window_l2.text = str(sbor_win.get("window2")) + " ш.т."
        self.window_l3.text = str(sbor_win.get("window3")) + " ш.т."

    def Clear(self): # Замена символов в полях
        self.window_l1.text = "мм"
        self.window_l2.text = "шт."
        self.window_l3.text = "шт."

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