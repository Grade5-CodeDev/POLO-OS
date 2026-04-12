import re
from tqdm import tqdm
import time, random
import os as sysOS
p_echo = re.compile("echo\s(.*)", re.DOTALL)
p_cls = re.compile("cls")
class OS:
  def boot(self):
    steps = {
      "커널 로딩": {"count": 15, "speed": (0.03, 0.06)},
      "드라이버 초기화": {"count": 20, "speed": (0.02, 0.05)},
      "메모리 체크": {"count": 25, "speed": (0.01, 0.04)},
      "네트워크 연결": {"count": 18, "speed": (0.03, 0.07)},
      "UI 시작": {"count": 12, "speed": (0.02, 0.05)}
    }

    for step, config in steps.items():
      for i in tqdm(range(config["count"]), desc=step, leave=False):
        time.sleep(random.uniform(*config["speed"]))

    print("부팅 완료!")
  def echo(self, text):
    print(text)
  def cls(self):
    sysOS.system("cls")
  def off(self):
    quit()