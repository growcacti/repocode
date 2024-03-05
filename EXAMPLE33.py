
# not saved
''' code here manages copyright notice '''
# not saved
authors = "David B. Sher"
# not saved
thanks = "John Zelle"
# not saved
year = "2020"

# not saved
NO_SAVE = '''
# not saved'''


# not saved
save_file = __file__

import tkinter as tk
import sys, io, os
import subprocess as subp
import re
from datetime import datetime
from tkinter import filedialog
from os import getcwd,system
from keyword import iskeyword
from math import sqrt


from contextlib import redirect_stdout
# begin shell not in app
# redirect stderr and stdout to strings
GUI_DEBUG=False  # can turn on and off debugging by changing this

def debug_print(to_print,end=''):
  ''' calls a print statement and puts it into the shell window '''
  global shell
  global GUI_DEBUG
  if GUI_DEBUG:
    shell.insert(tk.END,to_print+end,'debug')
    shell.tag_configure('debug',foreground='blue',font=('Consolas', 12, 'italic'))
    shell.mark_set(tk.INSERT, tk.END) # make sure the input cursor is at the end
    shell.cursor = shell.index(tk.INSERT) # save the input position
# end shell not in app

# begin shell not in app
say_number = 0    # makes all the tags different
def say(to_print,color='#884400',font=('serif',12),end='\n'):
  global say_number
  ''' allows programs to communicate with shell, don't use with stand alone apps '''
  global shell
  shell.insert(tk.END,to_print+end,'say{}'.format(say_number))
  shell.tag_configure('say{}'.format(say_number),foreground=color,font=font)
  say_number += 1 # will not change formating of other things said
  shell.see(tk.END) # make sure it is visible
  shell.mark_set(tk.INSERT, tk.END) # make sure the input cursor is at the end
  shell.cursor = shell.index(tk.INSERT) # save the input position

def ask(to_print,color='darkgreen',font=('serif',12),end=': '):
  ''' asks user a question and returns response '''
  global shell
  shell.set_asking(True) # make sure the shell doesn't execute user input
  say(to_print,color,font,end)
  shell.wait_variable(shell.cmd)
  shell.set_asking(False) # the shell can execute user input again
  return shell.cmd.get()
  
  
''' This is the code for the shell widget in python '''
class Shell(tk.Text):
  def __init__(self, parent, **kwargs):
    tk.Text.__init__(self, parent, **kwargs)
    self.bind('<Key>', self.on_key) # setup handler to process pressed keys
    self.cmd = tk.StringVar()        # hold the last command issued
    self.set_asking(False)          # execute user input
    self.show_prompt()

  def insert_text(self, txt='', end='\n'):
    ''' Appends the given text to the end of the Text Box. '''
    self.insert(tk.END, txt+end)
    self.see(tk.END) # make sure it is visible

  def insert_error(self, txt='', end='\n'):
    ''' Appends an error message to the end of the Text Box.  '''
    self.insert(tk.END, txt+end,'error')
    self.see(tk.END) # make sure it is visible
    shell.tag_configure('error',foreground='red',font=('Consolas', 12, 'bold'))

  def set_asking(self,asks):
    ''' When true doesn't execute user input '''
    self.asking = asks

  def get_asking(self):
    return self.asking

  def show_prompt(self):
    ''' Prompts for a command. '''
    self.insert_text('>> ', end='')
    self.mark_set(tk.INSERT, tk.END) # make sure the input cursor is at the end
    self.cursor = self.index(tk.INSERT) # save the input position

  # handler to process keyboard input
  def on_key(self, event):
    #print(event)
    if event.keysym == 'Up':
      # show the last command
      self.delete(self.cursor, tk.END)
      self.insert(self.cursor, self.cmd)
      return "break" # disable the default handling of up key
    if event.keysym == 'Down':
      return "break" # disable the default handling of down key
    if event.keysym in ('Left', 'BackSpace'):
      current = self.index(tk.INSERT) # get the current position of the input cursor
      if self.compare(current, '==', self.cursor):
        # if input cursor is at the beginning of input (after the prompt), do nothing
        return "break"
    if event.keysym == 'Return':
      # extract the command input
      cmd = self.get(self.cursor, tk.END).strip()
      self.insert_text() # advance to next line
      if cmd.startswith('`'):
        # it is an external command
        self.system(cmd)
      else:
        # it is python statement
        self.execute(cmd)
      self.show_prompt()
      return "break" # disable the default handling of Enter key
    if event.keysym == 'Escape':
      self.master.destroy() # quit the shell

  def execute(self, cmd):
    ''' execute input from user '''
    exec_result = io.StringIO()
    exec_error = io.StringIO()
    sys.stdout = exec_result
    sys.stderr = exec_error
    self.cmd.set(cmd) # save the command
    if not self.get_asking():  # don't execute user input when ask
      # capture the result and error from exec to shell
      try:
        exec(self.cmd.get(), globals())
      except: # catch all exceptions
        print(sys.exc_info(),file=sys.stderr)
      # then append the output of exec() in the Text box
      self.insert_text(exec_result.getvalue(), end='')
      self.insert_error(exec_error.getvalue(), end='')

  def system(self, cmd):
    ''' execute a command '''
    self.cmd.set(cmd)  # save the command
    if not self.get_asking():
      try:
        # extract the actual command
        cmd = cmd[cmd.index('`')+1:cmd.rindex('`')]
        proc = subp.Popen(cmd, stdout=subp.PIPE, stderr=subp.PIPE, text=True)
        stdout, stderr = proc.communicate(5) # get the command output
        # append the command output to Text box
        self.insert_text(stdout)
      except: # catch all exceptions
        self.insert_error(stderr)

''' This is the code for the clicks widget in python (text window with autoindent '''
class IndentText(tk.Text):
  def __init__(self, parent, **kwargs):
    tk.Text.__init__(self, parent, **kwargs)
    self.bind('<Key>', self.on_key) # setup handler to process pressed keys

  def insert_text(self, txt='', end='\n'):
    ''' Appends the given text to the end of the Text Box. '''
    self.insert(tk.END, txt+end)
    self.see(tk.END) # make sure it is visible

  # handler to process keyboard input
  def on_key(self, event):
    debug_print('In on_key: '+str(event),end='\n')
    if event.char == '\r':
      debug_print('Hit return',end='\n')
      debug_print('Cursor: '+tk.INSERT,end='\n')
      # extract the command input
      line = self.get('current linestart', 'current lineend')
      after = self.get('insert','current lineend')
      self.delete('insert','current lineend') # delete the characters to be moved to the end of the line
      debug_print('Indent_text line: '+line+'\nAfter: '+after,end='\n')
      self.add_indent(line,after)
      return "break" # disable the default handling of Enter key

  def add_indent(self,line,after):
    ''' Auto Indents Line '''
    debug_print('AutoIndent line: '+line,end='\n')
    spaces = re.match(r"^(\s*).*$", line)
    debug_print('Inserting: "'+spaces.group(1)+after,end='"\n')
    self.insert(tk.INSERT,'\n'+spaces.group(1)+after)
    self.mark_set('insert','insert -'+str(len(after))+' chars')
    self.see('insert')

# end shell not in app
''' this sets up the window with
  * header (with project file)
  * graphics
  * python shell
  * copyright notice
'''
root = tk.Tk()
root.title('Project in '+__file__)
root.configure(bg='darkblue')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# position for each frame
row_number = 0


# GUIframe holds clickable stuff
GUIframe = tk.Frame(root)
GUIframe.grid(row=row_number)
row_number+=1  # next row
GUIframe.columnconfigure(0,weight=1)
GUIframe.rowconfigure(0,weight=1)
# top frame will hold graphics window
top = tk.Frame(GUIframe)
top.pack(side=tk.LEFT)
top.columnconfigure(0, weight=1)
top.rowconfigure(0, weight=1)

# begin shell not in app
# buttons frame holds control buttons
buttons = tk.Frame(GUIframe)
buttons.pack(side=tk.RIGHT)


# click_toggle will switch between the python shell and the clicks editor
click_toggle = tk.Button(buttons,
                        width = 6,
                        text='Edit\nClicks',
                        bg = 'lightgreen',
                        fg = 'black',
                        font = 'courier',
                        justify = 'cent')
click_toggle.pack()

# make_app_button will call make_app to create an app from the code
make_app_button = tk.Button(buttons,
                        width = 4,
                        text='Make\nApp',
                        bg = 'lightgreen',
                        fg = 'black',
                        font = 'courier',
                        justify = 'cent')
make_app_button.pack()

# names_ button will output to the shell all the names of the graphics and GUI objects
names_button = tk.Button(buttons,
                        width = 5,
                        text = 'Names',
                        bg = 'lightgreen',
                        fg = 'black',
                        font = 'courier',
                        justify = 'cent')
names_button.pack()

                         
# end shell not in app

# bottom frame will hold shell
bottom = tk.Frame(root)
bottom.grid(row=row_number)
row_number+=1  # next row
bottom.columnconfigure(0, weight=1)
bottom.rowconfigure(0, weight=1)

# copy_frame will hold copyright information
copy_frame = tk.Frame(root,height=16)
copy_frame.grid(row=row_number)
row_number+=1  # next row
copy_frame.columnconfigure(0, weight=1)
copy_frame.rowconfigure(0, weight=1)

# begin shell not in app
''' create scrollbars for shell '''
# Vertical (y) Scroll Bar
shell_scroll = tk.Scrollbar(bottom)
shell_scroll.pack(side=tk.RIGHT, fill=tk.Y)
shell_hscroll = tk.Scrollbar(bottom, orient=tk.HORIZONTAL)
shell_hscroll.pack(side=tk.BOTTOM, fill=tk.X)
''' put shell window into bottom frame '''
shell = Shell(bottom,wrap=tk.NONE, yscrollcommand=shell_scroll.set, xscrollcommand=shell_hscroll.set, width=80, height=16,  font=('Consolas', 12))
shell.pack(fill=tk.BOTH, expand = tk.YES, side="left")
shell.focus_set()
shell.columnconfigure(0, weight=1)
shell.rowconfigure(0, weight=1)
# Configure the scrollbars
shell_scroll.config(command=shell.yview)
shell_hscroll.config(command=shell.xview)

