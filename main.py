from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class SimpleCalculator(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.result_label = TextInput(text='0', font_size=40, readonly=True, halign='right')
        layout.add_widget(self.result_label)
        self.num1 = TextInput(hint_text='第一个数字', font_size=24, input_filter='float')
        self.num2 = TextInput(hint_text='第二个数字', font_size=24, input_filter='float')
        layout.add_widget(self.num1)
        layout.add_widget(self.num2)

        btn_layout = BoxLayout(spacing=10)
        for op in ['+', '-', '*', '/']:
            btn = Button(text=op, font_size=30)
            btn.bind(on_press=self.calculate)
            btn_layout.add_widget(btn)

        layout.add_widget(btn_layout)
        return layout

    def calculate(self, instance):
        try:
            a = float(self.num1.text) if self.num1.text else 0
            b = float(self.num2.text) if self.num2.text else 0
            if instance.text == '+': result = a + b
            elif instance.text == '-': result = a - b
            elif instance.text == '*': result = a * b
            elif instance.text == '/': result = a / b if b != 0 else '错误：除数不能为0'
            self.result_label.text = str(result)
        except ValueError:
            self.result_label.text = '请输入数字'

if __name__ == '__main__':
    SimpleCalculator().run()