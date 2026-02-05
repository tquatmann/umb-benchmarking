# Log files

Tool configuration: prism_from-prism_to-umb-gz_default
Benchmark: [pacman.60](../../models/pacman.60)
Parsed values: [40.936, 49.36, 53.732, 43.679, 45.018]



### Log file: prism_from-prism_to-umb-gz_default_pacman.60_rep1.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/pacman.60/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 1176.484 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:42:37 GMT+01:00 2026
Hostname: r23m0047.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/pacman.60/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 46.69 seconds (average 0.255137, setup 0.00)

Time for model construction: 1134.036 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/pacman.60/model.umb.gz"...
Time for exporting: 40.936 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/pacman.60/model.umb.gz:	Size of output file is 1352241669 bytes
```



### Log file: prism_from-prism_to-umb-gz_default_pacman.60_rep2.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/pacman.60/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 2409.328 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:52 GMT+01:00 2026
Hostname: r23m0071.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/pacman.60/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 55.46 seconds (average 0.303060, setup 0.00)

Time for model construction: 2357.983 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/pacman.60/model.umb_rep2.gz"...
Time for exporting: 49.36 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/pacman.60/model.umb_rep2.gz:	Size of output file is 1352241669 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_default_pacman.60_rep3.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/pacman.60/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 2305.868 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:55 GMT+01:00 2026
Hostname: n23m0003.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/pacman.60/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 58.35 seconds (average 0.318852, setup 0.00)

Time for model construction: 2249.876 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/pacman.60/model.umb_rep3.gz"...
Time for exporting: 53.732 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/pacman.60/model.umb_rep3.gz:	Size of output file is 1352241669 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_default_pacman.60_rep4.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/pacman.60/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 1186.047 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:57 GMT+01:00 2026
Hostname: n23m0362.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/pacman.60/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 48.99 seconds (average 0.267705, setup 0.00)

Time for model construction: 1140.741 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/pacman.60/model.umb_rep4.gz"...
Time for exporting: 43.679 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/pacman.60/model.umb_rep4.gz:	Size of output file is 1352241669 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_default_pacman.60_rep5.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/pacman.60/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 2700.093 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:31:51 GMT+01:00 2026
Hostname: n23m0167.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/pacman.60/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 59.90 seconds (average 0.327322, setup 0.00)

Time for model construction: 2653.323 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/pacman.60/model.umb_rep5.gz"...
Time for exporting: 45.018 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/pacman.60/model.umb_rep5.gz:	Size of output file is 1352241669 bytes
Removing output file to save space for repetition #5
```

