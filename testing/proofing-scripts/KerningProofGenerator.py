# using datetime module 
import datetime; 
import math;
  
# Drawbot Character Set Slides

#------------------ 
# Customize this stuff
#------------------ 

v='v0.20'

fonts = [
    {
        'title': 'A',
        'fontPath': '../../fonts/static/otf/Kablammo' + v + '-A.otf'
    },
    {
        'title': 'B',
        'fontPath': '../../fonts/static/otf/Kablammo' + v + '-B.otf'
    },
    {
        'title': 'C',
        'fontPath': '../../fonts/static/otf/Kablammo' + v + '-C.otf'
    },
    {
        'title': 'D',
        'fontPath': '../../fonts/static/otf/Kablammo' + v + '-D.otf'
    }
]
txtFontSize = 24
txtLineHeight = 45
rowsPerPage = 15


bgColorR, bgColorG, bgColorB, bgColorA = 1,1,1,1
textColorR, textColorG, textColorB, textColorA = 0,0,0,1

docWidth, docHeight = 1150, 800
topMargin, rightMargin, bottomMargin, leftMargin = 60, 40, 40, 40 

textBoxWidth = docWidth - leftMargin - rightMargin
textBoxHeight = docHeight - topMargin - bottomMargin

showTitle = True # enable if you'd like to display the title
titleFont = 'ISO v0.9'
titleFontSize = 12
titleTextColorR, titleTextColorG, titleTextColorB, titleTextColorA = 0,0,0,1
titleX, titleY = docWidth/2, docHeight - 50


timestamp = str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M'))
fileName = '~/Desktop/Temp/KablammoKerningProof-' + timestamp + '.pdf'

pairsPerRow = 2

separator = 'HOH'

firstGroups = [
    {
        'name': 'UC',
        'active': True,
        'glyphs': ["A", "Æ", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "ẞ", "Þ"] 
    },
    {
        'name': 'Figures',
        'active': False,
        'glyphs': ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] 
    },
    {
        'name': 'Punctuation',
        'active': False,
        'glyphs': ["½", "¼", "¾", ".", ":", ";", "!", "¡", "?", "¿", "•", "*", "#", "/", "/", "\\", "[", "]", "-", "_", "’", "«", "»", "‹", "›", "⟨", "⟩", "₵", "¢", "₡", "¤", "$", "₫", "€", "ƒ", "₣", "₲", "₴", "₭", "₤", "₺", "₼", "₦", "₧", "₱", "₽", "₹", "£", "₸", "₮", "₩", "¥", "∙", "⁒", "∕", "+", "×", "÷", "=", "≠", ">", "<", "≥", "≤", "±", "≈", "~", "¬", "^", "∅", "∞", "∫", "Ω", "∆", "∏", "∑", "√", "µ", "∂", "%", "‰", "↑", "↗", "→", "↘", "↓", "↙", "←", "↖", "↔", "↕", "◊", "@", "&", "¶", "§", "©", "®", "™", "°", "′", "″", "|", "¦", "†", "ℓ", "‡", "№", "℮", "₀", "⁰", 'ª', 'º', 'π']  
    },
    {
        'name': 'Dingbats',
        'active': False,
        'glyphs': ["꩜", "☀", "★", "☆", "☺", "☼", "☾", "♈", "♉", "♊", "♋", "♌", "♍", "♎", "♏", "♐", "♑", "♒", "♓", "♡", "♥", "⚠", "⚡", "⛎", "✨", "🌐", "🌼", "🍕", "👀", "👁", "👄", "👑", "👻", "👽", "💎", "💖", "💥", "💩", "🔥", "🛸", "🪐", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    }
]
secondGroups = [
    {
        'name': 'UC',
        'active': True,
        'glyphs': ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "Ŀ", "M", "N", "Ŋ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "ẞ", "Þ"]
    },
    {
        'name': 'Figures',
        'active': False,
        'glyphs': ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] 
    },
    {
        'name': 'Punctuation',
        'active': False,
        'glyphs': ["½", "¼", "¾", ".", ":", ";", "!", "¡", "?", "¿", "•", "*", "#", "/", "/", "\\", "[", "]", "-", "_", "’", "«", "»", "‹", "›", "⟨", "⟩", "₵", "¢", "₡", "¤", "$", "₫", "€", "ƒ", "₣", "₲", "₴", "₭", "₤", "₺", "₼", "₦", "₧", "₱", "₽", "₹", "£", "₸", "₮", "₩", "¥", "∙", "⁒", "∕", "+", "×", "÷", "=", "≠", ">", "<", "≥", "≤", "±", "≈", "~", "¬", "^", "∅", "∞", "∫", "Ω", "∆", "∏", "∑", "√", "µ", "∂", "%", "‰", "↑", "↗", "→", "↘", "↓", "↙", "←", "↖", "↔", "↕", "◊", "@", "&", "¶", "§", "©", "®", "™", "°", "′", "″", "|", "¦", "†", "ℓ", "‡", "№", "℮", "₀", "⁰", 'ª', 'º', 'π']  
    },
    {
        'name': 'Dingbats',
        'active': False,
        'glyphs': ["꩜", "☀", "★", "☆", "☺", "☼", "☾", "♈", "♉", "♊", "♋", "♌", "♍", "♎", "♏", "♐", "♑", "♒", "♓", "♡", "♥", "⚠", "⚡", "⛎", "✨", "🌐", "🌼", "🍕", "👀", "👁", "👄", "👑", "👻", "👽", "💎", "💖", "💥", "💩", "🔥", "🛸", "🪐", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    }
]







