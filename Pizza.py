def main():

window = Tk()

window.geometry('300x250')

window.title("Pizza Application")

window.configure(background='#87CEEB')


# Top left frame

top_left_frame = Frame(window, background='#87CEEB')

top_left_frame.pack()


# Top right frame

top_right_frame = Frame(window, background='#87CEEB')

top_right_frame.pack()


# Bottom frame

bottom_frame = Frame(window, background='#87CEEB')

bottom_frame.pack()


# Top left label

size_label = Label(top_left_frame, text="Size", background='#87CEEB')

size_label.pack()


# Top right label

topping_label = Label(top_right_frame, text="Topping", background='#87CEEB')

topping_label.pack()


# Bottom label

tip_label = Label(bottom_frame, text="Tip", background='#87CEEB')

tip_label.pack()


# Size buttons (S, M, L, XL)

size_s = Button(top_left_frame, text="S", command=s_size)

size_s.pack()


size_m = Button(top_left_frame, text="M", command=m_size)

size_m.pack()


size_l = Button(top_left_frame, text="L", command=l_size)

size_l.pack()


size_xl = Button(top_left_frame, text="XL", command=xl_size)

size_xl.pack()


# Topping buttons (1-4)

topping_1 = Button(top_right_frame, text="1", command=t1)

topping_1.pack()


topping_2 = Button(top_right_frame, text="2", command=t2)

topping_2.pack()


topping_3 = Button(top_right_frame, text="3", command=t3)

topping_3.pack()


topping_4 = Button(top_right_frame, text="4", command=t4)

topping_4.pack()


# Premium Topping buttons (1-4)

p_topping_1 = Button(top_right_frame, text="1", command=pt1)

p_topping_1.pack()


p_topping_2 = Button(top_right_frame, text="2", command=pt2)

p_topping_2.pack()


p_topping_3 = Button(top_right_frame, text="3", command=pt3)

p_topping_3.pack()


p_topping_4 = Button(top_right_frame, text="4", command=pt4)

p_topping_4.pack()


# Tip buttons (0%, 15%, 18%, 20%)

tip_0 = Button(bottom_frame, text="0%", command=t0)

tip_0.pack()


tip_15 = Button(bottom_frame, text="15%", command=t15)

tip_15.pack()


tip_18 = Button(bottom_frame, text="18%", command=t18)

tip_18.pack()


tip_20 = Button(bottom_frame, text="20%", command=t20)

tip_20.pack()


# Total label

total_label = Label(window, text="Total: ", background='#87CEEB')

total_label.pack()


window.mainloop()


# SIZE

def s_size():

global size

size = 5


def m_size():

global size

size = 8


def l_size():

global size

size = 12


def xl_size():

global size

size = 15


# Topping

def t1():

global topping

topping = 1


def t2():

global topping

topping = 2


def t3():

global topping

topping = 3


def t4():

global topping

topping = 4


# Premium Topping

def pt1():

global p_topping

p_topping = 3


def pt2():

global p_topping

p_topping = 5


def pt3():

global p_topping

p_topping = 7


def pt4():

global p_topping

p_topping = 9


# Tip

def t0():

global tip

tip = 0


def t15():

global tip

tip = 0.15


def t18():

global tip

tip = 0.18


def t20():

global tip

tip = 0.20


main()

