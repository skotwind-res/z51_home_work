from traceback import format_exc as tb
from time import sleep

from .logs import Logs


logs = Logs("logs/action.log")

def run():
	while True:
		try:
			num1 = input('enter num 1: ')
			logs.trace(f"Get: {num1} as num 1.") 
			num2 = input('enter num 2: ')
			logs.trace(f"Get: {num2} as num 2.") 
			num1, num2 = int(num1), int(num2)
			logs.trace(f"result: {num1 / num2}") 
			sleep(1)
		except Exception as e:
			logs.trace(f"EGGOR: {e}\n {tb()}")			