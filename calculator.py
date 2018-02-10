# calculator.py

from tkinter import *
from tkinter import ttk
from functools import partial

# the list of all the keys in the keyboard
_keys = [
'*','/','AC',
'+','-','C',
'7','8','9',
'4','5','6',
'1','2','3',
'0','.','='
]
# list of all the numbers
nums = [
'7','8','9','.',
'4','5','6','0',
'1','2','3'
]
# list of all the commands
commands = [
'*','/','+',
'-','AC','C'
]

# the memory of the calculator
mem = {'x':0,'y':0,'math':'','act':[]}
# empty memory:
empty = mem
# active memory slot
#act = []


# the brain of the calculator
def brain(arg):
    if arg in [n for n in nums]:
        check(mem['act'],arg)
        make_num(mem['act'])
    elif arg in [c for c in commands]:
        do_command(arg)
    elif arg == '=':
        do_math()
    else:
        None

######## check the numbers and append them to act list ########        
def check(act,arg):
    if arg == '.' and act == []:
        act.append('0')
        act.append('.')
    elif arg == '.' and arg in act:
        None
    elif len(act) >= 12:
        None
    else:
        act.append(arg)

# join all elements in act list, turn them to one string and print them to _display
def make_num(act):
    n = list(act)
    n = ''.join(n)
    _display.set(n)
    print(n)
    print(mem['x'])

### checks the command, assigns it to 'math' in mem, assigns _display content into 'x' in mem ##
def do_command(arg):
    global mem
    #global act
    if arg in commands[:4]:
        mem['math'] = arg
        mem['x'] = float(_display.get())
        mem['act'] = []
    elif arg == 'C':
        None
    elif arg == 'AC':
        mem = {'x':0,'y':0,'math':'','act':[]}
        act = []
        _display.set('0')
    else:
	    None
    print(mem)
# assigns _display content into 'y' in mem, then does command assigned in the 'math' #
def do_math():
    global mem
    mem['y'] = float(_display.get())
    mem['act'] = []
    if mem['math'] == '+':
        res = mem['x'] + mem['y']
    elif mem['math'] == '-':
        res = mem['x'] - mem['y']
    elif mem['math'] == '*':
        res = mem['x'] * mem['y']
    elif mem['math'] == '/':
        res = mem['x'] / mem['y']
    else:
        None
    _display.set(res)
    print(mem)

# here comes the GUI #
if __name__ == '__main__':

# first create the root window
    _root = Tk()
    _root.title('Calculator')

#then comes the mainframe, where everything will be
    _mainframe = ttk.Frame(_root, padding='5 5 5 5')
    _mainframe.grid(row=0, column=0, sticky=(E, W, S, N))

# in the mainframe we define a frame for the display
    _dispfr = ttk.Frame(_mainframe, padding='5 5 5 5')
    _dispfr.grid(row=0, column=0, sticky=(E, W, S, N))

# and a variable for the display output	
    _display = StringVar()
    _display.set('0')
    _display_entry = ttk.Label(_dispfr, width=15, font=('Calibri','20'), textvariable=_display, anchor=W, background='white')
    _display_entry.grid(row=0, column=0, sticky=(E, W), padx=5)

# then comes the frame for the keyboard
    _keybfr = ttk.Frame(_mainframe, padding='5 5 5 5')
    _keybfr.grid(row=1, column=0, sticky=(E, W, S, N))
	
    _key = StringVar()
    k = 0

# the creation of the keyboard
    for i in range(6):
        for j in range(3):
            _keybtn = ttk.Button(_keybfr, text=_keys[k], command=partial(brain,_keys[k]))		
            _keybtn.grid(row=i, column=j, sticky=(E, W, S, N))
            k = k+1

    _root.mainloop()
