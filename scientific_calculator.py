
# Tkinter kütüphanesi GUI oluşturmak için kullanılır
import tkinter as tk
 # Matematiksel işlemler için math kütüphanesi
import math

# Bilimsel hesap makinesi sınıfı
class ScientificCalculator:
    # Hesap makinesinin başlatıcı metodu
     def __init__(self, master):
        self.master = master
        master.title("Bilimsel Hesap Makinesi")
        master.geometry("600x800")
        master.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    # Arayüz bileşenlerini oluşturan metod
     def create_widgets(self):
        # Ekran çerçevesi oluşturma
         display_frame = tk.Frame(self.master, bd=20, pady=2, bg='powder blue', relief='ridge')
         display_frame.pack(side=tk.TOP)

         # Giriş alanı (hesaplamaların gösterildiği yer)
         input_field = tk.Entry(display_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, bd=10, insertwidth=4, width=24, justify='right')
         input_field.grid(row=0, column=0)
         input_field.pack(ipady=10)

         # Butonların yer alacağı çerçeve
         btns_frame = tk.Frame(self.master, bd=20, pady=2, bg='gainsboro', relief='ridge')
         btns_frame.pack(side=tk.BOTTOM)

         # İlk buton sırası
         # C butonu: Tüm ekranı temizler
         clear = tk.Button(btns_frame, text="C", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.clear_all())
         clear.grid(row=0, column=0, pady=1)
         # Geri butonu: Son karakteri siler
         backspace = tk.Button(btns_frame, text="←", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.backspace())
         backspace.grid(row=0, column=1, pady=1)
         # Modulo butonu: Mod alma işlemi yapar
         mod = tk.Button(btns_frame, text="%", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.btn_click('%'))
         mod.grid(row=0, column=2, pady=1)
         # Bölme butonu
         divide = tk.Button(btns_frame, text="/", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.btn_click('/'))
         divide.grid(row=0, column=3, pady=1)

         # İkinci buton sırası
         seven = tk.Button(btns_frame, text="7", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.btn_click('7'))
         seven.grid(row=1, column=0, pady=1)
         eight = tk.Button(btns_frame, text="8", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.btn_click('8'))
         eight.grid(row=1, column=1, pady=1)
         nine = tk.Button(btns_frame, text="9", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.btn_click('9'))
         nine.grid(row=1, column=2, pady=1)
         # Çarpma butonu
         multiply = tk.Button(btns_frame, text="*", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.btn_click('*'))
         multiply.grid(row=1, column=3, pady=1)

         # Üçüncü buton sırası
         four = tk.Button(btns_frame, text="4", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.btn_click('4'))
         four.grid(row=2, column=0, pady=1)
         five = tk.Button(btns_frame, text="5", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.btn_click('5'))
         five.grid(row=2, column=1, pady=1)
         six = tk.Button(btns_frame, text="6", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.btn_click('6'))
         six.grid(row=2, column=2, pady=1)
         # Çıkarma butonu
         minus = tk.Button(btns_frame, text="-", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.btn_click('-'))
         minus.grid(row=2, column=3, pady=1)

         # Dördüncü buton sırası
         one = tk.Button(btns_frame, text="1", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.btn_click('1'))
         one.grid(row=3, column=0, pady=1)
         two = tk.Button(btns_frame, text="2", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.btn_click('2'))
         two.grid(row=3, column=1, pady=1)
         three = tk.Button(btns_frame, text="3", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.btn_click('3'))
         three.grid(row=3, column=2, pady=1)
         # Toplama butonu
         plus = tk.Button(btns_frame, text="+", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.btn_click('+'))
         plus.grid(row=3, column=3, pady=1)

         # Beşinci buton sırası
         zero = tk.Button(btns_frame, text="0", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.btn_click('0'))
         zero.grid(row=4, column=0, pady=1)
         dot = tk.Button(btns_frame, text=".", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.btn_click('.'))
         dot.grid(row=4, column=1, pady=1)
         # Eşittir butonu: İfadeyi değerlendirir
         equals = tk.Button(btns_frame, text="=", fg="black", width=17, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.btn_equal())
         equals.grid(row=4, column=2, columnspan=2, pady=1)

         # Bilimsel butonlar
         # Pi sayısı butonu
         pi = tk.Button(btns_frame, text="π", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.btn_click(str(math.pi)))
         pi.grid(row=0, column=4, pady=1)
         # e sayısı butonu
         e = tk.Button(btns_frame, text="e", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.btn_click(str(math.e)))
         e.grid(row=1, column=4, pady=1)
         # Sinüs butonu
         sin = tk.Button(btns_frame, text="sin", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.scientific_op('sin'))
         sin.grid(row=2, column=4, pady=1)
         # Kosinüs butonu
         cos = tk.Button(btns_frame, text="cos", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.scientific_op('cos'))
         cos.grid(row=3, column=4, pady=1)
         # Tanjant butonu
         tan = tk.Button(btns_frame, text="tan", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.scientific_op('tan'))
         tan.grid(row=4, column=4, pady=1)

         # Karekök butonu
         sqrt = tk.Button(btns_frame, text="√", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.scientific_op('sqrt'))
         sqrt.grid(row=0, column=5, pady=1)
         # Kare alma butonu
         power = tk.Button(btns_frame, text="x²", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.scientific_op('power2'))
         power.grid(row=1, column=5, pady=1)
         # Logaritma (taban 10) butonu
         log = tk.Button(btns_frame, text="log", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.scientific_op('log'))
         log.grid(row=2, column=5, pady=1)
         # Doğal logaritma (ln) butonu
         ln = tk.Button(btns_frame, text="ln", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.scientific_op('ln'))
         ln.grid(row=3, column=5, pady=1)
         # Faktöriyel butonu
         fact = tk.Button(btns_frame, text="n!", fg="black", width=8, height=3, bd=8, font=('arial', 18, 'bold'), command=lambda: self.scientific_op('fact'))
         fact.grid(row=4, column=5, pady=1)

    # Butonlara tıklandığında çalışan metod
    # Tıklanan butonun değerini ifadeye ekler ve ekranda gösterir.
     def btn_click(self, item):
        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)

    # Ekranı temizleme metodu
    # İfadeyi ve ekranı sıfırlar.
     def clear_all(self):
        self.expression = ""
        self.input_text.set("")

    # Son karakteri silme metodu
    # İfadeden son karakteri siler ve ekranda günceller.
     def backspace(self):
        self.expression = self.expression[:-1]
        self.input_text.set(self.expression)

    # Eşittir butonuna basıldığında çalışan metod
    # Mevcut ifadeyi değerlendirir, sonucu ekranda gösterir ve ifadeyi sonuçla günceller.
    # Hata durumunda 'Error' gösterir.
     def btn_equal(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            self.input_text.set("Error")
            self.expression = ""

    # Bilimsel işlemleri gerçekleştiren metod
    # Sinüs, kosinüs, tanjant, karekök, kare alma, logaritma (taban 10), doğal logaritma (ln) ve faktöriyel gibi bilimsel işlemleri yapar.
    # Sonucu ekranda gösterir ve ifadeyi sonuçla günceller.
    # Hata durumunda 'Error' gösterir.
     def scientific_op(self, op):
        try:
            val = float(self.expression)
            if op == 'sin':
                result = math.sin(math.radians(val))
            elif op == 'cos':
                result = math.cos(math.radians(val))
            elif op == 'tan':
                result = math.tan(math.radians(val))
            elif op == 'sqrt':
                result = math.sqrt(val)
            elif op == 'power2':
                result = val ** 2
            elif op == 'log':
                result = math.log10(val)
            elif op == 'ln':
                result = math.log(val)
            elif op == 'fact':
                result = math.factorial(int(val))
            else:
                result = "Error"
            self.input_text.set(str(result))
            self.expression = str(result)
        except Exception as e:
            self.input_text.set("Error")
            self.expression = ""

if __name__ == '__main__':
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()