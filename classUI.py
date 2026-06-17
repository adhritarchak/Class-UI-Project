from tkinter import *
from tkinter import ttk, PhotoImage
from PIL import Image, ImageTk
import tkinter.font as tkFont

ICON_SCALE = 0.1

class Ability:
    """Base class for moves and passives. Don't use this directly."""
    
    abilityType: str
    name: str
    level: int
    effect: str

    def __init__(self):
        self.abilityType = "ability"
        self.name = ""
        self.level = 0
        self.effect = ""

    def setData(self, data: dict) -> None:
        """Takes in a dict and updates the data accordingly."""

        self.name = data.get("name", "")
        self.effect = data.get("effect", "")
class Move(Ability):
    """Active moves that classes use."""
    
    weapon: int
    element: int
    moveType: int
    cost: int
    delay: int
    power: int
    range: int

    def __init__(self):
        self.abilityType = "move"
        self.name = "Move"
        self.level = 0
        self.weapon = 0
        self.element = 0
        self.moveType = 0
        self.cost = 0
        self.delay = 0
        self.power = 0
        self.range = 0
        self.effect = ""
    
    def setData(self, data: dict) -> None:
        self.name = data.get("name", "")
        self.level = data.get("level", 0)
        self.weapon = data.get("weapon", 0)
        self.element = data.get("element", 0)
        self.moveType = data.get("moveType", 0)
        self.cost = data.get("cost", 0)
        self.delay = data.get("delay", 0)
        self.power = data.get("power", 0)
        self.range = data.get("range", 0)
        self.effect = data.get("effect", "")
class Passive(Ability):
    """Passive effects that trigger when the conditions are met."""
    
    condition: str

    def __init__(self):
        self.abilityType = "passive"
        self.name = "Passive"
        self.level = 0
        self.condition = ""
        self.effect = ""

    def setData(self, data: dict) -> None:
        self.name = data.get("name", "")
        self.level = data.get("level", 0)
        self.condition = data.get("condition", "")
        self.effect = data.get("effect", "")

class CharacterClass:
    """Contains all data for a character class."""
    
    name: str
    description: str
    weapons: list[int]
    elements: list[int]
    movement: int
    baseStats: list[int]
    skill1Name: str
    skill1Data: str
    skill2Name: str
    skill2Data: str
    skill3Name: str
    skill3Data: str

    preClass1: str
    preClass2: str
    preClass3: str
    nextClass1: str
    nextClass2: str
    nextClass3: str

    abilities: list[dict]

    def __init__(self) -> None:
        self.name = ""
        self.description = ""
        self.weapons = []
        self.elements = []
        self.movement = 0
        self.baseStats = []
        self.skill1Name = ""
        self.skill1Data = ""
        self.skill2Name = ""
        self.skill2Data = ""
        self.skill3Name = ""
        self.skill3Data = ""

        self.preClass1 = ""
        self.preClass2 = ""
        self.preClass3 = ""
        self.nextClass1 = ""
        self.nextClass2 = ""
        self.nextClass3 = ""

        self.abilities = []

    def setData(self, data: dict) -> None:
        self.name = data.get("name", "")
        self.description = data.get("description", "")
        self.weapons = data.get("weapons", [])
        self.elements = data.get("elements", [])
        self.movement = data.get("movement", 0)
        self.baseStats = data.get("baseStats", [])
        self.skill1Name = data.get("skill1Name", "")
        self.skill1Data = data.get("skill1Data", "")
        self.skill2Name = data.get("skill2Name", "")
        self.skill2Data = data.get("skill2Data", "")
        self.skill3Name = data.get("skill3Name", "")
        self.skill3Data = data.get("skill3Data", "")

        self.preClass1 = data.get("preClass1", "")
        self.preClass2 = data.get("preClass2", "")
        self.preClass3 = data.get("preClass3", "")
        self.nextClass1 = data.get("nextClass1", "")
        self.nextClass2 = data.get("nextClass2", "")
        self.nextClass3 = data.get("nextClass3", "")
        self.abilities = data.get("abilities", [])

