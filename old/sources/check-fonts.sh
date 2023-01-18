#!/bin/bash
set -e

fontbakery check-googlefonts fonts/*.ttf  --json fontbakery-report-variable.json

# fontbakery check-googlefonts fonts/static/otf/Kablammo-A.otf  --json fontbakery-report-otf.json

# fontbakery check-googlefonts fonts/static/ttf/Kablammo-A.ttf  --json fontbakery-report-ttf.json