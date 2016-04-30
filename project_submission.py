from sys import exit

easy_paragraph = '''
Making web pages is very fun!
You can add content to a page with __1__.
To style the page you can use __2__.
If you want the page to actually do stuff you can use __3__.
Then you can use __4__ to interact with servers.
'''

medium_paragraph = '''
There are many frameworks for making websites.
If you are using Python most people would choose __1__.
If you like Ruby you would most probably use __2__.
Now in the PHP world there is a lot of options though you
could go with __3__, or __4__.
'''

hard_paragraph = '''
Web protocols are how servers interact. People mostly use
__1__ protocols. Some __1__ protocols are __2__ which takes
care of communication between a server and browser, __3__ which
is a secure version of the protocol I just mentioned, and __4__
which handles sending files.
'''

easy_awnsers = ['html', 'css', 'javascript', 'php']
medium_awnsers = ['django', 'rails', 'laravel', 'cake']
hard_awnsers = ['tcp', 'http', 'https', 'ftp'] 

def lowercase_awnser(obj):
	'''Taking care of case-sensitive input.'''
	return obj.lower()

def get_level_mode():
	'''Setting level difficulty.'''
	level_mode = raw_input("Select your difficulty(e, m, h): ")
	level_mode = lowercase_awnser(level_mode)

	if level_mode == "e" level_mode == "easy":
		return easy_paragraph, easy_awnsers
	elif level_mode == "m" or level_mode == "medium":
		return medium_paragraph, medium_awnsers
	elif level_mode == "h" or level_mode == "hard":
		return hard_paragraph, hard_awnsers
	else:
		print 'Unknown Gamemode!'
		exit(0)

def get_and_parse_awnser(blank_name, blank_num, array, paragraph):
	'''Seeing if awnser is wrong or right.'''
	blank_name = raw_input("Fill the blank for #" + str(blank_num) + ": ")
	blank_name = lowercase_awnser(blank_name)
	if blank_name == array[blank_num - 1]:
		print 'Correct!'
		print paragraph.replace("__"+str(blank_num)+"__", array[blank_num - 1])
	else: 
		print 'Wrong!'
		exit(0)

def play_level():
	'''Playing a level'''
	paragraph, awnsers = get_level_mode()

	print paragraph

	i=1
	while i < 5:
		get_and_parse_awnser("blank1", i, awnsers, paragraph)
		i+=1

def run():
	'''Main program function.'''
	print '\tFill in the Blanks || Web Pages\t'
	play_level()

if __name__ == '__main__':
	run()


