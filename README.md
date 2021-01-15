# Kablammo Variable Font

## Axes
- Movement(`move`): 1-1000 
  - Makes the glyphs dance!

## Build

Requirements
- Python 3
- Recent version of [fontmake](https://github.com/googlefonts/fontmake)

Setup (optional but recommended method to install dependences)
1. In terminal `cd` to project directory (tip: type `cd ` then drag folder into terminal for path)
2. run `virtualenv venv` 
3. run `source venv/bin/activate`
4. run `pip install -U -r requirements.txt`

Generate
1. In terminal `cd` to project directory
2. run `source venv/bin/activate`
3. run `sh sources/build-all.sh 0.13`. (use desired version number in place of `0.13`)
4. If successful, generated fonts should show up in `exports` directory under the specified version.


## Production Notes
- Brace layers that share axis values must have the same name, and belong to the same parent master, for fontmake generation. Please use the convention of `166 {166}`, when naming brace layers. 
- Brace layers must be assigned to the parent master in a way that makes sense for the axis values. For example, axis value of `166` is greater than master `A`(1), and less than `B`(333), so the brace layer `166 {166}`, should belong to `A`. `500 {500}` should belong to master `B`.

## Design notes
Will move this to readme eventually, but for now, it's here:
https://www.dropbox.com/scl/fi/e342iuhexlpbdsoy4fe63/Design-Notes.paper?dl=0&rlkey=j91pgf0dki1uz7pgtkdovr4os