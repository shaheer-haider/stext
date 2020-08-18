import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os


###################################### MAIN APP        #####################################
root = tk.Tk()
root.geometry("1000x700")
root.title("Spad Editor")
root.wm_iconbitmap("icon.ico")
###################################### MIAN APP END    ######################################


###################################### MAIN MENU START #########################################
###################################### MAIN MENU START #########################################
###################################### MAIN MENU START #########################################

main_menu = tk.Menu(root)

file_menu = tk.Menu(main_menu, tearoff=False, bg='black', fg='white')
edit_menu = tk.Menu(main_menu, tearoff=False, bg='black', fg='white')
view_menu = tk.Menu(main_menu, tearoff=False, bg='black', fg='white')
color_theme = tk.Menu(main_menu, tearoff=False, bg='black', fg='white')

new_icon = tk.PhotoImage(file = "Icons/new.png")

# Cascade of main menu
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit", menu=edit_menu)
main_menu.add_cascade(label="View", menu=view_menu)
main_menu.add_cascade(label="Color theme", menu=color_theme)




####################      File menu icons options    #####################
# icons of file menu
new_icon = tk.PhotoImage(file="Icons/new.png")
open_icon = tk.PhotoImage(file="Icons/open.png")
save_icon = tk.PhotoImage(file="Icons/save.png")
save_as_icon = tk.PhotoImage(file="Icons/save_as.png")
exit_icon = tk.PhotoImage(file="Icons/exit.png")

####################      File menu icons and command options  ENDS ######################





####################      Edit menu icons options commands   ######################
####################      Edit menu icons options commands   ######################
####################      Edit menu icons options commands   ######################
####################      Edit menu icons options commands   ######################

# icons of edit menu
copy_icon = tk.PhotoImage(file="Icons/copy.png")
cut_icon = tk.PhotoImage(file="Icons/cut.png")
paste_icon = tk.PhotoImage(file="Icons/paste.png")
clear_icon = tk.PhotoImage(file="Icons/clear.png")
find_icon = tk.PhotoImage(file="Icons/find.png")

####################      Edit menu icons options ENDS   ######################






####################      VIEW menu icons options    ######################

# icons of view menu
tool_bar_icon = tk.PhotoImage(file = "Icons/toolbar.png")
status_bar_icon = tk.PhotoImage(file = "Icons/status_bar.png")


####################      VIEW menu icons options END   ######################




####################      Themes menu icons options    ######################

# icons of themes menu
white_theme = tk.PhotoImage(file="Icons/white.png")
grey_theme = tk.PhotoImage(file="Icons/grey.png")
dark_theme = tk.PhotoImage(file="Icons/dark.png")
red_theme = tk.PhotoImage(file="Icons/red.png")
pink_theme = tk.PhotoImage(file="Icons/pink.png")

# adding command in themes menu
# variable for theme to change
theme_choice = tk.StringVar()

color_icons = (white_theme, grey_theme, dark_theme, red_theme, pink_theme)


color_dict = {
    'White Theme': '#ffffff',
    'Grey Theme': '#e0e0e0',
    'Dark Theme': '#2d2d2d',
    'Red Theme': '#ffe8e8',
    'Pink Theme': '#474747'
}
theme_choice.set(color_dict['White Theme'])


####################      THEME menu icons options END   ######################

# -----------------&&&&&&&&&&&&&&&&&&& MAIN MENU ENDs  &&&&&&&&&&&&&&&&&-----------------------#


###################################### TOOL BAR START #########################################
###################################### TOOL BAR START #########################################
###################################### TOOL BAR START #########################################

tool_bar = tk.Label(root, border=2, relief=tk.GROOVE, bg="black")
tool_bar.pack(side=tk.TOP,fill=tk.X)

font_tuple = font.families()

# font box
font_family = tk.StringVar()
font_name_label = tk.Label(tool_bar, text="Font Falimy :", bg="black", fg='white')
font_name_label.grid(row=0, column=0, padx=5, pady=(2,0))
fontbox = ttk.Combobox(tool_bar, width=25, textvariable=font_family, state="readonly")
fontbox['values'] = font_tuple
# font_tuple.index('Arial') ka matlb ye iska index number return karega as integer
fontbox.current(font_tuple.index('Arial'))
fontbox.grid(row=0, column=1, padx=5, pady=(2,0))

