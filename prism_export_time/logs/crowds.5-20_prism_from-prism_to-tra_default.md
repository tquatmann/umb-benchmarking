# Log files for prism_from-prism_to-tra_default on model [crowds.5-20](../../models/crowds.5-20)

Parsed values: `[8.766, 9.949, 8.482, 8.397, 8.951]`



### Log file: prism_from-prism_to-tra_default_crowds.5-20_rep1.log

```
Command(s):
../bin/prism  models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-tra_default/crowds.5-20/model.tra,lab,rew:precision=17
Wallclock time: 9.534 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:48:25 GMT+01:00 2026
Hostname: n23m0273.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/crowds.5-20/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 47 iterations in 0.09 seconds (average 0.001915, setup 0.00)

Time for model construction: 0.191 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 33232 nodes (7 terminal), 7374951 minterms, vars: 78r/78c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/crowds.5-20/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/crowds.5-20/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/crowds.5-20/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/crowds.5-20/model.trew"...
Time for exporting: 8.766 seconds.

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/crowds.5-20/model.tra:	Size of output file is 239739395 bytes
out/prism_from-prism_to-tra_default/crowds.5-20/model.lab:	Size of output file is 1042450 bytes
out/prism_from-prism_to-tra_default/crowds.5-20/model.srew:	File does not exist.
out/prism_from-prism_to-tra_default/crowds.5-20/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_crowds.5-20_rep2.log

```
Command(s):
../bin/prism  models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-tra_default/crowds.5-20/model_rep2.tra,lab,rew:precision=17
Wallclock time: 11.252 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:26:25 GMT+01:00 2026
Hostname: n23m0247.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/crowds.5-20/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 47 iterations in 0.14 seconds (average 0.002979, setup 0.00)

Time for model construction: 0.29 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 33232 nodes (7 terminal), 7374951 minterms, vars: 78r/78c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/crowds.5-20/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/crowds.5-20/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/crowds.5-20/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/crowds.5-20/model_rep2.trew"...
Time for exporting: 9.949 seconds.

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/crowds.5-20/model_rep2.tra:	Size of output file is 239739395 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/crowds.5-20/model_rep2.lab:	Size of output file is 1042450 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/crowds.5-20/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_default/crowds.5-20/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_crowds.5-20_rep3.log

```
Command(s):
../bin/prism  models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-tra_default/crowds.5-20/model_rep3.tra,lab,rew:precision=17
Wallclock time: 10.750 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:52:17 GMT+01:00 2026
Hostname: n23m0308.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/crowds.5-20/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 47 iterations in 0.10 seconds (average 0.002128, setup 0.00)

Time for model construction: 0.343 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 33232 nodes (7 terminal), 7374951 minterms, vars: 78r/78c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/crowds.5-20/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/crowds.5-20/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/crowds.5-20/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/crowds.5-20/model_rep3.trew"...
Time for exporting: 8.482 seconds.

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/crowds.5-20/model_rep3.tra:	Size of output file is 239739395 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/crowds.5-20/model_rep3.lab:	Size of output file is 1042450 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/crowds.5-20/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_default/crowds.5-20/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_crowds.5-20_rep4.log

```
Command(s):
../bin/prism  models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-tra_default/crowds.5-20/model_rep4.tra,lab,rew:precision=17
Wallclock time: 9.083 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:50:14 GMT+01:00 2026
Hostname: n23m0044.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/crowds.5-20/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 47 iterations in 0.09 seconds (average 0.001915, setup 0.00)

Time for model construction: 0.177 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 33232 nodes (7 terminal), 7374951 minterms, vars: 78r/78c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/crowds.5-20/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/crowds.5-20/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/crowds.5-20/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/crowds.5-20/model_rep4.trew"...
Time for exporting: 8.397 seconds.

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/crowds.5-20/model_rep4.tra:	Size of output file is 239739395 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/crowds.5-20/model_rep4.lab:	Size of output file is 1042450 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/crowds.5-20/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_default/crowds.5-20/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_crowds.5-20_rep5.log

```
Command(s):
../bin/prism  models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-tra_default/crowds.5-20/model_rep5.tra,lab,rew:precision=17
Wallclock time: 9.968 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:58:22 GMT+01:00 2026
Hostname: n23m0063.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/crowds.5-20/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 47 iterations in 0.18 seconds (average 0.003830, setup 0.00)

Time for model construction: 0.347 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 33232 nodes (7 terminal), 7374951 minterms, vars: 78r/78c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/crowds.5-20/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/crowds.5-20/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/crowds.5-20/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/crowds.5-20/model_rep5.trew"...
Time for exporting: 8.951 seconds.

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/crowds.5-20/model_rep5.tra:	Size of output file is 239739395 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/crowds.5-20/model_rep5.lab:	Size of output file is 1042450 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/crowds.5-20/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_default/crowds.5-20/model_rep5.trew:	File does not exist.
```

