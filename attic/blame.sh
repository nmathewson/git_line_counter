#!/bin/bash

YEAR=2015
DATE="master@{2016-01-01}"

for fn in `git ls-tree -r --name-only "$DATE"`; do
   echo "$fn" >2
   git blame "$DATE"  -- $fn
done

