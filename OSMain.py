class OS:
  def boot(self):
    print("boot test")
  def echo(self, text):
    print(text)

os = OS()
os.boot()
import re
p_echo = re.compile("echo\s(.*)", re.DOTALL)
while True:
  choice = input("cmd >>> ")
  if p_echo.match(choice):
    os.echo(p_echo.sub("\g<1>"))
