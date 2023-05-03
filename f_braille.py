import PySimpleGUI as sg

class Braille:
    dict_braille = {
        "100000":("A", "⠁"),
        "110000":("B", "⠃"), 
        "100100":("C", "⠉"), 
        "100110":("D", "⠙"),
        "100010":("E", "⠑"), 
        "110100":("F", "⠋"), 
        "110110":("G", "⠛"), 
        "110010":("H", "⠓"),
        "010100":("I", "⠊"), 
        "010110":("J", "⠚"), 
        "101000":("K", "⠅"), 
        "111000":("L", "⠇"),
        "101100":("M", "⠍"), 
        "101110":("N", "⠝"), 
        "101010":("O", "⠕"), 
        "111100":("P", "⠏"),
        "111110":("Q", "⠟"), 
        "111010":("R", "⠗"), 
        "011100":("S", "⠎"), 
        "011110":("T", "⠞"), 
        "101001":("U", "⠥"), 
        "111001":("V", "⠧"),
        "010111":("W", "⠺"), 
        "101101":("X", "⠭"),
        "101111":("Y", "⠽"), 
        "101011":("Z", "⠵"), 
        "010000":(",", "⠂"),
        "001000":("'", "⠄"),
        "001011":('"', "⠴"),
        "001001":("-", "⠤"),
        "011001":("?", "⠦"),
        "011010":("!", "⠖"),
        "001111":("number", "⠼"),
        "000011":("letter", "⠰"),
        "011011":("GG", "⠶"),
        "010010":("CON", "⠒"),
        "010011":("DIS", "⠲"),
        "100001":("CH", "⠡"),
        "010001":("EN", "⠢"),
        "100101":("SH", "⠩"),
        "100111":("TH", "⠹"),
        "100011":("WH", "⠱"),
        "110011":("OU", "⠳"),
        "001100":("ST", "⠌"),
        "110001":("GH", "⠣"),
        "010101":("OW", "⠪"),
        "110101":("ED", "⠫"),
        "001101":("ING", "⠬"),
        "001110":("AR", "⠜"),
        "110111":("ER", "⠻"),
        "111111":("FOR", "⠿"),
        "111101":("AND", "⠯"),
        "111011":("OF", "⠷"),
        "011000":("BE", "⠆"),
        "001010":("IN", "⠔"),
        "011101":("THE", "⠮"),
        "011111":("WITH", "⠾"),
        "000000":(" ", " "),
        "000100":("", "⠈"),
        "000010":("", "⠐"),
        "000001":("", "⠠"),
        "000110":("", "⠘"),
        "000101":("", "⠨"),
        "000111":("", "⠸")
    }

    def __init__(self, dots=" "):
        """
        creates a new braille character 
        parameter can be both a list [1, 0, 0, 0, 0, 0] or string "⠁"
        """
        self.dotstring = ""
        if isinstance(dots, list):
            for dot in dots:
                self.dotstring += str(dot)
        elif isinstance(dots, str):
            for key in self.dict_braille:
                if dots == self.dict_braille[key][1]:
                    self.dotstring = key
        self.val = self.dict_braille[self.dotstring]

    def getEng(self):
        return self.val[0]

    def getBrl(self):
        return self.val[1]

