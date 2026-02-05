# Log files for prism_from-prism_to-tra_default on model [pacman.100](../../models/pacman.100)

Parsed values: `[85.664, 92.74, 100.083, 87.505, 88.344]`



### Log file: prism_from-prism_to-tra_default_pacman.100_rep1.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-tra_default/pacman.100/model.tra,lab,rew:precision=17
Wallclock time: 1186.882 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:44:43 GMT+01:00 2026
Hostname: n23m0275.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/pacman.100/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 87.08 seconds (average 0.287393, setup 0.00)

Time for model construction: 1099.803 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/pacman.100/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/pacman.100/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/pacman.100/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/pacman.100/model.trew"...
Time for exporting: 85.664 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/pacman.100/model.tra:	Size of output file is 2942165159 bytes
out/prism_from-prism_to-tra_default/pacman.100/model.lab:	Size of output file is 43298323 bytes
out/prism_from-prism_to-tra_default/pacman.100/model.srew:	File does not exist.
out/prism_from-prism_to-tra_default/pacman.100/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_pacman.100_rep2.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-tra_default/pacman.100/model_rep2.tra,lab,rew:precision=17
Wallclock time: 1296.486 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:13 GMT+01:00 2026
Hostname: n23m0158.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/pacman.100/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 88.62 seconds (average 0.292475, setup 0.00)

Time for model construction: 1200.163 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/pacman.100/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/pacman.100/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/pacman.100/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/pacman.100/model_rep2.trew"...
Time for exporting: 92.74 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/pacman.100/model_rep2.tra:	Size of output file is 2942165159 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/pacman.100/model_rep2.lab:	Size of output file is 43298323 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/pacman.100/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_default/pacman.100/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_pacman.100_rep3.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-tra_default/pacman.100/model_rep3.tra,lab,rew:precision=17
Wallclock time: 3219.994 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:35:05 GMT+01:00 2026
Hostname: n23m0242.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/pacman.100/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 108.90 seconds (average 0.359406, setup 0.00)

Time for model construction: 3118.134 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/pacman.100/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/pacman.100/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/pacman.100/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/pacman.100/model_rep3.trew"...
Time for exporting: 100.083 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/pacman.100/model_rep3.tra:	Size of output file is 2942165159 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/pacman.100/model_rep3.lab:	Size of output file is 43298323 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/pacman.100/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_default/pacman.100/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_pacman.100_rep4.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-tra_default/pacman.100/model_rep4.tra,lab,rew:precision=17
Wallclock time: 1221.106 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:32 GMT+01:00 2026
Hostname: n23m0171.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/pacman.100/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 82.47 seconds (average 0.272178, setup 0.00)

Time for model construction: 1132.162 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/pacman.100/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/pacman.100/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/pacman.100/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/pacman.100/model_rep4.trew"...
Time for exporting: 87.505 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/pacman.100/model_rep4.tra:	Size of output file is 2942165159 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/pacman.100/model_rep4.lab:	Size of output file is 43298323 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/pacman.100/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_default/pacman.100/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_pacman.100_rep5.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-tra_default/pacman.100/model_rep5.tra,lab,rew:precision=17
Wallclock time: 1366.992 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:52 GMT+01:00 2026
Hostname: r23m0206.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/pacman.100/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 87.67 seconds (average 0.289340, setup 0.00)

Time for model construction: 1277.144 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/pacman.100/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/pacman.100/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/pacman.100/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/pacman.100/model_rep5.trew"...
Time for exporting: 88.344 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/pacman.100/model_rep5.tra:	Size of output file is 2942165159 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/pacman.100/model_rep5.lab:	Size of output file is 43298323 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/pacman.100/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_default/pacman.100/model_rep5.trew:	File does not exist.
```

