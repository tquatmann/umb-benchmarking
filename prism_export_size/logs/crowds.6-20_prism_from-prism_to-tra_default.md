# Log files

Tool configuration: prism_from-prism_to-tra_default
Benchmark: [crowds.6-20](../../models/crowds.6-20)
Parsed values: [1289226216.0, 1289226216.0, 1289226216.0, 1289226216.0, 1289226216.0]



### Log file: prism_from-prism_to-tra_default_crowds.6-20_rep1.log

```
Command(s):
../bin/prism  models/crowds.6-20/model.prism -exportmodel out/prism_from-prism_to-tra_default/crowds.6-20/model.tra,lab,rew:precision=17
Wallclock time: 42.268 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:43:41 GMT+01:00 2026
Hostname: n23m0380.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.6-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/crowds.6-20/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/crowds.6-20/model.prism"...

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

Reachability (BFS): 56 iterations in 0.13 seconds (average 0.002321, setup 0.00)

Time for model construction: 0.24 seconds.

Warning: Deadlocks detected and fixed in 230230 states

Type:        DTMC
States:      10633591 (1 initial)
Transitions: 38261191

Transition matrix: 40814 nodes (7 terminal), 38261191 minterms, vars: 78r/78c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/crowds.6-20/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/crowds.6-20/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/crowds.6-20/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/crowds.6-20/model.trew"...
Time for exporting: 41.224 seconds.

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/crowds.6-20/model.tra:	Size of output file is 1282720746 bytes
out/prism_from-prism_to-tra_default/crowds.6-20/model.lab:	Size of output file is 6505470 bytes
out/prism_from-prism_to-tra_default/crowds.6-20/model.srew:	File does not exist.
out/prism_from-prism_to-tra_default/crowds.6-20/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_crowds.6-20_rep2.log

```
Command(s):
../bin/prism  models/crowds.6-20/model.prism -exportmodel out/prism_from-prism_to-tra_default/crowds.6-20/model_rep2.tra,lab,rew:precision=17
Wallclock time: 48.749 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:20 GMT+01:00 2026
Hostname: n23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.6-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/crowds.6-20/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/crowds.6-20/model.prism"...

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

Reachability (BFS): 56 iterations in 0.20 seconds (average 0.003571, setup 0.00)

Time for model construction: 0.395 seconds.

Warning: Deadlocks detected and fixed in 230230 states

Type:        DTMC
States:      10633591 (1 initial)
Transitions: 38261191

Transition matrix: 40814 nodes (7 terminal), 38261191 minterms, vars: 78r/78c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/crowds.6-20/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/crowds.6-20/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/crowds.6-20/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/crowds.6-20/model_rep2.trew"...
Time for exporting: 47.542 seconds.

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/crowds.6-20/model_rep2.tra:	Size of output file is 1282720746 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/crowds.6-20/model_rep2.lab:	Size of output file is 6505470 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/crowds.6-20/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_default/crowds.6-20/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_crowds.6-20_rep3.log

```
Command(s):
../bin/prism  models/crowds.6-20/model.prism -exportmodel out/prism_from-prism_to-tra_default/crowds.6-20/model_rep3.tra,lab,rew:precision=17
Wallclock time: 47.267 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:12 GMT+01:00 2026
Hostname: n23m0149.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.6-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/crowds.6-20/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/crowds.6-20/model.prism"...

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

Reachability (BFS): 56 iterations in 0.15 seconds (average 0.002679, setup 0.00)

Time for model construction: 0.278 seconds.

Warning: Deadlocks detected and fixed in 230230 states

Type:        DTMC
States:      10633591 (1 initial)
Transitions: 38261191

Transition matrix: 40814 nodes (7 terminal), 38261191 minterms, vars: 78r/78c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/crowds.6-20/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/crowds.6-20/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/crowds.6-20/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/crowds.6-20/model_rep3.trew"...
Time for exporting: 44.858 seconds.

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/crowds.6-20/model_rep3.tra:	Size of output file is 1282720746 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/crowds.6-20/model_rep3.lab:	Size of output file is 6505470 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/crowds.6-20/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_default/crowds.6-20/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_crowds.6-20_rep4.log

```
Command(s):
../bin/prism  models/crowds.6-20/model.prism -exportmodel out/prism_from-prism_to-tra_default/crowds.6-20/model_rep4.tra,lab,rew:precision=17
Wallclock time: 44.065 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:01:55 GMT+01:00 2026
Hostname: n23m0142.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.6-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/crowds.6-20/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/crowds.6-20/model.prism"...

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

Reachability (BFS): 56 iterations in 0.18 seconds (average 0.003214, setup 0.00)

Time for model construction: 0.414 seconds.

Warning: Deadlocks detected and fixed in 230230 states

Type:        DTMC
States:      10633591 (1 initial)
Transitions: 38261191

Transition matrix: 40814 nodes (7 terminal), 38261191 minterms, vars: 78r/78c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/crowds.6-20/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/crowds.6-20/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/crowds.6-20/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/crowds.6-20/model_rep4.trew"...
Time for exporting: 43.003 seconds.

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/crowds.6-20/model_rep4.tra:	Size of output file is 1282720746 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/crowds.6-20/model_rep4.lab:	Size of output file is 6505470 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/crowds.6-20/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_default/crowds.6-20/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_crowds.6-20_rep5.log

```
Command(s):
../bin/prism  models/crowds.6-20/model.prism -exportmodel out/prism_from-prism_to-tra_default/crowds.6-20/model_rep5.tra,lab,rew:precision=17
Wallclock time: 47.532 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:51:16 GMT+01:00 2026
Hostname: n23m0042.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.6-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/crowds.6-20/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/crowds.6-20/model.prism"...

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

Reachability (BFS): 56 iterations in 0.14 seconds (average 0.002500, setup 0.00)

Time for model construction: 0.266 seconds.

Warning: Deadlocks detected and fixed in 230230 states

Type:        DTMC
States:      10633591 (1 initial)
Transitions: 38261191

Transition matrix: 40814 nodes (7 terminal), 38261191 minterms, vars: 78r/78c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/crowds.6-20/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/crowds.6-20/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/crowds.6-20/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/crowds.6-20/model_rep5.trew"...
Time for exporting: 46.67 seconds.

---------------------------------------------------------------------

Note: There were 33 warnings during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/crowds.6-20/model_rep5.tra:	Size of output file is 1282720746 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/crowds.6-20/model_rep5.lab:	Size of output file is 6505470 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/crowds.6-20/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_default/crowds.6-20/model_rep5.trew:	File does not exist.
```