class AutoScrollbar(ttk.Scrollbar):
    """A scrollbar that hides itself when it's not needed."""

    # Defining set method with all 
    # its parameter
    def set(self, low, high):
         
        if float(low) <= 0.0 and float(high) >= 1.0:
             
            # Using grid_remove
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        Scrollbar.set(self, low, high)
     
    # Defining pack method
    def pack(self, **kw):
         
        # If pack is used it throws an error
        raise (TclError,"pack cannot be used with \
        this widget")
     
    # Defining place method
    def place(self, **kw):
         
        # If place is used it throws an error
        raise (TclError, "place cannot be used  with \
        this widget")
class IconSelector:
    """A widget collection that allows the user to switch between multiple icons using buttons."""
    
    icons: list[PhotoImage]
    currentIcon: int
    baseFrame: ttk.Frame
    iconLabel: ttk.Label
    leftButton: ttk.Button
    rightButton: ttk.Button
    onUpdateAction: callable

    def setOnUpdate(self, action: callable) -> None:
        self.onUpdateAction = action

    def getTier(self) -> int:
        return self.currentIcon + 1
    def increaseTier(self) -> None:
        if self.currentIcon < len(self.icons) - 1:
            self.currentIcon += 1
            self.leftButton.config(state=NORMAL)
            self.iconLabel.config(image=self.icons[self.currentIcon])
            self.onUpdateAction()
        if self.currentIcon == len(self.icons) - 1: self.rightButton.config(state=DISABLED)
    def decreaseTier(self) -> None:
        if self.currentIcon > 0:
            self.currentIcon -= 1
            self.rightButton.config(state=NORMAL)
            self.iconLabel.config(image=self.icons[self.currentIcon])
            self.onUpdateAction()
        if self.currentIcon == 0: self.leftButton.config(state=DISABLED)
    def setIcon(self, iconIndex: int) -> None:
        if 0 <= iconIndex < len(self.icons):
            self.currentIcon = iconIndex
            self.iconLabel.config(image=self.icons[self.currentIcon])
            self.onUpdateAction()
            if self.currentIcon == 0:
                self.leftButton.config(state=DISABLED)
            else:
                self.leftButton.config(state=NORMAL)
            if self.currentIcon == len(self.icons) - 1:
                self.rightButton.config(state=DISABLED)
            else:
                self.rightButton.config(state=NORMAL)
        elif iconIndex < 0:
            self.setIcon(0)
        else:
            self.setIcon(len(self.icons) - 1)

    def __init__(self, parent: ttk.Panedwindow, icons: list[PhotoImage], initIcon: int = 0, border: bool = False) -> None:
        if initIcon < 0 or initIcon > len(icons) - 1:
            initIcon = 0

        self.currentIcon = initIcon
        self.icons = icons
        self.onUpdateAction = lambda: None

        if border:
            self.baseFrame = ttk.Frame(parent, border=1, relief="solid")
        else:
            self.baseFrame = ttk.Frame(parent)
        self.iconLabel = ttk.Label(self.baseFrame, image=self.icons[self.currentIcon], padding=0)
        self.iconLabel.pack(side=TOP)

        buttonFrame = ttk.Frame(self.baseFrame)
        buttonFrame.pack(side=BOTTOM)
        self.leftButton = ttk.Button(buttonFrame, text="<", command=self.decreaseTier, padding=0)
        self.leftButton.bind("<Shift-Button-1>", lambda event: self.setIcon(0))
        self.leftButton.bind("<Button-3>", lambda event: self.setIcon(self.currentIcon - 3))
        self.leftButton.grid(row=0, column=0)
        if self.currentIcon == 0: self.leftButton.config(state=DISABLED)
        self.rightButton = ttk.Button(buttonFrame, text=">", command=self.increaseTier, padding=0)
        self.rightButton.bind("<Shift-Button-1>", lambda event: self.setIcon(len(icons) - 1))
        self.rightButton.bind("<Button-3>", lambda event: self.setIcon(self.currentIcon + 3))
        self.rightButton.grid(row=0, column=1)
        if self.currentIcon == len(icons) - 1: self.rightButton.config(state=DISABLED)

    def pack(self, **kwargs) -> None:
        self.baseFrame.pack(**kwargs)

    def grid(self, **kwargs) -> None:
        self.baseFrame.grid(**kwargs)
        self.baseFrame.config(width=75)
