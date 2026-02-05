# Log files

Tool configuration: prism_from-prism_to-umb-gz_default
Benchmark: [herman.15](../../models/herman.15)
Parsed values: [419112383.0, 419112383.0, 419112383.0, 419112383.0, 419112383.0]



### Log file: prism_from-prism_to-umb-gz_default_herman.15_rep1.log

```
Command(s):
../bin/prism  models/herman.15/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/herman.15/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 6.690 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:49:27 GMT+01:00 2026
Hostname: n23m0401.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/herman.15/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/herman.15/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

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

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/herman.15/model.umb.gz"...
Time for exporting: 6.082 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/herman.15/model.umb.gz:	Size of output file is 419112383 bytes
```



### Log file: prism_from-prism_to-umb-gz_default_herman.15_rep2.log

```
Command(s):
../bin/prism  models/herman.15/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/herman.15/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 10.172 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:18:40 GMT+01:00 2026
Hostname: n23m0047.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/herman.15/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/herman.15/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

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

Time for model construction: 0.084 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908

Transition matrix: 810 nodes (9 terminal), 14348908 minterms, vars: 15r/15c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/herman.15/model.umb_rep2.gz"...
Time for exporting: 6.596 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/herman.15/model.umb_rep2.gz:	Size of output file is 419112383 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_default_herman.15_rep3.log

```
Command(s):
../bin/prism  models/herman.15/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/herman.15/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 6.205 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:25 GMT+01:00 2026
Hostname: n23m0287.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/herman.15/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/herman.15/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

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

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/herman.15/model.umb_rep3.gz"...
Time for exporting: 5.712 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/herman.15/model.umb_rep3.gz:	Size of output file is 419112383 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_default_herman.15_rep4.log

```
Command(s):
../bin/prism  models/herman.15/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/herman.15/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 6.318 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:33:33 GMT+01:00 2026
Hostname: n23m0380.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/herman.15/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/herman.15/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

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

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/herman.15/model.umb_rep4.gz"...
Time for exporting: 5.824 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/herman.15/model.umb_rep4.gz:	Size of output file is 419112383 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_default_herman.15_rep5.log

```
Command(s):
../bin/prism  models/herman.15/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/herman.15/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 7.796 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:29 GMT+01:00 2026
Hostname: n23m0003.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/herman.15/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/herman.15/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

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

Time for model construction: 0.019 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908

Transition matrix: 810 nodes (9 terminal), 14348908 minterms, vars: 15r/15c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/herman.15/model.umb_rep5.gz"...
Time for exporting: 7.04 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/herman.15/model.umb_rep5.gz:	Size of output file is 419112383 bytes
Removing output file to save space for repetition #5
```

