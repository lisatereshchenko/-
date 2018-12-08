# coding=utf-8
import Tkinter

memory, do, IHBC, SHBD, curval, SD = "0", "", True, False, "", False

Tk = Tkinter.Tk
Label = Tkinter.Label
Button = Tkinter.Button


def noth(e):
    ol["font"] = "arial 12"
    ol["width"] = 32
    ol["height"] = 2
    pass


def refill():
    if len(ol["text"]) > 2 and ol["text"][-2:] == ".0":
        ol["text"] = ol["text"][:-2]
    if "." not in ol["text"]:
        if len(ol["text"]) > 15:
            removeall()
            ol["text"] = "Переполнение"
    else:
        if len(ol["text"]) > 15:
            if ol["text"].index(".") <= 14:
                ol["text"] = str(round(float(ol["text"]), 15 - ol["text"].index(".")))
            else:
                removeall()
                ol["text"] = "Переполнение"


def remove(e=""):
    ol["text"] = ol["text"][: len(ol["text"]) - 1] if len(ol["text"]) > 1 else "0"


def removetext(e=""):
    ol["text"], curval = "0", ""


def removeall():
    global memory, IHBC, SHBD, curval, SD
    ol["text"], l["text"], memory, curval, do, IHBC, SHBD, ml["text"], SD = (
        "0",
        "",
        "0",
        "",
        "",
        False,
        False,
        "",
        False,
    )


def doing(x):
    global SHBD, IHBC, curval, do, SD
    if IHBC:
        if not SD:
            l["text"] += ol["text"] + " " + x + " "
        else:
            l["text"] += x + " "
        if ol["text"] == "0" and do == "/":
            removeall()
            ol["text"] = "Деление на ноль"
        if curval:
            ol["text"] = (
                str(float(curval) + float(ol["text"]))
                if do == "+"
                else str(float(curval) - float(ol["text"]))
                if do == "-"
                else str(float(curval) * float(ol["text"]))
                if do == "*"
                else str(float(curval) / float(ol["text"]))
                if do == "/"
                else ol["text"]
            )
        refill()
        IHBC, SHBD, curval, SD = (
            False,
            True,
            ol["text"] if ol["text"] != "Переполнение" else "",
            False,
        )
    else:
        l["text"] = (
            l["text"] + x + " " if l["text"][-2] == ")" else l["text"][:-2] + x + " "
        )


def wrinm():
    global memory
    memory, ml["text"] = ol["text"], "M"


def refrm():
    global IHBC
    ol["text"], IHBC = memory, True


def memoryplus():
    global memory
    memory = str(float(memory) + float(ol["text"]))
    if len(memory) > 2 and memory[-2:] == ".0":
        memory = memory[:-2]


def delm():
    global memory
    memory, ml["text"] = "0", ""


def plus(e=""):
    global do
    doing("+")
    do = "+"


def divide(e=""):
    global do
    doing("/")
    do = "/"


def mult(e=""):
    global do
    doing("*")
    do = "*"


def perc(e=""):
    global do
    do, l["text"] = "%", l["text"] + ol["text"] + " % "


def sqr(e=""):
    global do, curval, IHBC, SHBD, SD
    l["text"] += "sqrt(" + ol["text"] + ") "
    if float(ol["text"]) >= 0:
        ol["text"] = str(float(ol["text"]) ** 0.5)
        refill()
        IHBC, SHBD, SD = True, False, True
    else:
        removeall()
        ol["text"] = "Ошибка"


def minus(e=""):
    global do
    doing("-")
    do = "-"


def onedx(e=""):
    global do, curval, IHBC, SHBD, SD
    l["text"] += "1/" + ol["text"] + " "
    if float(ol["text"]) != 0:
        ol["text"] = str(1 / float(ol["text"]))
        refill()
        IHBC, SHBD, SD = True, False, True
    else:
        removeall()
        ol["text"] = "Ошибка"


