import io
import re
import sys
import tkinter as tk
from tkinter import filedialog, messagebox

# Defaults
STEPSIZE = 8
TABSIZE = 8
EXPANDTABS = False

next = {}
next['if'] = next['elif'] = 'elif', 'else', 'end'
next['while'] = next['for'] = 'else', 'end'
next['try'] = 'except', 'finally'
next['except'] = 'except', 'else', 'finally', 'end'
next['else'] = next['finally'] = next['with'] = \
    next['def'] = next['class'] = 'end'
next['end'] = ()
start = 'if', 'while', 'for', 'try', 'with', 'def', 'class'

class PythonIndenter:

    def __init__(self, fpi, fpo, indentsize=STEPSIZE, tabsize=TABSIZE, expandtabs=EXPANDTABS):
        self.fpi = fpi
        self.fpo = fpo
        self.indentsize = indentsize
        self.tabsize = tabsize
        self.lineno = 0
        self.expandtabs = expandtabs
        self._write = fpo.write
        self.kwprog = re.compile(
                r'^(?:\s|\\\n)*(?P<kw>[a-z]+)'
                r'((?:\s|\\\n)+(?P<id>[a-zA-Z_]\w*))?'
                r'[^\w]')
        self.endprog = re.compile(
                r'^(?:\s|\\\n)*#?\s*end\s+(?P<kw>[a-z]+)'
                r'(\s+(?P<id>[a-zA-Z_]\w*))?'
                r'[^\w]')
        self.wsprog = re.compile(r'^[ \t]*')
    # end def __init__

    def write(self, line):
        if self.expandtabs:
            self._write(line.expandtabs(self.tabsize))
        else:
            self._write(line)
        # end if
    # end def write

    def readline(self):
        line = self.fpi.readline()
        if line: self.lineno += 1
        # end if
        return line
    # end def readline

    def error(self, fmt, *args):
        if args: fmt = fmt % args
        # end if
        sys.stderr.write('Error at line %d: %s\n' % (self.lineno, fmt))
        self.write('### %s ###\n' % fmt)
    # end def error

    def getline(self):
        line = self.readline()
        while line[-2:] == '\\\n':
            line2 = self.readline()
            if not line2: break
            # end if
            line += line2
        # end while
        return line
    # end def getline

    def putline(self, line, indent):
        tabs, spaces = divmod(indent*self.indentsize, self.tabsize)
        i = self.wsprog.match(line).end()
        line = line[i:]
        if line[:1] not in ('\n', '\r', ''):
            line = '\t'*tabs + ' '*spaces + line
        # end if
        self.write(line)
    # end def putline

    def reformat(self):
        stack = []
        while True:
            line = self.getline()
            if not line: break      # EOF
            # end if
            m = self.endprog.match(line)
            if m:
                kw = 'end'
                kw2 = m.group('kw')
                if not stack:
                    self.error('unexpected end')
                elif stack.pop()[0] != kw2:
                    self.error('unmatched end')
                # end if
                self.putline(line, len(stack))
                continue
            # end if
            m = self.kwprog.match(line)
            if m:
                kw = m.group('kw')
                if kw in start:
                    self.putline(line, len(stack))
                    stack.append((kw, kw))
                    continue
                # end if
                if kw in next and stack:
                    self.putline(line, len(stack)-1)
                    kwa, kwb = stack[-1]
                    stack[-1] = kwa, kw
                    continue
                # end if
            # end if
            self.putline(line, len(stack))
        # end while
        if stack:
            self.error('unterminated keywords')
            for kwa, kwb in stack:
                self.write('\t%s\n' % kwa)
            # end for
        # end if
    # end def reformat

    def delete(self):
        begin_counter = 0
        end_counter = 0
        while True:
            line = self.getline()
            if not line: break      # EOF
            # end if
            m = self.endprog.match(line)
            if m:
                end_counter += 1
                continue
            # end if
            m = self.kwprog.match(line)
            if m:
                kw = m.group('kw')
                if kw in start:
                    begin_counter += 1
                # end if
            # end if
            self.write(line)
        # end while
        if begin_counter - end_counter < 0:
            sys.stderr.write('Warning: input contained more end tags than expected\n')
        elif begin_counter - end_counter > 0:
            sys.stderr.write('Warning: input contained less end tags than expected\n')
        # end if
    # end def delete

    def complete(self):
        stack = []
        todo = []
        currentws = thisid = firstkw = lastkw = topid = ''
        while True:
            line = self.getline()
            i = self.wsprog.match(line).end()
            m = self.endprog.match(line)
            if m:
                thiskw = 'end'
                endkw = m.group('kw')
                thisid = m.group('id')
            else:
                m = self.kwprog.match(line)
                if m:
                    thiskw = m.group('kw')
                    if thiskw not in next:
                        thiskw = ''
                    # end if
                    if thiskw in ('def', 'class'):
                        thisid = m.group('id')
                    else:
                        thisid = ''
                    # end if
                elif line[i:i+1] in ('\n', '#'):
                    todo.append(line)
                    continue
                else:
                    thiskw = ''
                # end if
            # end if
            indentws = line[:i]
            indent = len(indentws.expandtabs(self.tabsize))
            current = len(currentws.expandtabs(self.tabsize))
            while indent < current:
                if firstkw:
                    if topid:
                        s = '# end %s %s\n' % (
                                firstkw, topid)
                    else:
                        s = '# end %s\n' % firstkw
                    # end if
                    self.write(currentws + s)
                    firstkw = lastkw = ''
                # end if
                currentws, firstkw, lastkw, topid = stack.pop()
                current = len(currentws.expandtabs(self.tabsize))
            # end while
            if indent == current and firstkw:
                if thiskw == 'end':
                    if endkw != firstkw:
                        self.error('mismatched end')
                    # end if
                    firstkw = lastkw = ''
                elif not thiskw or thiskw in start:
                    if topid:
                        s = '# end %s %s\n' % (
                                firstkw, topid)
                    else:
                        s = '# end %s\n' % firstkw
                    # end if
                    self.write(currentws + s)
                    firstkw = lastkw = topid = ''
                # end if
            # end if
            if indent > current:
                stack.append((currentws, firstkw, lastkw, topid))
                if thiskw and thiskw not in start:
                    # error
                    thiskw = ''
                # end if
                currentws, firstkw, lastkw, topid = \
                          indentws, thiskw, thiskw, thisid
            # end if
            if thiskw:
                if thiskw in start:
                    firstkw = lastkw = thiskw
                    topid = thisid
                else:
                    lastkw = thiskw
                # end if
            # end if
            for l in todo: self.write(l)
            # end for
            todo = []
            if not line: break
            # end if
            self.write(line)
        # end while
    # end def complete