class SortButtons:
    baseFrame: ttk.Frame
    upButton: ttk.Button
    downButton: ttk.Button
    removeButton: ttk.Button

    def __init__(self, parent: ttk.Frame):
        self.baseFrame = ttk.Frame(parent)
        self.upButton = ttk.Button(self.baseFrame, text="↑", width=2, padding=0)
        self.downButton = ttk.Button(self.baseFrame, text="↓", width=2, padding=0)
        self.removeButton = ttk.Button(self.baseFrame, text="✕", width=2, padding=0)

        self.removeButton.pack(side=LEFT)
        self.upButton.pack(side=LEFT)
        self.downButton.pack(side=LEFT)

    def configureCommands(self, upCommand: callable, downCommand: callable, removeCommand: callable) -> None:
        self.upButton.config(command=upCommand)
        self.downButton.config(command=downCommand)
        self.removeButton.config(command=removeCommand)

    def pack(self, **kwargs) -> None:
        self.baseFrame.pack(**kwargs)
    def grid(self, **kwargs) -> None:
        self.baseFrame.grid(**kwargs)
    def pack_forget(self) -> None:
        self.baseFrame.pack_forget()
    def grid_forget(self) -> None:
        self.baseFrame.grid_forget()
class WidgetSorter:
    baseFrame: ttk.Frame
    emptyFrame: ttk.Frame
    objectList: list[ttk.Widget]
    buttonList: list[SortButtons]

    def __init__(self, parent: PanedWindow):
        self.baseFrame = ttk.Frame(parent)
        self.emptyFrame = ttk.Frame(self.baseFrame)
        self.emptyFrame.pack(side=TOP, fill=BOTH, expand=True)
        self.objectList = []
        self.buttonList = []

        self.refresh()

    def refresh(self) -> None:
        self.emptyFrame.pack_forget()
        for btn in self.buttonList:
            btn.pack_forget()
        for obj in self.objectList:
            obj.pack_forget()
        self.emptyFrame.pack(side=TOP, fill=BOTH, expand=True)
        for i in range(len(self.objectList)):
            self.buttonList[i].pack(side=TOP, anchor='w', pady=2)
            self.objectList[i].pack(side=TOP, anchor='w', pady=2)
            
        try:
            self.buttonList[0].upButton.config(state=DISABLED)
            self.buttonList[-1].downButton.config(state=DISABLED)
            self.buttonList[1].upButton.config(state=NORMAL)
            self.buttonList[-2].downButton.config(state=NORMAL)
        except IndexError:
            pass

        self.baseFrame.update_idletasks()

    def clear(self) -> None:
        self.emptyFrame.pack_forget()
        if len(self.objectList) == 0:
            self.emptyFrame.pack(side=TOP, fill=BOTH, expand=True)
            return
        for index in range(len(self.objectList) - 1, -1, -1):
            # print("Clearing index: ", index)
            self.objectList[index].pack_forget()
            self.buttonList[index].pack_forget()
            delObj = self.objectList.pop(index)
            delBtn = self.buttonList.pop(index)
            del delObj
            del delBtn
        self.emptyFrame.pack(side=TOP, fill=BOTH, expand=True)
        self.baseFrame.update()

    def moveObjectUp(self, obj: ttk.Widget) -> None:
        index = self.objectList.index(obj)
        if index > 0:
            self.objectList[index], self.objectList[index - 1] = self.objectList[index - 1], self.objectList[index]
            self.buttonList[index], self.buttonList[index - 1] = self.buttonList[index - 1], self.buttonList[index]

            self.refresh()

    def moveObjectDown(self, obj: ttk.Widget) -> None:
        index = self.objectList.index(obj)
        if index < len(self.objectList) - 1:
            self.objectList[index], self.objectList[index + 1] = self.objectList[index + 1], self.objectList[index]
            self.buttonList[index], self.buttonList[index + 1] = self.buttonList[index + 1], self.buttonList[index]

            self.refresh()

    def removeObject(self, obj: ttk.Widget) -> None:
        index = self.objectList.index(obj)
        self.objectList[index].pack_forget()
        self.buttonList[index].pack_forget()
        delObj = self.objectList.pop(index)
        delBtn = self.buttonList.pop(index)
        del delObj
        del delBtn

        self.refresh()

    def addObject(self, obj: ttk.Widget) -> None:
        self.objectList.append(obj)
        buttonFrame = SortButtons(self.baseFrame)
        buttonFrame.configureCommands(
            lambda o=obj: self.moveObjectUp(o),
            lambda o=obj: self.moveObjectDown(o),
            lambda o=obj: self.removeObject(o)
        )
        self.buttonList.append(buttonFrame)

        self.refresh()

    def pack(self, **kwargs) -> None:
        self.baseFrame.pack(**kwargs)
    def grid(self, **kwargs) -> None:
        self.baseFrame.grid(**kwargs)