def dot(e=""):
    global SHBD, IHBC
    ol["text"], IHBC, SHBD = (
        ol["text"] + "."
        if len(ol["text"]) < 14 and not SHBD
        else "0."
        if ol["text"] == "0" or SHBD
        else ol["text"],
        True,
        False,
    )


def enter(e=""):
    global SHBD, IHBC, curval, do
    if IHBC:
        l["text"] = ""
        if ol["text"] == "0" and do == "/":
            removeall()
            ol["text"] = "Деление на ноль"
        if curval:
            ol["text"] = (
                str(float(curval) + float(ol["text"]))
                if do == "+"
                else str(float(curval) - float(ol["text"]))
                if do == "-"
                else str(float(curval) * float(ol["text"]))
                if do == "*"
                else str(float(curval) / float(ol["text"]))
            )
        refill()
        IHBC, SHBD, curval, do = True, True, "", ""


def negate(e=""):
    if ol["text"] != "0":
        ol["text"] = str(-float(ol["text"]))
    if len(ol["text"]) > 2 and ol["text"][-2:] == ".0":
        ol["text"] = ol["text"][:-2]


def place0(e=""):
    global SHBD, IHBC, SD
    if not SD:
        ol["text"], IHBC, SHBD = (
            ol["text"] + "0"
            if ol["text"] != "0" and len(ol["text"]) < 14 and not SHBD
            else "0"
            if ol["text"] == "0" or SHBD
            else ol["text"],
            True,
            False,
        )
    else:
        ol["text"], SD, IHBC, SHBD = "0", False, True, False
        i = len(l["text"]) - 1
        while (
            i != 0
            and l["text"][i] != "+"
            and l["text"][i] != "-"
            and l["text"][i] != "*"
            and l["text"][i] != "/"
        ):
            l["text"], i = l["text"][:i], i - 1
        l["text"] += " "


def place1(e=""):
    global SHBD, IHBC, SD
    if not SD:
        ol["text"], IHBC, SHBD = (
            ol["text"] + "1"
            if ol["text"] != "0" and len(ol["text"]) < 14 and not SHBD
            else "1"
            if ol["text"] == "0" or SHBD
            else ol["text"],
            True,
            False,
        )
    else:
        ol["text"], SD, IHBC, SHBD = "1", False, True, False
        i = len(l["text"]) - 1
        while (
            i != 0
            and l["text"][i] != "+"
            and l["text"][i] != "-"
            and l["text"][i] != "*"
            and l["text"][i] != "/"
        ):
            l["text"], i = l["text"][:i], i - 1
        l["text"] += " "


def place2(e=""):
    global SHBD, IHBC, SD
    if not SD:
        ol["text"], IHBC, SHBD = (
            ol["text"] + "2"
            if ol["text"] != "0" and len(ol["text"]) < 14 and not SHBD
            else "2"
            if ol["text"] == "0" or SHBD
            else ol["text"],
            True,
            False,
        )
    else:
        ol["text"], SD, IHBC, SHBD = "2", False, True, False
        i = len(l["text"]) - 1
        while (
            i != 0
            and l["text"][i] != "+"
            and l["text"][i] != "-"
            and l["text"][i] != "*"
            and l["text"][i] != "/"
        ):
            l["text"], i = l["text"][:i], i - 1
        l["text"] += " "


def place3(e=""):
    global SHBD, IHBC, SD
    if not SD:
        ol["text"], IHBC, SHBD = (
            ol["text"] + "3"
            if ol["text"] != "0" and len(ol["text"]) < 14 and not SHBD
            else "3"
            if ol["text"] == "0" or SHBD
            else ol["text"],
            True,
            False,
        )
    else:
        ol["text"], SD, IHBC, SHBD = "3", False, True, False
        i = len(l["text"]) - 1
        while (
            i != 0
            and l["text"][i] != "+"
            and l["text"][i] != "-"
            and l["text"][i] != "*"
            and l["text"][i] != "/"
        ):
            l["text"], i = l["text"][:i], i - 1
        l["text"] += " "


