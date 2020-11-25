#!/bin/bash
set -e

if [ -z "$1" ]
then
  echo "No version number supplied. Please add one as a build argument. Example"
  echo "sh build-all.sh 0.13"
  version="0.13"
else
  version=$1


  glyphsSource="working/Kablammo.glyphs"

  output_path="exports/Kablammo-v${version}"
  static_output_path="${output_path}/static"
  variable_output_path="${output_path}/variable"

  mkdir -p $output_path $static_output_path $variable_output_path 

  # Generate VFs
  VF_full_output_path="${variable_output_path}/Kablammo-Variable-v${version}.ttf"
  fontmake -g $glyphsSource -o variable --output-path $VF_full_output_path

  # Generate OTFS
  fontmake -g $glyphsSource -o otf -i --output-dir $static_output_path 

fi


