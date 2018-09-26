# "Stopwatch: The Game" by Augie

import simplegui

# define global variables

n = 0    # time; updated
interval = 100 # defines the 'speed' of the timer (100 ms = 0.1 sec = 1 tsec) 
total = 0     # updated when 'stop' button pressed as defined in "def start():"
got_it = 0    # same as above
stop = True   # Boolean variable 
hint = ""   # updated by "def hanna():" function

# define helper function format that converts time 
# in tenths of seconds into formatted string A:BC.D
def format(n):
    min = n//600  
    sec = n % 600/10
    tsec = (n % 600) % 10
    if sec > 9:
        return str(min) + ":" + str(sec) + "." + str(tsec) # returns formatted time as string
    else:
        return str(min) + ":" + "0" + str(sec) + "." + str(tsec) # returns formatted time as string
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global stop
    stop = False       
    timer.start()

def stop():
    global stop, n, total, got_it
    
    # Ensures that pressing 'Stop' updates score only when stopwatch is running.
    if stop == False:      # if stop is False, the stopwatch is ticking.         
        if n % 10 == 0:            
            got_it += 1
            total += 1
        else:
            total += 1
    timer.stop()
    stop = True
    
def reset():
    global stop, n, total, got_it, hint
    n = 0
    total = 0
    got_it = 0
    stop = True
    timer.stop()
    hint = ""            # deletes 'hint' from 'hanna'

def hanna():
    global hint
    hint = "Daddy loves you!"
    
# define event handler for timer with 0.1 sec interval (defined as global variable)
# it updates the global variable n (time) every 100 ms (as specified by the interval)
def tick():
    global n
    n += 1
    
# define draw handler
def draw(canvas):
    # links to and calls (i.e. prints) the helper function 'format(n)'; start coordinates, font, color
    canvas.draw_text(format(n), [105, 110], 42, "White")
    frame.set_canvas_background("Brown")
    # links to and prints global variables 'total' and 'got_it', as updated by "def stop():" 
    canvas.draw_text(str(got_it) + "/" + str(total), [250, 30], 24, "Yellow")
    # links to and prints global variable 'hint', as updated by "def hanna():"
    canvas.draw_text(hint, [68, 180], 24, "Red")
    
# create frame
frame = simplegui.create_frame("Stopwatch Game", 300, 200)


# Register event handlers. Create buttons and timer. 
frame.set_draw_handler(draw) # Modifies the canvas. Only one draw_handler needed.
# creates button and links it to button event handler 'def start()'
frame.add_button("Start", start, 100) 
# same as above
frame.add_button("Stop", stop, 100)
# same as above
frame.add_button("Reset", reset, 100)
# creates the button and links to event handler 'def hanna()"
frame.add_button("For Hanna", hanna, 100) 
# timer interval (in ms) is defined as global variable. Links to event handler 'def tick()'.
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()
# timer.start() # if enabled the timer starts automatically rather than activated by 'start' button