# clicks window
clicks_window = IndentText(bottom,wrap=tk.NONE, yscrollcommand=shell_scroll.set, xscrollcommand=shell_hscroll.set, width=80, height=16,  font=('Lucida Console', 12))


# end shell not in app


def my_exec(cmd, globals=None, locals=None, description='source string'):
    ''' executes a string (like from my_clicks and reports where errors occured in shell '''
    try:
        exec(cmd, globals, locals)
    except SyntaxError as err:
        error_class = err.__class__.__name__
        detail = err.args[0]
        line_number = err.lineno
    except (NameError, AttributeError) as err: 
        error_class = err.__class__.__name__
        detail = err.args[0]
        line_number = err.lineno
    except Exception as err:
        error_class = err.__class__.__name__
        detail = err.args[0]
        cl, exc, tb = sys.exc_info()
        line_number = traceback.extract_tb(tb)[-1][1]
    else:
        return
    say("%s at line %d of %s: %s" % (error_class, line_number, description, detail),color='red')


''' define a canvas that captures mouse events '''
GRAPHICS_WIDTH = 600
GRAPHICS_HEIGHT = 300
class MouseCanvas(tk.Canvas):
  def __init__(self,parent=top,bg='snow',width=GRAPHICS_WIDTH,height=GRAPHICS_HEIGHT):
    tk.Canvas.__init__(self,parent,bg=bg,width=width,height=height)
    self.click_point = tk.StringVar()
    self.click_point.set('Point(0,0)')  # start with 0,0 clicked
    self.bind('<Button-1>', self.mouse_click)
    self.bind('<Motion>', self.mouse_move)
    self.tracking = False # when tracking draws gray horizontal and vertical lines for mouse

  def mouse_click(self,event):
    ''' puts the last clicked mouse position into the variable mouse_click_position '''
    self.click_point.set('Point('+str(event.x)+','+str(event.y)+')')
    self.mouse_point = Point(event.x,event.y)

  def get_mouse_click(self):
    ''' waits for a mouse click and returns the point '''
    debug_print('Waiting for click',end='\n')
    self.wait_variable(self.click_point)
    debug_print('Clicked',end='\n')
    return self.mouse_point

  def toggle_tracking(self):
    if self.tracking:
      # delete tracking lines
      self.delete(self.vertical)
      self.delete(self.horizontal)
      self.tracking = False
    else:
      # put down initial tracking lines and draw them
      self.vertical = self.create_line(0,0,0,GRAPHICS_HEIGHT,fill='lightgray')
      self.horizontal = self.create_line(0,0,GRAPHICS_WIDTH,0,fill='lightgray')
      self.tracking = True
      

  def mouse_move(self,event):
    if self.tracking:
      # delete old tracking lines
      self.delete(self.vertical)
      self.delete(self.horizontal)
      # draw new tracking lines
      self.vertical = self.create_line(event.x,0,event.x,GRAPHICS_HEIGHT,fill='lightgray')
      self.horizontal = self.create_line(0,event.y,GRAPHICS_WIDTH,event.y,fill='lightgray')
      
    
  

''' put graphics canvas in top frame '''
graphics = MouseCanvas()
graphics.pack(fill=tk.BOTH, expand = 1)


copyright_string = tk.StringVar()
copyright_string.set('Copyright {} {} with thanks to {}'.format(authors,year,thanks))
copyright_label = tk.Label(copy_frame,textvariable=copyright_string)
copyright_label.pack()

''' adds an author to the copyright statement '''
def add_author(auth):
  global authors
  authors += ' and ' + auth
  copyright_string.set('Copyright {} {} with thanks to {}'.format(authors,year,thanks))
  save_gui4sher()

''' sets the copyright year to the present year '''
def update_year():
  global year
  year = str(datetime.now().year)
  copyright_string.set('Copyright {} {} with thanks to {}'.format(authors,year,thanks))
  save_gui4sher()

''' adds an author to the copyright statement '''
def add_thanks(thank):
  global thanks
  thanks += ' and ' + thank
  copyright_string.set('Copyright {} {} with thanks to {}'.format(authors,year,thanks))
  save_gui4sher()

''' Copyright David B. Sher 2020 '''

''' code here manages objects in the graphics window '''
objects = [] # no objects initially
##########################################################################
# Module Exceptions

class GraphicsError(Exception):
    """Generic error class for graphics module exceptions."""
    pass

OBJ_ALREADY_DRAWN = "Object currently drawn"
UNSUPPORTED_METHOD = "Object doesn't support operation"
BAD_OPTION = "Illegal option value"


object_number = 0; # used to number objects

class GraphicsObject:

    """Generic base class for all of the drawable objects"""
    # A subclass of GraphicsObject should override _draw and
    #   and _move methods.
    
    def __init__(self, fill='',outline='black',width='1'):
        global object_number
        # options is a list of strings indicating which options are
        # legal for this object.
        
        # When an object is drawn, canvas is set to the GraphWin(canvas)
        #    object where it is drawn and id is the TK identifier of the
        #    drawn shape.
        self.canvas = None
        self.id = None

        # config is the dictionary of configuration options for the widget.
        self.name = 'object'+str(object_number)
        object_number+=1 # each object starts with a unique name
        self.set_fill(fill)
        self.set_outline(outline)
        self.set_width(width)
        

    def set_name(self, name):
        """Set name of object to name"""
        self.name = name
        if self.id:
            save_gui4sher() # update the save file
            root.update()

    def get_name(self):
      return self.name
        
    def set_fill(self, color):
        """Set interior color to color"""
        self.fill = color
        if self.id:
          self.canvas.itemconfig(self.id,fill=self.get_fill())
          save_gui4sher() # update the save file
          root.update()

    def get_fill(self):
      return self.fill
        
    def set_outline(self, color):
        """Set outline color to color"""
        self.outline = color
        if self.id:
          self.canvas.itemconfig(self.id,outline=self.get_outline())
          save_gui4sher() # update the save file
          root.update()

    def get_outline(self):
      return self.outline
        
    def set_width(self, width):
        """Set line weight to width"""
        self.width = width
        if self.id:
          self.canvas.itemconfig(self.id,width=self.get_width())
          save_gui4sher() # update the save file
          root.update()

    def get_width(self):
      return self.width

    def draw(self):

        """Draw the object in graphics, which should be a Canvas
        object.  A GraphicsObject may only be drawn into one
        window. Raises an error if attempt made to draw an object that
        is already visible."""

        global objects
        self.canvas = graphics
        self.id = self._draw(graphics)
        # add colors, fonts etc to drawn object
        # if the objects lacks one of these ignore
        try: self.set_fill(self.get_fill())
        except (NameError, AttributeError): None
        try:  self.set_outline(self.get_outline())
        except (NameError, AttributeError): None
        try:  self.set_width(self.get_width())
        except (NameError, AttributeError): None
        try:  self.set_arrow(self.get_arrow())
        except (NameError, AttributeError): None
        try:  self.set_font(self.get_font())
        except (NameError, AttributeError): None
        try:  self.set_justify(self.get_justify())
        except (NameError, AttributeError): None
        objects.append(self)
        save_gui4sher() # update the save file
        root.update()
        return self

            
    def undraw(self):

        """Undraw the object (i.e. hide it). Returns silently if the
        object is not currently drawn."""
        
        global objects
        if self.canvas: # if object has been drawn
          self.canvas.delete(self.id)
          self.canvas = None
          self.id = None
          objects.remove(self)
          save_gui4sher() # update the save file


    def move(self, dx, dy):

        """move object dx units in x direction and dy units in y
        direction"""
        
        self._move(dx,dy)
        if self.canvas: # if object has been drawn
            x = dx
            y = dy
            self.canvas.move(self.id, x, y)
            root.update()
            save_gui4sher() # update the save file
           


    def _draw(self, canvas):
        """draws appropriate figure on canvas with options provided
        Returns Tk id of item drawn"""
        pass # must override in subclass


    def _move(self, dx, dy):
        """updates internal state of object to move it dx,dy units"""
        pass # must override in subclass

    def _to_exec(self):
      """ create statements that initialize and object and draw it """
      exec_lines = [ self.name+ ' = ' + self.__class__.__name__ +'({})', # parameters of object will be done with a .format
                     self.name + '.set_name(\'' + self.get_name() + '\')',
                     self.name + '.set_fill(\''+ self.get_fill() + '\')',
                     self.name + ".set_outline('"+ self.get_outline() + "')",
                     self.name + ".set_width('"+ str(self.get_width())+ "')",
                     self.name + '.draw()']
      return '''
'''.join(exec_lines)
      

         
class Point(GraphicsObject):
    def __init__(self, x, y):
        GraphicsObject.__init__(self)
        self.set_fill = self.set_outline
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)
        
    def _draw(self, canvas):
        return canvas.create_rectangle(self.x-2,self.y-1,self.x+2,self.y+2,fill=self.get_fill())
        
    def _move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        
    def clone(self):
        other = Point(self.x,self.y)
        other.set_name(self.name)
        other.outline = self.outline
        return other
                
    def get_x(self): return self.x
    def get_y(self): return self.y
    def to_exec(): return super()._to_exec.format('' + self.x + ',' + self.y)

