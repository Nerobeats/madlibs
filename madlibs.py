def main():
	print ("Mad libs where libs get mad.")
	print ("Start below: ")
	time = input("Enter a number from 1 to 12:  ")
	try:
		time = int(time)
	except ValueError as err:
		print ("Oh! We ran into an issue! please try again")
	else :
		if  0 >= int(time) or int(time) > 12:
			raise ValueError("incorrect number")
		items = input("Enter a noun (plural):  ")
		name = str(input("Enter a name:  ")).title()
		scream = str(input("Enter any sentence:"  )).upper()
		action = input("Enter a verb:  ")
		print( "")

		print ("The story goes...")

		print ("")
		print( " It was {} o'clock when I heard a knock at the door\n. I opened the door and there was a box full of {} with a note saying \"From Mr. {}.\"\n Just as I closed the door I heard a scream\"{}\" \n I froze in place and all I could do was {}.".format(time, items ,name ,scream , action))



if __name__ == '__main__':
	main()
