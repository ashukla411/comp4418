#!/usr/bin/python
import random

#ran on cse machine under z5151301

variables = input("Enter the number of propositional variables:\n")
clauses = input("Enter the number of clauses to generate randomly:\n")
#creating only 1 file.cnf to test, so run the entire program multiple times to test different scenarios
file=open("file.cnf","wb")
file.write("c example CNF file with {} propositional variables and {} clauses\n".format(variables,clauses))
file.write("p cnf {} {}\n".format(variables,clauses))

#generating random clauses and variable formulas in those clauses
for i in range(1,clauses+1):
	formula = ""
	j=0
#4 literal specification for 4-SAT
	while(j<4):
		num = random.randint(-variables,variables)
		while(num==0):
			num = random.randint(-variables,variables)
		if (`num` not in formula and `-num` not in formula):
			formula = formula + `num` +" "
			j=j+1
	formula = formula+"0\n"
#writing a clause into a file-line for 4-SAT only
	file.write(formula)
file.close()
