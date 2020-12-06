# Start

# Import modules
import time
import os
import shlex
import struct
import platform
import subprocess
# /Import modules

# Determine console width and height
def get_terminal_size():
    current_os = platform.system()
    tuple_xy = None

    if current_os == 'Windows':
        tuple_xy = _get_terminal_size_windows()

        if tuple_xy is None:
            tuple_xy = _get_terminal_size_tput()

    if current_os in ['Linux', 'Darwin'] or current_os.startswith('CYGWIN'):
        tuple_xy = _get_terminal_size_linux()

    if tuple_xy is None:
        tuple_xy = (80, 25)
    return tuple_xy
 
 
def _get_terminal_size_windows():

    try:
        from ctypes import windll, create_string_buffer
        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
        if res:
            (bufx, bufy, curx, cury, wattr,
             left, top, right, bottom,
             maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
            return sizex, sizey
    except:
        pass
 

def _get_terminal_size_tput():

    try:
        cols = int(subprocess.check_call(shlex.split('tput cols')))
        rows = int(subprocess.check_call(shlex.split('tput lines')))
        return (cols, rows)
    except:
        pass
 
 
def _get_terminal_size_linux():

    def ioctl_GWINSZ(fd):
        try:
            import fcntl
            import termios
            cr = struct.unpack('hh',
                               fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
            return cr

        except:
            pass

    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)

    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)

        except:
            pass

    if not cr:
        try:
            cr = (os.environ['LINES'], os.environ['COLUMNS'])

        except:
            return None

    return int(cr[1]), int(cr[0])

def det_size():
    if __name__ == "__main__":
        sizex, sizey = get_terminal_size()

        return [sizex, sizey]
# /Determine console width and height

# Define variables
def variables():
    # f - stands for figure
    global f0 
    global f1
    global f2
    global f3
    global f4
    global f5
    global f6
    global f7
    global f8
    global f9

    # dots between figures
    global dots

    # variables for converted figures into art
    global h1
    global h2
    global m1
    global m2
    global s1
    global s2

    global size

    #figures themselves
    f0 = '  ___   \n / _ \\  \n| | | | \n| | | | \n| |_| | \n \\___/  '
    f1 = ' __  \n/_ | \n | | \n | | \n | | \n |_| '
    f2 = ' ___   \n|__ \\  \n   ) | \n  / /  \n / /_  \n|____| '
    f3 = ' ____   \n|___ \\  \n  __) | \n |__ <  \n ___) | \n|____/  '
    f4 = ' _  _    \n| || |   \n| || |_  \n|__   _| \n   | |   \n   |_|   '
    f5 = ' _____  \n| ____| \n| |__   \n|___ \\  \n ___) | \n|____/  '
    f6 = "   __   \n  / /   \n / /_   \n| '_ \\  \n| (_) | \n \\___/  "
    f7 = ' ______  \n|____  | \n    / /  \n   / /   \n  / /    \n /_/     '
    f8 = '  ___   \n / _ \\  \n| (_) | \n > _ <  \n| (_) | \n \\___/  '
    f9 = '  ___   \n / _ \\  \n| (_) | \n \\__, | \n   / /  \n  /_/   '
    dots = '   \n _ \n(_)\n   \n _ \n(_)'
# /Define variables

# Function for screen cleaning
def clearscreen(numlines=11):
    current_os = platform.system()
    if current_os == 'Windows':
        os.system('CLS')
    if current_os in ['Linux', 'Darwin'] or current_os.startswith('CYGWIN'):
        os.system('clear')
# /Function for screen cleaning

# Returns an art figure from a given figure
def return_number(number):
    if number == '0':
        return f0
    if number == '1':
        return f1
    if number == '2':
        return f2
    if number == '3':
        return f3
    if number == '4':
        return f4
    if number == '5':
        return f5
    if number == '6':
        return f6
    if number == '7':
        return f7
    if number == '8':
        return f8
    if number == '9':
        return f9
