from classUI import *
from tkinter import *
from tkinter import ttk
import sv_ttk, darkdetect

def main():
    buttonNum = 5    

    root = Tk()
    root.title("Tester")
    buttonFrame = ttk.Frame(root)
    buttonFrame.pack(side=TOP, fill=X)

    addButton = ttk.Button(buttonFrame, text="+")
    addButton.pack(side=LEFT)
    addImageButton = ttk.Button(buttonFrame, text="+IMG")
    addImageButton.pack(side=LEFT)

    testIcon = Icon("Assets\\Placeholders\\IconPerson.PNG", 1)

    sorter = WidgetSorter(root)
    sorter.pack(side=TOP, fill=BOTH, expand=True)

    for i in range(buttonNum):
        txtLabel = ttk.Label(sorter.baseFrame, text=f"Item {i+1}")
        sorter.addObject(txtLabel)
    def addNew():
        nonlocal buttonNum
        buttonNum += 1
        txtLabel = ttk.Label(sorter.baseFrame, text=f"Item {buttonNum}")
        sorter.addObject(txtLabel)

    addButton.config(command=addNew)
    addImageButton.config(command=lambda: sorter.addObject(ttk.Label(sorter.baseFrame, image=testIcon)))
    sv_ttk.set_theme(darkdetect.theme())
    root.mainloop()

if __name__ == "__main__":
    main()