class UIEntry(ttk.Entry):
    def clearEntry(self) -> None:
        self.delete(0, END)
        self.focus_set()

    def replaceEntry(self, text: str) -> None:
        self.delete(0, END)
        self.insert(0, text)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind("<Button-3>", lambda event: self.clearEntry())
class UIText(Text):
    def clearText(self) -> None:
        self.delete("1.0", END)
        self.focus_set()

    def replaceText(self, text: str) -> None:
        self.delete("1.0", END)
        self.insert("1.0", text)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind("<Button-3>", lambda event: self.clearText())

class AbilityBlock:
    """Base class for move and passive blocks. Don't use this directly."""
    
    baseFrame: ttk.Frame
    abilityIcon: ttk.Label
    nameEntry: UIEntry
    levelEntry: UIEntry
    effectText: UIText

    def delete(self) -> None:
        self.baseFrame.destroy()
    def setFont(self, font: tkFont.Font) -> None:
        self.effectText.config(font=font)
    def getData(self) -> Ability:
        pass
    def setData(self, ability: Ability) -> None:
        pass

    def printDebug(self) -> None:
        pass

    def pack(self, **kwargs) -> None:
        self.baseFrame.pack(**kwargs)
    def grid(self, **kwargs) -> None:
        self.baseFrame.grid(**kwargs)
    def pack_forget(self) -> None:
        self.baseFrame.pack_forget()
    def grid_forget(self) -> None:
        self.baseFrame.grid_forget()
