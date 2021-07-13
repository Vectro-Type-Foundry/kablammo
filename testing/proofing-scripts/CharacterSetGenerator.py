# using datetime module 
import datetime; 
  
# Drawbot Character Set Slides

#------------------ 
# Customize this stuff
#------------------ 

v='v0.22'

fonts = [
    {
        'title': 'Kablammo A',
        'fontPath': '../../fonts/static/otf/Kablammo' + v + '-A.otf'
    },
    {
        'title': 'Kablammo B',
        'fontPath': '../../fonts/static/otf/Kablammo' + v + '-B.otf'
    },
    {
        'title': 'Kablammo C',
        'fontPath': '../../fonts/static/otf/Kablammo' + v + '-C.otf'
    },
    {
        'title': 'Kablammo D',
        'fontPath': '../../fonts/static/otf/Kablammo' + v + '-D.otf'
    }
]
txtFontSize = 60
txtLineHeight = 100
numCols = 3
numRows = 10

bgColorR, bgColorG, bgColorB, bgColorA = 1,1,1,1
textColorR, textColorG, textColorB, textColorA = 0,0,0,1

docWidth, docHeight = 800, 1150
topMargin, rightMargin, bottomMargin, leftMargin = 70, 20, 50, 20 

textBoxWidth = docWidth - leftMargin - rightMargin
textBoxHeight = docHeight - topMargin - bottomMargin

showTitle = True # enable if you'd like to display the title
titleFont = 'ISO v0.9'
titleFontSize = 12
titleTextColorR, titleTextColorG, titleTextColorB, titleTextColorA = 0,0,0,1
titleX, titleY = docWidth/2, docHeight - 50


timestamp = str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M'))
fileName = '~/Desktop/Temp/KablammoCharacterSet-' + timestamp + '.pdf'

blacklistSuffixes = ['.rev', '.bottomless', '.topless', '.nodot', '.toplessbottomless', '.midless']
wideGlyphs = ['uni01C4', 'uni01CA', 'border_4', 'pattern_1', 'pattern_3', 'kablammo_blast', 'kablammo', 'kablammocyrillic']

#------------------ 
# End Customization
#------------------ 


def setup():
    newPage(docWidth, docHeight)
    fill(bgColorR, bgColorG, bgColorB, bgColorA)
    rect(0, 0, docWidth, docHeight)
    
def main():
    #for f in fonts:        
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
    
    for name in wideGlyphs:
        glyphs = list(filter(lambda g: g != name, glyphs))
        
    for name in wideGlyphs:
        glyphs.append(name)
            
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
        text('Kablammo Character Set: ' + timestamp, (titleX, titleY), align='center')
    
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
        xPos = (col * colWidth) + (colWidth * .5)
        tabList.append((xPos, "center"))
        
    txt.tabs(*tabList)
    
    txt.append('\t')
    col = 1
    for glyph in glyphList:
        for i, f in enumerate(fonts):            
            txt.font(f['fontPath'])
            txt.appendGlyph(glyph)
        if col == numCols:
            txt.append('\n\t')
            col = 1
        else:
            txt.append('\t')
            col += 1

    textBox(txt, (leftMargin, bottomMargin, textBoxWidth, textBoxHeight))
    #fileName = "exports/{0}-{1}.png".format((f['title']), pNum).replace(' ', '-')
    #saveImage(fileName)

main()


