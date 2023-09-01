import random
from tkinter import *
from tkinter import messagebox

#initialize Window
root = Tk()
root.title("1v1 Champ Generator")
root.geometry("500x600")

#How much Champions to generate Label + Input field
labelQuestion = Label(root, text="How many Champions to generate?")
labelQuestion.grid(row=0, column=0)
e = Entry(root, width=30)
e.grid(row=0, column=1, padx=20, pady=10)

#Label for Player 1 Name and Player 2 Name
labelS1 = Label(root, text="Name S1:")
labelS1.grid(row=1, column=0)
labelS2 = Label(root, text="Name S2:")
labelS2.grid(row=2, column=0)
nS1 = Entry(root, width=30)
nS2 = Entry(root, width=30)
nS1.grid(row=1, column=1, padx=20, pady=10)
nS2.grid(row=2, column=1, padx=20, pady=10)

#Champion Listen for Player 1 and Player 2
champsLabelS1 = Label(root, text="", font=("Arial", 16))
champsLabelS1.grid(row = 6, column=0, columnspan=1, pady=5)
champsLabelS2 = Label(root, text="", font=("Arial", 16))
champsLabelS2.grid(row = 6, column=1, columnspan=1, pady=5)
#Label Name Player 1 and Player 2
nameS1 = Label(root, text="", font=("Arial", 16))
nameS1.grid(row = 5, column=0, columnspan=1, pady=5)
nameS1.config(fg= "purple")
nameS2 = Label(root, text="", font=("Arial", 16))
nameS2.grid(row = 5, column=1, columnspan=1, pady=5)
nameS2.config(fg= "purple")

#Clear Button for everything
def button_clear():
    e.delete(0, END)
    nS1.delete(0, END)
    nS2.delete(0, END)
    e.insert(0, 1)
clearbtn = Button(root, text="Clear", command=button_clear)
clearbtn.grid(row=0, column=2)

#Für Mirror Matchups
isMirror = 0
def mirror_matchups():
    global isMirror
    if c1.get() == 1:
        isMirror = 1
    else:
        isMirror = 0
c1 = IntVar()
mirrorcheckbox = Checkbutton(root, text= "Mirror-Matchup?", variable=c1 ,command=mirror_matchups)
mirrorcheckbox.grid(row=3, column=0, columnspan=3)

#Button Generate Champs
def generateChamps():
    champlistS1 = ''
    champlistS2 = ''
    my_list = ["Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe",
               "Aurelion Sol", "Azir", "Bard", "Bel'Veth", "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille",
               "Cassiopeia", "Cho'Gath", "Corki", "Darius", "Diana", "Dr. Mundo", "Draven", "Ekko", "Elise", "Evelynn",
               "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves",
               "Gwen", "Hecarim", "Heimerdinger", "Illaoi", "Irelia", "Ivern", "Janna", "Jarvan IV", "Jax", "Jayce",
               "Jhin", "Jinx", "K'Sante", "Kai'Sa", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle",
               "Kayn", "Kennen", "Kha'Zix", "Kindred", "Kled", "Kog'Maw", "LeBlanc", "Lee Sin", "Leona", "Lillia",
               "Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "Master Yi", "Miss Fortune",
               "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee", "Nilah", "Nocturne",
               "Nunu & Willump", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana", "Quinn", "Rakan",
               "Rammus", "Rek'Sai", "Rell", "Renata Glasc", "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Samira",
               "Sejuani", "Senna", "Seraphine", "Sett", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir",
               "Skarner", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "Tahm Kench", "Taliyah", "Talon", "Taric",
               "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch", "Udyr", "Urgot",
               "Varus", "Vayne", "Veigar", "Vel'Koz", "Vex", "Vi", "Viego", "Viktor", "Vladimir", "Volibear", "Warwick",
               "Wukong", "Xayah", "Xerath", "Xin Zhao", "Yasuo", "Yone", "Yorick", "Yuumi", "Zac", "Zed", "Zeri",
               "Ziggs", "Zilean", "Zoe", "Zyra"]
    temp = e.get()
    if temp.isdigit() == False:
        messagebox.showwarning("Invalid Input", "Invadlid Input")
        return
    elif int(temp) < 1:
        messagebox.showwarning("Invalid Input", "Cannot be less than 1")
        return
    elif isMirror == 1:
        if int(temp) > len(my_list):
            messagebox.showwarning("Invalid Input", "Cannot be greater than 162")
            return
    else:
        if int(temp) > len(my_list)/2:
            messagebox.showwarning("Invalid Input", "Cannot be greater than 81")
            return
    number_of_champs = e.get()
    global n_o_c
    n_o_c = int(number_of_champs)
    # Pick 10 random Elements
    if isMirror == 0:
        random_itemsS1 = random.sample(my_list, n_o_c)
        inChampList = set(my_list)
        alreadySelectedList = set(random_itemsS1)
        inChampButNotInSelected = inChampList - alreadySelectedList
        random_itemsS2 = random.sample([*inChampButNotInSelected], n_o_c)
        # Print the Elements
        for item in random_itemsS1:
            champlistS1 += item + '\n'
        for item in random_itemsS2:
            champlistS2 += item + '\n'
        champsLabelS1['text'] = champlistS1
        champsLabelS2['text'] = champlistS2
    else:
        random_items = random.sample(my_list, n_o_c)
        for item in random_items:
            champlistS1 += item + '\n'
        champsLabelS1['text'] = champlistS1
        champsLabelS2['text'] = champlistS1
    if nS1.get() == "":
        nameS1['text'] = "Player 1"
    else:
        nameS1['text'] = nS1.get()
    if nS2.get() == "":
        nameS2['text'] = "Player 2"
    else:
        nameS2['text'] = nS2.get()

genChampBtn = Button(root, text="Generate Champions", command=generateChamps)
genChampBtn.grid(row=4, column=0, columnspan=3)

#magicLabel = Label(root, text="", font=("Arial", 16))
#magicLabel.grid(row = 5, column=0, columnspan=3, pady=10)
#def magicIstToll():
#    magicLabel['text'] = "Nein, Magic ist ein Huso!"
#genMagic = Button(root, text="Magic ist toll!", command=magicIstToll)
#genMagic.grid(row=2, column=0, columnspan=3)

#Button Exit
#def expopup():
#    response = messagebox.askquestion("Exit", "Do you want to Exit?")
#    if response == 'yes':
#        root.destroy()
#exitbtn = Button(root, text="Exit", command=expopup)
#exitbtn.grid(row=5, column=0, columnspan=3, pady=20, rowspan=10)

#Close Window Button
def on_close():
    response=messagebox.askyesno('Exit','Are you sure you want to exit?')
    if response:
        root.destroy()
root.protocol('WM_DELETE_WINDOW',on_close)

root.mainloop()


