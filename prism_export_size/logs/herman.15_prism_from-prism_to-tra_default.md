# Log files for prism_from-prism_to-tra_default on model [herman.15](../../models/herman.15)

Parsed values: `[419647423.0, 419647423.0, 419647423.0, 419647423.0, 419647423.0]`



### Log file: prism_from-prism_to-tra_default_herman.15_rep1.log

```
Command(s):
../bin/prism  models/herman.15/model.prism -exportmodel out/prism_from-prism_to-tra_default/herman.15/model.tra,lab,rew:precision=17
Wallclock time: 7.345 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:38:54 GMT+01:00 2026
Hostname: n23m0273.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/herman.15/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/herman.15/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/herman.15/model.prism"...

Type:        DTMC
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10 process11 process12 process13 process14 process15
Actions:     [step]
Variables:   x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15
Labels:      "stable"
Rewards:     "steps"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.013 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908

Transition matrix: 810 nodes (9 terminal), 14348908 minterms, vars: 15r/15c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/herman.15/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/herman.15/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/herman.15/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/herman.15/model.trew"...
Time for exporting: 6.3 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/herman.15/model.tra:	Size of output file is 419112383 bytes
out/prism_from-prism_to-tra_default/herman.15/model.lab:	Size of output file is 283895 bytes
out/prism_from-prism_to-tra_default/herman.15/model.srew:	Size of output file is 251089 bytes
out/prism_from-prism_to-tra_default/herman.15/model.trew:	Size of output file is 56 bytes
```



### Log file: prism_from-prism_to-tra_default_herman.15_rep2.log

```
Command(s):
../bin/prism  models/herman.15/model.prism -exportmodel out/prism_from-prism_to-tra_default/herman.15/model_rep2.tra,lab,rew:precision=17
Wallclock time: 7.029 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:25:55 GMT+01:00 2026
Hostname: r23m0016.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/herman.15/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/herman.15/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/herman.15/model.prism"...

Type:        DTMC
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10 process11 process12 process13 process14 process15
Actions:     [step]
Variables:   x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15
Labels:      "stable"
Rewards:     "steps"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.015 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908

Transition matrix: 810 nodes (9 terminal), 14348908 minterms, vars: 15r/15c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/herman.15/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/herman.15/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/herman.15/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/herman.15/model_rep2.trew"...
Time for exporting: 6.409 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/herman.15/model_rep2.tra:	Size of output file is 419112383 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/herman.15/model_rep2.lab:	Size of output file is 283895 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/herman.15/model_rep2.srew:	Size of output file is 251089 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/herman.15/model_rep2.trew:	Size of output file is 56 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_default_herman.15_rep3.log

```
Command(s):
../bin/prism  models/herman.15/model.prism -exportmodel out/prism_from-prism_to-tra_default/herman.15/model_rep3.tra,lab,rew:precision=17
Wallclock time: 6.487 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:23:42 GMT+01:00 2026
Hostname: r23m0204.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/herman.15/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/herman.15/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/herman.15/model.prism"...

Type:        DTMC
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10 process11 process12 process13 process14 process15
Actions:     [step]
Variables:   x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15
Labels:      "stable"
Rewards:     "steps"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.013 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908

Transition matrix: 810 nodes (9 terminal), 14348908 minterms, vars: 15r/15c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/herman.15/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/herman.15/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/herman.15/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/herman.15/model_rep3.trew"...
Time for exporting: 5.921 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/herman.15/model_rep3.tra:	Size of output file is 419112383 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/herman.15/model_rep3.lab:	Size of output file is 283895 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/herman.15/model_rep3.srew:	Size of output file is 251089 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/herman.15/model_rep3.trew:	Size of output file is 56 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_default_herman.15_rep4.log

```
Command(s):
../bin/prism  models/herman.15/model.prism -exportmodel out/prism_from-prism_to-tra_default/herman.15/model_rep4.tra,lab,rew:precision=17
Wallclock time: 6.487 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:02 GMT+01:00 2026
Hostname: n23m0281.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/herman.15/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/herman.15/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/herman.15/model.prism"...

Type:        DTMC
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10 process11 process12 process13 process14 process15
Actions:     [step]
Variables:   x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15
Labels:      "stable"
Rewards:     "steps"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.012 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908

Transition matrix: 810 nodes (9 terminal), 14348908 minterms, vars: 15r/15c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/herman.15/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/herman.15/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/herman.15/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/herman.15/model_rep4.trew"...
Time for exporting: 5.932 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/herman.15/model_rep4.tra:	Size of output file is 419112383 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/herman.15/model_rep4.lab:	Size of output file is 283895 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/herman.15/model_rep4.srew:	Size of output file is 251089 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/herman.15/model_rep4.trew:	Size of output file is 56 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_default_herman.15_rep5.log

```
Command(s):
../bin/prism  models/herman.15/model.prism -exportmodel out/prism_from-prism_to-tra_default/herman.15/model_rep5.tra,lab,rew:precision=17
Wallclock time: 7.135 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:14:02 GMT+01:00 2026
Hostname: n23m0099.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/herman.15/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/herman.15/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/herman.15/model.prism"...

Type:        DTMC
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10 process11 process12 process13 process14 process15
Actions:     [step]
Variables:   x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15
Labels:      "stable"
Rewards:     "steps"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.014 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908

Transition matrix: 810 nodes (9 terminal), 14348908 minterms, vars: 15r/15c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/herman.15/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/herman.15/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/herman.15/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/herman.15/model_rep5.trew"...
Time for exporting: 6.57 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/herman.15/model_rep5.tra:	Size of output file is 419112383 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/herman.15/model_rep5.lab:	Size of output file is 283895 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/herman.15/model_rep5.srew:	Size of output file is 251089 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/herman.15/model_rep5.trew:	Size of output file is 56 bytes
Removing output file to save space for repetition #5
```