class _BBox(GraphicsObject):
    # Internal base class for objects represented by bounding box
    # (opposite corners) Line segment is a degenerate case.
    
    def __init__(self, p1, p2):
        GraphicsObject.__init__(self)
        self.p1 = p1.clone()
        self.p2 = p2.clone()

    def _move(self, dx, dy):
        self.p1.x = self.p1.x + dx
        self.p1.y = self.p1.y + dy
        self.p2.x = self.p2.x + dx
        self.p2.y = self.p2.y  + dy
                
    def get_p1(self): return self.p1.clone()

    def get_p2(self): return self.p2.clone()
    
    def get_center(self):
        p1 = self.p1
        p2 = self.p2
        return Point((p1.x+p2.x)/2.0, (p1.y+p2.y)/2.0)

    
class Rectangle(_BBox):
    
    def __init__(self, p1, p2):
        _BBox.__init__(self, p1, p2)

    def __repr__(self):
        return "Rectangle({}, {})".format(str(self.p1), str(self.p2))
    
    def _draw(self, canvas):
        p1 = self.p1
        p2 = self.p2
        try:
          return canvas.create_rectangle(p1.x,p1.y,p2.x,p2.y,outline=self.get_outline(),fill=self.get_fill(),width=self.get_width())
        except Exception as e:
          say(str(e),color='red') # tell user about problem drawing
          return None
        
    def clone(self):
        other = Rectangle(self.p1, self.p2)
        other.set_name(self.name)
        other.set_fill(self.fill)
        other.set_outline(self.outline)
        other.set_width(self.width)
        return other
    
    def to_exec(self):
      ''' creates commands to create the rectangle '''
      return super()._to_exec().format('Point('+str(self.p1.x)+','+str(self.p1.y)+'),Point('+str(self.p2.x)+','+str(self.p2.y)+')')


class Oval(_BBox):
    
    def __init__(self, p1, p2):
        _BBox.__init__(self, p1, p2)

    def __repr__(self):
        return "Oval({}, {})".format(str(self.p1), str(self.p2))

        
    def clone(self):
        other = Oval(self.p1, self.p2)
        other.set_name(self.name)
        other.set_fill(self.fill)
        other.set_outline(self.outline)
        other.set_width(self.width)
        return other
   
    def _draw(self, canvas):
        p1 = self.p1
        p2 = self.p2
        try:
          return canvas.create_oval(p1.x,p1.y,p2.x,p2.y,outline=self.get_outline(),fill=self.get_fill(),width=self.get_width())
        except Exception as e:
          say(str(e),color='red') # tell user about problem drawing
          return None

    def to_exec(self):
      ''' creates commands to create the oval '''
      return super()._to_exec().format('Point('+str(self.p1.x)+','+str(self.p1.y)+'),Point('+str(self.p2.x)+','+str(self.p2.y)+')')
    
class Circle(Oval):
    
    def __init__(self, center, radius):
        p1 = Point(center.x-radius, center.y-radius)
        p2 = Point(center.x+radius, center.y+radius)
        Oval.__init__(self, p1, p2)
        self.radius = radius

    def __repr__(self):
        return "Circle({}, {})".format(str(self.get_center()), str(self.radius))
        
    def clone(self):
        other = Circle(self.get_center(), self.radius)
        other.set_name(self.get_name())
        other.set_fill(self.get_fill())
        other.set_outline(self.get_outline())
        other.set_width(self.get_width())
        return other
        
    def get_radius(self):
        return self.radius

    def to_exec(self):
      ''' creates commands to create the circle '''
      return super()._to_exec().format('Point('+str(self.get_center().x)+','+str(self.get_center().y)+'),'+str(self.radius))

                  
class Line(_BBox):
    
    def __init__(self, p1, p2):
        _BBox.__init__(self, p1, p2)
        self.set_arrow('none')
   
    def __repr__(self):
        return "Line({}, {})".format(str(self.p1), str(self.p2))

    def clone(self):
        other = Line(self.p1, self.p2)
        other.set_name(self.get_name())
        other.set_outline(self.get_outline())
        other.set_width(self.get_width())
        other.set_dash(self.get_dash())
        return other

    def set_arrow(self,arrow):
      self.arrow = arrow
      if self.id:
          self.canvas.itemconfig(self.id,arrow=self.get_arrow())
          save_gui4sher() # update the save file
          root.update()

    def get_arrow(self):
      return self.arrow

  
    def _draw(self, canvas):
        p1 = self.p1
        p2 = self.p2
        try:
          return canvas.create_line(p1.x,p1.y,p2.x,p2.y,fill=self.get_outline(),width=self.get_width(),arrow=self.get_arrow())
        except Exception as e:
          say(str(e),color='red') # tell user about problem drawing
          return None

    def set_outline(self, color):
        """Set line color to color"""
        self.outline = color
        if self.id:
          self.canvas.itemconfig(self.id,fill=self.get_outline())
          save_gui4sher() # update the save file
          root.update()
        
   
    def to_exec(self):
      ''' creates commands to create the line '''
      exec_lines = [ self.name+ ' = ' + self.__class__.__name__ +'(Point('+str(self.p1.x)+','+str(self.p1.y)+'),Point('+str(self.p2.x)+','+str(self.p2.y)+'))',
                     self.name + '.set_name(\'' + self.name + '\')',
                     self.name + '.set_fill(\''+ self.get_fill() + '\')',
                     self.name + ".set_outline('"+ self.get_outline() + "')",
                     self.name + ".set_width('"+ str(self.get_width())+ "')",
                     self.name + ".set_arrow('"+ self.get_arrow() + "')",
                     self.name + '.draw()']
      return '''
'''.join(exec_lines)
class Dashed_Line(_BBox):
    
    def __init__(self, p1, p2):
        _BBox.__init__(self, p1, p2)
        self.set_dash((5,5))
        self.set_arrow('none')
   
    def __repr__(self):
        return "Dashed_Line({}, {})".format(str(self.p1), str(self.p2))

    def clone(self):
        other = Line(self.p1, self.p2)
        other.set_name(self.get_name())
        other.set_outline(self.get_outline())
        other.set_width(self.get_width())
        other.set_dash(self.get_dash())
        return other
  
    def set_arrow(self,arrow):
      self.arrow = arrow
      if self.id:
          self.canvas.itemconfig(self.id,arrow=self.get_arrow())
          save_gui4sher() # update the save file
          root.update()

    def get_arrow(self):
      return self.arrow

    def _draw(self, canvas):
        p1 = self.p1
        p2 = self.p2
        try:
          return canvas.create_line(p1.x,p1.y,p2.x,p2.y,fill=self.get_outline(),dash=self.get_dash(),width=self.get_width(),arrow=self.get_arrow())
        except Exception as e:
          say(str(e),color='red') # tell user about problem drawing
          return None


    def set_dash(self,dash):
      self.dash = dash
      if self.id:
        self.canvas.itemconfig(self.id,dash=self.get_dash())

    def get_dash(self):
      return self.dash

    def set_outline(self, color):
        """Set line color to color"""
        self.outline = color
        if self.id:
          self.canvas.itemconfig(self.id,fill=self.get_outline())
          save_gui4sher() # update the save file
          root.update()
        
   
    def to_exec(self):
      ''' creates commands to create the line '''
      exec_lines = [ self.name+ ' = ' + self.__class__.__name__ +'(Point('+str(self.p1.x)+','+str(self.p1.y)+'),Point('+str(self.p2.x)+','+str(self.p2.y)+'))',
                     self.name + '.set_name(\'' + self.name + '\')',
                     self.name + '.set_fill(\''+ self.get_fill() + '\')',
                     self.name + ".set_outline('"+ self.get_outline() + "')",
                     self.name + ".set_width('"+ str(self.get_width())+ "')",
                     self.name + ".set_arrow('"+ self.get_arrow() + "')",
                     self.name + ".set_dash("+ str(self.get_dash()) + ")",
                     self.name + '.draw()']
      return '''
'''.join(exec_lines)


class Polygon(GraphicsObject):
    
    def __init__(self, *points):
        # if points passed as a list, extract it
        if len(points) == 1 and type(points[0]) == type([]):
            points = points[0]
        self.points = list(map(Point.clone, points))
        GraphicsObject.__init__(self)

    def __repr__(self):
        return "Polygon"+str(tuple(p for p in self.points))
        
    def clone(self):
        other = Polygon(*self.points)
        other.set_name(self.name)
        other.set_name(self.name)
        other.set_fill(self.fill)
        other.set_outline(self.outline)
        other.set_width(self.width)
        return other

    def get_points(self):
        return list(map(Point.clone, self.points))

    def _move(self, dx, dy):
        for p in self.points:
            p.move(dx,dy)
   
    def _draw(self, canvas):
        args = []
        for p in self.points:
            args.append(p.x)
            args.append(p.y)
        try:
          return graphics.create_polygon(*args,outline=self.get_outline(),fill=self.get_fill(),width=self.get_width()) 
        except Exception as e:
          say(str(e),color='red') # tell user about problem drawing
          return None


    def to_exec(self):
      ''' creates commands to create the polygon '''
      arguments =""  # make a list of the points
      for point in self.points:
        arguments += 'Point('+str(point.x)+','+str(point.y)+'),'
      return super()._to_exec().format(arguments[:-1])   # :-1 gets rid of last ,

def font_string(font):
  ''' returns the string corresponding to the font '''
  if isinstance(font,str):
    # put quotes around the font if it is represented as a string
    return '"'+font+'"'
  # otherwise just turn it into a string
  return str(font)

