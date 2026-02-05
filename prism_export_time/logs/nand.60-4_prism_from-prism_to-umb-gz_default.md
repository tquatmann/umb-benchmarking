# Log files

Tool configuration: prism_from-prism_to-umb-gz_default
Benchmark: [nand.60-4](../../models/nand.60-4)
Parsed values: [13.492, 13.395, 15.643, 13.565, 13.734]



### Log file: prism_from-prism_to-umb-gz_default_nand.60-4_rep1.log

```
Command(s):
../bin/prism  models/nand.60-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/nand.60-4/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 22.178 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:45:15 GMT+01:00 2026
Hostname: r23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.60-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/nand.60-4/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2162 iterations in 7.76 seconds (average 0.003589, setup 0.00)

Time for model construction: 8.048 seconds.

Type:        DTMC
States:      18826082 (1 initial)
Transitions: 29772212

Transition matrix: 97452 nodes (1103 terminal), 29772212 minterms, vars: 33r/33c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/nand.60-4/model.umb.gz"...
Time for exporting: 13.492 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/nand.60-4/model.umb.gz:	Size of output file is 706998144 bytes
```



### Log file: prism_from-prism_to-umb-gz_default_nand.60-4_rep2.log

```
Command(s):
../bin/prism  models/nand.60-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/nand.60-4/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 21.401 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:08 GMT+01:00 2026
Hostname: n23m0351.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.60-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/nand.60-4/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2162 iterations in 7.29 seconds (average 0.003372, setup 0.00)

Time for model construction: 7.503 seconds.

Type:        DTMC
States:      18826082 (1 initial)
Transitions: 29772212

Transition matrix: 97452 nodes (1103 terminal), 29772212 minterms, vars: 33r/33c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/nand.60-4/model.umb_rep2.gz"...
Time for exporting: 13.395 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/nand.60-4/model.umb_rep2.gz:	Size of output file is 706998144 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_default_nand.60-4_rep3.log

```
Command(s):
../bin/prism  models/nand.60-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/nand.60-4/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 25.671 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:46:12 GMT+01:00 2026
Hostname: r23m0195.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.60-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/nand.60-4/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2162 iterations in 9.01 seconds (average 0.004167, setup 0.00)

Time for model construction: 9.328 seconds.

Type:        DTMC
States:      18826082 (1 initial)
Transitions: 29772212

Transition matrix: 97452 nodes (1103 terminal), 29772212 minterms, vars: 33r/33c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/nand.60-4/model.umb_rep3.gz"...
Time for exporting: 15.643 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/nand.60-4/model.umb_rep3.gz:	Size of output file is 706998144 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_default_nand.60-4_rep4.log

```
Command(s):
../bin/prism  models/nand.60-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/nand.60-4/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 21.779 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:56 GMT+01:00 2026
Hostname: n23m0197.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.60-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/nand.60-4/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2162 iterations in 7.47 seconds (average 0.003455, setup 0.00)

Time for model construction: 7.7 seconds.

Type:        DTMC
States:      18826082 (1 initial)
Transitions: 29772212

Transition matrix: 97452 nodes (1103 terminal), 29772212 minterms, vars: 33r/33c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/nand.60-4/model.umb_rep4.gz"...
Time for exporting: 13.565 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/nand.60-4/model.umb_rep4.gz:	Size of output file is 706998144 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_default_nand.60-4_rep5.log

```
Command(s):
../bin/prism  models/nand.60-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/nand.60-4/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 21.980 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:24:43 GMT+01:00 2026
Hostname: n23m0249.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.60-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/nand.60-4/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2162 iterations in 7.45 seconds (average 0.003446, setup 0.00)

Time for model construction: 7.691 seconds.

Type:        DTMC
States:      18826082 (1 initial)
Transitions: 29772212

Transition matrix: 97452 nodes (1103 terminal), 29772212 minterms, vars: 33r/33c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/nand.60-4/model.umb_rep5.gz"...
Time for exporting: 13.734 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/nand.60-4/model.umb_rep5.gz:	Size of output file is 706998144 bytes
Removing output file to save space for repetition #5
```

