import os as sysOS
class OS:
  def boot(self):
    print("boot test")
  def echo(self, text):
    print(text)
  def cls():
    sysOS.system("cls")

os = OS()
os.boot()
import re
p_echo = re.compile("echo\s(.*)", re.DOTALL)
p_cls = re.compilr("cls")
while True:
  choice = input("cmd >>> ")
  if p_echo.match(choice):
    os.echo(p_echo.sub("\g<1>", choice))
  elif p_cls.match():
    os.cls()