combinationGroups = []

#------------------ 
# End Customization
#------------------ 

    
def main():
    buildCombinationGroups()
    drawGlyphs(fonts[0])
    saveImage(fileName, multipage=True)
    
    
def buildCombinationGroups():
    global combinationGroups
    combinationGroups = []
    for firstGroup in firstGroups:
        for secondGroup in secondGroups:
            if firstGroup['active'] and secondGroup['active']:
                combinations = []
                for firstGlyph in firstGroup['glyphs']:
                    for secondGlyph in secondGroup['glyphs']:
                        combinations.append("%s%s" % (firstGlyph, secondGlyph))
                        
                combinationGroups.append({
                    'name': "%s -> %s" % (firstGroup['name'], secondGroup['name']),
                    'combinations': combinations
                    }) 

def numberOfCombinations():
    total = 0
    for group in combinationGroups:
        total += len(group['combinations'])
    return total
            
def combinationsToPages(combinations):
    combinationsPerPage = pairsPerRow * rowsPerPage    
    pages = []
    for i in range(0, len(combinations), combinationsPerPage):
        pages.append(combinations[i : i+combinationsPerPage])
    return pages
    
def combinationsToRows(combinations):
    rows = []
    for i in range(0, len(combinations), pairsPerRow):
        rows.append(combinations[i : i+pairsPerRow])
    return rows

def drawGlyphs(f):
    pNum = 1
    for group in combinationGroups:
        for page in combinationsToPages(group['combinations']):
            pNum += 1
            drawPage(f, page, group['name'], pNum)
        
def setupNewPage():
    newPage(docWidth, docHeight)
    fill(bgColorR, bgColorG, bgColorB, bgColorA)
    rect(0, 0, docWidth, docHeight)
    
    
def drawPageTitle(f):
    if showTitle:
        font(titleFont)
        fontSize(titleFontSize)
        fill(titleTextColorR, titleTextColorG, titleTextColorB, titleTextColorA)
        text('Kablammo Kerning Test: ' + timestamp, (titleX, titleY), align='center')

def drawSectionTitle(sectionName):
    font(titleFont)
    fontSize(titleFontSize)
    fill(titleTextColorR, titleTextColorG, titleTextColorB, titleTextColorA)
    
    text(sectionName, (leftMargin, titleY), align='left')

def drawPage(f, combinations, sectionName, pNum):
    setupNewPage()
    drawPageTitle(f)
    drawSectionTitle(sectionName)
    txt = FormattedString()
    txt.fill(textColorR,textColorG,textColorB,textColorA)

    
    tabList = []
    colWidth = textBoxWidth / len(fonts)
    for col in range(len(fonts)):
        xPos = (col * colWidth) + 1
        tabList.append((xPos, "left"))
        
    txt.tabs(*tabList)
    
    #txt.append('\t')
    col = 1
    for f in fonts:
        txt.font(titleFont)
        txt.fontSize(12)
        txt.lineHeight(12)
        txt.append(f['title'] + '\t')
    txt.append('\n')        
        
    txt.fontSize(txtFontSize)
    txt.lineHeight(txtLineHeight)

    for rowCombinations in combinationsToRows(combinations):
        for f in fonts:
            txt.font(f['fontPath'])
            for combination in rowCombinations:                
                txt.append(separator)
                txt.append(combination)
                txt.append(separator)
            txt.append('\t')

    textBox(txt, (leftMargin, bottomMargin, textBoxWidth, textBoxHeight))


main()


