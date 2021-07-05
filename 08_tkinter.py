"""
Tkinter.
I cannot run this code in a vertual enviroment.
There are many events thet I din't use this time.

Widget common options.
anchor: Position.
width
height
padx
pady
bd: Border width.
relief
bg: Background color.
fg: Foreground color.
highlightbackground
highlightcolor
highlightthickness
text
textvariable: Use a tk variable.
image
bitmap

How to change options after.
widget_name.config(option_name=values)

Tk variables is used as the textvariable.
var.set(): Set values.
var.get(): Get values.

The window(frame) size is determined by child widgets.
When keep the size of parent widgets, use "frame_name.propagate(0)"
If you want to set the parent wiget size, you must use it.

pack(), grid() and place() have many methods.
They can extend widget frame.
"""

import os
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

def main():

    print('Hello')
    TkGUI()


class TkGUI():
    """
    Create a Tk GUI window.
    """

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('tk GUI')
        self.frame = tk.Frame(self.root,
                              #width=800,
                              #height=600,
                              bg='gray',
                              )
        self.frame.pack()
        self.frames()
        #self.frame.propagate(0)
        #self.frame.grid_propagate(0)
        self.widgets()
        self.root.mainloop()

    def frames(self):
        self.frame00 = tk.Frame(self.frame,
                                width=300,
                                height=300,
                                relief='solid',
                                borderwidth=1,
                                bg='#ffaaaa',
                                padx=10,
                                pady=10,
                                )
        self.frame01 = tk.Frame(self.frame,
                                width=300,
                                height=300,
                                relief='solid',
                                borderwidth=1,
                                bg='#aaffaa',
                                padx=10,
                                pady=10,
                                )
        self.frame02 = tk.Frame(self.frame,
                                width=300,
                                height=350,  # Longest in frames.
                                relief='solid',
                                borderwidth=1,
                                bg='#aaaaff',
                                padx=10,
                                pady=10,
                                )
        self.frame03 = tk.Frame(self.frame,
                                width=300,
                                height=300,
                                relief='solid',
                                borderwidth=1,
                                bg='#aaaaaa',
                                padx=10,
                                pady=10,
                                )
        # Frames position.
        self.frame00.pack(side=tk.LEFT, fill=tk.Y)
        self.frame01.pack(side=tk.LEFT, fill=tk.Y)
        self.frame02.pack(side=tk.LEFT, fill=tk.Y)
        self.frame03.pack(side=tk.LEFT, fill=tk.Y)

        self.frame00.grid_propagate(0)
        self.frame01.pack_propagate(0)
        self.frame02.pack_propagate(0)
        self.frame03.pack_propagate(0)

    def widgets(self):
        self.widgets_frame00(self.frame00)
        self.widgets_frame01(self.frame01)
        self.widgets_frame02(self.frame02)
        self.widgets_frame03(self.frame03)
        self.btn = tk.Button(self.root,
                             text='Message box',
                             )
        self.btn.bind('<Button-1>', self.btn_click)
        self.btn.pack()

    def widgets_frame00(self, parent):
        """
        Entory, text and scrolledtext.
        """

        self.entry_lbl = tk.Label(parent,
                                  text='Entry',
                                  fg='#000000',
                                  bg=parent.cget('bg'),
                                  )
        self.entry = tk.Entry(parent,
                              width=20,
                              fg='#000000',
                              bg='#ffffff',
                              )
        self.entry.insert(tk.END, 'Entry')

        self.text_lbl = tk.Label(parent,
                                 text='Text',
                                 fg='#000000',
                                 bg=parent.cget('bg'),
                                 )
        self.text = tk.Text(parent,
                            width=30,
                            height=5,
                            fg='#000000',
                            bg='#ffffff',
                            )
        self.text.insert(tk.END, 'Text')

        self.scrolled_text_lbl = tk.Label(parent,
                                          text='Scrolled text',
                                          fg='#000000',
                                          bg=parent.cget('bg'),
                                          )
        self.scrolled_text = ScrolledText(parent,
                                           width=20,
                                           height=5,
                                           fg='#000000',
                                           bg='#ffffff',
                                           )
        self.scrolled_text.insert(tk.END, 'Scrolled text')

        self.btn00 = tk.Button(parent,
                               text='Button00',
                               fg='#ffffff',
                               bg='#ff0000',
                               )
        self.btn00.bind('<Button-1>', self.btn00_click)

        self.entry_lbl.grid(row=0, column=0, sticky=tk.W)
        self.entry.grid(row=0, column=1, sticky=tk.W)
        self.text_lbl.grid(row=1, column=0, columnspan=2, sticky=tk.W)
        self.text.grid(row=2, column=1, sticky=tk.W)
        self.scrolled_text_lbl.grid(row=3, column=0, columnspan=2, sticky=tk.W)
        self.scrolled_text.grid(row=4, column=1, sticky=tk.W+tk.E)
        self.btn00.grid(row=5, column=1, sticky=tk.E, pady=10)

    def widgets_frame01(self, parent):

        self.check_btn_frame = tk.LabelFrame(parent,
                                             text='Check button',
                                             padx=10,
                                             pady=10,
                                             fg='#000000',
                                             bg=parent.cget('bg'),
                                             )
        self.check_btn_val0 = tk.StringVar()
        self.check_btn_val1 = tk.StringVar()
        self.check_btn_val2 = tk.StringVar()
        self.check_btn_val0.set('Check 0')
        self.check_btn_val1.set('Uncheck 1')
        self.check_btn_val2.set('Uncheck 2')
        self.check_btn0 = tk.Checkbutton(self.check_btn_frame,
                                         text='Check button 0',
                                         variable=self.check_btn_val0,
                                         onvalue='Check 0',
                                         offvalue='Uncheck 0',
                                         fg='#000000',
                                         bg=parent.cget('bg'),
                                         )
        self.check_btn1 = tk.Checkbutton(self.check_btn_frame,
                                         text='Check button 1',
                                         variable=self.check_btn_val1,
                                         onvalue='Check 1',
                                         offvalue='Uncheck 1',
                                         fg='#000000',
                                         bg=parent.cget('bg'),
                                         )
        self.check_btn2 = tk.Checkbutton(self.check_btn_frame,
                                         text='Check button 2',
                                         variable=self.check_btn_val2,
                                         onvalue='Check 2',
                                         offvalue='Uncheck 2',
                                         fg='#000000',
                                         bg=parent.cget('bg'),
                                         )
        self.check_btn0.pack(anchor=tk.W)
        self.check_btn1.pack(anchor=tk.W)
        self.check_btn2.pack(anchor=tk.W)

        self.radio_btn_frame = tk.LabelFrame(parent,
                                             text='Radio button',
                                             padx=10,
                                             pady=10,
                                             fg='#000000',
                                             bg=parent.cget('bg'),
                                             )
        self.radio_btn_val = tk.StringVar(value='Radio 0')
        #self.radio_btn_val = tk.StringInt(value=0)
        self.radio_btn0 = tk.Radiobutton(self.radio_btn_frame,
                                         text='Radio button 0',
                                         value='Radio 0',
                                         variable=self.radio_btn_val,
                                         fg='#000000',
                                         bg=parent.cget('bg'),
                                         )
        self.radio_btn1 = tk.Radiobutton(self.radio_btn_frame,
                                         text='Radio button 1',
                                         value='Radio 1',
                                         variable=self.radio_btn_val,
                                         fg='#000000',
                                         bg=parent.cget('bg'),
                                         )
        self.radio_btn2 = tk.Radiobutton(self.radio_btn_frame,
                                         text='Radio button 2',
                                         value='Radio 2',
                                         variable=self.radio_btn_val,
                                         fg='#000000',
                                         bg=parent.cget('bg'),
                                         )
        self.radio_btn0.pack(anchor=tk.W)
        self.radio_btn1.pack(anchor=tk.W)
        self.radio_btn2.pack(anchor=tk.W)

        self.btn01 = tk.Button(parent,
                               text='Button01',
                               fg='#ffffff',
                               bg='#00ff00',
                               )
        self.btn01.bind('<Button-1>', self.btn01_click)

        self.check_btn_frame.pack()
        self.radio_btn_frame.pack()
        self.btn01.pack(pady=10)

    def widgets_frame02(self, parent):

        self.list_box_lbl = tk.Label(parent,
                                     text='List box',
                                     fg='#000000',
                                     bg=parent.cget('bg'),
                                     )
        self.list_ref = ['List 0', 'List 1', 'List 2']
        self.list_contents = tk.StringVar(value=self.list_ref)
        self.list_box = tk.Listbox(parent,
                                   listvariable=self.list_contents,
                                   height=5,
                                   fg='#000000',
                                   bg='#ffffff',
                                   )
        self.list_box.insert('end', 'List 3')
        self.list_box.insert('end', 'List 4')
        self.list_box.insert('end', 'List 5')

        self.spin_box_lbl = tk.Label(parent,
                                     text='Spin box',
                                     fg='#000000',
                                     bg=parent.cget('bg'),
                                     )
        self.spin_box_val = tk.StringVar(value='aaaaa')
        self.spin_box = tk.Spinbox(parent,
                                   format='%3.1f',
                                   from_=0,
                                   to=3,
                                   increment=0.1,
                                   state='readonly',
                                   fg='#ffffff',
                                   #bg='#ffffff',
                                   )

        self.menu_button = tk.Menubutton(parent,
                                         text='Menu button',
                                         fg='#000000',
                                         bg='#ffffff',
                                         )
        self.menu_button.menu = tk.Menu(self.menu_button)
        self.menu_button['menu'] = self.menu_button.menu
        self.menu_button.menu.add_command(label='Select a folder', command=self.menu00)
        self.menu_button.menu.add_command(label='Select a file', command=self.menu01)
        self.menu_button.menu.add_command(label='Close', command=self.menu02)

        self.scale = tk.Scale(parent,
                              from_=-10,
                              to=10,
                              orient='horizontal',
                              fg='#000000',
                              bg='#ffffff',
                              )


        self.btn02 = tk.Button(parent,
                               text='Button02',
                               fg='#ffffff',
                               #bg='#0000ff',
                               )
        self.btn02.bind('<Button-1>', self.btn02_click)

        self.list_box_lbl.pack()
        self.list_box.pack()
        self.spin_box_lbl.pack()
        self.spin_box.pack()
        self.menu_button.pack(pady=10)
        self.scale.pack()
        self.btn02.pack(pady=10)

    def widgets_frame03(self, parent):

        self.pos_x = tk.StringVar()
        self.pos_y = tk.StringVar()
        self.x_val = 0
        self.y_val = 0
        self.pos_x.set("x: {}".format(self.x_val))
        self.pos_y.set("y: {}".format(self.y_val))
        self.canvas_lbl = tk.Label(parent,
                                   text='Canvas',
                                   fg='#000000',
                                   bg=parent.cget('bg'),
                                   )
        self.canvas_lbl_x = tk.Label(parent,
                                     textvariable=self.pos_x,
                                     fg='#000000',
                                     bg=parent.cget('bg'),
                                     )
        self.canvas_lbl_y = tk.Label(parent,
                                     textvariable=self.pos_y,
                                     fg='#000000',
                                     bg=parent.cget('bg'),
                                     )

        self.canvas = tk.Canvas(parent,
                                bg='#ffffff',
                                borderwidth=0,
                                highlightthickness=0,
                                cursor='pencil',
                                )
        self.canvas.create_line(0, 0,
                                50, 50,
                                100, 0,
                                150, 50,
                                fill='#000000',
                                )
        self.canvas.create_line(50, 0,
                                100, 50,
                                150, 0,
                                200, 50,
                                width=3,
                                dash=(10, 5),
                                fill='#000000',
                                smooth=True,
                                arrow=tk.LAST,
                                arrowshape=(20, 20, 10),
                                capstyle=tk.ROUND,
                                )
        self.canvas.create_oval(50, 50,
                                100, 100,
                                outline='#000000',
                                fill='#ff0000',
                                )
        self.canvas.create_arc(100, 100,
                               200, 200,
                               start=0,
                               extent=90,
                               outline='#000000',
                               fill='#00ff00',
                               )
        self.canvas.create_rectangle(30, 150,
                                     80, 180,
                                     outline='#000000',
                                     fill='#0000ff',
                                     )
        self.canvas.create_polygon(200, 180,
                                   250, 220,
                                   250, 250,
                                   150, 250,
                                   150, 220,
                                   outline='#000000',
                                   fill='#ffff00',
                                   activefill='#00ffff'
                                   )
        self.canvas.create_text(50, 220,
                                text='Hello',
                                fill='#000000',
                                font=('', 30),
                                )
        self.canvas.bind('<Motion>', self.mouse_pos)
        self.canvas.bind('<Button-1>', self.draw)
        self.canvas.bind('<Button1-Motion>', self.drag)

        self.canvas_lbl.pack()
        self.canvas_lbl_x.pack()
        self.canvas_lbl_y.pack()
        self.canvas.pack(expand=True, fill=tk.BOTH)



    def btn_click(self, event):
        """
        Callback functions.
        """

        tk.messagebox.showinfo('Messagebox',
                               'Hello',
                               )

    def btn00_click(self, event):
        """
        Callback functions.
        """

        self.info_entry = self.entry.get()
        self.info_text = self.text.get('1.0', 'end-1c')
        self.info_scrolled_text = self.scrolled_text.get('1.0', 'end-1c')
        print(self.info_entry)
        print(self.info_text)
        print(self.info_scrolled_text)

    def btn01_click(self, event):
        """
        Callback functions.
        """

        self.info_check0 = self.check_btn_val0.get()
        self.info_check1 = self.check_btn_val1.get()
        self.info_check2 = self.check_btn_val2.get()
        self.info_radio = self.radio_btn_val.get()
        print(self.info_check0)
        print(self.info_check1)
        print(self.info_check2)
        print(self.info_radio)

    def btn02_click(self, event):
        """
        Callback functions.
        """

        self.info_list = self.list_box.curselection()
        if self.info_list:
            self.info_list = self.list_box.get(self.info_list[0])
        self.info_spin = self.spin_box.get()
        self.info_scale = self.scale.get()
        print(self.info_list)
        print(self.info_spin)
        print(self.info_scale)

    def menu00(self):
        """
        Callback functions.
        Get selected directory path.
        """

        self.dir_path = __file__
        self.dir_path = os.path.split(self.dir_path)[0]
        self.dir_path = filedialog.askdirectory(initialdir=self.dir_path)
        print(self.dir_path)

    def menu01(self):
        """
        Callback functions.
        Get selected file path.
        """

        self.dir_path = __file__
        self.dir_path = os.path.split(self.dir_path)[0]
        self.typ = [('', '*')]
        self.file_path = filedialog.askopenfilename(filetypes=self.typ, initialdir=self.dir_path)
        print(self.file_path)

    def menu02(self):
        """
        Callback functions.
        Close this root.
        """

        print('Close the GUI window.')
        self.root.destroy()

    def mouse_pos(self, event):
        """
        Callback functions.
        Update x and y positions.
        """

        self.x_val = event.x
        self.y_val = event.y
        self.pos_x.set("x: {}".format(self.x_val))
        self.pos_y.set("y: {}".format(self.y_val))

    def draw(self, event):
        """
        Callback functions.
        Draw a circle.
        """

        self.r = 10
        self.x = self.canvas.winfo_width()
        self.y = self.canvas.winfo_height()
        self.x = int(self.x) / 2
        self.y = int(self.y) / 2
        self.oval = self.canvas.create_oval(self.x-self.r, self.y-self.r,
                                            self.x+self.r, self.y+self.r,
                                            outline='#000000',
                                            fill='#000000',
                                            )

    def drag(self, event):
        """
        Callback functions.
        Update the x and y positions.
        Drag the circle.
        """

        self.x_val = event.x
        self.y_val = event.y
        self.pos_x.set("x: {}".format(self.x_val))
        self.pos_y.set("y: {}".format(self.y_val))

        self.x = event.x
        self.y = event.y
        self.canvas.coords(self.oval,
                           self.x-self.r, self.y-self.r,
                           self.x+self.r, self.y+self.r,
                           )


if __name__ == '__main__':
    main()
