#!/bin/sh

# Use with
# 1. `./copy.sh 1`
# 2. `./copy.sh 14`
# 3. `./copy.sh ..`
# Generates dayXX.cpp from template.cpp
# Adds dayXX.cpp build recipe into makefile

single_digit="^[0-9]$"
valid_day="^([01][0-9]|2[0-5])$"
dependencies=" parser.o" # Update dependencies here as required

if [ "$#" -lt "1" ]; then
  echo "Day is missing. Use '$0 xx' to generate dayxx."
fi

while [ "$#" -gt "0" ]
do
  day=$1
  shift

  # pad 0 for single digit (i.e. 2 -> 02)
  if [[ "$day" =~ $single_digit ]]; then
    day="0$day"
  fi
  if ! [[ "$day" =~ $valid_day ]]; then
    echo "$day is an invalid day, skipping!"
    continue
  fi

  name="day$day"
  object_file="$name.o"
  file="$name.cpp"

  if [ -f $file ]; then
    echo "$file already exists, skipping!"
    continue
  fi

  cp template.cpp $file

  mkdir -p bin
  # add recipe into makefile
  make_recipe="d$day"
  make_build_recipe="d$day-build"
  echo "" >> makefile
  echo "$make_recipe: $make_build_recipe" >> makefile
  echo "\tbin/$name" >> makefile

  echo "$make_build_recipe: $object_file $dependencies" >> makefile
	echo "\tcd bin; \\" >> makefile
	echo "\t\$(CC) -o $name $object_file $dependencies" >> makefile

  echo "$object_file: $file" >> makefile
	echo "\t\$(CC) -c -o bin/$object_file $file" >> makefile

  echo "Created day$day."
done
