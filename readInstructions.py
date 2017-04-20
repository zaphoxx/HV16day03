'''
	readInstrunctions.py 
	a short py script to solve the HV16 day3 challenge on http://hackvent.hacking-lab.com
	instructions are stored as gcode
	turtle will lower pen if it finds an E (extrusion) command in the line
	turtle will raise pen if there is no E command and just move to the coordinates given without drawing
	Z-coordinate values are ignored
	the result will be a QR code that can be scanned in right from the screen and provides the solution flag for the challenge
'''
from turtle import *
def executeInstruction(line,i):
	x=-1.0
	y=-1.0
	try:
		if(line.find('E')>-1):
			t.down()
		else:
			t.up()
			#print("[+] line {}: {}".format(i,line))
			#input("[+] check graphics - 'enter' to continue")
		if(line.find('G1')>-1):
			nx=line.find('X')
			ny=line.find('Y')
			if (nx>-1) and (ny>-1):
				nx=nx+1
				ny=ny+1
				x=float(line[nx:nx+6])
				y=float(line[ny:ny+6])
				#print("[+] x={} y={}".format(x,y))
				t.setpos(x,y)
			else:
				#print("[-] line {}: could not assign 'X/Y' coordinates.".format(i))
				pass
		else:
			#print("[-] 'G1' not found in line '{}'".format(line))
			pass
	except:
		print("[-] Error in 'executeInstruction()'!")
		
def resetPosition():
	pass
	
def main():
	try:
		t.color("red")
		t.setworldcoordinates(0,0,+200,+200)
		t.down()
	except:
		pass
	try:
		f=open("instructions","r")
		i=0
		for line in f:
			i=i+1
			executeInstruction(line,i)
	except:
		pass

if __name__=="__main__":
	from turtle import *
	import turtle as t
	
	main()
	input("press 'enter' to continue")
else:
	pass