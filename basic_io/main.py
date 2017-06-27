""" USE PYTHON3.x to execute """
import sys

def main():
	"""Main entry point for the script."""
	
	#basic print operation
	print(1,2,3,4)
	print(1,2,3,4,sep='*')
	print(1,2,3,4,sep='#',end='&')
	x=5;y=10
	
	#using str.format()
	print('The value of x is {} and y is {}'.format(x,y))
	print('I love {0} and {1}'.format('bread','butter'))
	print('I love {1} and {0}'.format('bread','butter'))
	print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))
	
	#formatters using %
	formatter = "%r %r %r %r" # or %s
	print (formatter % (1, 2, 3, 4))
	print (formatter % ("one", "two", "three", "four"))
	print (formatter % (True, False, False, True))
	print (formatter % (formatter, formatter, formatter, formatter))
	print (formatter % ("I had this thing.","That you could type up right.","But it didn't sing.","So I said goodnight."))

	# c printf style
	x = 11.235756
	print('The value of x is %3.2f' %x)
	print('The value of x is %3.4f' %x)

	# string duplicate and concatinate
	print("-" * 20)

	#cmdline args
	if(len(sys.argv)): # to check if args set. 1 because sys.argv[0] is the filename itself.
		if(sys.argv[1]=="greet"):
			a=input("Enter your name:")
			print("Hello %s, Good Day!" %a)
		else:
			print("Invalid cmdline arg.") # Error Proofing
	pass


if __name__ == '__main__':
	sys.exit(main())