class Label(GraphicsObject):
    
    def __init__(self, p, text, name):
        GraphicsObject.__init__(self)
        self.name = name
        self.set_text(text)
        self.set_justify(tk.CENTER)
        self.set_font(('helvetica',12))
        self.set_width(10000)    # too large width works by default
        self.anchor = p.clone()

    def __repr__(self):
        return "Label({}, '{}')".format(self.anchor, self.getText())
    
    def _draw(self, canvas):
        p = self.anchor
        try:
          return canvas.create_text(p.x,p.y,anchor='nw',fill=self.get_outline(),text=self.get_text(),font=self.get_font(), justify=self.get_justify())
        except Exception as e:
          say(str(e),color='red') # tell user about problem drawing
          return None

        
    def _move(self, dx, dy):
        self.anchor.move(dx,dy)
        
    def clone(self):
        other = Text(self.anchor, self.text)
        other.set_name(self.get_name())
        other.set_fill(self.get_fill())
        other.set_outline(self.get_outline())
        other.set_width(self.get_width())
        other.set_font(self.get_font())
        return other

    def set_text(self,text):
      self.text = text
      if self.id:
          self.canvas.itemconfig(self.id,text=self.get_text())
          save_gui4sher() # update the save file
          root.update()


    def get_text(self):
      return self.text

    def set_justify(self,justify):
      self.justify = justify
      if self.id:
          self.canvas.itemconfig(self.id,justify=self.get_justify())
          save_gui4sher() # update the save file
          root.update()

    def get_justify(self):
      return self.justify

    def set_font(self,font):
      self.font = font
      if self.id:
          self.canvas.itemconfig(self.id,font=self.get_font())
          save_gui4sher() # update the save file
          root.update()

    def get_font(self):
      return self.font

            
    def get_anchor(self):
        return self.anchor.clone()

    def set_outline(self, color):
        """Set text color to color"""
        self.outline = color
        if self.id:
          self.canvas.itemconfig(self.id,fill=self.get_outline())
          save_gui4sher() # update the save file
          root.update()

    def to_exec(self):
      ''' creates commands to create the line '''
      exec_lines = [ self.name+ ' = ' + self.__class__.__name__ +'(Point('+str(self.anchor.x)+','+str(self.anchor.y)+'),"'+self.get_text()+'","'+self.get_name()+'")',
                     self.name + '.set_name(\'' + self.name + '\')',
                     self.name + '.set_fill(\''+ self.get_fill() + '\')',
                     self.name + ".set_outline('"+ self.get_outline() + "')",
                     self.name + ".set_width('"+ str(self.get_width())+ "')",
                     self.name + ".set_text('"+ self.get_text()+ "')",
                     self.name + ".set_font(" + font_string(self.get_font()) + ")",
                     self.name + '.draw()']
      return '''
'''.join(exec_lines)


class Entry(GraphicsObject):

    def __init__(self, p, width,name):
        global clicks_window
        GraphicsObject.__init__(self)
        self.name = name
        self.anchor = p.clone()
        #print self.anchor
        self.width = width
        self.text = tk.StringVar()
        self.anchor = p.clone()
        self.set_fill("white")
        self.text.set("")
        self.set_outline("black")
        self.set_font(("courier", 12))
        self.set_justify('left')
        self.frm = tk.Frame(graphics.master)
        self.entry = tk.Entry(self.frm,
                              width=self.width,
                              textvariable=self.text,
                              bg = self.get_fill(),
                              fg = self.get_outline(),
                              font = self.get_font())
        self.entry.bind("<Return>",self.handle_return)
# begin shell not in app
        # put an empty definition for the return handler into the clicks window if no definition is already in the clicks window
        # put an empty definition for the click handler into the clicks window if no definition is already in the clicks window
        clicks = clicks_window.get('1.0','end')
        if clicks.find('def '+self.get_name()+'_return') == -1:
          debug_print('Putting click definition in ')
          debug_print('for '+self.get_name(),end='\n')
          clicks_window.insert('end','\ndef '+self.get_name()+'_return():\n\tpass\n')
        debug_print('Clicks:\n'+clicks_window.get('1.0','end'))
# end shell not in app

    def __repr__(self):
        return "Entry({}, {})".format(self.anchor, self.width)

    def _draw(self, canvas):
        p = self.anchor
        try:
          the_entry = canvas.create_window(p.x,p.y,window=self.frm,anchor='nw')
        except Exception as e:
          say(str(e),color='red') # tell user about problem drawing
          return None
        self.entry.pack()
        self.entry.focus_set()
        return the_entry

    def handle_return(self,event):
      ''' if it exists call the return function from the clicks file '''
      # do a return command if the return function exists
      try:
        try:
          globals()[self.get_name()+'_return']()
        except Exception as e:
          say(str(e),color='red')
      except (NameError, AttributeError): return None # otherwise no return behavior
      except Error as e: say(e,color='red',font=('Consolas', 12, 'bold')) # output error
      except Exception as exp: say(exp,color='red',font=('Consolas', 12, 'bold')) # output Exception


    def get_text(self):
        return self.text.get()

    def _move(self, dx, dy):
        self.anchor.move(dx,dy)

    def get_anchor(self):
        return self.anchor.clone()

    def clone(self):
        other = Entry(self.anchor, self.width)
        other.config = self.config.copy()
        other.set_name(self.name)
        other.text = tk.StringVar()
        other.text.set(self.text.get())
        other.fill = self.fill
        return other

    def set_text(self, t):
        self.text.set(t)
        save_gui4sher() # update the save file
        root.update()

    def set_name(self, name):
        """Set name of enty to name"""
        old_name = self.name
        self.name = name
        # add a click command if one exists
        try: exec('self.command = '+self.get_name()+'_return')
        except (NameError, AttributeError): self.command = None # otherwise no command
        if self.command != None:
          self.button.config(command=self.command)
        if self.id:
            save_gui4sher() # update the save file
            root.update()
# begin shell not in app
       # translate old name to new name in clicks_window
        clicks = clicks_window.get('1.0','end')
        clicks = re.sub(r'(\W)'+old_name+r'(\W)',r'\1'+name+r'\2',clicks) # change the old name to the new name in clicks
        clicks = re.sub(r'(\W)'+old_name+r'_return(\W)',r'\1'+name+r'_return\2',clicks) # change the old name to the new name in clicks
        clicks_window.delete('1.0','end')
        clicks_window.insert('end',clicks)
# end shell not in app
           

            
    def set_justify(self,justify):
      self.justify = justify
      if self.id:
          self.entry.config(justify=self.get_justify())
          save_gui4sher() # update the save file
          root.update()

    def get_justify(self):
      return self.justify

    def set_font(self,font):
      self.font = font
      if self.id:
          self.entry.config(font=self.get_font())
          save_gui4sher() # update the save file
          root.update()

    def get_font(self):
      return self.font

    def set_fill(self, color):
        """Set interior color to color"""
        self.fill = color
        if self.id:
          self.entry.config(bg=self.get_fill())
          save_gui4sher() # update the save file
          root.update()

    def set_outline(self, color):
        """Set outline color to color"""
        self.outline = color
        if self.id:
          self.entry.config(fg=self.get_outline())
          save_gui4sher() # update the save file
          root.update()

    def set_width(self, width):
        """Set line weight to width"""
        self.width = width
        if self.id:
          self.entry.config(width=self.get_width())
          save_gui4sher() # update the save file
          root.update()

    def get_width(self):
      return self.width


    def to_exec(self):
      debug_print('Creating string to execute for Entry')
      ''' creates commands to create the line '''
      exec_lines = [ self.name + ' = ' + self.__class__.__name__ +'(Point('+str(self.anchor.x)+','+str(self.anchor.y)+'),'+str(self.width)+',"'+self.get_name()+'")',
                     self.name + '.set_fill(\''+ self.get_fill() + '\')',
                     self.name + ".set_outline('"+ self.get_outline() + "')",
                     self.name + ".set_width('"+ str(self.get_width())+ "')",
                     self.name + ".set_text('"+ self.text.get()+ "')",
                     self.name + ".set_font(" + font_string(self.get_font()) + ")",
                     self.name + '.set_justify(\''+self.get_justify() + '\')',
                     self.name + '.draw()']
      return '''
'''.join(exec_lines)

class Text(GraphicsObject):

    def __init__(self, p, width, height,name):
        GraphicsObject.__init__(self)
        self.name = name
        self.anchor = p.clone()
        #print self.anchor
        self.width = width
        self.height = height
        self.anchor = p.clone()
        self.set_fill("white")
        self.set_outline("black")
        self.set_font(("courier", 12))
        self.frm = tk.Frame(graphics.master)
        self.scroll = tk.Scrollbar(self.frm)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.box = tk.Text(self.frm,
                              width=self.width,
                              height=self.height,
                              bg = self.get_fill(),
                              fg = self.get_outline(),
                              font = self.get_font(),
                              yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.box.yview)

    def __repr__(self):
        return "Entry({}, {})".format(self.anchor, self.width)

    def _draw(self, canvas):
        p = self.anchor
        try:
          the_box = canvas.create_window(p.x,p.y,window=self.frm,anchor='nw')
        except Exception as e:
          say(str(e),color='red') # tell user about problem drawing
          return None
        self.box.pack()
        self.box.focus_set()
        return the_box


    def get_text(self):
        return self.box.get("1.0", "end-1c")

    def _move(self, dx, dy):
        self.anchor.move(dx,dy)

    def get_anchor(self):
        return self.anchor.clone()

    def clone(self):
        other = Text(self.anchor, self.width, self.height)
        other.set_name(self.name)
        other.set_text(self.get_text())
        other.fill = self.get_fill()
        other.outline = self.get_outline()
        other.font = self.get_font()
        other.justify = self.get_justify()
        return other

    def set_text(self, t):
        self.box.delete("1.0", "end-1c")
        self.box.insert("1.0",t)
        save_gui4sher() # update the save file
        root.update()

    def get_height(self):
      return self.height

    def set_height(self,height):
      self.height = height
      if self.id:
          self.box.config(height=self.get_height())
          save_gui4sher() # update the save file
          root.update()

            
    def set_font(self,font):
      self.font = font
      if self.id:
          self.box.config(font=self.get_font())
          save_gui4sher() # update the save file
          root.update()

    def get_font(self):
      return self.font

    def set_fill(self, color):
        """Set interior color to color"""
        self.fill = color
        if self.id:
          self.box.config(bg=self.get_fill())
          save_gui4sher() # update the save file
          root.update()

    def set_outline(self, color):
        """Set outline color to color"""
        self.outline = color
        if self.id:
          self.box.config(fg=self.get_outline())
          save_gui4sher() # update the save file
          root.update()

    def set_width(self, width):
        """Set line weight to width"""
        self.width = width
        if self.id:
          self.box.config(width=self.get_width())
          save_gui4sher() # update the save file
          root.update()

    def get_width(self):
      return self.width


    def to_exec(self):
      debug_print('Creating string to execute for Text')
      ''' creates commands to create the line '''
      exec_lines = [ self.name + ' = ' + self.__class__.__name__ +'(Point('+str(self.anchor.x)+','+str(self.anchor.y)+'),'+str(self.width)+','+str(self.height)+',"'+self.get_name()+'")',
                     self.name + '.set_fill(\''+ self.get_fill() + '\')',
                     self.name + ".set_outline('"+ self.get_outline() + "')",
                     self.name + ".set_width('"+ str(self.get_width())+ "')",
                     self.name + ".set_height('"+ str(self.get_height())+ "')",
                     self.name + ".set_text('''"+ self.get_text()+ "''')", # text has multiple lines
                     self.name + ".set_font(" + font_string(self.get_font()) + ")",
                     self.name + '.draw()']
      return '''
'''.join(exec_lines)

