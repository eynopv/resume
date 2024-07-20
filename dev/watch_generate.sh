#!/bin/bash

run() {
  make resume
}

run

while true; do
  inotifywait -r -e modify,move,create,delete --include '.*\.py$|.*\.jinja$' . |
    while read -r file; do
      run
    done
done
