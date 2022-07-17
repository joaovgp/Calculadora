from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config


class Calculator(BoxLayout):
  flag = False

  def evaluate(self, label):
    try:
      label.text = str(eval(label.text))
      self.flag = True
    except:
      label.text = "Error"

  def addToDisplay(self, input):
    display = self.ids.calc_display
    ops = ['+', '-', '/', '*']
    if ((display.text == "Error" and (input == "DEL" or input == "C")) or (display.text != "Error" and input == "C")):
      display.text = '0'
    elif ((display.text == "Error" and input != "DEL" and input != "C") or (input not in ops and self.flag)):
      display.text = input
      self.flag = False
    elif (display.text != "Error" and input == "DEL"):
      display.text = display.text[:-1]
    elif (display.text == '0' and input != "DEL" and input != "C" and input != '.'):
      display.text = input
    elif (display.text != '0' and input == "C"):
      display.text = '0'
    else:
      display.text += input
      self.flag = False


class CalculatorApp(App):
  def build(self):
    return Calculator()


if __name__ == '__main__':
  Config.set('graphics', 'resizable', True)
  Config.set('kivy', 'keyboard_mode', 'system')
  Config.write()
  Config.set('graphics', 'width', '400')
  Config.set('graphics', 'heigth', '600')
  Config.write()

  CalculatorApp().run()
