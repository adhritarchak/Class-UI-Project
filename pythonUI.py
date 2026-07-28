from classUI import *
from tkinter import *
from tkinter import ttk, PhotoImage
import sv_ttk, darkdetect, json, os

def TierIcons() -> list[PhotoImage]:
    tiers = []
    tiers.append(Icon("Assets\\Tiers\\IconF.PNG", 1))
    tiers.append(Icon("Assets\\Tiers\\IconD-.PNG", 1))
    tiers.append(Icon("Assets\\Tiers\\IconD.PNG", 1))
    tiers.append(Icon("Assets\\Tiers\\IconD+.PNG", 1))
    tiers.append(Icon("Assets\\Tiers\\IconC-.PNG", 1))
    tiers.append(Icon("Assets\\Tiers\\IconC.PNG", 1))
    tiers.append(Icon("Assets\\Tiers\\IconC+.PNG", 1))
    tiers.append(Icon("Assets\\Tiers\\IconB-.PNG", 1))
    tiers.append(Icon("Assets\\Tiers\\IconB.PNG", 1))
    tiers.append(Icon("Assets\\Tiers\\IconB+.PNG", 1))
    tiers.append(Icon("Assets\\Tiers\\IconA-.PNG", 1))
    tiers.append(Icon("Assets\\Tiers\\IconA.PNG", 1))
    tiers.append(Icon("Assets\\Tiers\\IconA+.PNG", 1))
    tiers.append(Icon("Assets\\Tiers\\IconS-.PNG", 1))
    tiers.append(Icon("Assets\\Tiers\\IconS.PNG", 1))
    tiers.append(Icon("Assets\\Tiers\\IconS+.PNG", 1))
    tiers.append(Icon("Assets\\Tiers\\IconSS.PNG", 1))
    tiers.append(Icon("Assets\\Tiers\\IconSS+.PNG", 1))
    tiers.append(Icon("Assets\\Tiers\\IconSSS.PNG", 1))
    tiers.append(Icon("Assets\\Tiers\\IconX.PNG", 1))
    return tiers
def WeaponIcons() -> list[PhotoImage]:
    weapons = []
    weapons.append(Icon("Assets\\Labels\\IconCrossSmall.PNG", 1))
    weapons.append(Icon("Assets\\Weapons\\IconBroadsword.PNG", 1))
    weapons.append(Icon("Assets\\Weapons\\IconLongsword.PNG", 1))
    weapons.append(Icon("Assets\\Weapons\\IconKnife.PNG", 1))
    weapons.append(Icon("Assets\\Weapons\\IconRapier.PNG", 1))
    weapons.append(Icon("Assets\\Weapons\\IconKatana.PNG", 1))
    weapons.append(Icon("Assets\\Weapons\\IconSpear.PNG", 1))
    weapons.append(Icon("Assets\\Weapons\\IconBattleAxe.PNG", 1))
    weapons.append(Icon("Assets\\Weapons\\IconHammer.PNG", 1))
    weapons.append(Icon("Assets\\Weapons\\IconScythe.PNG", 1))
    weapons.append(Icon("Assets\\Weapons\\IconGauntlet.PNG", 1))
    weapons.append(Icon("Assets\\Weapons\\IconBow.PNG", 1))
    weapons.append(Icon("Assets\\Weapons\\IconRifle.PNG", 1))
    weapons.append(Icon("Assets\\Weapons\\IconStaff.PNG", 1))
    weapons.append(Icon("Assets\\Weapons\\IconWand.PNG", 1))
    weapons.append(Icon("Assets\\Weapons\\IconFocus.PNG", 1))
    weapons.append(Icon("Assets\\Weapons\\IconTome.PNG", 1))
    return weapons
def ElementIcons() -> list[PhotoImage]:
    elements = []
    elements.append(Icon("Assets\\Labels\\IconCrossSmall.PNG", 1))
    elements.append(Icon("Assets\\Elements\\IconFire.PNG", 1))
    elements.append(Icon("Assets\\Elements\\IconIce.PNG", 1))
    elements.append(Icon("Assets\\Elements\\IconLightning.PNG", 1))
    elements.append(Icon("Assets\\Elements\\IconWind.PNG", 1))
    elements.append(Icon("Assets\\Elements\\IconEarth.PNG", 1))
    elements.append(Icon("Assets\\Elements\\IconWater.PNG", 1))
    elements.append(Icon("Assets\\Elements\\IconLight.PNG", 1))
    elements.append(Icon("Assets\\Elements\\IconDark.PNG", 1))
    elements.append(Icon("Assets\\Elements\\IconLife.PNG", 1))
    elements.append(Icon("Assets\\Elements\\IconAstral.PNG", 1))
    return elements
