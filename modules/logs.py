from datetime import datetime


class Logs:

  def __init__(self, file_name):
    self.file_name = file_name

  def trace(self, data):
    if data:
      with open(self.file_name, "a") as log_file:
        log_file.write(self.template(data))

  def template(self, data):
    return f"{self.pretty_time()}: {data}\n"

  def pretty_time(self):
    d = datetime.now().day
    m = datetime.now().month
    y = datetime.now().year
    s = datetime.now().second
    v = datetime.now().minute
    h = datetime.now().hour    

    return f"{y}:{m}:{d} {h}:{v}:{s}"  