#!/bin/bash
set -e

if [ -z "$1" ]
then
  echo "No version number supplied. If you wish to update the version number in UFOs & built fonts, add one as a build argument:"
  echo "build-all.sh 0.13"
  version="0.13"
else
  version=$1
fi


glyphsSource="working/Kablammo.glyphs"
version="0.13"

output_path="exports/Kablammo-v${version}"
static_output_path="${output_path}/static"
variable_output_path="${output_path}/variable"

mkdir -p $output_path $static_output_path $variable_output_path 

# Generate VFs
VF_full_output_path="${variable_output_path}/Kablammo-Variable-v${version}.ttf"

fontmake -g $glyphsSource -o variable --output-path $VF_full_output_path --feature-writer None
# fontmake -g $glyphsSource -o variable --output-path $VF_full_output_path
