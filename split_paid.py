#!/usr/bin/python
# coding=utf-8
import sys

PAID = set(name.strip() for name in """
Arlo Breault
Andrea Shepard
Arthur Edelstein
David Goulet
Donncha O'Cearbhaill
Georg Koppen
George Kadianakis
Jacob Appelbaum
Karsten Loesing
Mike Perry
Nick Mathewson
Roger Dingledine
Sebastian Hahn
Sukhbir Singh
Yawning Angel
Kathy Brade
Cristóbal
""".strip().split("\n"))

# Extra ilv -- 4283 for work outside tsop months.
# Isis did 83067 on bridgedb!  Was it paid??

UNPAID = set(name.strip() for name in """
David Fifield
Damian Johnson
Peter Palfrader
Sina Rabbani
Yan Zhu
iwakeh
leeroy
orlando
poly
vi
Joan Queralt
Foxboron
Randall Degges
Robert Ransom
Sharif Olorin
Alden S. Page
Andreas Stieger
Andrew Kvalheim
Anthony G. Basile
Chaoyi Zha
Daniel Martí
Fabian Keil
Jamie Nguyen
Jeremy
John Brooks
Kevin Butler
Linus Nordberg
Marcin Cieślak
Matthew Finkel
Ola Bini
Patrick Schleizer
Reinaldo de Souza Jr
Tom van der Woerdt
Tomasz Torcz
anonym
cypherpunks
intrigeri
linostar
rl1987
teor
teor (Tim Wilson-Brown)
tom lurge
Amogh Pradeep
George Tankersley
Nima Fatemi
Philipp Winter
Sambuddha Basu
Serene Han
icodemachine
""".strip().split("\n"))


paid = 0
unpaid = 0
unknown = 0
unknown_folks = set()

for line in sys.stdin:
    if line[0] == '/':
        continue
    items = line.split()
    n = int(items[0])

    name = " ".join(items[1:])

    if name in PAID:
        paid += n
    elif name in UNPAID:
        unpaid += n
    else:
        unknown += n
        unknown_folks.add(name)

print "%d\t%d"%(paid,unpaid)
#print "%d lines paid"%paid
#print "%d lines unpaid"%unpaid
#print "%d lines unknown"%unknown
#print "I don't know:"
#for name in sorted(unknown_folks):
#Q    print name