class Button(GraphicsObject):

    def __init__(self, p, text, name):
        debug_print('Initializing button graphics object',end='\n')
        GraphicsObject.__init__(self)
        self.name = name
        debug_print('Button Object initialized',end='\n')
        self.anchor = p.clone()
        #print self.anchor
        self.text = text
        self.anchor = p.clone()
        self.set_fill("cyan")
        self.set_outline("black")
        self.set_font(("sanserif", 14,'bold'))
        self.set_justify('center')
        self.frm = tk.Frame(graphics.master)
        self.set_width(len(text))
        debug_print('Button Object name: '+self.get_name(),end='\n')
# begin shell not in app
        # put an empty definition for the click handler into the clicks window if no definition is already in the clicks window
        clicks = clicks_window.get('1.0','end')
        if clicks.find('def '+self.get_name()+'_click') == -1:
          debug_print('Putting click definition in ')
          debug_print('for '+self.get_name(),end='\n')
          clicks_window.insert('end','\ndef '+self.get_name()+'_click():\n\tpass\n')
        debug_print('Clicks:\n'+clicks_window.get('1.0','end'))
# end shell not in app

        self.button = tk.Button(self.frm,
                              width = len(text),
                              text=text,
                              bg = self.get_fill(),
                              fg = self.get_outline(),
                              font = self.get_font(),
                              justify = self.get_justify(),
                              command = self.handle_click)

          

    def __repr__(self):
        return "Button({}, {})".format(self.anchor, self.text)

    def _draw(self, canvas):
        p = self.anchor
        try:
          the_button = canvas.create_window(p.x,p.y,window=self.frm,anchor='nw')
        except Exception as e:
          say(str(e),color='red') # tell user about problem drawing
          return None
        self.button.pack()
        return the_button

    def handle_click(self):
      global globals
      global locals
      ''' if it exists call the return function from the clicks file '''
      # do a return command if the return function exists
      try:
        try:
          globals()[self.get_name()+'_click']()
        except Exception as e:
          say(str(e),color='red')
      except (NameError, AttributeError): return None # otherwise no return behavior
      except: say(sys.exc_info(),color='red',font=('Consolas', 12, 'bold')) # output error

    def set_name(self, name):
        """Set name of button to name"""
        old_name = self.name
        self.name = name
        # add a click command if one exists
        try: exec('self.command = '+self.get_name()+'_click')
        except (NameError, AttributeError): self.command = None # otherwise no command
        if self.command != None:
          self.button.config(command=self.command)
        if self.id:
            save_gui4sher() # update the save file
            root.update()
# begin shell not in app
        # translate old name to new name in clicks_window
        clicks = clicks_window.get('1.0','end')
        clicks = re.sub(r'(\W)'+old_name+r'(\W)',r'\1'+name+r'\2',clicks) # change the old name to the new name in clicks
        clicks = re.sub(r'(\W)'+old_name+r'_click(\W)',r'\1'+name+r'_click\2',clicks) # change the old name to the new name in clicks
        clicks_window.delete('1.0','end')
        clicks_window.insert('end',clicks)
# end shell not in app


    def set_text(self,text):
      self.text = text
      self.button.config(text=self.get_text())
      self.set_width(len(self.get_text()))
      if self.id:
          save_gui4sher() # update the save file
          root.update()

    def get_text(self):
        return self.text

    def _move(self, dx, dy):
        self.anchor.move(dx,dy)

    def get_anchor(self):
        return self.anchor.clone()

    def clone(self):
        other = Button(self.anchor, self.get_text())
        other.config = self.config.copy()
        other.set_name(self.name)
        other.text = self.text
        return other

    def set_justify(self,justify):
      self.justify = justify
      if self.id:
          self.button.config(justify=self.get_justify())
          save_gui4sher() # update the save file
          root.update()

    def get_justify(self):
      return self.justify

    def set_font(self,font):
      self.font = font
      if self.id:
          self.button.config(font=self.get_font())
          save_gui4sher() # update the save file
          root.update()

    def get_font(self):
      return self.font

    def set_fill(self, color):
        """Set interior color to color"""
        self.fill = color
        if self.id:
          self.button.config(bg=self.get_fill())
          save_gui4sher() # update the save file
          root.update()

    def set_outline(self, color):
        """Set outline color to color"""
        self.outline = color
        if self.id:
          self.button.config(fg=self.get_outline())
          save_gui4sher() # update the save file
          root.update()

    def set_width(self, width):
        """Set line weight to width"""
        self.width = width
        if self.id:
          self.button.config(width=self.get_width())
          save_gui4sher() # update the save file
          root.update()



    def to_exec(self):
      ''' creates commands to create the line '''
      exec_lines = [ self.name+ ' = ' + self.__class__.__name__ +'(Point('+str(self.anchor.x)+','+str(self.anchor.y)+'),"'+str(self.get_text())+'","'+self.get_name()+'")',
                     self.name + '.set_fill(\''+ self.get_fill() + '\')',
                     self.name + ".set_outline('"+ self.get_outline() + "')",
                     self.name + ".set_width('"+ str(self.get_width())+ "')",
                     self.name + ".set_text('"+ self.get_text()+ "')",
                     self.name + ".set_font(" + font_string(self.get_font()) + ")",
                     self.name + '.set_justify(\''+self.get_justify() + '\')',
                     self.name + '.draw()'
                     ]
      return '''
'''.join(exec_lines)

class Check(GraphicsObject):

    def __init__(self, p, text, name):
        GraphicsObject.__init__(self)
        self.name = name
        self.anchor = p.clone()
        #print self.anchor
        self.text = text
        self.anchor = p.clone()
        self.set_fill('#EEEEEE')
        self.set_outline("black")
        self.set_font(("sanserif", 14,'bold'))
        self.set_justify('center')
        self.frm = tk.Frame(graphics.master)
        self.set_width(len(text))
        self.checked = tk.BooleanVar()
        self.set_checked(False)
# begin shell not in app
        # put an empty definition for the click handler into the clicks window if no definition is already in the clicks window
        clicks = clicks_window.get('1.0','end')
        if clicks.find('def '+self.get_name()+'_click') == -1:
          debug_print('Putting click definition in ')
          debug_print('for '+self.get_name(),end='\n')
          clicks_window.insert('end','\ndef '+self.get_name()+'_click():\n\tpass\n')
        debug_print('Clicks:\n'+clicks_window.get('1.0','end'))
# end shell not in app
        self.button = tk.Checkbutton(self.frm,
                              width = len(text),
                              text=text,
                              bg = self.get_fill(),
                              fg = self.get_outline(),
                              font = self.get_font(),
                              justify = self.get_justify(),
                              variable=self.checked,
                              onvalue=True,offvalue=False,
                              command = self.handle_click)
          

    def __repr__(self):
        return "Button({}, {})".format(self.anchor, self.text)

    def _draw(self, canvas):
        p = self.anchor
        try:
          the_button = canvas.create_window(p.x,p.y,window=self.frm,anchor='nw')
        except Exception as e:
          say(str(e),color='red') # tell user about problem drawing
          return None
        self.button.pack()
        return the_button

    def handle_click(self):
      ''' if it exists call the return function from the clicks file '''
      # do a return command if the return function exists
      try:
        try:
          globals()[self.get_name()+'_click']()
        except Exception as e:
          say(str(e),color='red')
      except (NameError, AttributeError): return None # otherwise no return behavior
      except Error as e: say(e,color='red',font=('Consolas', 12, 'bold')) # output error
      except Exception as exp: say(exp,color='red',font=('Consolas', 12, 'bold')) # output Exception

    def get_checked(self):
      ''' gets whether the button is checked '''
      return self.checked.get()

    def set_checked(self,value):
      ''' sets the check to either true or false '''
      self.checked.set(value)
      if self.id:
        save_gui4sher() # update the save file
        root.update()
      

    def set_name(self, name):
        """Set name of button to name"""
        old_name = self.name
        self.name = name
        # add a click command if one exists
        try: exec('self.command = '+self.get_name()+'_click')
        except (NameError, AttributeError): self.command = None # otherwise no command
        if self.command != None:
          self.button.config(command=self.command)
        if self.id:
            save_gui4sher() # update the save file
            root.update()