class MoveBlock(AbilityBlock):
    """Block of widgets that display and allow editing of a Move."""

    move: Move
    weapon: IconSelector
    typeIcon: IconSelector
    elementIcon: IconSelector
    rangeIcon: IconSelector
    costEntry: UIEntry
    delayEntry: UIEntry
    powerEntry: UIEntry
    effectText: UIText

    # weapon: int
    # element: int
    # moveType: int
    # cost: int
    # delay: int
    # power: int
    # range: int
    # effect: str

    def __init__(self, parent: ttk.Panedwindow, moveIcon: PhotoImage, weaponIcons: list[PhotoImage],
                  typeIcons: list[PhotoImage], elementIcons: list[PhotoImage], rangeIcons: list[PhotoImage], move: Move = None) -> None:
        self.baseFrame = ttk.Frame(parent, padding=5, border=1, relief="solid")
        self.baseFrame.pack(side=TOP, fill=X, pady=5)
        if move is None:
            self.move = Move()
        else:
            self.move = move
        self.abilityIcon = ttk.Label(self.baseFrame, image=moveIcon, padding=1)
        self.nameEntry = UIEntry(master=self.baseFrame, width=40)
        self.levelLabel = ttk.Label(self.baseFrame, text="Level:")
        self.levelEntry = UIEntry(master=self.baseFrame, width=4)
        self.iconFrame = ttk.Frame(self.baseFrame)
        self.weapon = IconSelector(self.iconFrame, weaponIcons, self.move.weapon)
        self.typeIcon = IconSelector(self.iconFrame, typeIcons, self.move.moveType)
        self.elementIcon = IconSelector(self.iconFrame, elementIcons, self.move.element)
        self.rangeIcon = IconSelector(self.iconFrame, rangeIcons, self.move.range)
        self.cdpFrame = ttk.Frame(self.baseFrame)
        self.costLabel = ttk.Label(self.cdpFrame, text="Cost")
        self.delayLabel = ttk.Label(self.cdpFrame, text="Delay")
        self.powerLabel = ttk.Label(self.cdpFrame, text="Power")
        self.costEntry = UIEntry(master=self.cdpFrame, width=5)
        self.delayEntry = UIEntry(master=self.cdpFrame, width=5)
        self.powerEntry = UIEntry(master=self.cdpFrame, width=5)
        self.effectText = UIText(master=self.baseFrame, width=40, height=4)

        self.abilityIcon.grid(row=0, column=0)
        self.nameEntry.grid(row=0, column=1, columnspan=3, sticky="ew", padx=5, pady=5)
        self.levelLabel.grid(row=0, column=5, padx=1)
        self.levelEntry.grid(row=0, column=6)
        self.weapon.pack(side=LEFT)
        self.typeIcon.pack(side=LEFT)
        self.elementIcon.pack(side=LEFT)
        self.rangeIcon.pack(side=LEFT)
        self.iconFrame.grid(row=1, column=0, columnspan=2)
        self.cdpFrame.grid(row=2, column=0, columnspan=4, sticky="ew", pady=5)
        self.costLabel.pack(side=LEFT, padx=2)
        self.costEntry.pack(side=LEFT, padx=2)
        self.delayLabel.pack(side=LEFT, padx=2)
        self.delayEntry.pack(side=LEFT, padx=2)
        self.powerLabel.pack(side=LEFT, padx=2)
        self.powerEntry.pack(side=LEFT, padx=2)
        self.effectText.grid(row=3, column=0, columnspan=7, padx=5, pady=5, sticky="ew")

        self.nameEntry.insert(0, self.move.name)
        self.levelEntry.insert(0, str(self.move.level))
        self.costEntry.insert(0, str(self.move.cost))
        self.delayEntry.insert(0, str(self.move.delay))
        self.powerEntry.insert(0, str(self.move.power))
        self.effectText.insert("1.0", self.move.effect)

    def updateMove(self) -> None:
        self.move.name = self.nameEntry.get()
        self.move.level = int(self.levelEntry.get()) if self.levelEntry.get().isdigit() else 0
        self.move.weapon = self.weapon.currentIcon
        self.move.moveType = self.typeIcon.currentIcon
        self.move.element = self.elementIcon.currentIcon
        self.move.range = self.rangeIcon.currentIcon
        self.move.cost = int(self.costEntry.get()) if self.costEntry.get().isdigit() else 0
        self.move.delay = int(self.delayEntry.get()) if self.delayEntry.get().isdigit() else 0
        self.move.power = int(self.powerEntry.get()) if self.powerEntry.get().isdigit() else 0
        self.move.effect = self.effectText.get("1.0", "end-1c")
    def getData(self) -> Move:
        self.updateMove()
        return self.move
    def setData(self, move: dict) -> None:
        self.move.setData(move)
        self.nameEntry.delete(0, END)
        self.nameEntry.insert(0, self.move.name)
        self.levelEntry.delete(0, END)
        self.levelEntry.insert(0, str(self.move.level))
        self.weapon.setIcon(self.move.weapon)
        self.typeIcon.setIcon(self.move.moveType)
        self.elementIcon.setIcon(self.move.element)
        self.rangeIcon.setIcon(self.move.range)
        self.costEntry.delete(0, END)
        self.costEntry.insert(0, str(self.move.cost))
        self.delayEntry.delete(0, END)
        self.delayEntry.insert(0, str(self.move.delay))
        self.powerEntry.delete(0, END)
        self.powerEntry.insert(0, str(self.move.power))
        self.effectText.replaceText(self.move.effect)

    def printDebug(self) -> None:
        try:
            print("Move: " + self.move.name)
        except Exception as e:
            print("Move: " + self.__str__())