def place4(e=""):
    global SHBD, IHBC, SD
    if not SD:
        ol["text"], IHBC, SHBD = (
            ol["text"] + "4"
            if ol["text"] != "0" and len(ol["text"]) < 14 and not SHBD
            else "4"
            if ol["text"] == "0" or SHBD
            else ol["text"],
            True,
            False,
        )
    else:
        ol["text"], SD, IHBC, SHBD = "4", False, True, False
        i = len(l["text"]) - 1
        while (
            i != 0
            and l["text"][i] != "+"
            and l["text"][i] != "-"
            and l["text"][i] != "*"
            and l["text"][i] != "/"
        ):
            l["text"], i = l["text"][:i], i - 1
        l["text"] += " "


def place5(e=""):
    global SHBD, IHBC, SD
    if not SD:
        ol["text"], IHBC, SHBD = (
            ol["text"] + "5"
            if ol["text"] != "0" and len(ol["text"]) < 14 and not SHBD
            else "5"
            if ol["text"] == "0" or SHBD
            else ol["text"],
            True,
            False,
        )
    else:
        ol["text"], SD, IHBC, SHBD = "5", False, True, False
        i = len(l["text"]) - 1
        while (
            i != 0
            and l["text"][i] != "+"
            and l["text"][i] != "-"
            and l["text"][i] != "*"
            and l["text"][i] != "/"
        ):
            l["text"], i = l["text"][:i], i - 1
        l["text"] += " "


def place6(e=""):
    global SHBD, IHBC, SD
    if not SD:
        ol["text"], IHBC, SHBD = (
            ol["text"] + "6"
            if ol["text"] != "0" and len(ol["text"]) < 14 and not SHBD
            else "6"
            if ol["text"] == "0" or SHBD
            else ol["text"],
            True,
            False,
        )
    else:
        ol["text"], SD, IHBC, SHBD = "6", False, True, False
        i = len(l["text"]) - 1
        while (
            i != 0
            and l["text"][i] != "+"
            and l["text"][i] != "-"
            and l["text"][i] != "*"
            and l["text"][i] != "/"
        ):
            l["text"], i = l["text"][:i], i - 1
        l["text"] += " "


def place7(e=""):
    global SHBD, IHBC, SD
    if not SD:
        ol["text"], IHBC, SHBD = (
            ol["text"] + "7"
            if ol["text"] != "0" and len(ol["text"]) < 14 and not SHBD
            else "7"
            if ol["text"] == "0" or SHBD
            else ol["text"],
            True,
            False,
        )
    else:
        ol["text"], SD, IHBC, SHBD = "7", False, True, False
        i = len(l["text"]) - 1
        while (
            i != 0
            and l["text"][i] != "+"
            and l["text"][i] != "-"
            and l["text"][i] != "*"
            and l["text"][i] != "/"
        ):
            l["text"], i = l["text"][:i], i - 1
        l["text"] += " "


def place8(e=""):
    global SHBD, IHBC, SD
    if not SD:
        ol["text"], IHBC, SHBD = (
            ol["text"] + "8"
            if ol["text"] != "0" and len(ol["text"]) < 14 and not SHBD
            else "8"
            if ol["text"] == "0" or SHBD
            else ol["text"],
            True,
            False,
        )
    else:
        ol["text"], SD, IHBC, SHBD = "8", False, True, False
        i = len(l["text"]) - 1
        while (
            i != 0
            and l["text"][i] != "+"
            and l["text"][i] != "-"
            and l["text"][i] != "*"
            and l["text"][i] != "/"
        ):
            l["text"], i = l["text"][:i], i - 1
        l["text"] += " "