# begin shell not in app
       # translate old name to new name in clicks_window
        clicks = clicks_window.get('1.0','end')
        clicks = re.sub(r'(\W)'+old_name+r'(\W)',r'\1'+name+r'\2',clicks) # change the old name to the new name in clicks
        clicks = re.sub(r'(\W)'+old_name+r'_click(\W)',r'\1'+name+r'_click\2',clicks) # change the old name to the new name in clicks
        clicks_window.delete('1.0','end')
        clicks_window.insert('end',clicks)
# end shell not in app


    def set_text(self,text):
      self.text = text
      self.button.config(text=self.get_text())
      self.set_width(len(self.get_text()))
      if self.id:
          save_gui4sher() # update the save file
          root.update()

    def get_text(self):
        return self.text

    def _move(self, dx, dy):
        self.anchor.move(dx,dy)

    def get_anchor(self):
        return self.anchor.clone()

    def clone(self):
        other = Button(self.anchor, self.get_text())
        other.config = self.config.copy()
        other.set_name(self.name)
        other.text = self.text
        return other

    def set_justify(self,justify):
      self.justify = justify
      if self.id:
          self.button.config(justify=self.get_justify())
          save_gui4sher() # update the save file
          root.update()

    def get_justify(self):
      return self.justify

    def set_font(self,font):
      self.font = font
      if self.id:
          self.button.config(font=self.get_font())
          save_gui4sher() # update the save file
          root.update()

    def get_font(self):
      return self.font

    def set_fill(self, color):
        """Set interior color to color"""
        self.fill = color
        if self.id:
          self.button.config(bg=self.get_fill())
          save_gui4sher() # update the save file
          root.update()

    def set_outline(self, color):
        """Set outline color to color"""
        self.outline = color
        if self.id:
          self.button.config(fg=self.get_outline())
          save_gui4sher() # update the save file
          root.update()

    def set_width(self, width):
        """Set line weight to width"""
        self.width = width
        if self.id:
          self.button.config(width=self.get_width())
          save_gui4sher() # update the save file
          root.update()



    def to_exec(self):
      ''' creates commands to create the line '''
      exec_lines = [ self.name+ ' = ' + self.__class__.__name__ +'(Point('+str(self.anchor.x)+','+str(self.anchor.y)+'),"'+str(self.get_text())+'","'+self.get_name()+'")',
                     self.name + '.set_fill(\''+ self.get_fill() + '\')',
                     self.name + ".set_outline('"+ self.get_outline() + "')",
                     self.name + ".set_width('"+ str(self.get_width())+ "')",
                     self.name + ".set_text('"+ self.get_text()+ "')",
                     self.name + ".set_font(" + font_string(self.get_font()) + ")",
                     self.name + '.set_justify(\''+self.get_justify() + '\')',
                     self.name + '.set_checked(\''+str(self.get_checked()) + '\')',
                     self.name + '.draw()'
                     ]
      return '''
'''.join(exec_lines)


class List(GraphicsObject):

    def __init__(self, p, items, name):
        GraphicsObject.__init__(self)
        self.name = name
        self.anchor = p.clone()
        #print self.anchor
        self.anchor = p.clone()
        self.set_fill("yellow")
        self.set_outline("black")
        self.set_font(("arial", 12,'bold'))
        self.set_justify('left')
        self.frm = tk.Frame(graphics.master)
        # height is the number of items but it is at least 1 and <= 5
        self.set_height(len(items))
        if int(self.get_height()) == 0: self.set_height(1)
        elif int(self.get_height()) > 5 : self.set_height(5)
        self.set_width(1)
        self.scroll = tk.Scrollbar(self.frm)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.list = tk.Listbox(self.frm,
                              bg = self.get_fill(),
                              fg = self.get_outline(),
                              font = self.get_font(),
                              justify = self.get_justify(),
                              height = self.get_height(),
                              selectmode = tk.SINGLE,   # one one item selected at a time
                              yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.list.yview)
        # add the items to a list
        self.set_items(items)
        self.list.bind("<<ListboxSelect>>",self.handle_select)
# begin shell not in app
        # put an empty definition for the click handler into the clicks window if no definition is already in the clicks window
        clicks = clicks_window.get('1.0','end')
        if clicks.find('def '+self.get_name()+'_select') == -1:
          debug_print('Putting click definition in ')
          debug_print('for '+self.get_name(),end='\n')
          clicks_window.insert('end','\ndef '+self.get_name()+'_select():\n\tpass\n')
        debug_print('Clicks:\n'+clicks_window.get('1.0','end'))
# end shell not in app
    def __repr__(self):
        to_return = "List({}, {})".format(self.anchor, self.width)
        return "List({}, {})".format(self.anchor, self.width)

    def _draw(self, canvas):
        p = self.anchor
        try:
          the_listbox = canvas.create_window(p.x,p.y,window=self.frm,anchor='nw')
        except Exception as e:
          say(str(e),color='red') # tell user about problem drawing
          return None
        self.list.pack()
        return the_listbox

    def handle_select(self,event):
      ''' if it exists call the select function from the clicks file '''
      # do a return command if the return function exists
      try:
        try:
          globals()[self.get_name()+'_select']()
        except Exception as e:
          say(str(e),color='red')
      except (NameError, AttributeError): return None # otherwise no return behavior
      except Error as e: say(e,color='red',font=('Consolas', 12, 'bold')) # output error
      except Exception as exp: say(exp,color='red',font=('Consolas', 12, 'bold')) # output Exception


    def get_items(self):
        ''' List of items in List. '''
        to_return = []
        # make a list of items in the list
        for item in self.list.get(0,self.list.size()-1):
          to_return.append(item)
        return to_return

    def set_items(self,items):
      ''' Change items in List. '''
      # first empty the list
      self.list.delete(0,self.list.size()-1)
      # then put new list in
      for item in items:
        self.add(item)

    def _move(self, dx, dy):
        self.anchor.move(dx,dy)

    def get_anchor(self):
        return self.anchor.clone()

    def clone(self):
        other = List(self.anchor, self.width)
        other.config = self.config.copy()
        other.set_name(self.name)
        other.set_items(self.get_items())
        other.set_outline(self.get_outline())
        other.set_fill(self.get_fill())
        other.set_font(self.get_font())
        other.set_justify(self.get_justify())
        other.set_height(self.get_height())
        return other

    def add(self, item):
      ''' Adds item into list. '''
      self.list.insert(tk.END,item)
      # if item is wider than list make list wider
      if len(str(item)) > int(self.get_width()) : self.set_width(len(str(item)))
      if self.id:
        save_gui4sher() # update the save file
        root.update()

    def delete(self, item):
      ''' Deletes item from list. '''
      try:
        self.list.delete(self.get_items().index(item))
      except ValueError as ve: say(str(ve),color='red',font=('Consolas', 12, 'bold'))
      if self.id:
        save_gui4sher() # update the save file
        root.update()

    def selected(self):
      ''' Returns the selected item or None if none selected. '''
      tup = self.list.curselection()  # a tuple either empty or with selected item
      if len(tup) == 0:
        return None
      else:
        return self.list.get(tup)

    def select(self,item):
      ''' Selects item in list. '''
      self.list.activate(self.data.index(item))
            
    def get_height(self): return self.height

    def set_height(self,height):
      self.height = height
      if self.id:
          self.list.config(height=self.get_height())
          save_gui4sher() # update the save file
          root.update()
            
    def set_justify(self,justify):
      self.justify = justify
      if self.id:
          self.list.config(justify=self.get_justify())
          save_gui4sher() # update the save file
          root.update()

    def get_justify(self):
      return self.justify

    def set_font(self,font):
      self.font = font
      if self.id:
          self.list.config(font=self.get_font())
          save_gui4sher() # update the save file
          root.update()

    def get_font(self):
      return self.font

    def set_fill(self, color):
        """Set interior color to color"""
        self.fill = color
        if self.id:
          self.list.config(bg=self.get_fill())
          save_gui4sher() # update the save file
          root.update()

    def set_outline(self, color):
        """Set outline color to color"""
        self.outline = color
        if self.id:
          self.list.config(fg=self.get_outline())
          save_gui4sher() # update the save file
          root.update()

    def set_width(self, width):
        """Set line weight to width"""
        self.width = width
        if self.id:
          self.list.config(width=self.get_width())
          save_gui4sher() # update the save file
          root.update()

    def get_width(self):
      return self.width

    def set_name(self, name):
        """Set name of select to name"""
        old_name = self.name
        self.name = name
        # add a click command if one exists
        try: exec('self.command = '+self.get_name()+'_select')
        except (NameError, AttributeError): self.command = None # otherwise no command
        if self.command != None:
          self.button.config(command=self.command)
        if self.id:
            save_gui4sher() # update the save file
            root.update()
# begin shell not in app
        # translate old name to new name in clicks_window
        clicks = clicks_window.get('1.0','end')
        clicks = re.sub(r'(\W)'+old_name+r'(\W)',r'\1'+name+r'\2',clicks) # change the old name to the new name in clicks
        clicks = re.sub(r'(\W)'+old_name+r'_select(\W)',r'\1'+name+r'_select\2',clicks) # change the old name to the new name in clicks
        clicks_window.delete('1.0','end')
        clicks_window.insert('end',clicks)
# end shell not in app


    def to_exec(self):
      debug_print('Creating string to execute for Entry')
      ''' creates commands to create the line '''
      exec_lines = [ self.name + ' = ' + self.__class__.__name__ +'(Point('+str(self.anchor.x)+','+str(self.anchor.y)+'),'+str(self.get_items())+',"'+self.get_name()+'")',
                     self.name + '.set_fill(\''+ self.get_fill() + '\')',
                     self.name + ".set_outline('"+ self.get_outline() + "')",
                     self.name + ".set_width('"+ str(self.get_width())+ "')",
                     self.name + ".set_height('"+ str(self.get_height())+ "')",
                     self.name + ".set_font(" + font_string(self.get_font()) + ")",
                     self.name + '.set_justify(\''+self.get_justify() + '\')',
                     self.name + '.draw()']
      return '''
'''.join(exec_lines)