## size box
font_size_label = tk.Label(tool_bar, text="Font Size :", bg="black", fg='white')
font_size_label.grid(row=0, column=2, padx=5, pady=(2,0))
size_var = tk.IntVar()
size_var.set(12)
font_size = ttk.Combobox(tool_bar, width=8, textvariable=size_var, state="readonly")
font_size['values'] = tuple(range(6,80))
# font_size.current(12)
font_size.grid(row=0, column=3, padx=5, pady=(2,0))

## BOLD, Italic, alignment icons and button#
## BOLD, Italic, alignment icons and button#
## BOLD, Italic, alignment icons and button#
bold_icon = tk.PhotoImage(file="icons/bold.png")
bold_button = ttk.Button(tool_bar, image=bold_icon)
bold_button.grid(row=0, column=4, padx=5, pady=(2,0))

italic_icon = tk.PhotoImage(file="icons/italic.png")
italic_button = ttk.Button(tool_bar, image=italic_icon)
italic_button.grid(row=0, column=5, padx=5, pady=(2,0))

underline_icon = tk.PhotoImage(file="icons/underline.png")
underline_button = ttk.Button(tool_bar, image=underline_icon)
underline_button.grid(row=0, column=6, padx=5, pady=(2,0))

#### Font color button and icon ###
#### Font color button and icon ###
font_color_icon = tk.PhotoImage(file="icons/color.png")
font_color_button = ttk.Button(tool_bar, image=font_color_icon)
font_color_button.grid(row=0, column=7, padx=5, pady=(2, 0))

#### Align Text button and icon ###             
# #### Align Text button and icon ##### 
#   #### Align Text button and icon ###

align_left_icon = tk.PhotoImage(file="icons/left.png")
align_left_button = ttk.Button(tool_bar, image=align_left_icon)
align_left_button.grid(row=0, column=8, padx=5, pady=(2,0))

align_center_icon = tk.PhotoImage(file="icons/center.png")
align_center_button = ttk.Button(tool_bar, image=align_center_icon)
align_center_button.grid(row=0, column=9, padx=5, pady=(2,0))

align_right_icon = tk.PhotoImage(file="icons/right.png")
align_right_button = ttk.Button(tool_bar, image=align_right_icon)
align_right_button.grid(row=0, column=10, padx=5, pady=(2,0))

# -----------------&&&&&&&&&&&&&&&&&&& TOOL BAR ENDS  &&&&&&&&&&&&&&&&&-----------------------#






###################################### Text Editor Start #########################################

text_editor = tk.Text(root, padx=10, pady=10)
text_editor.config(wrap="word", relief=tk.FLAT)

y_scroll_bar = tk.Scrollbar(root)
text_editor.focus_set()
y_scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
y_scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=y_scroll_bar.set)


# -----------------&&&&&&&&&&&&&&&&&&& TEXT EDITOR ENDS  &&&&&&&&&&&&&&&&&-----------------------#


###################################### MAIN STATUS BAR Start #########################################

status_bar = tk.Label(root, text='Status Bar', bg='black', fg='white')
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# -----------------&&&&&&&&&&&&&&&&&&& MAIN STATUS BAR ENDs  &&&&&&&&&&&&&&&&&-----------------------#


###################################### MAIN MENU FUNCTIONALITY Start #########################################
###################################### MAIN MENU FUNCTIONALITY Start #########################################
###################################### MAIN MENU FUNCTIONALITY Start #########################################
###################################### MAIN MENU FUNCTIONALITY Start #########################################
###################################### MAIN MENU FUNCTIONALITY Start #########################################
###################################### MAIN MENU FUNCTIONALITY Start #########################################
###################################### MAIN MENU FUNCTIONALITY Start #########################################
updated_it = False
file = ''


