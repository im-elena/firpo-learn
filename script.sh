#!/bin/bash

getsize() {
  local size=$(du -hs "$1" )
  #2>/dev/null | cut -f1
  echo $size
}
IFS=$'\n'
items=($(ls -A))
unset IFS
for i in "${items[@]}"; do
  gs="$(getsize "$i")"
  echo -e "$gs\t$i"
done | sort -rh -k1,1