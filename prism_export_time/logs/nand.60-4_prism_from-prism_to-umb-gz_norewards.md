# Log files

Tool configuration: prism_from-prism_to-umb-gz_norewards
Benchmark: [nand.60-4](../../models/nand.60-4)
Parsed values: [15.904, 13.505, 13.394, 15.087, 13.57]



### Log file: prism_from-prism_to-umb-gz_norewards_nand.60-4_rep1.log

```
Command(s):
../bin/prism  models/nand.60-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/nand.60-4/model.umb.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 25.169 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:30:24 GMT+01:00 2026
Hostname: r23m0129.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.60-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/nand.60-4/model.umb.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2162 iterations in 8.40 seconds (average 0.003885, setup 0.00)

Time for model construction: 8.675 seconds.

Type:        DTMC
States:      18826082 (1 initial)
Transitions: 29772212

Transition matrix: 97452 nodes (1103 terminal), 29772212 minterms, vars: 33r/33c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/nand.60-4/model.umb.gz"...
Time for exporting: 15.904 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/nand.60-4/model.umb.gz:	Size of output file is 706998144 bytes
```



### Log file: prism_from-prism_to-umb-gz_norewards_nand.60-4_rep2.log

```
Command(s):
../bin/prism  models/nand.60-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/nand.60-4/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 21.850 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:26 GMT+01:00 2026
Hostname: n23m0308.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.60-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/nand.60-4/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2162 iterations in 7.53 seconds (average 0.003483, setup 0.00)

Time for model construction: 7.78 seconds.

Type:        DTMC
States:      18826082 (1 initial)
Transitions: 29772212

Transition matrix: 97452 nodes (1103 terminal), 29772212 minterms, vars: 33r/33c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/nand.60-4/model.umb_rep2.gz"...
Time for exporting: 13.505 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/nand.60-4/model.umb_rep2.gz:	Size of output file is 706998144 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_norewards_nand.60-4_rep3.log

```
Command(s):
../bin/prism  models/nand.60-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/nand.60-4/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 21.679 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:51:15 GMT+01:00 2026
Hostname: n23m0313.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.60-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/nand.60-4/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2162 iterations in 7.53 seconds (average 0.003483, setup 0.00)

Time for model construction: 7.77 seconds.

Type:        DTMC
States:      18826082 (1 initial)
Transitions: 29772212

Transition matrix: 97452 nodes (1103 terminal), 29772212 minterms, vars: 33r/33c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/nand.60-4/model.umb_rep3.gz"...
Time for exporting: 13.394 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/nand.60-4/model.umb_rep3.gz:	Size of output file is 706998144 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_norewards_nand.60-4_rep4.log

```
Command(s):
../bin/prism  models/nand.60-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/nand.60-4/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 24.026 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:32:32 GMT+01:00 2026
Hostname: n23m0252.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.60-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/nand.60-4/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2162 iterations in 8.03 seconds (average 0.003714, setup 0.00)

Time for model construction: 8.282 seconds.

Type:        DTMC
States:      18826082 (1 initial)
Transitions: 29772212

Transition matrix: 97452 nodes (1103 terminal), 29772212 minterms, vars: 33r/33c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/nand.60-4/model.umb_rep4.gz"...
Time for exporting: 15.087 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/nand.60-4/model.umb_rep4.gz:	Size of output file is 706998144 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_norewards_nand.60-4_rep5.log

```
Command(s):
../bin/prism  models/nand.60-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/nand.60-4/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 23.194 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:22:10 GMT+01:00 2026
Hostname: r23m0195.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.60-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/nand.60-4/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2162 iterations in 8.67 seconds (average 0.004010, setup 0.00)

Time for model construction: 8.962 seconds.

Type:        DTMC
States:      18826082 (1 initial)
Transitions: 29772212

Transition matrix: 97452 nodes (1103 terminal), 29772212 minterms, vars: 33r/33c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/nand.60-4/model.umb_rep5.gz"...
Time for exporting: 13.57 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/nand.60-4/model.umb_rep5.gz:	Size of output file is 706998144 bytes
Removing output file to save space for repetition #5
```