def new_file(event=None):
    global file, updated_it
    if updated_it == False:
        file = ''
        root.title("Untitled - Shaheer's Editor")
        text_editor.delete(1.0, 'end')
    elif updated_it == True:
        newbox = messagebox.askyesnocancel('Warning', "Do you want to Save this file or not?")
        if newbox == True:
            save_file()
            updated_it = False
            new_file()
        elif newbox == False:
            file = ''
            root.title("Untitled - Shaheer's Editor")
            text_editor.delete(1.0, 'end')


def open_file(event=None):
    global file, updated_it
    # os. get current working directory (initial working)
    file = filedialog.askopenfilename(
                                    initialdir=os.getcwd, title='Select File',
                                    filetypes=(('Text Files', "*.txt"), ("Python files","*.py"),("All Files", "*.*"))
                                    )
    try:
        with open(file, 'r') as f:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(tk.INSERT, f.read())
    except FileNotFoundError:
        return
    root.title(f"{os.path.basename(file)} - Shaheer's Editor")
    updated_it = False


def save_file(event=None):
    global file, updated_it
    x_content = text_editor.get(1.0, tk.END)
    try:
        if file == "":
            file = filedialog.asksaveasfilename(
                    defaultextension=".txt",
                    filetypes=(('Text Files', "*.txt"), ("Python files", "*.py"), ("All Files", "*.*")))
            if file != "":
                f = open(file, "w")
                f.write(x_content)
                root.title(f"{os.path.basename(file)} - Shaheer's Editor")
                f.close()
        else:
            f = open(file, "w")
            f.write(x_content)
            f.close()
        updated_it = False
    except FileNotFoundError:
        return


def save_as(event=None):
    global file, updated_it
    try:
        x_content = str(text_editor.get(1.0, tk.END))
        file = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=(('Text Files', "*.txt"), ("Python files","*.py"),("All Files", "*.*")))
        f = open(file, "w")
        f.write(x_content)
        f.close()
    except FileNotFoundError:
        return
    updated_it = False


def quit_it(event=None):
    if updated_it == False:
        root.destroy()
    elif updated_it == True:
        mbox = messagebox.askyesnocancel('Warning', "Do you want to Save this file or not?")
        if mbox == True:
            save_file()
            root.destroy()
        elif mbox == False:
            root.destroy()


# adding command in file menu
file_menu.add_command(label="New", image=new_icon, compound = tk.LEFT, accelerator = "Ctrl+N", command=new_file)
file_menu.add_command(label="Open", image=open_icon, compound = tk.LEFT, accelerator = "Ctrl+O", command=open_file)
file_menu.add_command(label="Save", image=save_icon, compound = tk.LEFT, accelerator = "Ctrl+S", command=save_file)
file_menu.add_command(label="Save as", image=save_as_icon, compound = tk.LEFT, accelerator = "Ctrl+Alt+S", command=save_as)
file_menu.add_command(label="Exit", image=exit_icon, compound = tk.LEFT, accelerator = "Ctrl+Q", command=quit_it)


####################################  COMMAND FUNCTIONALITIES ####################
####################################  COMMAND FUNCTIONALITIES ####################
####################################  COMMAND FUNCTIONALITIES ####################
####################################  COMMAND FUNCTIONALITIES ####################
def cut():
    text_editor.event_generate(("<<Cut>>"))


def copy():
    text_editor.event_generate(("<<Copy>>"))


def paste():
    text_editor.event_generate(("<<Paste>>"))


