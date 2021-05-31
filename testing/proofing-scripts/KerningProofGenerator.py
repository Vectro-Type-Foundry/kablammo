# using datetime module 
import datetime; 
import math;
  
# Drawbot Character Set Slides

#------------------ 
# Customize this stuff
#------------------ 

v='v0.21'

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
txtLineHeight = 28
rowsPerPage = 24


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

groupsToKern = [
    ['Exceptions', 'UC'],
    ['UC', 'Exceptions'],
    ['Exceptions', 'Figures'],
    ['Figures', 'Exceptions'],
    ['Exceptions', 'Punctuation'],
    ['Punctuation', 'Exceptions']
]

firstGroups = [
    {
        'name': 'UC',
        'glyphs': 'ABCDEFGHIJKLMNŊOPÞQRSẞƏTUVWXYZ'
    },
    {
        'name': 'Figures',
        'glyphs': '0123456789'
    },
    {
        'name': 'Punctuation',
        'glyphs': '.‘’:;!¡?¿•*#/\[]-_«»⟨⟩@&¶§©°|¦ℓ№π½¼¾℮%↑↗→↘↓↙←↖↔↕'
    },
    {
        'name': 'Currency & Math',
        'glyphs': '₵¢₡¤$₫€ƒ₣₲₴₭₤₺₼₦₧₱₽₹£₸₮₩¥∙⁒∕+-×÷=≠><≥≤±≈~¬^∅∞∫Ω∆∏∑√µ∂◊'
    },
    {
        'name': 'Dingbats',
        'glyphs': '꩜☀★☆☺☼☾♈♉♊♋♌♍♎♏♐♑♒♓♡♥⚠⚡⛎✨🌐🌼🍕👀👁👄👑👻👽💎💖💥💩🔥🛸🪐'
    },
    {
        'name': 'Select Math',
        'glyphs': '¢$€£¥/+-=><~^'
    },
    {
        'name': 'Select Punct',
        'glyphs': '.‘’:;!¡?¿•*#/\[]-_@&¶§©°%'
    },
    {
        'name': 'Exceptions',
        'glyphs': 'ĦƠƯ'
    }
]
secondGroups = [
    {
        'name': 'UC',
        'glyphs': 'AÆBCDEFGHIJKLMNOPÞQRSẞƏTUVWXYZ'
    },
    {
        'name': 'Figures',
        'glyphs': '0123456789'
    },
    {
        'name': 'Punctuation',
        'glyphs': '.’:;!¡?¿•*#/\[]-_«»⟨⟩@&¶§©°|¦ℓ№π½¼¾℮%↑↗→↘↓↙←↖↔↕'
    },
    {
        'name': 'Currency & Math',
        'glyphs': '₵¢₡¤$₫€ƒ₣₲₴₭₤₺₼₦₧₱₽₹£₸₮₩¥∙⁒∕+-×÷=≠><≥≤±≈~¬^∅∞∫Ω∆∏∑√µ∂◊'
    },
    {
        'name': 'Dingbats',
        'glyphs': '꩜☀★☆☺☼☾♈♉♊♋♌♍♎♏♐♑♒♓♡♥⚠⚡⛎✨🌐🌼🍕👀👁👄👑👻👽💎💖💥💩🔥🛸🪐'
    },
    {
        'name': 'Select Math',
        'glyphs': '¢$€£¥/+-=><~^'
    },
    {
        'name': 'Select Punct',
        'glyphs': '.‘’:;!¡?¿•*#/\[]-_@&¶§©°%'
    },
    {
        'name': 'Problem Second',
        'glyphs': 'ATVWXY'
    },
    {
        'name': 'Exceptions',
        'glyphs': 'ĦŁ'
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
 

def findGroup(name, position):
    groupLists = [firstGroups, secondGroups]
    groupList = groupLists[position]
    return next(group for group in groupList if group['name'] == name)
    
def buildCombinationGroups():
    global combinationGroups
    combinationGroups = []
    
    for groupPair in groupsToKern:
        firstGroup = findGroup(groupPair[0], 0)
        secondGroup = findGroup(groupPair[1], 1)
    
        combinations = []
        for firstGlyph in list(firstGroup['glyphs']):
            for secondGlyph in list(secondGroup['glyphs']):
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
    txt.openTypeFeatures(calt=False)                
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


