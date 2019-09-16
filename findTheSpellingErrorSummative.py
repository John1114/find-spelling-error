# \/ IMPORTS \/

import re     # This imports tools which help to read the KingJames.txt file.
import time   # This imports tools which help to measre the time it takes to run a certain code

# \/ DEFINING VARIABLES AND LISTS \/

file = open("/Users/21rytel_j/Desktop/folder/KingJames.txt", "r")      # This sets "file" equal to the .txt file of the bible
bibleText = file.read()                                                # This sets bibleText equal to to the content of the file as a string.
bibleText = re.findall(r'\w+', bibleText)                              # This changes bibleText into a list where every word is an item in the list.

file = open("/Users/21rytel_j/Desktop/folder/Words_alpha.txt", "r")   # This sets "file" equal to the .txt file of the dictionary
dictionaryWords = file.read()                                          # This sets dictionaryWords equal to to the content of the file as a string.
dictionaryWords = re.findall(r'\w+', dictionaryWords)                  # This changes dictionaryWords into a list where every word is an item in the list.

wordsInText = 0          # This will be the total amount of words in the bible
uniqueWords = []         # This will be a list with all the uniqe words in the bible
wordsInDictionary = 0    # This will be the amount of words that are in the dictionary
wordsInText = 0          # This will be the total amount of words in the bible
wordsMispelled = 0       # This will be the amount of words that are not in the dictionary

commonWordList = ["the","of","and","that","to","in","he","for","unto","a","lord","his","shall","I","they","not","be","is","them","with","all","him","it","thou","but","said","my","was","their"]    # This is the list of all the most common words in the bible (41.9% of all the words) to save time
lessCommonWordList = ["after","man","thee","she","behold","god","king","no","you","your","there","live","also","out","from","heaven","upon","day","earth","our","are","before"]                     # This is the list of some of the less common words in the bible (4.5% of all the words) to save time
leastCommonWordList = ['COMMANDED', 'VOICE', 'CHRIST', 'OFFERING', 'WOULD', 'PRIEST', 'THREE', 'SPIRIT', 'THOUSAND', 'SERVANTS', 'ANOTHER', 'SOUL', 'YEARS', 'SERVANT', 'THEMSELVES', 'FIRST', 'FOUND', 'GLORY', 'WITHOUT', 'PEACE', 'WHERE', 'GOLD', 'MOUTH', 'BEING', 'WHEREFORE', 'DEATH', 'PRIESTS', 'CITIES', 'SWORD', 'BOTH', 'SIN', 'SEVEN', 'FACE', 'WATER', 'KEEP', 'SEA', 'LEFT', 'WORK', 'BLOOD', 'WIFE', 'WICKED', 'BEEN', 'FLESH', 'UNDER', 'WOMAN', 'DEAD', 'NONE', 'TAKEN', 'MUCH', 'OLD','MORE', 'JUDAH', 'WORD', 'LIKE', 'HEARD', 'CALLED', 'ABOUT', 'NOR', 'OWN', 'MANY', 'WAY', 'HOLY', 'DONE', 'EVIL', 'SEE', 'BRETHREN', 'HUNDRED', 'WORDS', 'EAT', 'MINE', 'SAW', 'SPAKE', 'FIRE', 'TOGETHER', 'THOSE', 'EGYPT', 'HIMSELF', 'THING', 'HOW', 'LAW', 'GIVEN', 'HEAR', 'FATHERS', 'MIGHT', 'HIGH', 'THAN', 'GAVE', 'ART', 'CAST', 'ANSWERED', 'LIFE', 'EVER', 'HANDS', 'OTHER', 'SPEAK', 'EYES', 'THROUGH', 'FEAR', 'OFF','WHO', 'MAKE', 'DID', 'MAY', 'SAY', 'SONS', 'AWAY', 'WHAT', 'HAST', 'OVER', 'OR', 'GIVE', 'FORTH', 'PUT', 'AMONG', 'ANY', 'NEITHER', 'BROUGHT', 'THINE', 'TAKE', 'JERUSALEM', 'CITY', 'JESUS','FATHER', 'NAME', 'HEART', 'DAYS', 'TOOK', 'DAVID', 'AM', 'SHOULD', 'PASS', 'GOOD', 'SET', 'ACCORDING', 'SENT', 'THEREOF', 'TWO', 'WHOM', 'MOSES', 'PLACE', 'KNOW', 'YET', 'TIME', 'THUS', 'BRING', 'AGAIN','WHICH', 'HAVE', 'AS', 'THY', 'ME', 'WILL', 'WHEN', 'YE', 'THIS', 'WERE', 'BY', 'THEN', 'UP','ISRAEL','PEOPLE', 'HAD', 'CAME', 'SO', 'INTO', 'HATH', 'COME', 'ONE', 'SON', 'AN', 'ON', 'MEN', 'HOUSE', 'AT', 'CHILDREN', 'NOW', 'AGAINST', 'IF', 'MADE', 'LAND', 'WE', 'HER', 'GO', 'WENT', 'SAYING', 'EVEN', 'DO', 'THEREFORE', 'THINGS', 'HAND', 'LET', 'THESE', 'US', 'SHALT', 'BECAUSE', 'GREAT', 'EVERY', 'SAITH', 'DOWN', 'O'] # This is the list of some of the least common words used in the bible, to save time.