################################     FIND FUNCTION     #######################
def find_func(event=None):
    def find_it_button():
        word = text_find_entry.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')

    def replace_it_button():
        word = text_find_entry.get()
        replace = text_replace_entry.get()
        content = text_editor.get(1.0, tk.END)
        text_editor.tag_remove('match', '1.0', tk.END)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, content.replace(word, replace))
    find_dialogue = tk.Toplevel()
    find_dialogue.geometry("450x250")
    find_dialogue.title('Find')
    find_dialogue.resizable(0, 0)

    find_frame = ttk.LabelFrame(find_dialogue, text="Find/Replace")
    find_frame.pack(pady=20)
    # label
    text_find_label = ttk.Label(find_frame, text="Find : ")
    text_replace_label = ttk.Label(find_frame, text="Replace : ")
    
    # Entry
    text_find_entry = ttk.Entry(find_frame, width=30)
    text_replace_entry = ttk.Entry(find_frame, width=30)

    # Button
    find_button = ttk.Button(find_frame, text="Find", command=find_it_button)
    replace_button = ttk.Button(find_frame, text="Replace", command=replace_it_button)

    # label grid
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)
    
    # entry grid
    text_find_entry.grid(row=0, column=1, padx=4, pady=4, columnspan=2)
    text_replace_entry.grid(row=1, column=1, padx=4, pady=4, columnspan=2)

    # Button grid
    find_button.grid(row=3, column=1, padx=4, pady=4)
    replace_button.grid(row=3, column=2, padx=4, pady=4)
    find_dialogue.mainloop()


def clear_all(root):
    text_editor.delete(1.0, tk.END)


# adding command in edit menu
# adding command in edit menu
edit_menu.add_command(label="Copy", image=copy_icon, compound = tk.LEFT, accelerator = "Ctrl+C", command=copy)
edit_menu.add_command(label="Cut", image=cut_icon, compound = tk.LEFT, accelerator = "Ctrl+X", command=cut)
edit_menu.add_command(label="Paste", image=paste_icon, compound = tk.LEFT, accelerator = "Ctrl+V", command=paste)
edit_menu.add_command(label="Clear All", image=clear_icon, compound = tk.LEFT, accelerator = "Ctrl+Alt+C",
                      command=lambda: clear_all(root))
edit_menu.add_command(label="Find", image=find_icon, compound = tk.LEFT, accelerator = "Ctrl+F", command=find_func)


# adding checkbuttons in view menu
# adding checkbuttons in view menu
# adding checkbuttons in view menu
show_tool_var = tk.BooleanVar()
show_tool_var.set(True)
show_status_var = tk.BooleanVar()
show_status_var.set(True)


def hide_tool_bar():
    if show_tool_var.get() == False:
        tool_bar.pack_forget()
    else:
        text_editor.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)


def hide_status_bar():
    if show_status_var.get() == False:
        status_bar.pack_forget()
    else:
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)


view_menu.add_checkbutton(label="Tool Bar", onvalue=True, offvalue=False, variable=show_tool_var, image=tool_bar_icon,
                          compound=tk.LEFT, command=hide_tool_bar)
view_menu.add_checkbutton(label="Status Bar", onvalue=True, offvalue=False, variable=show_status_var, image=status_bar_icon,
                          compound=tk.LEFT, command=hide_status_bar)


# radio buttons for themes


def change_theme():
    chosen_theme = theme_choice.get()
    text_editor.config(bg=color_dict[chosen_theme])


count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icons[count], variable=theme_choice,
                                compound=tk.LEFT, command=change_theme)
    count += 1




# font family and font size functionality

text_editor.configure(font='Arial 12')

# theme_choice.set(color_dict['White Theme'])

current_font_family = 'Arial'
current_font_size = 12


def change_font(root):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))


def change_font_size(root):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))


fontbox.bind('<<ComboboxSelected>>', change_font)
font_size.bind('<<ComboboxSelected>>', change_font_size)

bold_or_not = 'normal'
underline_or_not = 'normal'
italic_or_not = 'roman'
######## BUTTON Functionality BOLD, Italic, underline ###############
######## BUTTON Functionality BOLD, Italic, underline ###############
######## BUTTON Functionality BOLD, Italic, underline ###############
# is me jis hisab se font ko set kiya gia hai is tarteeb ko bigarney se iski what lag jae gi
# 
# 
# BOLD FUNCTION


def do_it_bold(root):
    global bold_or_not
    # .actual ka method is lia bar bar apply kar rahe hain qk ye bar bar current data access karega or jis jaga
    # ka font bold karna hai waha k identifier ka name likh kr ['font'] b likhna hai taaa k font me har bar 
    # change detect ho
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        bold_or_not = 'bold'
        text_editor.configure(font=(current_font_family, current_font_size, underline_or_not, italic_or_not, bold_or_not))
    elif text_property.actual()['weight'] == 'bold':
        bold_or_not = 'normal'
        text_editor.configure(font=(current_font_family, current_font_size, underline_or_not, italic_or_not, bold_or_not))


