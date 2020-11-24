# Kablammo Variable Font

## Axes
Movement(move): 1-1000

## Design notes
Will move this to readme eventually, but for now, it's here:
https://www.dropbox.com/scl/fi/e342iuhexlpbdsoy4fe63/Design-Notes.paper?dl=0&rlkey=j91pgf0dki1uz7pgtkdovr4os


## Build

Setup
1. In terminal `cd` to project directory
2. `virtualenv venv`
3. `source venv/bin/activate`
4. `pip install -U -r requirements.txt`

Generate
1. `sh build-all.sh`


## Production Notes
- Brace layers that share axis values must have the same name, and belong to the same parent master, for fontmake generation. Please use the convention of `166 {166}`, when naming brace layers. And assign them to the parent master in a way that makes sense for the axis values. For example, axis value of `166` is greater than master `A`(1), and less than `B`(333), so the brace layer `166 {166}`, should belong to `A`. `500 {500}` should belong to master `B`.