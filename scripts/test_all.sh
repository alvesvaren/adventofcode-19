#!/bin/sh

for file in *{a,b}.py
do
    echo; echo "$file:"
    python "./$file"
done