bold_button.config(command=lambda: do_it_bold(root))


#
#  Italic Function
def do_it_italic(root):
    global italic_or_not
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        italic_or_not = 'italic'
        text_editor.configure(font=(current_font_family, current_font_size, underline_or_not, italic_or_not, bold_or_not))
    elif text_property.actual()['slant'] == 'italic':
        italic_or_not = 'roman'
        text_editor.configure(font=(current_font_family, current_font_size, underline_or_not, italic_or_not, bold_or_not))


italic_button.config(command=lambda: do_it_italic(root))


#
#  Underline Function

def do_it_underline(root):
    global underline_or_not
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        underline_or_not = 'underline'
        text_editor.configure(font=(current_font_family, current_font_size, underline_or_not, italic_or_not, bold_or_not))
    elif text_property.actual()['underline'] == 1:
        underline_or_not = 'normal'
        text_editor.configure(font=(current_font_family, current_font_size, underline_or_not, italic_or_not, bold_or_not))


underline_button.config(command=lambda: do_it_underline(root))


# font color functionality
# font color functionality
# font color functionality

def change_font_color():
    global color_var
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


font_color_button.config(command=change_font_color)


##### Align functionality #####
##### Align functionality #####
##### Align functionality #####
def align_left_func():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, 'end')
    text_editor.insert(tk.INSERT,text_content, 'left')


align_left_button.config(command=align_left_func)


def align_right_func():
    text_content = text_editor.get(1.0, tk.END)
    ##################### tagname    attribute=right
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, 'end')
    ################## insert , what_to_insert, tagname_for_functionality #
    text_editor.insert(tk.INSERT,text_content, 'right')


align_right_button.config(command=align_right_func)


def align_center_func():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, 'end')
    text_editor.insert(tk.INSERT,text_content, 'center')


align_center_button.config(command=align_center_func)


###################          STATUS BAR FUNCTIONALITY          #################
###################          STATUS BAR FUNCTIONALITY          #################
###################          STATUS BAR FUNCTIONALITY          #################
###################          STATUS BAR FUNCTIONALITY          #################

def update_status_bar(root):
    global updated_it
    if text_editor.edit_modified():
        updated_it = True
        words = len(text_editor.get(1.0, 'end').split())
        # -1c for avoid reading new line /n character
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f"Character :  {characters}, Words : {words}")
        text_editor.tag_remove('match', '1.0', tk.END)

    text_editor.edit_modified(False)


text_editor.bind('<<Modified>>', update_status_bar)


# -----------------&&&&&&&&&&&&&&&&&&& MAIN MENU FUNCTIONALITY ENDs  &&&&&&&&&&&&&&&&&-----------------------#


# BIND SHORTCUT KEYS
root.bind('<Control-n>', new_file)
root.bind('<Control-N>', new_file)
root.bind('<Control-o>', open_file)
root.bind('<Control-O>', open_file)
root.bind('<Control-S>', save_file)
root.bind('<Control-s>', save_file)
root.bind('<Control-Alt-S>', save_as)
root.bind('<Control-Alt-s>', save_as)
root.bind('<Control-q>', quit_it)
root.bind('<Control-Q>', quit_it)
root.bind('<Alt-F4>', quit_it)
root.bind('<Control-Alt-C>', clear_all)
root.bind('<Control-Alt-c>', clear_all)
root.bind('<Control-F>', find_func)
root.bind('<Control-f>', find_func)
root.bind('<Control-B>', do_it_bold)
root.bind('<Control-b>', do_it_bold)
root.bind('<Control-i>', do_it_italic)
root.bind('<Control-I>', do_it_italic)
root.bind('<Control-U>', do_it_underline)
root.bind('<Control-u>', do_it_underline)


root.config(menu=main_menu)
root.mainloop()
