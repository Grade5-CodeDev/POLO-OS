class OS:
  def start(self):
    self.boot()
  def boot(self):
    print("boot test")

os = OS()
os.start()
