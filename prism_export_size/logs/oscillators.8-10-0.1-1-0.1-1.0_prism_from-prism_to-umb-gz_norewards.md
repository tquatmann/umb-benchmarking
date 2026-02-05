# Log files

Tool configuration: prism_from-prism_to-umb-gz_norewards
Benchmark: [oscillators.8-10-0.1-1-0.1-1.0](../../models/oscillators.8-10-0.1-1-0.1-1.0)
Parsed values: [1928653.0, 1928653.0, 1928653.0, 1928653.0, 1928653.0]



### Log file: prism_from-prism_to-umb-gz_norewards_oscillators.8-10-0.1-1-0.1-1.0_rep1.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 25.675 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:48:24 GMT+01:00 2026
Hostname: n23m0383.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2 iterations in 0.06 seconds (average 0.030000, setup 0.00)

Time for model construction: 22.816 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb.gz"...
Time for exporting: 0.085 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb.gz:	Size of output file is 1928653 bytes
```



### Log file: prism_from-prism_to-umb-gz_norewards_oscillators.8-10-0.1-1-0.1-1.0_rep2.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 95.912 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:45:18 GMT+01:00 2026
Hostname: r23m0217.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2 iterations in 0.20 seconds (average 0.100000, setup 0.00)

Time for model construction: 83.088 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep2.gz"...
Time for exporting: 0.404 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep2.gz:	Size of output file is 1928653 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_norewards_oscillators.8-10-0.1-1-0.1-1.0_rep3.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 24.954 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:12:28 GMT+01:00 2026
Hostname: n23m0043.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2 iterations in 0.06 seconds (average 0.030000, setup 0.00)

Time for model construction: 22.146 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep3.gz"...
Time for exporting: 0.087 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep3.gz:	Size of output file is 1928653 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_norewards_oscillators.8-10-0.1-1-0.1-1.0_rep4.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 23.605 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:52:47 GMT+01:00 2026
Hostname: n23m0307.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2 iterations in 0.05 seconds (average 0.025000, setup 0.00)

Time for model construction: 20.741 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep4.gz"...
Time for exporting: 0.088 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep4.gz:	Size of output file is 1928653 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_norewards_oscillators.8-10-0.1-1-0.1-1.0_rep5.log

```
Command(s):
../bin/prism  models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 22.992 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:37 GMT+01:00 2026
Hostname: n23m0287.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2 iterations in 0.06 seconds (average 0.030000, setup 0.00)

Time for model construction: 20.167 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Transition matrix: 80638 nodes (438 terminal), 76623 minterms, vars: 40r/40c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep5.gz"...
Time for exporting: 0.086 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep5.gz:	Size of output file is 1928653 bytes
Removing output file to save space for repetition #5
```