class PassiveBlock(AbilityBlock):
    """Block of widgets that display and allow editing of a Passive."""
    
    passive: Passive
    conditionEntry: UIEntry

    def __init__(self, parent: ttk.Panedwindow, passiveIcon: PhotoImage, passive: Passive = None) -> None:
        self.baseFrame = ttk.Frame(parent, padding=5, border=1, relief="solid")
        self.baseFrame.pack(side=TOP, fill=X, pady=5)
        if passive is None:
            self.passive = Passive()
        else:
            self.passive = passive
        self.abilityIcon = ttk.Label(self.baseFrame, image=passiveIcon, padding=1)
        self.nameEntry = UIEntry(master=self.baseFrame)
        self.levelLabel = ttk.Label(self.baseFrame, text="Level:")
        self.levelEntry = UIEntry(master=self.baseFrame, width=4)
        self.conditionLabel = ttk.Label(self.baseFrame, text="Condition")
        self.conditionEntry = UIEntry(master=self.baseFrame)
        self.effectLabel = ttk.Label(self.baseFrame, text="Effect")
        self.effectText = UIText(master=self.baseFrame, width=40, height=4)

        self.abilityIcon.grid(row=0, column=0)
        self.nameEntry.grid(row=0, column=1, columnspan=4, sticky="ew", padx=5, pady=5)
        self.levelLabel.grid(row=0, column=5, padx=1)
        self.levelEntry.grid(row=0, column=6)
        self.conditionLabel.grid(row=1, column=0, padx=1, sticky="ew")
        self.conditionEntry.grid(row=2, column=0, columnspan=7, sticky="ew", padx=5, pady=5)
        self.effectLabel.grid(row=3, column=0, padx=1, sticky="ew")
        self.effectText.grid(row=4, column=0, columnspan=7, padx=5, pady=5, sticky="ew")

        self.nameEntry.insert(0, self.passive.name)
        self.levelEntry.insert(0, str(self.passive.level))
        self.conditionEntry.insert(0, self.passive.condition)
        self.effectText.insert("1.0", self.passive.effect)

    def updatePassive(self) -> None:
        self.passive.name = self.nameEntry.get()
        self.passive.level = int(self.levelEntry.get()) if self.levelEntry.get().isdigit() else 0
        self.passive.condition = self.conditionEntry.get()
        self.passive.effect = self.effectText.get("1.0", "end-1c")
    def getData(self) -> Passive:
        self.updatePassive()
        return self.passive
    def setData(self, ability: dict) -> None:
        self.passive.setData(ability)
        self.nameEntry.delete(0, END)
        self.nameEntry.insert(0, self.passive.name)
        self.levelEntry.delete(0, END)
        self.levelEntry.insert(0, str(self.passive.level))
        self.conditionEntry.delete(0, END)
        self.conditionEntry.insert(0, self.passive.condition)
        self.effectText.replaceText(self.passive.effect)

    def printDebug(self) -> None:
        try:
            print("Passive: " + self.passive.name)
        except Exception as e:
            print("Passive: " + self.__str__())

def Icon(filename: str, scale: float) -> PhotoImage:
    icon = Image.open(filename)
    icon = icon.resize((int(icon.size[0] * ICON_SCALE * scale), int(icon.size[1] * ICON_SCALE * scale)))
    return ImageTk.PhotoImage(icon)
