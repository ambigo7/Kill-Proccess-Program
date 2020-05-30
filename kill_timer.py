import os
import time
from tqdm import tqdm

num = 0

def waktu(tm):
	time.sleep(tm)

def main():
	print("\n------Close Application With Timer In Python-----")
	app = input("Application Name : ")
	print("")
	print("Program Execution Options: ")
	print("1. Now")
	print("2. Set Timer")
	switch = input("Input your choice : ")
	print("--------------------------------------------------")
	if switch == "1":
		global num
		num = 0
		#waktu(num)
		print("Start the application end task...")
	elif switch == "2":
		print("----------------Options----------------")
		print("A. 15 Minute")
		print("B. 30 Minute")
		print("C.  1 Hour")
		print("D. Set Manually")
		switch_time = input("Input your choice : ")
		print("---------------------------------------")
		if switch_time == "A" or switch_time == "a":
			num = 900
		elif switch_time == "B" or switch_time == "b":
			num = 1800
		elif switch_time == "C" or switch_time == "c":
			num = 3600
		elif switch_time == "D" or switch_time == "d":
			num = int(input("Input Time[second] : "))
	print("Start the application end task...")
	print("End Task "+app+" in {} second".format(num))
	for i in tqdm(range(4)):
		waktu(num)
	os.system("taskkill /f /im "+app+".exe")

main()
print("© 2020@dendirzkptr")
