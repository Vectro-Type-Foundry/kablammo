# using datetime module 
import datetime; 
  
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
txtFontSize = 25
txtLineHeight = 45
numCols = 1
numRows = 15

spaceStrings=['HOH','OHO']

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
fileName = '~/Desktop/Temp/KablammoSpacingProof-' + timestamp + '.pdf'

blacklistSuffixes = ['.rev', '.bottomless', '.topless', '.nodot', '.toplessbottomless', '.midless']

#------------------ 
# End Customization
#------------------ 


def setup():
    newPage(docWidth, docHeight)
    fill(bgColorR, bgColorG, bgColorB, bgColorA)
    rect(0, 0, docWidth, docHeight)
    
def main():
    drawGlyphs(fonts[0])
    saveImage(fileName, multipage=True)
    
def drawGlyphs(f):
    pNum = 1
    for glyphs in glyphGroups(f['fontPath']):
        drawPage(f, glyphs, pNum)
        pNum += 1
    
def glyphGroups(fontPath):
    font(fontPath)
    
    glyphs = listFontGlyphNames()
    
    for suffix in blacklistSuffixes:        
        glyphs = list(filter(lambda g: suffix not in g, glyphs))
    
    glyphsPerPage = numCols * numRows
    glyphGroups = []
    for i in range(0, len(glyphs), glyphsPerPage):
        glyphGroups.append(glyphs[i : i+glyphsPerPage])
    
    return(glyphGroups)
    
def setupNewPage():
    newPage(docWidth, docHeight)
    fill(bgColorR, bgColorG, bgColorB, bgColorA)
    rect(0, 0, docWidth, docHeight)
    
    
def drawTitle(f):
    if showTitle:
        font(titleFont)
        fontSize(titleFontSize)
        fill(titleTextColorR, titleTextColorG, titleTextColorB, titleTextColorA)
        text('Kablammo Test: ' + timestamp, (titleX, titleY), align='center')
    
def drawPage(f, glyphList, pNum):
    setupNewPage()
    drawTitle(f)

    txt = FormattedString()
    txt.fill(textColorR,textColorG,textColorB,textColorA)

    
    tabList = []
    colWidth = textBoxWidth / (len(fonts) * numCols)
    for col in range(len(fonts) * numCols):
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

    for glyph in glyphList:
        for i, f in enumerate(fonts):
            txt.font(f['fontPath'])            
            for s in spaceStrings:
                txt.append(s)
                txt.appendGlyph(glyph)
                txt.append(s)
            #if i < len(fonts) - 1:
            txt.append('\t')
        txt.append('\n')

    textBox(txt, (leftMargin, bottomMargin, textBoxWidth, textBoxHeight))


main()


