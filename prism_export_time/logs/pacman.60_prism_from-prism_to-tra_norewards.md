# Log files for prism_from-prism_to-tra_norewards on model [pacman.60](../../models/pacman.60)

Parsed values: `[47.194, 49.938, 61.364, 47.678, 47.885]`



### Log file: prism_from-prism_to-tra_norewards_pacman.60_rep1.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/pacman.60/model.tra,lab:precision=17
Wallclock time: 1140.175 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:24:51 GMT+01:00 2026
Hostname: n23m0248.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/pacman.60/model.tra,lab:precision=17'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 46.78 seconds (average 0.255628, setup 0.00)

Time for model construction: 1091.573 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/pacman.60/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/pacman.60/model.lab"...
Time for exporting: 47.194 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/pacman.60/model.tra:	Size of output file is 1419324397 bytes
out/prism_from-prism_to-tra_norewards/pacman.60/model.lab:	Size of output file is 21439123 bytes
```



### Log file: prism_from-prism_to-tra_norewards_pacman.60_rep2.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/pacman.60/model_rep2.tra,lab:precision=17
Wallclock time: 1698.392 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:23:11 GMT+01:00 2026
Hostname: r23m0195.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/pacman.60/model_rep2.tra,lab:precision=17'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 61.83 seconds (average 0.337869, setup 0.00)

Time for model construction: 1646.846 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/pacman.60/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/pacman.60/model_rep2.lab"...
Time for exporting: 49.938 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/pacman.60/model_rep2.tra:	Size of output file is 1419324397 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_norewards/pacman.60/model_rep2.lab:	Size of output file is 21439123 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_norewards_pacman.60_rep3.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/pacman.60/model_rep3.tra,lab:precision=17
Wallclock time: 1698.757 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:56:51 GMT+01:00 2026
Hostname: n23m0043.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/pacman.60/model_rep3.tra,lab:precision=17'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 53.53 seconds (average 0.292514, setup 0.00)

Time for model construction: 1635.402 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/pacman.60/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/pacman.60/model_rep3.lab"...
Time for exporting: 61.364 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/pacman.60/model_rep3.tra:	Size of output file is 1419324397 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_norewards/pacman.60/model_rep3.lab:	Size of output file is 21439123 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_norewards_pacman.60_rep4.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/pacman.60/model_rep4.tra,lab:precision=17
Wallclock time: 1073.549 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:09 GMT+01:00 2026
Hostname: n23m0211.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/pacman.60/model_rep4.tra,lab:precision=17'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 45.23 seconds (average 0.247158, setup 0.00)

Time for model construction: 1024.46 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/pacman.60/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/pacman.60/model_rep4.lab"...
Time for exporting: 47.678 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/pacman.60/model_rep4.tra:	Size of output file is 1419324397 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_norewards/pacman.60/model_rep4.lab:	Size of output file is 21439123 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_norewards_pacman.60_rep5.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/pacman.60/model_rep5.tra,lab:precision=17
Wallclock time: 1270.143 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:51:16 GMT+01:00 2026
Hostname: n23m0341.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/pacman.60/model_rep5.tra,lab:precision=17'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 46.02 seconds (average 0.251475, setup 0.00)

Time for model construction: 1220.856 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/pacman.60/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/pacman.60/model_rep5.lab"...
Time for exporting: 47.885 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/pacman.60/model_rep5.tra:	Size of output file is 1419324397 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_norewards/pacman.60/model_rep5.lab:	Size of output file is 21439123 bytes
Removing output file to save space for repetition #5
```

