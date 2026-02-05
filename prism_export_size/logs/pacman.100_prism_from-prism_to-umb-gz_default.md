# Log files

Tool configuration: prism_from-prism_to-umb-gz_default
Benchmark: [pacman.100](../../models/pacman.100)
Parsed values: [2803929191.0, 2803929191.0, 2803929191.0, 2803929191.0, 2803929191.0]



### Log file: prism_from-prism_to-umb-gz_default_pacman.100_rep1.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/pacman.100/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 1440.647 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:44:11 GMT+01:00 2026
Hostname: r23m0140.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/pacman.100/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 89.69 seconds (average 0.296007, setup 0.00)

Time for model construction: 1359.302 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/pacman.100/model.umb.gz"...
Time for exporting: 79.757 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/pacman.100/model.umb.gz:	Size of output file is 2803929191 bytes
```



### Log file: prism_from-prism_to-umb-gz_default_pacman.100_rep2.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/pacman.100/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 2854.850 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:55 GMT+01:00 2026
Hostname: n23m0165.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/pacman.100/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 115.80 seconds (average 0.382178, setup 0.00)

Time for model construction: 2756.958 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/pacman.100/model.umb_rep2.gz"...
Time for exporting: 96.048 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/pacman.100/model.umb_rep2.gz:	Size of output file is 2803929191 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_default_pacman.100_rep3.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/pacman.100/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 1120.266 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:06 GMT+01:00 2026
Hostname: n23m0380.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/pacman.100/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 81.63 seconds (average 0.269406, setup 0.00)

Time for model construction: 1040.392 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/pacman.100/model.umb_rep3.gz"...
Time for exporting: 78.361 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/pacman.100/model.umb_rep3.gz:	Size of output file is 2803929191 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_default_pacman.100_rep4.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/pacman.100/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 2854.182 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:12 GMT+01:00 2026
Hostname: n23m0082.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/pacman.100/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 103.21 seconds (average 0.340627, setup 0.00)

Time for model construction: 2754.173 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/pacman.100/model.umb_rep4.gz"...
Time for exporting: 97.599 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/pacman.100/model.umb_rep4.gz:	Size of output file is 2803929191 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_default_pacman.100_rep5.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/pacman.100/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 1619.950 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:27 GMT+01:00 2026
Hostname: r23m0204.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/pacman.100/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 148.87 seconds (average 0.491320, setup 0.00)

Time for model construction: 1539.524 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/pacman.100/model.umb_rep5.gz"...
Time for exporting: 78.663 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/pacman.100/model.umb_rep5.gz:	Size of output file is 2803929191 bytes
Removing output file to save space for repetition #5
```

