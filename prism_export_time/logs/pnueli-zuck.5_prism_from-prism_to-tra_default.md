# Log files

Tool configuration: prism_from-prism_to-tra_default
Benchmark: [pnueli-zuck.5](../../models/pnueli-zuck.5)
Parsed values: [1.232, 1.16, 1.345, 1.417, 1.055]



### Log file: prism_from-prism_to-tra_default_pnueli-zuck.5_rep1.log

```
Command(s):
../bin/prism  models/pnueli-zuck.5/model.prism -exportmodel out/prism_from-prism_to-tra_default/pnueli-zuck.5/model.tra,lab,rew:precision=17
Wallclock time: 1.957 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:34:37 GMT+01:00 2026
Hostname: n23m0134.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.5/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/pnueli-zuck.5/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/pnueli-zuck.5/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4
Actions:     []
Variables:   p0 p1 p2 p3 p4
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.05 seconds (average 0.001316, setup 0.00)

Time for model construction: 0.082 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2492035

Transition matrix: 5161 nodes (3 terminal), 2492035 minterms, vars: 20r/20c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/pnueli-zuck.5/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/pnueli-zuck.5/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/pnueli-zuck.5/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/pnueli-zuck.5/model.trew"...
Time for exporting: 1.232 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/pnueli-zuck.5/model.tra:	Size of output file is 44098427 bytes
out/prism_from-prism_to-tra_default/pnueli-zuck.5/model.lab:	Size of output file is 97042 bytes
out/prism_from-prism_to-tra_default/pnueli-zuck.5/model.srew:	File does not exist.
out/prism_from-prism_to-tra_default/pnueli-zuck.5/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_pnueli-zuck.5_rep2.log

```
Command(s):
../bin/prism  models/pnueli-zuck.5/model.prism -exportmodel out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep2.tra,lab,rew:precision=17
Wallclock time: 1.811 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:01 GMT+01:00 2026
Hostname: n23m0099.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.5/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/pnueli-zuck.5/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4
Actions:     []
Variables:   p0 p1 p2 p3 p4
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.05 seconds (average 0.001316, setup 0.00)

Time for model construction: 0.085 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2492035

Transition matrix: 5161 nodes (3 terminal), 2492035 minterms, vars: 20r/20c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep2.trew"...
Time for exporting: 1.16 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep2.tra:	Size of output file is 44098427 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep2.lab:	Size of output file is 97042 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_pnueli-zuck.5_rep3.log

```
Command(s):
../bin/prism  models/pnueli-zuck.5/model.prism -exportmodel out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep3.tra,lab,rew:precision=17
Wallclock time: 2.179 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:08 GMT+01:00 2026
Hostname: r23m0177.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.5/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/pnueli-zuck.5/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4
Actions:     []
Variables:   p0 p1 p2 p3 p4
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.05 seconds (average 0.001316, setup 0.00)

Time for model construction: 0.1 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2492035

Transition matrix: 5161 nodes (3 terminal), 2492035 minterms, vars: 20r/20c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep3.trew"...
Time for exporting: 1.345 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep3.tra:	Size of output file is 44098427 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep3.lab:	Size of output file is 97042 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_pnueli-zuck.5_rep4.log

```
Command(s):
../bin/prism  models/pnueli-zuck.5/model.prism -exportmodel out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep4.tra,lab,rew:precision=17
Wallclock time: 2.283 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:29 GMT+01:00 2026
Hostname: n23m0230.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.5/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/pnueli-zuck.5/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4
Actions:     []
Variables:   p0 p1 p2 p3 p4
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.07 seconds (average 0.001842, setup 0.00)

Time for model construction: 0.122 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2492035

Transition matrix: 5161 nodes (3 terminal), 2492035 minterms, vars: 20r/20c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep4.trew"...
Time for exporting: 1.417 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep4.tra:	Size of output file is 44098427 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep4.lab:	Size of output file is 97042 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_pnueli-zuck.5_rep5.log

```
Command(s):
../bin/prism  models/pnueli-zuck.5/model.prism -exportmodel out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep5.tra,lab,rew:precision=17
Wallclock time: 1.679 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:25:43 GMT+01:00 2026
Hostname: r23m0204.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.5/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/pnueli-zuck.5/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4
Actions:     []
Variables:   p0 p1 p2 p3 p4
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.05 seconds (average 0.001316, setup 0.00)

Time for model construction: 0.082 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2492035

Transition matrix: 5161 nodes (3 terminal), 2492035 minterms, vars: 20r/20c/5nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep5.trew"...
Time for exporting: 1.055 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep5.tra:	Size of output file is 44098427 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep5.lab:	Size of output file is 97042 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_default/pnueli-zuck.5/model_rep5.trew:	File does not exist.
```