def place9(e=""):
    global SHBD, IHBC, SD
    if not SD:
        ol["text"], IHBC, SHBD = (
            ol["text"] + "9"
            if ol["text"] != "0" and len(ol["text"]) < 14 and not SHBD
            else "9"
            if ol["text"] == "0" or SHBD
            else ol["text"],
            True,
            False,
        )
    else:
        ol["text"], SD, IHBC, SHBD = "9", False, True, False
        i = len(l["text"]) - 1
        while (
            i != 0
            and l["text"][i] != "+"
            and l["text"][i] != "-"
            and l["text"][i] != "*"
            and l["text"][i] != "/"
        ):
            l["text"], i = l["text"][:i], i - 1
        l["text"] += " "


main = Tk()
main.title("Калькулятор")
main["height"], main["width"] = 300, 308
main.resizable(False, False)
memory, do = "0", ""
ol = Label(
    main,
    anchor="e",
    fg="blue",
    font="arial 24",
    height=1,
    width=15,
    relief="sunken",
    text="0",
)
l = Label(main, anchor="e", font="arial 10", height=1, width=36, relief="sunken")
ml = Label(main, font="arial 25", height=1, width=1)
ol.place(x=10, y=5)
l.place(x=10, y=50)
ml.place(x=271, y=75)
buttons = [
    Button(main, text="Backspace", height=2, width=10, command=remove),
    Button(main, text="CE", height=2, width=10, command=removetext),
    Button(main, text="C", height=2, width=10, command=removeall),
    Button(main, text="MC", height=2, width=5, command=delm),
    Button(main, text="7", height=2, width=5, command=place7),
    Button(main, text="8", height=2, width=5, command=place8),
    Button(main, text="9", height=2, width=5, command=place9),
    Button(main, text="/", height=2, width=5, command=divide),
    Button(main, text="SQRT", height=2, width=5, command=sqr),
    Button(main, text="MR", height=2, width=5, command=refrm),
    Button(main, text="4", height=2, width=5, command=place4),
    Button(main, text="5", height=2, width=5, command=place5),
    Button(main, text="6", height=2, width=5, command=place6),
    Button(main, text="*", height=2, width=5, command=mult),
    Button(main, text="%", height=2, width=5, command=perc),
    Button(main, text="MS", height=2, width=5, command=wrinm),
    Button(main, text="1", height=2, width=5, command=place1),
    Button(main, text="2", height=2, width=5, command=place2),
    Button(main, text="3", height=2, width=5, command=place3),
    Button(main, text="-", height=2, width=5, command=minus),
    Button(main, text="1/x", height=2, width=5, command=onedx),
    Button(main, text="M+", height=2, width=5, command=memoryplus),
    Button(main, text="0", height=2, width=5, command=place0),
    Button(main, text="+/-", height=2, width=5, command=negate),
    Button(main, text=".", height=2, width=5, command=dot),
    Button(main, text="+", height=2, width=5, command=plus),
    Button(main, text="=", height=2, width=5, command=enter),
]
buttons[0].place(x=7, y=75)
buttons[1].place(x=95, y=75)
buttons[2].place(x=183, y=75)
x, y = 7, 120
for i in range(3, len(buttons)):
    buttons[i].place(x=x, y=y)
    x = x + 50 if x < 250 else 7
    y = y + 45 if x == 7 else y
main.bind("<Shift_L>", noth)
main.bind("<Shift_R>", noth)
main.bind("<BackSpace>", remove)
main.bind("<KeyPress-0>", place0)
main.bind("<KeyPress-1>", place1)
main.bind("<KeyPress-2>", place2)
main.bind("<KeyPress-3>", place3)
main.bind("<KeyPress-4>", place4)
main.bind("<KeyPress-5>", place5)
main.bind("<KeyPress-6>", place6)
main.bind("<KeyPress-7>", place7)
main.bind("<KeyPress-8>", place8)
main.bind("<KeyPress-9>", place9)
main.bind("<KeyPress->", dot)
main.bind("<minus>", minus)
main.bind("<slash>", divide)
main.bind("<asterisk>", mult)
main.bind("<plus>", plus)
main.bind("<Return>", enter)
main.bind("<Delete>", removetext)
