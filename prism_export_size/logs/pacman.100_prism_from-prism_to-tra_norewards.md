# Log files for prism_from-prism_to-tra_norewards on model [pacman.100](../../models/pacman.100)

Parsed values: `[2985463482.0, 2985463482.0, 2985463482.0, 2985463482.0, 2985463482.0]`



### Log file: prism_from-prism_to-tra_norewards_pacman.100_rep1.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/pacman.100/model.tra,lab:precision=17
Wallclock time: 1675.884 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:42:37 GMT+01:00 2026
Hostname: r23m0088.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/pacman.100/model.tra,lab:precision=17'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 91.68 seconds (average 0.302574, setup 0.00)

Time for model construction: 1588.071 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/pacman.100/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/pacman.100/model.lab"...
Time for exporting: 86.394 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/pacman.100/model.tra:	Size of output file is 2942165159 bytes
out/prism_from-prism_to-tra_norewards/pacman.100/model.lab:	Size of output file is 43298323 bytes
```



### Log file: prism_from-prism_to-tra_norewards_pacman.100_rep2.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/pacman.100/model_rep2.tra,lab:precision=17
Wallclock time: 2245.640 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:01 GMT+01:00 2026
Hostname: n23m0379.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/pacman.100/model_rep2.tra,lab:precision=17'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 94.15 seconds (average 0.310726, setup 0.00)

Time for model construction: 2155.412 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/pacman.100/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/pacman.100/model_rep2.lab"...
Time for exporting: 88.237 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/pacman.100/model_rep2.tra:	Size of output file is 2942165159 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_norewards/pacman.100/model_rep2.lab:	Size of output file is 43298323 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_norewards_pacman.100_rep3.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/pacman.100/model_rep3.tra,lab:precision=17
Wallclock time: 1146.487 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:12 GMT+01:00 2026
Hostname: r23m0076.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/pacman.100/model_rep3.tra,lab:precision=17'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 90.67 seconds (average 0.299241, setup 0.00)

Time for model construction: 1059.421 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/pacman.100/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/pacman.100/model_rep3.lab"...
Time for exporting: 85.684 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/pacman.100/model_rep3.tra:	Size of output file is 2942165159 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_norewards/pacman.100/model_rep3.lab:	Size of output file is 43298323 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_norewards_pacman.100_rep4.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/pacman.100/model_rep4.tra,lab:precision=17
Wallclock time: 3189.079 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:19:37 GMT+01:00 2026
Hostname: n23m0096.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/pacman.100/model_rep4.tra,lab:precision=17'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 123.31 seconds (average 0.406964, setup 0.00)

Time for model construction: 3079.576 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/pacman.100/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/pacman.100/model_rep4.lab"...
Time for exporting: 107.556 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/pacman.100/model_rep4.tra:	Size of output file is 2942165159 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_norewards/pacman.100/model_rep4.lab:	Size of output file is 43298323 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_norewards_pacman.100_rep5.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/pacman.100/model_rep5.tra,lab:precision=17
Wallclock time: 1297.014 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:25:43 GMT+01:00 2026
Hostname: n23m0380.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/pacman.100/model_rep5.tra,lab:precision=17'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 83.15 seconds (average 0.274422, setup 0.00)

Time for model construction: 1201.439 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/pacman.100/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/pacman.100/model_rep5.lab"...
Time for exporting: 86.036 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/pacman.100/model_rep5.tra:	Size of output file is 2942165159 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_norewards/pacman.100/model_rep5.lab:	Size of output file is 43298323 bytes
Removing output file to save space for repetition #5
```