def TypeIcons() -> list[PhotoImage]:
    types = []
    types.append(Icon("Assets\\Placeholders\\IconBlank.PNG", 1))
    types.append(Icon("Assets\\Labels\\IconWeapon.PNG", 1))
    types.append(Icon("Assets\\Labels\\IconMagic.PNG", 1))
    types.append(Icon("Assets\\Labels\\IconSupport.PNG", 1))
    types.append(Icon("Assets\\Labels\\IconDefensive.PNG", 1))
    types.append(Icon("Assets\\Labels\\IconBuff.PNG", 1))
    types.append(Icon("Assets\\Labels\\IconSpecial.PNG", 1))
    types.append(Icon("Assets\\Labels\\IconMisc.PNG", 1))
    return types
def RangeIcons() -> list[PhotoImage]:
    ranges = []
    ranges.append(Icon("Assets\\Placeholders\\IconBlank.PNG", 1))
    ranges.append(Icon("Assets\\Labels\\IconSelf.PNG", 1))
    ranges.append(Icon("Assets\\Labels\\IconMelee.PNG", 1))
    ranges.append(Icon("Assets\\Labels\\IconRanged.PNG", 1))
    ranges.append(Icon("Assets\\Labels\\IconAoE.PNG", 1))
    ranges.append(Icon("Assets\\Labels\\IconRadius.PNG", 1))
    ranges.append(Icon("Assets\\Labels\\IconCone.PNG", 1))
    ranges.append(Icon("Assets\\Labels\\IconLine.PNG", 1))
    ranges.append(Icon("Assets\\Labels\\IconLineThru.PNG", 1))
    return ranges
def MoveIcons() -> list[PhotoImage]:
    moves = []
    moves.append(Icon("Assets\\Placeholders\\IconBlank.PNG", 1))
    moves.append(Icon("Assets\\Labels\\IconInfantry.PNG", 1))
    moves.append(Icon("Assets\\Labels\\IconMage.PNG", 1))
    moves.append(Icon("Assets\\Labels\\IconScout.PNG", 1))
    moves.append(Icon("Assets\\Labels\\IconLight.PNG", 1))
    moves.append(Icon("Assets\\Labels\\IconHeavy.PNG", 1))
    moves.append(Icon("Assets\\Labels\\IconMounted.PNG", 1))
    moves.append(Icon("Assets\\Labels\\IconFlying.PNG", 1))
    return moves

def LoadCharacterFile(classname: str) -> CharacterClass:
    """Loads a .JSON file. If thew file does not exist, returns None."""
    
    try:
        with open(f"Characters\\{classname}.json", "r") as f:
            data = json.load(f)
            character = CharacterClass()
            character.setData(data)
            return character
    except FileNotFoundError:
        return None
def GetCharacterFiles() -> list[str]:
    """Returns a list of all .JSON files in the Characters folder, without the .JSON extension."""
    
    if not os.path.exists("Characters"):    # If no Character folder, return nothing   
        return []
    files = []
    for file in os.listdir("Characters"):
        if file.endswith(".json") and file.find("Test") == -1:
            files.append(file[:-5])
    return files
def GetCharacterIndex(charName: str) -> int:
    files = GetCharacterFiles()
    if charName in files:
        return files.index(charName)
    return -1

