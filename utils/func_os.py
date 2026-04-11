import re
from tqdm import tqdm as progressBar
p_echo = re.compile("echo\s(.*)", re.DOTALL)
p_cls = re.compile("cls")
class OS:
  def boot(self):
    for i in progressBar(range(100),desc="OS 부팅 중"):
      time.sleep(0.02 + i/1000)
  def echo(self, text):
    print(text)
  def cls(self):
    sysOS.system("cls")