def names():
  ''' returns a list of object names for all the objects drawn on screen '''
  to_return = []
  for thing in objects:
     to_return.append(thing.get_name())
  return(to_return)
  

''' controls the title '''


def change_title(titler):
  root.title(titler)

''' common colors '''
red = 'red'
green = 'green'
blue = 'blue'
white = 'white'
black = 'black'
gray = 'gray'
orange = 'orange'
purple = 'purple'
violet = 'violet'
yellow = 'yellow'
brown = 'brown'
cyan = 'cyan'
magenta = 'magenta'
pink = 'pink'

''' common fonts '''
serif = 'serif'
sans_serif = 'sans-serif'
monospaced = 'monospaced'
courier = 'courier'
helvetica = 'helvetica'
times = 'times'



# begin shell not in app
# end shell not in app

# begin shell not in app
def save_gui4sher():
  ''' save_gui4sher creates a gui4sher with all the current objects '''
  global read_file
  global save_file
  global NO_SAVE
  # open the basic gui4sher
  reader = open(read_file,mode='r')
  debug_print('Reading from ')
  debug_print(read_file)
  debug_print('''
''')
  # string to put lines to write to the save file
  save_lines = ''
  # put in copyright line info
  save_lines += NO_SAVE+"\n''' code here manages copyright notice '''"
  save_lines += NO_SAVE+'\nauthors = "'+authors+'"'
  save_lines += NO_SAVE+'\nthanks = "'+thanks+'"'
  save_lines += NO_SAVE+'\nyear = "'+year+'"\n'
  save_lines += NO_SAVE+'\nNO_SAVE = \'\'\'\n# not saved\'\'\'\n\n'
  # put in the save file name
  save_lines += NO_SAVE+"\nsave_file = __file__\n\n"
  # copy all the lines from reader to saver except code lines with comment # not saved
  for line in reader:
    if 0 == line.find('# not to copy'): break # everything afterwards are objects and stuff that will be automatically updated and copied
    if 0 == line.find('# not saved'):
      # don't write this line or the next
      reader.readline()
    else:
      save_lines += line
  # insert comment to indicate what shouldn't be copied
  save_lines += '\n# not to copy'
  # set up clicks window in save file
  debug_print('clicks_window.insert(\'end\','+repr(clicks_window.get('1.0','end'))+')\n')
  save_lines += NO_SAVE+'\nclicks_window.insert(\'end\','+repr(clicks_window.get('1.0','end'))+')\n'

  # put in comment establishing objects
  save_lines +="''' All the objects in the graphics are below '''"+ '''
'''
  # put commands to put every object drawn on graphics window into saver
  for obj in objects:
    save_lines += obj.to_exec()+ '''
'''
    debug_print('Saving Object: ')
    debug_print(obj.to_exec())
    debug_print('''
''')
  debug_print('try:\n\texec(clicks_window.get(\'1.0\',\'end\'))\nexcept:\n\tsay(sys.exc_info(),color=red,font=("courier",14,"bold"))\n')
  save_lines +='''
my_exec(clicks_window.get(\'1.0\',\'end\'),globals())
'''
  # read all lines from original file 
  reader.close()
  # open the file to save to 
  saver = open(save_file,mode='w+')
  debug_print('Saving to ')
  debug_print(save_file)
  debug_print('''
''')
  print(save_lines,file=saver, flush = True)
  # needed to make gui work right
  print(NO_SAVE+"\nroot.mainloop()",file=saver,flush=True)
  debug_print('Done Saving')
  debug_print('''
''')
  # finish saving files
  saver.close()



''' creates a py file that generates an app with the graphics and gui but no shell '''  
def make_app():
  global read_file
  global save_file
    
  root.withdraw()  # GUI4sher window dissapears
  app_file = tk.filedialog.asksaveasfilename(title='Select or enter name for app',filetypes = (("python files","*.py"),("all files","*.*")))
  root.deiconify() # Get GUI4sher window back

  if len(app_file) == 0: # dialog was cancelled
    say('Not making an app!',color='red')
    return
  if not app_file.endswith('.py'):  # add .py extension to files without any extension
    app_file += '.py'

  # open the basic gui4sher
  reader = open(read_file,mode='r')
  # open the file to save to 
  saver = open(app_file,mode='w+')

  # put in copyright line info
  print("''' code here manages copyright notice '''",file=saver,flush = True)
  print('\nauthors = "'+authors+'"',file=saver,flush = True)
  print('\nthanks = "'+thanks+'"',file=saver,flush = True)
  print('\nyear = "'+year+'"',file=saver,flush = True)

  # don't do debug_print's in app
  print("def debug_print(to_print,end=''):\n\tpass\n",file=saver,flush = True)


  read_lines = True # this is true when one should copy lines from the file into the app
  # copy all the lines from reader to saver except code lines with comment # not saved
  for line in reader:
    if read_lines:
      if 0 == line.find(NO_SAVE):
        # don't write this line or the next
        reader.readline()
      elif 0 == line.find('# begin shell not in app'):
        # don't write line until # end shell not in app
        read_lines = False
      else:
        print(line,end='',file=saver,flush=True)
        debug_print('''Copied {}
'''.format(line))
    else:
      if 0 == line.find('# end shell not in app'):
        # start copying lines again
        read_lines = True
  # don't do any saving since app won't modify
  print("def save_gui4sher(): return None\n",file=saver,flush=True)
  # set up app title
  print('change_title("'+os.path.basename(app_file)+'")',file=saver,flush = True)
  
  # put in comment establishing objects
  print("''' All the objects in the graphics are below '''",file=saver,flush=True)
  # put commands to put every object drawn on graphics window into saver
  for obj in objects:
    debug_print('Saving object in app: '+obj.to_exec())
    print(obj.to_exec(),file=saver,flush=True)
  # needed to make gui work right
  debug_print('Saving clicks in app: '+clicks_window.get('1.0','end'))
  print(clicks_window.get('1.0','end'),file=saver,flush=True)
  print("root.mainloop()",file=saver,flush=True)
  # finish files
  reader.close()
  saver.close()
  debug_print('''Done make_app
''')
  # run the app
  debug_print('''python "{}"
'''.format(app_file))
  system('python "{}"'.format(app_file))


def get_save():
  ''' gets a file to save changes to.
      file will be saved after each graphics draw command
  '''
  global save_file
  global root
  debug_print('In get_save',end='\n')
  save_file = ''
  counter = 0
  # keep demanding a save file until the user provides one
  while len(save_file)==0:
    root.withdraw()  # GUI4sher window dissapears
    debug_print('Updated root\n')
    counter+=1
    debug_print('getting save file '+str(counter),end='\n')
    save_file = tk.filedialog.asksaveasfilename(title='Select or enter project file',filetypes = (("python files","*.py"),("all files","*.*")))
    root.deiconify() # Get GUI4sher window back
  
  debug_print('Got save file',end='\n')
  if not save_file.endswith('.py'):  # add .py extension to files without a .py extension
    save_file += '.py'
  change_title('Project in '+save_file)
  save_gui4sher()
  shell.focus_set()
# end shell not in app



# source
read_file = __file__

# begin shell not in app
# end shell not in app


# begin shell not in app
''' set up button clicks for buttons '''
edit_mode = 'SHELL'
def toggle_edit():
  global edit_mode
  global clicks_window
  global shell
  if edit_mode == 'SHELL':
    edit_mode = 'CLICKS'
    click_toggle.config(text='Change\nClicks')
    shell.pack_forget()
    clicks_window.pack(fill=tk.BOTH, expand = tk.YES, side="left") 
    shell_scroll.config(command=clicks_window.yview)
    shell_hscroll.config(command=clicks_window.xview)
  else:
    edit_mode = 'SHELL'
    debug_print('Changing clicks',end='\n')
    click_toggle.config(text='Edit\nClicks')
    clicks_window.pack_forget()
    shell.pack(fill=tk.BOTH, expand = tk.YES, side="left")
    shell_scroll.config(command=shell.yview)
    shell_hscroll.config(command=shell.xview)
    debug_print('executing changing clicks functions',end='\n')
    debug_print('Executing:\n'+clicks_window.get('1.0','end'))
    my_exec(clicks_window.get('1.0','end'),globals())
    debug_print('Widget Actions Changed\n')
    say('Widget Actions Changed\n',color='gray')
    save_gui4sher()

click_toggle.config(command=toggle_edit)
make_app_button.config(command=make_app)

def names_command():
  for name in names():
    say(name)

names_button.config(command=names_command)



''' interactive functions to put down graphics and gui '''
def valid_name(name,thing,prefix=''):
  ''' Interactively dialogs with the user until a valid name is acquired and then returns it. '''
  if name == '':
    name = ask('Name of '+thing)
  while not (prefix+name).isidentifier() or iskeyword(prefix+name) or prefix+name in names():
    if not name.isidentifier():
      name = ask(name+' is not a valid python variable name, Enter a new name')
    elif iskeyword(name):
      name = ask(name+' is a python keyword, Enter a new name')
    elif name in names():
      name = ask('You already used '+name+', Enter a new name')
    else:
      name = ask('Something is wrong with '+name+', Enter a new name')
  return name

def mouse_ask(to_print,color='darkgreen',font=('serif',12),end=': '):
  ''' Prompts the user and returns a point that the user clicked on in the graphics window. '''
  graphics.toggle_tracking()
  say(to_print,color=color,font=font)
  to_return = graphics.get_mouse_click()
  graphics.toggle_tracking()
  return to_return