def main():
    # --- Setup ---

    # Function declarations for type hinting
    saveCharacter: callable
    loadCharacter: callable
    updateClassButton: callable
    setStatTotal: callable
    
    # Root definition
    root = Tk()
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    windowWidth = min(screenWidth-275, 700)
    windowHeight = screenHeight-110

    # Window size is set to be 700px wide max and as tall as possible, positoned just right of the file list on this editor.
    root.geometry(f"{windowWidth}x{windowHeight}+250+20")
    root.title("Character Builder")

    # Scrollbars and canvas
    xScroll = AutoScrollbar(root, orient=HORIZONTAL)
    xScroll.grid(row=1, column=0, sticky=E+W)
    yScroll = AutoScrollbar(root, orient=VERTICAL)
    yScroll.grid(row=0, column=1, sticky=N+S)

    canvas = Canvas(root, xscrollcommand=xScroll.set, yscrollcommand=yScroll.set, width=700)
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    xScroll.config(command=canvas.xview)
    yScroll.config(command=canvas.yview)
    root.grid_rowconfigure(0, weight=2)
    root.grid_columnconfigure(0, weight=1)

    # Base frame
    base = ttk.Frame(canvas, border=1, padding=5)       # Use this frame as the parent for other frames/widgets in this program.
    base.rowconfigure(1, weight=1)
    base.columnconfigure(1, weight=1)

    # Misc definitions
    currentCharacter = CharacterClass()
    FONT = tkFont.Font(family="Segoe UI", size=10)      # This has to be defined after root is created. I don't know why, but it cannot be defined outside the main function.
    skillFrameWidth = 10
    characterFiles: list[str] = GetCharacterFiles()

    # Icons
    tierIcons = TierIcons()         # Stat Tiers
    weaponIcons = WeaponIcons()     # Weapon Types
    elementIcons = ElementIcons()   # Elements
    typeIcons = TypeIcons()         # Ability Types
    rangeIcons = RangeIcons()       # Ability Ranges
    moveIcons = MoveIcons()         # Class Movement Types

    personIcon = Icon("Assets\\Placeholders\\IconPerson.PNG", 2)
    skillIcon = Icon("Assets\\Labels\\IconSkill.PNG", 1)
    abilityIcon = Icon("Assets\\Labels\\IconAbility.PNG", 1)
    hpIcon = Icon("Assets\\Labels\\IconHP.PNG", 1)
    mpIcon = Icon("Assets\\Labels\\IconMP.PNG", 1)
    strIcon = Icon("Assets\\Labels\\IconSTR.PNG", 1)
    magIcon = Icon("Assets\\Labels\\IconMAG.PNG", 1)
    agiIcon = Icon("Assets\\Labels\\IconAGI.PNG", 1)
    dexIcon = Icon("Assets\\Labels\\IconDEX.PNG", 1)
    defIcon = Icon("Assets\\Labels\\IconDEF.PNG", 1)
    mdfIcon = Icon("Assets\\Labels\\IconMDF.PNG", 1)
    # ----------------------------

    # --- Basic Class Info ---
    infoFrame = ttk.Frame(base)
    infoFrame.pack(side=TOP, fill=X, pady=8)

    personLabel = ttk.Label(infoFrame, image=personIcon)                # Person Icon
    personLabel.grid(row=0, column=0, rowspan=2, columnspan=2)
    nameStr = StringVar()
    name = UIEntry(master=infoFrame, width=20, textvariable=nameStr)    # Class Name
    nameStr.set("Name")
    name.grid(row=0, column=2, columnspan=5, sticky="ew")

    weapon1 = IconSelector(infoFrame, weaponIcons, 0)   # Weapon 1
    weapon1.grid(row=1, column=2)
    weapon2 = IconSelector(infoFrame, weaponIcons, 0)   # Weapon 2
    weapon2.grid(row=1, column=3)
    weapon3 = IconSelector(infoFrame, weaponIcons, 0)   # Weapon 3
    weapon3.grid(row=1, column=4)

    element1 = IconSelector(infoFrame, elementIcons, 0) # Element 1
    element1.grid(row=1, column=5)
    element2 = IconSelector(infoFrame, elementIcons, 0) # Element 2
    element2.grid(row=1, column=6)
    movement = IconSelector(infoFrame, moveIcons, 0)    # Movement Type
    movement.grid(row=1, column=7)
    # --------------------------------

    # --- Stat Aptitudes ---
    aptitudeFrame = ttk.Frame(base)
    aptitudeFrame.pack(side=TOP, expand=False, pady=8)
    aptitudeFrame.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=0)

    hpLabel = ttk.Label(aptitudeFrame, image=hpIcon, padding=1)
    hpLabel.grid(row=0, column=0)
    mpLabel = ttk.Label(aptitudeFrame, image=mpIcon, padding=1)
    mpLabel.grid(row=0, column=1)
    strLabel = ttk.Label(aptitudeFrame, image=strIcon, padding=1)
    strLabel.grid(row=0, column=2)
    magLabel = ttk.Label(aptitudeFrame, image=magIcon, padding=1)
    magLabel.grid(row=0, column=3)
    agiLabel = ttk.Label(aptitudeFrame, image=agiIcon, padding=1)
    agiLabel.grid(row=0, column=4)
    dexLabel = ttk.Label(aptitudeFrame, image=dexIcon, padding=1)
    dexLabel.grid(row=0, column=5)
    defLabel = ttk.Label(aptitudeFrame, image=defIcon, padding=1)
    defLabel.grid(row=0, column=6)
    mdfLabel = ttk.Label(aptitudeFrame, image=mdfIcon, padding=1)
    mdfLabel.grid(row=0, column=7)
    totalLabel = ttk.Label(aptitudeFrame, text="Total: ", padding=1)
    totalLabel.grid(row=0, column=8)

    HPSelector = IconSelector(aptitudeFrame, tierIcons)
    HPSelector.grid(row=1, column=0, padx=2, sticky="ew")
    MPSelector = IconSelector(aptitudeFrame, tierIcons)
    MPSelector.grid(row=1, column=1, padx=2, sticky="ew")
    STRSelector = IconSelector(aptitudeFrame, tierIcons)
    STRSelector.grid(row=1, column=2, padx=2, sticky="ew")
    MAGSelector = IconSelector(aptitudeFrame, tierIcons)
    MAGSelector.grid(row=1, column=3, padx=2, sticky="ew")
    AGISelector = IconSelector(aptitudeFrame, tierIcons)
    AGISelector.grid(row=1, column=4, padx=2, sticky="ew")
    DEXSelector = IconSelector(aptitudeFrame, tierIcons)
    DEXSelector.grid(row=1, column=5, padx=2, sticky="ew")
    DEFSelector = IconSelector(aptitudeFrame, tierIcons)
    DEFSelector.grid(row=1, column=6, padx=2, sticky="ew")
    MDFSelector = IconSelector(aptitudeFrame, tierIcons)
    MDFSelector.grid(row=1, column=7, padx=2, sticky="ew")
    # ---------------------------

    # --- Description ---
    descriptionFrame = ttk.Frame(base)
    descriptionFrame.pack(side=TOP, fill=X, pady=4)
    descLabel = ttk.Label(descriptionFrame, text="Description", padding=1)
    descLabel.pack(side=TOP,pady=2)
    descText = UIText(master=descriptionFrame, height=3, width=80, font=FONT)
    descText.pack(side=TOP,pady=2)
    # ---------------------------

    # --- Class Skills ---
    skill1Frame = ttk.Frame(base)                               # Skill 1
    skill1Frame.pack(side=TOP, fill=X, pady=8)
    skill1Label = ttk.Label(skill1Frame, image=skillIcon, padding=1)
    skill1Label.grid(row=0, column=0)
    skill1NameStr = StringVar()
    skill1Name = UIEntry(master=skill1Frame, textvariable=skill1NameStr)
    skill1Name.grid(row=0, column=1, columnspan=skillFrameWidth - 1, sticky="ew")
    skill1Data = UIText(master=skill1Frame, height=2, width=60, font=FONT)
    skill1Data.grid(row=1, column=0, rowspan=2, columnspan=skillFrameWidth, sticky="nsew")

    skill2Frame = ttk.Frame(base)                               # Skill 2
    skill2Frame.pack(side=TOP, fill=X, pady=8)
    skill2Label = ttk.Label(skill2Frame, image=skillIcon, padding=1)
    skill2Label.grid(row=0, column=0)
    skill2NameStr = StringVar()
    skill2Name = UIEntry(master=skill2Frame, textvariable=skill2NameStr)
    skill2Name.grid(row=0, column=1, columnspan=skillFrameWidth - 1, sticky="ew")
    skill2Data = UIText(master=skill2Frame, height=2, width=60, font=FONT)
    skill2Data.grid(row=1, column=0, rowspan=2, columnspan=skillFrameWidth, sticky="nsew")

    skill3Frame = ttk.Frame(base)                               # Skill 3
    skill3Frame.pack(side=TOP, fill=X, pady=8)
    skill3Label = ttk.Label(skill3Frame, image=skillIcon, padding=1)
    skill3Label.grid(row=0, column=0)
    skill3NameStr = StringVar()
    skill3Name = UIEntry(master=skill3Frame, textvariable=skill3NameStr)
    skill3Name.grid(row=0, column=1, columnspan=skillFrameWidth - 1, sticky="ew")
    skill3Data = UIText(master=skill3Frame, height=2, width=60, font=FONT)
    skill3Data.grid(row=1, column=0, rowspan=2, columnspan=skillFrameWidth, sticky="nsew")
    # ------------------------------

    # --- Previous Classes ---
    prevClassText = ttk.Label(base, text="Previous Classes")
    prevClassText.pack(side=TOP, pady=5)
    prevClassFrame = ttk.Frame(base)
    prevClassFrame.pack(side=TOP, pady=5)
    prevClassEntry1 = UIEntry(master=prevClassFrame, width=15)
    prevClassEntry1.pack(side=LEFT, padx=2)
    prevClassButton1 = ttk.Button(prevClassFrame, text="^", padding=0)
    prevClassButton1.pack(side=LEFT, padx=2)
    prevClassEntry2 = UIEntry(master=prevClassFrame, width=15)
    prevClassEntry2.pack(side=LEFT, padx=2)
    prevClassButton2 = ttk.Button(prevClassFrame, text="^", padding=0)
    prevClassButton2.pack(side=LEFT, padx=2)
    prevClassEntry3 = UIEntry(master=prevClassFrame, width=15)
    prevClassEntry3.pack(side=LEFT, padx=2)
    prevClassButton3 = ttk.Button(prevClassFrame, text="^", padding=0)
    prevClassButton3.pack(side=LEFT, padx=2)
    # -------------------------------

    # --- Next Classes ---
    nextClassText = ttk.Label(base, text="Next Classes")
    nextClassText.pack(side=TOP, pady=5)
    nextClassFrame = ttk.Frame(base)
    nextClassFrame.pack(side=TOP, pady=5)
    nextClassEntry1 = UIEntry(master=nextClassFrame, width=15)
    nextClassEntry1.pack(side=LEFT, padx=2)
    nextClassButton1 = ttk.Button(nextClassFrame, text="^", padding=0)
    nextClassButton1.pack(side=LEFT, padx=2)
    nextClassEntry2 = UIEntry(master=nextClassFrame, width=15)
    nextClassEntry2.pack(side=LEFT, padx=2)
    nextClassButton2 = ttk.Button(nextClassFrame, text="^", padding=0)
    nextClassButton2.pack(side=LEFT, padx=2)
    nextClassEntry3 = UIEntry(master=nextClassFrame, width=15)
    nextClassEntry3.pack(side=LEFT, padx=2)
    nextClassButton3 = ttk.Button(nextClassFrame, text="^", padding=0)
    nextClassButton3.pack(side=LEFT, padx=2)
    # -------------------------------

    # --- Ability List ---
    abilityFrame = ttk.Frame(base)
    abilityFrame.pack(side=TOP, fill=X, pady=20)
    addFrame = ttk.Frame(abilityFrame)
    addMoveButton = ttk.Button(addFrame, text="+ Move", padding=5)
    addPassiveButton = ttk.Button(addFrame, text="+ Passive", padding=5)
    # debugButton = ttk.Button(addFrame, text="DEBUG", padding=5)
    addMoveButton.pack(side=LEFT, padx=5)
    addPassiveButton.pack(side=LEFT, padx=1)
    # debugButton.pack(side=RIGHT, padx=5)

    sorter = WidgetSorter(abilityFrame)
    sorter.pack(side=TOP, fill=BOTH, expand=True)
    addFrame.pack(side=TOP, fill=X, pady=10)
    # --------------------------------

    # --- Save/Load Frame (Outside Canvas) ---
    saveLoadFrame = ttk.Frame(root, borderwidth=10 ,relief='raised')
    saveLoadFrame.grid(row=2, column=0, sticky="ew")
    loadStatus = ttk.Label(saveLoadFrame)
    # --------------------------------

    # --- Functions ---
    def setStatTotal() -> None:
        """Displays the sum of all stats. The stat tiers are numbered in increasing order, so F = 1, D- = 2, D = 3, ..., X = 20."""
        
        total: int = HPSelector.getTier() + MPSelector.getTier() + STRSelector.getTier() + MAGSelector.getTier() \
            + AGISelector.getTier() + DEXSelector.getTier() + DEFSelector.getTier() + MDFSelector.getTier()
        totalLabel.config(text=f"Total: {total}")
    def printLoadStatus(message: str) -> None:
        """Makes the loadStatus label display text for 3 seconds, then clears it."""

        loadStatus.config(text=message)
        loadStatus.after(3000, lambda: loadStatus.config(text=""))
    def saveCharacter():
        """Saves a character to a .JSON file with the filename being the string in the loadEntry box."""

        if loadEntry.get().strip() == "":                       # Cancels if loadEntry is blank
            printLoadStatus("The Class Name cannot be blank.")
            return
        
        abilityList: list[dict] = []
        try:
            abilityList = [block.getData().__dict__ for block in sorter.objectList]
        except Exception as e:                                  # If some error occurs, just print the error and each block's data to the console.
            print("Error in saveCharacter: {}".format(e))
            for block in sorter.objectList:
                try:
                    block.printDebug()
                except:
                    pass
            printLoadStatus("Error saving character. See console for details.")
        # print(abilityList)
        currentCharacter.setData(
            {
                "name": nameStr.get(),
                "description": descText.get("1.0", END).strip(),
                "weapons": [weapon1.currentIcon, weapon2.currentIcon, weapon3.currentIcon],   
                "elements": [element1.currentIcon, element2.currentIcon],
                "movement": movement.currentIcon,
                "baseStats": [
                    HPSelector.currentIcon,
                    MPSelector.currentIcon,
                    STRSelector.currentIcon,
                    MAGSelector.currentIcon,
                    AGISelector.currentIcon,
                    DEXSelector.currentIcon,
                    DEFSelector.currentIcon,
                    MDFSelector.currentIcon
                ],
                "skill1Name": skill1NameStr.get(),
                "skill1Data": skill1Data.get("1.0", END).strip(),
                "skill2Name": skill2NameStr.get(),
                "skill2Data": skill2Data.get("1.0", END).strip(),
                "skill3Name": skill3NameStr.get(),
                "skill3Data": skill3Data.get("1.0", END).strip(),
                "preClass1": prevClassEntry1.get(),
                "preClass2": prevClassEntry2.get(),
                "preClass3": prevClassEntry3.get(),
                "nextClass1": nextClassEntry1.get(),
                "nextClass2": nextClassEntry2.get(),
                "nextClass3": nextClassEntry3.get(),

                "abilities": abilityList
            })
        if not os.path.exists("Characters"):                                # If no Characters folder exists, create one
            os.makedirs("Characters")
        if not os.path.exists(f"Characters\\{loadEntry.get()}.json"):       # If the character file does not exist, create it
            with open(f"Characters\\{loadEntry.get()}.json", "x") as f:
                json.dump(currentCharacter.__dict__, f, indent=4)
        else:
            with open(f"Characters\\{loadEntry.get()}.json", "w") as f:     # If the character file exists, overwrite it
                json.dump(currentCharacter.__dict__, f, indent=4)
        printLoadStatus("Successfully saved.")
        characterFiles = GetCharacterFiles()                                # Update characterFiles list
    def loadCharacter(loadee: str = None, print = True):
        """Loads a character from the specified .JSON file."""

        loadedCharacter = LoadCharacterFile(loadee)
        if loadedCharacter is not None:
            if(print): printLoadStatus("Successfully loaded.")
            currentCharacter = loadedCharacter
            loadEntry.replaceEntry(loadee)
            nameStr.set(currentCharacter.name)
            descText.replaceText(currentCharacter.description)
            weapon1.setIcon(currentCharacter.weapons[0])
            weapon2.setIcon(currentCharacter.weapons[1])
            weapon3.setIcon(currentCharacter.weapons[2])
            element1.setIcon(currentCharacter.elements[0])
            element2.setIcon(currentCharacter.elements[1])
            movement.setIcon(currentCharacter.movement)

            HPSelector.setIcon(currentCharacter.baseStats[0])
            MPSelector.setIcon(currentCharacter.baseStats[1])
            STRSelector.setIcon(currentCharacter.baseStats[2])
            MAGSelector.setIcon(currentCharacter.baseStats[3])
            AGISelector.setIcon(currentCharacter.baseStats[4])
            DEXSelector.setIcon(currentCharacter.baseStats[5])
            DEFSelector.setIcon(currentCharacter.baseStats[6])
            MDFSelector.setIcon(currentCharacter.baseStats[7])

            skill1NameStr.set(currentCharacter.skill1Name)
            skill1Data.replaceText(currentCharacter.skill1Data)
            skill2NameStr.set(currentCharacter.skill2Name)
            skill2Data.replaceText(currentCharacter.skill2Data)
            skill3NameStr.set(currentCharacter.skill3Name)
            skill3Data.replaceText(currentCharacter.skill3Data)

            prevClassEntry1.replaceEntry(currentCharacter.preClass1)
            prevClassEntry2.replaceEntry(currentCharacter.preClass2)
            prevClassEntry3.replaceEntry(currentCharacter.preClass3)
            nextClassEntry1.replaceEntry(currentCharacter.nextClass1)
            nextClassEntry2.replaceEntry(currentCharacter.nextClass2)
            nextClassEntry3.replaceEntry(currentCharacter.nextClass3)
            
            updateClassButton(prevClassButton1, prevClassEntry1.get())
            updateClassButton(prevClassButton2, prevClassEntry2.get())
            updateClassButton(prevClassButton3, prevClassEntry3.get())
            updateClassButton(nextClassButton1, nextClassEntry1.get())
            updateClassButton(nextClassButton2, nextClassEntry2.get())
            updateClassButton(nextClassButton3, nextClassEntry3.get())

            sorter.clear()

            for ability in currentCharacter.abilities:
                if(ability.get("abilityType", "ability") == "move"):
                    addMoveBlock(ability)
                elif(ability.get("abilityType", "ability") == "passive"):
                    addPassiveBlock(ability)
        else:
            if(print): printLoadStatus("Character not found.")
    def updateClassButton(button: ttk.Button, characterName: str) -> None:
        """Enables/Disables class load button based on if class file exists."""

        if os.path.exists(f"Characters\\{characterName}.json"):
            button.config(state=NORMAL)
        else:
            button.config(state=DISABLED)
    def configureClassButton(button: ttk.Button, classEntry: UIEntry) -> None:
        """Sets up the configs for a class load button and its corresponding entry."""

        button.config(command=lambda: loadCharacter(classEntry.get()))
        classEntry.bind("<Any-KeyRelease>", lambda event: updateClassButton(button, classEntry.get()))
        updateClassButton(button, classEntry.get())
    def addMoveBlock(move: dict = None) -> None:
        """Adds a new move block to the ability list. Can pre-populate with data from a dict."""

        newMoveBlock = MoveBlock(parent=sorter.baseFrame, moveIcon=abilityIcon, weaponIcons=weaponIcons, 
                                 typeIcons=typeIcons, elementIcons=elementIcons, rangeIcons=rangeIcons)
        if move is not None:
            newMoveBlock.setData(move)

        newMoveBlock.setFont(FONT)
        sorter.addObject(newMoveBlock)

        base.update_idletasks()
        canvas.config(scrollregion=[0, 0, base.winfo_width() - 700, base.winfo_height()])
    def addPassiveBlock(passive: dict = None) -> None:
        """Adds a new passive block to the ability list. Can pre-populate with data from a dict."""
        
        newPassiveBlock = PassiveBlock(sorter.baseFrame, abilityIcon)
        if passive is not None:
            newPassiveBlock.setData(passive)

        newPassiveBlock.setFont(FONT)
        sorter.addObject(newPassiveBlock)

        base.update_idletasks()
        canvas.config(scrollregion=[0, 0, base.winfo_width() - 700, base.winfo_height()])
    def newCharacter() -> None:
        """Resets all fields to blank values."""
        yScroll.set(0)

        currentCharacter = CharacterClass()

        nameStr.set("Name")
        weapon1.setIcon(0)
        weapon2.setIcon(0)
        weapon3.setIcon(0)
        element1.setIcon(0)
        element2.setIcon(0)
        movement.setIcon(0)

        HPSelector.setIcon(0)
        MPSelector.setIcon(0)
        STRSelector.setIcon(0)
        MAGSelector.setIcon(0)
        AGISelector.setIcon(0)
        DEXSelector.setIcon(0)
        DEFSelector.setIcon(0)
        MDFSelector.setIcon(0)

        descText.delete("1.0", END)
        skill1NameStr.set("")
        skill1Data.delete("1.0", END)
        skill2NameStr.set("")
        skill2Data.delete("1.0", END)
        skill3NameStr.set("")
        skill3Data.delete("1.0", END)

        prevClassEntry1.delete(0, END)
        prevClassEntry2.delete(0, END)
        prevClassEntry3.delete(0, END)
        nextClassEntry1.delete(0, END)
        nextClassEntry2.delete(0, END)
        nextClassEntry3.delete(0, END)

        sorter.clear()
        loadEntry.delete(0, END)
        printLoadStatus("New character ready.")

        base.update_idletasks()
        canvas.config(scrollregion=[0, 0, base.winfo_width() - 700, base.winfo_height()])
    def prevCharacter() -> None:
        """Loads the previous character in the characterFiles list."""

        characterFiles = GetCharacterFiles()
        if len(characterFiles) == 0:
            printLoadStatus("No character files found.")
            return
        if GetCharacterIndex(loadEntry.get()) == -1:
            loadCharacter(characterFiles[-1])
            return
        prevIndex = (GetCharacterIndex(loadEntry.get()) - 1) % len(characterFiles)
        loadCharacter(characterFiles[prevIndex])
    def nextCharacter() -> None:
        """Loads the next character in the characterFiles list."""
        
        characterFiles = GetCharacterFiles()
        if len(characterFiles) == 0:
            printLoadStatus("No character files found.")
            return
        nextIndex = (GetCharacterIndex(loadEntry.get()) + 1) % len(characterFiles)
        loadCharacter(characterFiles[nextIndex])
    # --------------------------------

    # --- Event Configurations ---
    addMoveButton.config(command=lambda: addMoveBlock())
    addPassiveButton.config(command=lambda: addPassiveBlock())
    HPSelector.setOnUpdate(setStatTotal)
    MPSelector.setOnUpdate(setStatTotal)
    STRSelector.setOnUpdate(setStatTotal)
    MAGSelector.setOnUpdate(setStatTotal)
    AGISelector.setOnUpdate(setStatTotal)
    DEXSelector.setOnUpdate(setStatTotal)
    DEFSelector.setOnUpdate(setStatTotal)
    MDFSelector.setOnUpdate(setStatTotal)
    setStatTotal()
    # debugButton.config(command=lambda: print("Current Abilities: {}".format([block.getData().__dict__ for block in sorter.objectList])))
    # --------------------------------

    # --- Save/Load Buttons ---
    loadEntry = UIEntry(master=saveLoadFrame, width=20)
    loadEntry.pack(side=LEFT, padx=3)
    saveButton = ttk.Button(saveLoadFrame, text="Save", padding=5, command=saveCharacter)
    saveButton.pack(side=LEFT)
    loadButton = ttk.Button(saveLoadFrame, text="Load", padding=5, command=lambda: loadCharacter(loadEntry.get()))
    loadButton.pack(side=LEFT)
    newCharacterButton = ttk.Button(saveLoadFrame, text="New", padding=5, command=newCharacter)
    newCharacterButton.pack(side=LEFT, padx=10)
    prevButton = ttk.Button(saveLoadFrame, text="Prev", padding=5, command=prevCharacter)
    prevButton.pack(side=LEFT)
    nextButton = ttk.Button(saveLoadFrame, text="Next", padding=5, command=nextCharacter)
    nextButton.pack(side=LEFT, padx=2)
    loadStatus.pack(side=LEFT, padx=3)
    loadEntry.bind("<Return>", lambda event: loadCharacter(loadEntry.get()))        # Load character when Enter is pressed in loadEntry
    # -----------------------------

    # --- Class Save/Load Button Configuration ---
    configureClassButton(prevClassButton1, prevClassEntry1)
    configureClassButton(prevClassButton2, prevClassEntry2)
    configureClassButton(prevClassButton3, prevClassEntry3)
    configureClassButton(nextClassButton1, nextClassEntry1)
    configureClassButton(nextClassButton2, nextClassEntry2)
    configureClassButton(nextClassButton3, nextClassEntry3)
    # -----------------------------

    # --- Final Canvas Configuration ---
    canvas.create_window((0,0), window=base, anchor="nw")
    base.update_idletasks()
    canvas.config(scrollregion=[0, 0, base.winfo_width() - 700, base.winfo_height()])
    root.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))        # Bind scrl to vertical scrolling
    root.bind_all("<Shift-MouseWheel>", lambda event: canvas.xview_scroll(int(-1*(event.delta/120)), "units"))  # Bind shift+scrl to horizontal scrolling
    root.bind("<Control-KeyPress-w>", lambda event: quit())                                                     # Bind ctrl+w to quit
    root.bind("<Control-KeyPress-s>", lambda event: saveButton.invoke())                                        # Bind ctrl+s to save
    # -----------------------------

    sv_ttk.set_theme(darkdetect.theme())
    root.mainloop()
    

if __name__ == "__main__":
    main()