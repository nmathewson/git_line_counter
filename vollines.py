#!/usr/bin/python

import os
import re
import subprocess

YEAR = 2015

def parse_log(year):

    cmdline = ["git",
               "log",
               "--since=%s-01-01" % year,
               "--until=%s-12-31" % year,
               "--format=:: %an",
               "--shortstat"
    ]

    p = subprocess.Popen(cmdline, stdout=subprocess.PIPE)

    lines_added = {}

    user = None

    user_pat = re.compile(r'^:: (.*)$')
    insert_pat = re.compile(r'(\d+) insertion')

    for line in p.stdout:
        m = user_pat.match(line)
        if m:
            user = m.group(1)
            continue

        m = insert_pat.search(line)
        if m:
            assert user is not None
            try:
                lines_added[user] += int(m.group(1))
            except KeyError:
                lines_added[user] = int(m.group(1))

    return lines_added

la = parse_log(2015)

for lines, user in sorted((l,u) for u, l in la.items()):
    print("% 10d  %s" % (lines, user))
