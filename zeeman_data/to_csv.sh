#!/bin/bash

function convert {
  in_file=$1
  out_file="$(echo "${in_file}" |sed s/\.[^.]*$/\.csv/)"

  echo "${in_file} -> ${out_file}"
  cat "${in_file}" |grep -oE '[0-9]+(\.[0-9]+) [0-9]+' |tr ' ' ',' > "${out_file}"
}

for i in *.dat; do
  convert "$i"
done