# \/ THE ACTUAL CHECKING \/

print("\nChecking is in Progress . . .") # This is prints out a message saying that the spellchecker is working

for word in dictionaryWords:                                                          # This loop removes all the words in the dictionary which are longer than 18 letter, since 18 letters is the most letter a word has in the bible, to svae time.
    if len(word) >= 16 and word != "unprofitableness" and word != "unenforceability": # This checks if the word being checked has more than 16 letters, and is not certain words
        dictionaryWords.remove(word)                                                  # This removes the word from the dictionary, so later it will have less words to check, and will save time

startTimeForSize = time.time()                                                  # This sets startTimeForSize equal to the time when the code starts checking the size
for word in bibleText:                                                          # This loop will create a list with all the unique words of the bible, as well as count the total amount of words in the text. It will use the list to loop through the dictionary to save time.
    if word in uniqueWords or any(char.isdigit() for char in word) == True:     # This check if the word is already checked and if its a number.
        continue                                                                # This will tell the loop to skip this word since it is not unique anymore, or it is a number
    else:                                                                       # This is an else statement, where all the words go which are uniqe
        uniqueWords.append(word)                                                # This will add the word to the list of unique words, if its unique
        wordsInText += bibleText.count(word)                                    # This will add the amount of time the word appears in the bible to the total amount of words, to find the total amount of words.

endTimeForSize = time.time()                                                    # This sets endTimeForCheck equal to the time when the code ends checking
startTimeForCheck = time.time()                                  # This sets startTimeForCheck equal to the time when the code starts checking

for word in uniqueWords:                                         # This loop checks all the words in the unique words list, and sees if they are mispelled
    if word.lower() in commonWordList:                           # This will first check if the word is one of the common words, and if it is then it just moves on, this is to save a lot more time.
        continue                                                 # This will tell the code to skip the word since it is in the dictionary and is not mispelled.
    elif word.lower() in lessCommonWordList:                     # This will check if the word is one of the less common words in the bible, to save time
        continue                                                 # This will tell the code to skip the word since it is in the dictionary and is not mispelled.
    elif word.upper() in leastCommonWordList:                    # This will check if the word is one of the least common words in the bible, to save time
        continue                                                 # This will tell the code to skip the word since it is in the dictionary and is not mispelled.
    elif word.lower() in dictionaryWords:                        # This check if the word is in the dictionary.
        continue                                                 # This will tell the code to skip the word since it is in the dictionary and is not mispelled.
    else:                                                        # This is an else statement which all words go through if they are mispelled
        wordsMispelled += bibleText.count(word)                  # This adds the amount of times the word appears in the bible to the total amount of mispelled words.
endTimeForCheck = time.time()                                    # This sets endTimeForCheck equal to the time when the code ends checking

wordsInDictionary = wordsInText - wordsMispelled          # This sets the wordsInDictionary variable equal to the amount of words which are both in the bible and dictionary.
checkTime = round(endTimeForCheck - startTimeForCheck, 6) # This sets the checkTime variable equal to the time it took to check the text, rounded to the 1,000,000ths
sizeTime = round(endTimeForSize - startTimeForSize, 6)    # This sets the sizeTime variable equal to the time it took to check the size of thetext, rounded to the 1,000,000ths
totalTimeInMinutes = round((sizeTime+checkTime)/60, 2)    # This sets the totalTimeInMinutes variable equal to the total time in minutes, rounded to the nearest 100th.

# \/ OUTPUT \/

print("\nThere are "+str(wordsMispelled)+" words mispelled.")                                                                                                                          # This prints out the amount of words mispelled
print("There are "+str(wordsInDictionary)+" words which can be found in the dictionary.")                                                                                              # This prints out the amount of words spelled correctly
print("There is a total of "+str(wordsInText)+" words in this text.")                                                                                                                  # This prints out the amount of words in the text
print("\nIt took a total of "+str(sizeTime)+" seconds, or "+str(sizeTime*1000000)+" microseconds, to check the size of the whole text")                                                # This prints out the amount of microseconds it took to check the size of the text
print("It took a total of "+str(checkTime)+" seconds, or "+str(checkTime*1000000)+" microseconds, to check the whole text")                                                            # This prints out the amount of microseconds it took to check the text
print("It took a total of "+str(totalTimeInMinutes)+" minutes, or "+str(sizeTime+checkTime)+" seconds, or "+str((checkTime+sizeTime)*1000000)+" microseconds, to run the code")        # This prints out the amount of minutes, seconds, and microseconds it took to run the code
print("\nHope you found what you were looking for!\n")                                                                                                                                 # This prints out a nice goodbye message to the user.