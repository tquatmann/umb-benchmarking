# Log files

Tool configuration: prism_from-prism_to-umb-gz_default
Benchmark: [nand.40-4](../../models/nand.40-4)
Parsed values: [2.893, 2.897, 3.178, 3.509, 3.016]



### Log file: prism_from-prism_to-umb-gz_default_nand.40-4_rep1.log

```
Command(s):
../bin/prism  models/nand.40-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/nand.40-4/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 6.127 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:43:08 GMT+01:00 2026
Hostname: r23m0061.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.40-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/nand.40-4/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/nand.40-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1442 iterations in 2.52 seconds (average 0.001748, setup 0.00)

Time for model construction: 2.622 seconds.

Type:        DTMC
States:      3999522 (1 initial)
Transitions: 6288542

Transition matrix: 49073 nodes (493 terminal), 6288542 minterms, vars: 33r/33c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/nand.40-4/model.umb.gz"...
Time for exporting: 2.893 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/nand.40-4/model.umb.gz:	Size of output file is 138940537 bytes
```



### Log file: prism_from-prism_to-umb-gz_default_nand.40-4_rep2.log

```
Command(s):
../bin/prism  models/nand.40-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/nand.40-4/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 6.461 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:21 GMT+01:00 2026
Hostname: n23m0191.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.40-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/nand.40-4/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/nand.40-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1442 iterations in 2.54 seconds (average 0.001761, setup 0.00)

Time for model construction: 2.709 seconds.

Type:        DTMC
States:      3999522 (1 initial)
Transitions: 6288542

Transition matrix: 49073 nodes (493 terminal), 6288542 minterms, vars: 33r/33c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/nand.40-4/model.umb_rep2.gz"...
Time for exporting: 2.897 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/nand.40-4/model.umb_rep2.gz:	Size of output file is 138940537 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_default_nand.40-4_rep3.log

```
Command(s):
../bin/prism  models/nand.40-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/nand.40-4/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 6.560 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:56:51 GMT+01:00 2026
Hostname: n23m0109.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.40-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/nand.40-4/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/nand.40-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1442 iterations in 2.72 seconds (average 0.001886, setup 0.00)

Time for model construction: 2.824 seconds.

Type:        DTMC
States:      3999522 (1 initial)
Transitions: 6288542

Transition matrix: 49073 nodes (493 terminal), 6288542 minterms, vars: 33r/33c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/nand.40-4/model.umb_rep3.gz"...
Time for exporting: 3.178 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/nand.40-4/model.umb_rep3.gz:	Size of output file is 138940537 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_default_nand.40-4_rep4.log

```
Command(s):
../bin/prism  models/nand.40-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/nand.40-4/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 7.228 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:27 GMT+01:00 2026
Hostname: r23m0069.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.40-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/nand.40-4/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/nand.40-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1442 iterations in 3.01 seconds (average 0.002087, setup 0.00)

Time for model construction: 3.121 seconds.

Type:        DTMC
States:      3999522 (1 initial)
Transitions: 6288542

Transition matrix: 49073 nodes (493 terminal), 6288542 minterms, vars: 33r/33c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/nand.40-4/model.umb_rep4.gz"...
Time for exporting: 3.509 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/nand.40-4/model.umb_rep4.gz:	Size of output file is 138940537 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_default_nand.40-4_rep5.log

```
Command(s):
../bin/prism  models/nand.40-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/nand.40-4/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 6.285 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:02:25 GMT+01:00 2026
Hostname: n23m0112.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.40-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/nand.40-4/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/nand.40-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1442 iterations in 2.60 seconds (average 0.001803, setup 0.00)

Time for model construction: 2.705 seconds.

Type:        DTMC
States:      3999522 (1 initial)
Transitions: 6288542

Transition matrix: 49073 nodes (493 terminal), 6288542 minterms, vars: 33r/33c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/nand.40-4/model.umb_rep5.gz"...
Time for exporting: 3.016 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/nand.40-4/model.umb_rep5.gz:	Size of output file is 138940537 bytes
Removing output file to save space for repetition #5
```