# end class PythonIndenter

def complete_string(source, stepsize=STEPSIZE, tabsize=TABSIZE, expandtabs=EXPANDTABS):
    input = io.StringIO(source)
    output = io.StringIO()
    pi = PythonIndenter(input, output, stepsize, tabsize, expandtabs)
    pi.complete()
    return output.getvalue()
# end def complete_string

def delete_string(source, stepsize=STEPSIZE, tabsize=TABSIZE, expandtabs=EXPANDTABS):
    input = io.StringIO(source)
    output = io.StringIO()
    pi = PythonIndenter(input, output, stepsize, tabsize, expandtabs)
    pi.delete()
    return output.getvalue()
# end def delete_string

def reformat_string(source, stepsize=STEPSIZE, tabsize=TABSIZE, expandtabs=EXPANDTABS):
    input = io.StringIO(source)
    output = io.StringIO()
    pi = PythonIndenter(input, output, stepsize, tabsize, expandtabs)
    pi.reformat()
    return output.getvalue()
# end def reformat_string

def make_backup(filename):
    import os, os.path
    backup = filename + '~'
    if os.path.lexists(backup):
        try:
            os.remove(backup)
        except OSError:
            print("Can't remove backup %r" % (backup,), file=sys.stderr)
        # end try
    # end if
    try:
        os.rename(filename, backup)
    except OSError:
        print("Can't rename %r to %r" % (filename, backup), file=sys.stderr)
    # end try
# end def make_backup

def complete_file(filename, stepsize=STEPSIZE, tabsize=TABSIZE, expandtabs=EXPANDTABS):
    with open(filename, 'r') as f:
        source = f.read()
    # end with
    result = complete_string(source, stepsize, tabsize, expandtabs)
    if source == result: return 0
    # end if
    make_backup(filename)
    with open(filename, 'w') as f:
        f.write(result)
    # end with
    return 1
# end def complete_file

def delete_file(filename, stepsize=STEPSIZE, tabsize=TABSIZE, expandtabs=EXPANDTABS):
    with open(filename, 'r') as f:
        source = f.read()
    # end with
    result = delete_string(source, stepsize, tabsize, expandtabs)
    if source == result: return 0
    # end if
    make_backup(filename)
    with open(filename, 'w') as f:
        f.write(result)
    # end with
    return 1
# end def delete_file

def reformat_file(filename, stepsize=STEPSIZE, tabsize=TABSIZE, expandtabs=EXPANDTABS):
    with open(filename, 'r') as f:
        source = f.read()
    # end with
    result = reformat_string(source, stepsize, tabsize, expandtabs)
    if source == result: return 0
    # end if
    make_backup(filename)
    with open(filename, 'w') as f:
        f.write(result)
    # end with
    return 1
# end def reformat_file

# GUI Implementation
class PIndentGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Python Indenter GUI")

        self.filepath = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        self.file_entry = tk.Entry(frame, textvariable=self.filepath, width=50)
        self.file_entry.pack(side=tk.LEFT, padx=5)

        browse_button = tk.Button(frame, text="Browse", command=self.browse_file)
        browse_button.pack(side=tk.LEFT, padx=5)

        complete_button = tk.Button(self.root, text="Complete", command=self.complete)
        complete_button.pack(pady=5)

        delete_button = tk.Button(self.root, text="Delete", command=self.delete)
        delete_button.pack(pady=5)

        reformat_button = tk.Button(self.root, text="Reformat", command=self.reformat)
        reformat_button.pack(pady=5)

    def browse_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Python files", "*.py"), ("All files", "*.*")])
        if filename:
            self.filepath.set(filename)

    def complete(self):
        filepath = self.filepath.get()
        if filepath:
            if complete_file(filepath):
                messagebox.showinfo("Success", "File completed successfully.")
            else:
                messagebox.showinfo("Info", "No changes were made to the file.")
        else:
            messagebox.showerror("Error", "No file selected.")

    def delete(self):
        filepath = self.filepath.get()
        if filepath:
            if delete_file(filepath):
                messagebox.showinfo("Success", "End directives deleted successfully.")
            else:
                messagebox.showinfo("Info", "No changes were made to the file.")
        else:
            messagebox.showerror("Error", "No file selected.")

    def reformat(self):
        filepath = self.filepath.get()
        if filepath:
            if reformat_file(filepath):
                messagebox.showinfo("Success", "File reformatted successfully.")
            else:
                messagebox.showinfo("Info", "No changes were made to the file.")
        else:
            messagebox.showerror("Error", "No file selected.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PIndentGUI(root)
    root.mainloop()
