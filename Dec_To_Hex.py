from tkinter import *
from tkinter import ttk

def Transfrom(key):
    Hex = 0
    Dec = int(Dec_TextBox.get())
    HexOtherList = []
    
    if Dec > 15:
        while Dec > 15:
            HexValue = int(Dec / 16)
            HexOtherList.append(Dec % 16)
            Dec = int(Dec / 16)

        if Dec < 16:
            if Dec == 15:
                Dec = 'F'
            elif Dec == 14:
                Dec = 'E'
            elif Dec == 13:
                Dec = 'D'
            elif Dec == 12:
                Dec = 'C'
            elif Dec == 11:
                Dec = 'B'
            elif Dec == 10:
                Dec = 'A'
            
            i = 0
            HexOtherList.reverse()
            
            while i < len(HexOtherList):
                if HexOtherList[i] == 15:
                    HexOtherList[i] = 'F'
                elif HexOtherList[i] == 14:
                    HexOtherList[i] = 'E'
                elif HexOtherList[i] == 13:
                    HexOtherList[i] = 'D'
                elif HexOtherList[i] == 12:
                    HexOtherList[i] = 'C'
                elif HexOtherList[i] == 11:
                    HexOtherList[i] = 'B'
                elif HexOtherList[i] == 10:
                    HexOtherList[i] = 'A'
                else:
                    pass

                i += 1

            Hex = str(Dec)
            
            Len_HexOtherList = len(HexOtherList) -1
            i, j = 0, 0
            while True:
                Hex += str(HexOtherList[j])
                if i >= Len_HexOtherList:
                    break
                else:
                    j += 1
                    i += 1

    else:
        if Dec == 15:
            Hex = 'F'
        elif Dec == 14:
            Hex = 'E'
        elif Dec == 13:
            Hex = 'D'
        elif Dec == 12:
            Hex = 'C'
        elif Dec == 11:
            Hex = 'B'
        elif Dec == 10:
            Hex = 'A'
        else:
            Hex = Dec

    Hex_Text.configure(text = Hex)
    

window = Tk()
window.title("Dec_To_Hex")
window.geometry("300x20")
window.resizable(False, False)
window.configure(background = 'blue')

Dec_TextBox = Entry(window, width = 10, font = "Jalnan")
NONE_Text = Label(window, font = "Jalnan", text = "=")
Hex_Text = Label(window, font = "Jalnan", text = None, width = 10)
Dec_TextBox.grid(column = 0, row = 0, padx = 5)
NONE_Text.grid(column = 1, row = 0, padx = 5)
Hex_Text.grid(column = 2, row = 0, padx = 5)

window.bind('<Return>', Transfrom)
window.mainloop()