def place_rectangle(name='',fill='',outline='black',width=1):
  ''' Interactive placement of a rectangle. '''
  global objects
  name = valid_name(name,'Rectangle') # make sure the name of the object is valid
  # get the corners of the rectangle
  corner = mouse_ask('Click on a corner of rectangle "'+name+'"')
  dot = Circle(corner,3) # dot to put on screen
  dot.set_fill('darkgray')
  dot.draw()
  opposite = mouse_ask('Click on the opposite corner of rectangle "'+name+'"')
  dot.undraw() # don't need dot anymore
  # make the rectangle
  rect = Rectangle(corner,opposite)
  rect.set_name(name)
  rect.set_fill(fill)
  rect.set_outline(outline)
  rect.set_width(width)
  rect.draw()
  exec(name+'=objects[-1]',globals())

''' interactive functions to put down graphics and gui '''
def place_oval(name='',fill='',outline='black',width=1):
  ''' Interactive placement of a oval. '''
  name = valid_name(name,'Oval') # make sure the name of the object is valid
  # get the corners of the rectangle enclosing
  corner = mouse_ask('Click on a corner of rectangle that encloses the oval "'+name+'"')
  dot = Circle(corner,3) # dot to put on screen
  dot.set_fill('darkgray')
  dot.draw()
  opposite = mouse_ask('Click on the opposite corner of rectangle that encloses the oval "'+name+'"')
  dot.undraw() # don't need dot anymore
  # make the oval
  oval = Oval(corner,opposite)
  oval.set_name(name)
  oval.set_fill(fill)
  oval.set_outline(outline)
  oval.set_width(width)
  oval.draw()
  exec(name+'=objects[-1]',globals())
  
''' interactive functions to put down graphics and gui '''
def place_line(name='',fill='',outline='black',width=1):
  ''' Interactive placement of a line. '''
  name = valid_name(name,'Line') # make sure the name of the object is valid
  # get the corners of the rectangle enclosing
  corner = mouse_ask('Click on an endpoint of "'+name+'"')
  dot = Circle(corner,3) # dot to put on screen
  dot.set_fill('darkgray')
  dot.draw()
  opposite = mouse_ask('Click on the other endpoint of "'+name+'"')
  dot.undraw() # don't need dot anymore
  # make the Line
  line = Line(corner,opposite)
  line.set_name(name)
  line.set_fill(fill)
  line.set_outline(outline)
  line.set_width(width)
  line.draw()
  exec(name+'=objects[-1]',globals())
    
''' interactive functions to put down graphics and gui '''
def place_dashed_line(name='',fill='',outline='black',width=1,dash=(5,5)):
  ''' Interactive placement of a line. '''
  name = valid_name(name,'Dashed_Line') # make sure the name of the object is valid
  # get the corners of the rectangle enclosing
  corner = mouse_ask('Click on an endpoint of "'+name+'"')
  dot = Circle(corner,3) # dot to put on screen
  dot.set_fill('darkgray')
  dot.draw()
  opposite = mouse_ask('Click on the other endpoint of "'+name+'"')
  dot.undraw() # don't need dot anymore
  # make the Line
  line = Dashed_Line(corner,opposite)
  line.set_name(name)
  line.set_fill(fill)
  line.set_outline(outline)
  line.set_width(width)
  line.set_dash(dash)
  line.draw()
  exec(name+'=objects[-1]',globals())
    
''' interactive functions to put down graphics and gui '''
def place_circle(name='',fill='',outline='black',width=1):
  ''' Interactive placement of a circle. '''
  name = valid_name(name,'Circle') # make sure the name of the object is valid
  # get the center and radius
  center = mouse_ask('Click on the center of the circle "'+name+'"')
  dot = Circle(center,3) # dot to put on screen
  dot.set_fill('darkgray')
  dot.draw()
  circumference = mouse_ask('Click on the circumference of the circle "'+name+'"')
  dot.undraw() # don't need dot anymore
  # find the radius
  x_difference = center.get_x() - circumference.get_x()
  y_difference = center.get_y() - circumference.get_y()
  radius = sqrt(x_difference*x_difference + y_difference*y_difference)
  # make the circle
  circ = Circle(center,radius)
  circ.set_name(name)
  circ.set_fill(fill)
  circ.set_outline(outline)
  circ.set_width(width)
  circ.draw()
  exec(name+'=objects[-1]',globals())
    
''' interactive functions to put down graphics and gui '''
def place_polygon(name='',fill='',outline='black',width=1):
  ''' Interactive placement of a circle. '''
  name = valid_name(name,'Polygon') # make sure the name of the object is valid
  # holds all the corners of the polygon
  corners = []
  circles = []
  while True:
    # get the first corner of the polygon
    first = mouse_ask('Click on the a corner of the polygon "'+name+'"',color='orange')
    first_circle = Circle(first,5)
    first_circle.set_fill('orange')
    first_circle.draw()
    corners.append(first)
    circles.append(first_circle)
    # get more corners of the polygon
    while True:
      another = mouse_ask('Click on another corner of the polygon "'+name+'"',color='#444444')
      # find if the new point is near the first one
      x_difference = first.get_x() - another.get_x()
      y_difference = first.get_y() - another.get_y()
      distance = sqrt(x_difference*x_difference + y_difference*y_difference)
      if distance < 5:
        break
      corners.append(another)
      another_circle = Circle(another,2)
      another_circle.set_fill('#444444')
      another_circle.draw()
      circles.append(another_circle)
    # clear the points
    for circle in circles:
      circle.undraw()
    if len(corners) < 3:
      say('You need at least 3 points for a polygon, try again',color='red')
    else: break # finished the points
  # make the polygon
  poly = Polygon(corners)
  poly.set_name(name)
  poly.set_fill(fill)
  poly.set_outline(outline)
  poly.set_width(width)
  poly.draw()
  exec(name+'=objects[-1]',globals())
    
    
''' interactive functions to put down graphics and gui '''
def place_label(text,name='',fill='',outline='black',font=('times',14)):
    ''' Interactive placement of a label. '''
    try:
      name = valid_name(name,'Label') # make sure the name of the object is valid
      # get position of upper left corner of label
      anchor = mouse_ask('Click on the position of the Label "'+name+'"')
      # make the label
      labl = Label(anchor,text,name)
      labl.set_name(name)
      labl.set_fill(fill)
      labl.set_outline(outline)
      labl.set_font(font)
      labl.draw()
      exec(name+'=objects[-1]',globals())
    except: pass
    
''' interactive functions to put down graphics and gui '''
def place_entry(width,name='',fill='white',outline='black',font=('times',14)):
    ''' Interactive placement of a label. '''
    try:
      name = valid_name(name,'Entry') # make sure the name of the object is valid
      # get position of upper left corner of Entry
      anchor = mouse_ask('Click on the position of the Entry "'+name+'"')
      # make the Entry
      entr = Entry(anchor,width,name)
      entr.set_name(name)
      entr.set_fill(fill)
      entr.set_outline(outline)
      entr.set_font(font)
      entr.draw()
      exec(name+'=objects[-1]',globals())
    except: pass

''' interactive functions to put down graphics and gui '''
def place_text(width,height,name='',fill='white',outline='black',font=('times',10)):
  ''' Interactive placement of a label. '''
  name = valid_name(name,'Text') # make sure the name of the object is valid
  # get position of upper left corner of Entry
  anchor = mouse_ask('Click on the position of the Text "'+name+'"')
  # make the Entry
  box = Text(anchor,width,height,name)
  box.set_name(name)
  box.set_fill(fill)
  box.set_outline(outline)
  box.set_font(font)
  debug_print('Executing text box insert:\n'+box.to_exec())
  box.draw()
  exec(name+'=objects[-1]',globals())
    
''' interactive functions to put down graphics and gui '''
def place_button(text,name='',fill='cyan',outline='black',font=('times',14)):
  ''' Interactive placement of a Button. '''
  name = valid_name(name,'Button') # make sure the name of the object is valid
  # get position of upper left corner of Button
  anchor = mouse_ask('Click on the position of the Button "'+name+'"')
  # make the button
  debug_print('Creating Buttton',end='\n')
  butn = Button(anchor,text,name)
  debug_print('Button created',end='\n')
  butn.set_name(name)
  debug_print('Button named',end='\n')
  butn.set_fill(fill)
  butn.set_outline(outline)
  butn.set_font(font)
  # initialize and draw the object with the name specified
  butn.draw()
  exec(name+'=objects[-1]',globals())
    
''' interactive functions to put down graphics and gui '''
def place_check(text,name='',fill='#EEEEEE',outline='black',font=('times',14)):
  ''' Interactive placement of a Check (checkbox). '''
  name = valid_name(name,'Check') # make sure the name of the object is valid
  # get position of upper left corner of Button
  anchor = mouse_ask('Click on the position of the Check "'+name+'"')
  # make the button
  butn = Check(anchor,text,name)
  butn.set_name(name)
  butn.set_fill(fill)
  butn.set_outline(outline)
  butn.set_font(font)
  butn.draw()
  exec(name+'=objects[-1]',globals())
    
''' interactive functions to put down graphics and gui '''
def place_list(items,name='',fill='yellow',outline='black',font=('times',14)):
  ''' Interactive placement of a Button. '''
  name = valid_name(name,'List') # make sure the name of the object is valid
  # get position of upper left corner of List
  anchor = mouse_ask('Click on the position of the List "'+name+'"')
  # make the List
  lst = List(anchor,items,name)
  lst.set_name(name)
  lst.set_fill(fill)
  lst.set_outline(outline)
  lst.set_font(font)
  lst.draw()
  exec(name+'=objects[-1]',globals())
    
      



  
# end shell not in app




# not to copy
# not saved
clicks_window.insert('end','\n')
''' All the objects in the graphics are below '''

my_exec(clicks_window.get('1.0','end'),globals())


# not saved
root.mainloop()
