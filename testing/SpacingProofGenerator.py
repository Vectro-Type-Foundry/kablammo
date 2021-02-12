# using datetime module 
import datetime; 
  
# Drawbot Character Set Slides

#------------------ 
# Customize this stuff
#------------------ 

v='v0.17'

fonts = [
    {
        'title': 'Kablammo A',
        'fontPath': '../fonts/static/otf/Kablammo' + v + '-A.otf'
    },
    {
        'title': 'Kablammo B',
        'fontPath': '../fonts/static/otf/Kablammo' + v + '-B.otf'
    },
    {
        'title': 'Kablammo C',
        'fontPath': '../fonts/static/otf/Kablammo' + v + '-C.otf'
    },
    {
        'title': 'Kablammo D',
        'fontPath': '../fonts/static/otf/Kablammo' + v + '-D.otf'
    }
]
txtFontSize = 35
txtLineHeight = 50
numCols = 2
numRows = 20

spaceStrings=['HOH','OHO']

bgColorR, bgColorG, bgColorB, bgColorA = 1,1,1,1
textColorR, textColorG, textColorB, textColorA = 0,0,0,1

docWidth, docHeight = 800, 1150
topMargin, rightMargin, bottomMargin, leftMargin = 70, 50, 50, 50 

textBoxWidth = docWidth - leftMargin - rightMargin
textBoxHeight = docHeight - topMargin - bottomMargin

showTitle = True # enable if you'd like to display the title
titleFont = 'ISO v0.8'
titleFontSize = 18
titleTextColorR, titleTextColorG, titleTextColorB, titleTextColorA = 0,0,0,1
titleX, titleY = docWidth/2, docHeight - 50


timestamp = str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M'))
fileName = '~/Desktop/Temp/KablammoSpacingProof-' + timestamp + '.pdf'


#------------------ 
# End Customization
#------------------ 


def setup():
    newPage(docWidth, docHeight)
    fill(bgColorR, bgColorG, bgColorB, bgColorA)
    rect(0, 0, docWidth, docHeight)
    
def main():
    for f in fonts:        
        drawGlyphs(f)
        
    saveImage(fileName, multipage=True)
    
def drawGlyphs(f):
    pNum = 1
    for glyphs in glyphGroups(f['fontPath']):
        drawPage(f, glyphs, pNum)
        pNum += 1
    
def glyphGroups(fontPath):
    font(fontPath)

    glyphs = listFontGlyphNames()
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
        text(f['title'], (titleX, titleY), align='center')
    
def drawPage(f, glyphList, pNum):
    setupNewPage()
    drawTitle(f)

    txt = FormattedString()
    txt.font(f['fontPath'])
    txt.fontSize(txtFontSize)
    txt.lineHeight(txtLineHeight)

    txt.fill(textColorR,textColorG,textColorB,textColorA)

    
    tabList = []
    colWidth = textBoxWidth / (numCols)
    for col in range(numCols):
        xPos = (col * colWidth) + 1
        tabList.append((xPos, "left"))
        
    txt.tabs(*tabList)
    
    txt.append('\t')
    col = 1
    for glyph in glyphList:
        for s in spaceStrings:
            txt.append(s)
            txt.appendGlyph(glyph)
            txt.append(s)
        
        if col == numCols:
            txt.append('\n\t')
            col = 1
        else:
            txt.append('\t')
            col += 1

    textBox(txt, (leftMargin, bottomMargin, textBoxWidth, textBoxHeight))


main()


