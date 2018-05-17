#!/bin/bash

YEAR=2015
BRANCH=master
START_DATE="${YEAR}-01-01"
END_DATE="${YEAR}-12-31"

rm -f blame_all
touch blame_all

which=`git log --since="$START_DATE" --until="$END_DATE" -n 1 --format='%an' --shortstat`

for fn in `git ls-tree -r --name-only $which`; do
   git blame "$which"  -- $fn >> blame_all
done

grep "${YEAR}-" blame_all | perl -pe 's/^[^\(]+\(//; s/\s+20\d+-\d+-\d+.*//;' | sort |uniq -c|sort -n

