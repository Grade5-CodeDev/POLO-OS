import os as sysOS
import time, random
from utils.func_os import *
os = OS()
os.boot()
import re
 = re.compile("echo\s(.*)", re.DOTALL)
p_cls = re.compile("cls")
while True:
  choice = input("cmd >>> ")
  if p_echo.match(choice):
    os.echo(p_echo.sub("\g<1>", choice))
  elif p_cls.match(choice):
    os.cls()