# /Returns an art figure from a given figure

# Converts local time to figures
def def_time():
    global h1
    global h2
    global m1
    global m2
    global s1
    global s2
    global current_time

    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec
    
    hour = str(hour)
    if len(hour) < 2:
        hour = '0' + hour
        
    minute = str(minute)
    if len(minute) < 2:
        minute = '0' + minute
        
    second = str(second)
    if len(second) < 2:
        second = '0' + second
    
    h1 = return_number(hour[0])
    h2 = return_number(hour[1])
    m1 = return_number(minute[0])
    m2 = return_number(minute[1])
    s1 = return_number(second[0])
    s2 = return_number(second[1])
# /Converts local time to figures

# Stuck art figures and print them line by line
def render():
    
    def_time()
    
    # s - stands for a list
    h1s = h1.split('\n')
    h2s = h2.split('\n')
    m1s = m1.split('\n')
    m2s = m2.split('\n')
    s1s = s1.split('\n')
    s2s = s2.split('\n')
    sdots = dots.split('\n')
    
    down = int(size[1])
    down = (down - 6) / 2
    down = round(down)
    down = int(down) - 1
    for i in range(down):
        print('')

    # i - stands for a line number, starting from 0
    # l stands for a line
    i = 0
    l1 = h1s[i] + h2s[i] + sdots[i] + m1s[i] + m2s[i] + sdots[i] + s1s[i] + s2s[i]
    i = 1
    l2 = h1s[i] + h2s[i] + sdots[i] + m1s[i] + m2s[i] + sdots[i] + s1s[i] + s2s[i]
    i = 2
    l3 = h1s[i] + h2s[i] + sdots[i] + m1s[i] + m2s[i] + sdots[i] + s1s[i] + s2s[i]
    i = 3
    l4 = h1s[i] + h2s[i] + sdots[i] + m1s[i] + m2s[i] + sdots[i] + s1s[i] + s2s[i]
    i = 4
    l5 = h1s[i] + h2s[i] + sdots[i] + m1s[i] + m2s[i] + sdots[i] + s1s[i] + s2s[i]
    i = 5
    l6 = h1s[i] + h2s[i] + sdots[i] + m1s[i] + m2s[i] + sdots[i] + s1s[i] + s2s[i]

    space = []
    space.append(len(l1))
    space.append(len(l2))
    space.append(len(l3))
    space.append(len(l4))
    space.append(len(l5))
    space.append(len(l6))
    space = max(space)
    space = int(size[0]) - space
    space = space / 2
    space = round(space)
    space = int(space)

    i = 0
    l1 = ' ' * space + h1s[i] + h2s[i] + sdots[i] + m1s[i] + m2s[i] + sdots[i] + s1s[i] + s2s[i]
    i = 1
    l2 = ' ' * space + h1s[i] + h2s[i] + sdots[i] + m1s[i] + m2s[i] + sdots[i] + s1s[i] + s2s[i]
    i = 2
    l3 = ' ' * space + h1s[i] + h2s[i] + sdots[i] + m1s[i] + m2s[i] + sdots[i] + s1s[i] + s2s[i]
    i = 3
    l4 = ' ' * space + h1s[i] + h2s[i] + sdots[i] + m1s[i] + m2s[i] + sdots[i] + s1s[i] + s2s[i]
    i = 4
    l5 = ' ' * space + h1s[i] + h2s[i] + sdots[i] + m1s[i] + m2s[i] + sdots[i] + s1s[i] + s2s[i]
    i = 5
    l6 = ' ' * space + h1s[i] + h2s[i] + sdots[i] + m1s[i] + m2s[i] + sdots[i] + s1s[i] + s2s[i]

    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
# /Stuck art figures and print them line by line

# Start up a second iteration (output)
def start():
    global size
    size = det_size()
    render()
    time.sleep(1)
    clearscreen()
# /Start up a second iteration (output)

variables()

# Loop iterations
while True:
    start()
# /Loop iterations

# /End
