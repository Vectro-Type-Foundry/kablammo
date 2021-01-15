#!/bin/bash
set -e

if [ -z "$1" ]
then
  echo "No version number supplied. Please add one as a build argument. Example"
  echo "sh build-all.sh 0.13"
  version="0.13"
else
  version=$1


  glyphsSource="sources/Kablammo.glyphs"

  output_path="fonts/"
  static_output_path="${output_path}/static"
  variable_output_path="${output_path}/variable"

  rm -rf $output_path
  mkdir -p $output_path $static_output_path $variable_output_path 

  echo "generate variable font"
  VF_full_output_path="${variable_output_path}/Kablammo${version}[move].ttf"
  fontmake -g $glyphsSource -o variable --output-path $VF_full_output_path

  echo "generate otfs"
  fontmake -g $glyphsSource -o otf -i --output-dir $static_output_path 

  echo "add stat table"
  gftools gen-stat $VF_full_output_path --src sources/scripts/stat.yaml --inplace

  echo "misc table fixes"
  function fixMiscTables {
    gftools fix-nonhinting $1 $1
    gftools fix-fstype $1
    mv $1.fix $1 2>/dev/null
    gftools fix-dsig -f $1
  }

  fixMiscTables $VF_full_output_path
  for filename in $static_output_path/*.otf; do

    fixMiscTables $filename
  done

  # cleanup 
  echo "cleanup"
  rm -rf $static_output_path/*prep-gasp.otf
  rm -rf $variable_output_path/*prep-gasp.ttf
  rm -rf fonts/variable/*prep-gasp.ttf
  rm -rf instance_ufo
  rm -rf master_ufo
fi

