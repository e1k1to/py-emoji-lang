from operator import itemgetter as ig
import sys
emojiAliasses = {}
def aliasses():
    global emojiAliasses
    emojiAliasses= {
    '👋':'Hello',
    '🌎':'World',
    '🖨':'print',
    '🌜':'(',
    '🌛':')',
    '❕':'!',
    '❗':'!',
    '📎':'"',
    '🖇':"'",
    '🕳':' ',
    '👙':'strip',
    '👍':'True',
    '👎':'False',
    '🔁':'for',
    '🔂':'while',
    '📑':'  ',
    '📄':'"""',
    '📝':'#',
    '👐':'range',
    '➡':'in',
    '↩':'return',
    '🚩':'raise',
    '⛔':'break',
    '🤝':'and',
    '❌':'not',
    '🙌':'or',
    '⏪':'=',
    '✈':'import',
    '🎲':'random',
    '🔢':'randint',
    '🤔':'choice',
    '⏲':'time',
    '💤':'sleep',
    '👠':'upper',
    '👟':'lower',
    '🤏':'len',
    '📮':'def',
    '📬':'class',
    '📚':'read',
    '🖊':'write',
    '👉':'as',
    '📭':'open',
    '📪':'close',
    '☯':'with',
    '✖':'*',
    '➗':'/',
    '➖':'-',
    '➕':'+',
    '🔝':'+= 1',
    '👌':'pop',
    '👉':'[',
    '👈':']',
    '🤜':'{',
    '🤛':'}'
    }

def emojiToPy(emojiCode):
    emojiList = tuple(emojiCode)
    codestart = False
    code = ''
    for emoji in emojiList:
        if emoji in emojiAliasses:
            code += ig(emoji)(emojiAliasses)
        else:
            code+= emoji
    exec(code)

def usage():
    print('''py-emoji-lang usage:\n\npython3 compiler.py {file.mongus}''')

def main():
    aliasses()
    if len(sys.argv) == 1:
        print('Incorrect usage.')
        usage()
        sys.exit()
    else:
        file = sys.argv[1]
        emojiCode = ''
        with open(file,'r') as ecode:
            emojiCode += str(ecode.read())
        emojiToPy(emojiCode)

main()