class Translator:
    nums = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 0,
    }

    contractions = {
        'AB': 'ABOUT', 
        'AG': 'AGAIN', 
        'ALM': 'ALMOST', 
        'ALR': 'ALREADY', 
        'AL': 'ALSO', 
        'ALT': 'ALTHOUGH', 
        'ALW': 'ALWAYS', 
        'BEC': 'BECAUSE', 
        'BEF': 'BEFORE',
        'BET': 'BETWEEN', 
        'BL': 'BLIND', 
        'BRL': 'BRAILLE', 
        'CD': 'COULD', 
        'EI': 'EITHER', 
        'FST': 'FIRST', 
        'FR': 'FRIEND', 
        'GD': 'GOOD', 
        'GRT': 'GREAT', 
        'HM': 'HIM', 
        'LL': 'LITTLE', 
        'MCH': 'MUCH', 
        'MST': 'MUST', 
        'NEI': 'NEITHER', 
        'SCH': 'SUCH', 
        'SD': 'SAID', 
        'SHD': 'SHOULD', 
        'TD': 'TODAY', 
        'TGR': 'TOGETHER', 
        'TM': 'TOMORROW', 
        'TN': 'TONIGHT', 
        'WD': 'WOULD', 
        'XS': 'ITS', 
        'YR': 'YOUR', 
        'B': 'BUT', 
        'C': 'CAN', 
        'D': 'DO', 
        'E': 'EVERY', 
        'F': 'FROM', 
        'G': 'GO', 
        'H': 'HAVE', 
        'J': 'JUST', 
        'K': 'KNOWLEDGE', 
        'L': 'LIKE', 
        'M': 'MORE', 
        'N': 'NOT', 
        'P': 'PEOPLE', 
        'Q': 'QUITE', 
        'R': 'RATHER',
        'S': 'SO', 
        'T': 'THAT', 
        'U': 'US', 
        'V': 'VERY', 
        'X': 'IT', 
        'Y': 'YOU', 
        'Z': 'AS', 
        '?': 'HIS', 
        '"': 'WAS', 
        'GG': 'WERE', 
        'CH': 'CHILD', 
        'OU': 'OUT', 
        'ST': 'STILL', 
        'SH': 'SHALL', 
        'TH': 'THIS', 
        'WH': 'WHICH', 
        'EN': 'ENOUGH'
    }
    prefixes = {
        'DIS': '.', 
        'CON': ':', 
    }
    
    key_map = {"S": 3, "D": 2, "F": 1, "J": 4, "K": 5, "L": 6}

    def __init__(self):
        self.in_string = ""
        self.out_string = ""
        self.cell = [0, 0, 0, 0, 0, 0]
        self.number = False
        
    def clickDot(self, key):
        idx = self.key_map[key.upper()] - 1
        self.cell[idx] = 1

    def newCell(self):
        """
        newCell() confirms a set of clicks and adds a braille character to input string
        Adds the corresponding English letter/word to the output string
        Resets the clicks for the next braille character
        """
        brl = Braille(self.cell)
        self.in_string += brl.getBrl()
        self.out_string += self.checkEng(brl.getEng())
        self.cell = [0, 0, 0, 0, 0, 0]
    
    def newLine(self):
        """
        Insert newline character to both input and output string
        If the user calls newLine() in the middle of typing a braille character,
        newCell() is automatically called to insert the braille character
        """
        if self.cell != [0, 0, 0, 0, 0, 0]:
            self.newCell()
        self.in_string += "\n"
        self.out_string += "\n"
    
    def backspace(self):
        """
        backspace() deletes the previous braille character from the input string
        and re-translates the braille characters to English using refreshEng()
        However, if the function is called in the middle of typing a braille character, 
        it simply resets the clicks instead of deleting a character
        """
        
        if self.cell == [0, 0, 0, 0, 0, 0]:
            self.in_string = self.in_string[:-1]
            self.refreshEng()
        else:
            self.cell = [0, 0, 0, 0, 0, 0]

    def checkEng(self, temp):
        """
        checkEng(temp) returns the appropriate English letter/word for the output string  
        Checks for indicators (number/letter) that should not be a part of the output
        If the setting is 'Number' and the given letter is A~J, 
        checkEng() returns a number 0~9 
        """
        if temp == "number":
            self.number = True
            temp = ""
        elif temp == "letter":
            self.number = False
            temp = ""
        elif self.number and self.nums.get(temp) != None:
            temp = str(self.nums[temp])
        return temp

    def refreshEng(self):
        """
        re-translates the characters in input string to the
        corresponding English letter/word in output string
        """
        self.out_string = ""
        for brl_char in self.in_string:
            if brl_char == '\n':
                self.out_string += '\n'
            else:
                eng_char = Braille(brl_char).getEng()
                self.out_string += self.checkEng(eng_char)

    def isNumber(self):
        """
        returns the current setting of input (Number/Letter)
        """
        if self.number:
            return "Number"
        else:
            return "Letter"

    def getBrlstring(self):
        """
        returns the string of braille characters
        """
        return self.in_string
    
    def getEngstring(self):
        """
        returns the English string corresponding to the input
        """
        return self.out_string

    def checkContracts(self):
        """
        returns the new output string that substitutes the abbreviations
        or variants present in the original output string
        """
        punctuations = {"!", "?", ".", ",", " ", "\n"}
        for p in self.prefixes:
            for stop in punctuations:
                self.out_string = self.out_string.replace(p+stop, self.prefixes[p]+stop)
        for c in self.contractions:
            for stop in punctuations:
                self.out_string = self.out_string.replace(' '+c+stop, ' '+self.contractions[c]+stop)
                self.out_string = self.out_string.replace('\n'+c+stop, '\n'+self.contractions[c]+stop)
                if len(self.out_string)>len(c) and self.out_string[:len(c)+1] == c+stop:
                    self.out_string = self.contractions[c]+stop+self.out_string[len(c)+1:]
        return self.out_string



"""
Creates the graphic interface used to visually demonstrate the program
"""
sg.theme("Reddit")
font1 = ("Georgia", 18)
font2 = ("Times New Roman", 16)
font3 = ("Times New Roman", 14)
layout = [[sg.Text('Simple Braille Clicker', text_color = 'Crimson', font=font1, justification='center', pad=(0, 10))],
        [sg.Frame('Braille to English', 
            [[sg.Text('', pad=(0,0))],
            [sg.Multiline(size=(30, 3),  font= font2, autoscroll = True, key='-myinput-')],
            [sg.Multiline(size=(30, 3), font= font2, autoscroll = True, key='-myoutput-')],
            [sg.Text(font=font2, key='-inMode-')]],
        size=(540, 300), font= font3, element_justification='c')]
        ]

window = sg.Window('Simple Braille Clicker', layout, size = (600, 350), margins = (20, 20), element_justification='c', return_keyboard_events=True, finalize=True)
input1 = window['-myinput-']
output1 = window['-myoutput-']
mode = window['-inMode-']
translator = Translator()

while True:
    event, values = window.read()
    if event in (None, "Exit"):
        break
    elif event in "sdfjklSDFJKL":
        translator.clickDot(event)
    elif event == " ":
        translator.newCell()
    elif event == ";":
        translator.newLine()
    elif event in "aA":
        translator.backspace()
    input1.update(translator.getBrlstring())
    output1.update(translator.getEngstring())
    output1.update(translator.checkContracts())
    mode.update(translator.isNumber())
window.close()


