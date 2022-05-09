#!/bin/sh
for x in benchmarks/blocks/task*.pddl; do 
	pyperplan -H hff -s wastar $x; 
done
