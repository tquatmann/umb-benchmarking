# Log files

Tool configuration: prism_from-prism_to-umb-gz_default
Benchmark: [cluster.128-2000-20](../../models/cluster.128-2000-20)
Parsed values: [1.365, 1.521, 1.657, 1.371, 1.347]



### Log file: prism_from-prism_to-umb-gz_default_cluster.128-2000-20_rep1.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/cluster.128-2000-20/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 1.947 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:43:10 GMT+01:00 2026
Hostname: r23m0138.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/cluster.128-2000-20/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.06 seconds (average 0.000230, setup 0.00)

Time for model construction: 0.095 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/cluster.128-2000-20/model.umb.gz"...
Time for exporting: 1.365 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/cluster.128-2000-20/model.umb.gz:	Size of output file is 66915127 bytes
```



### Log file: prism_from-prism_to-umb-gz_default_cluster.128-2000-20_rep2.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/cluster.128-2000-20/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 2.271 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:08:58 GMT+01:00 2026
Hostname: n23m0058.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/cluster.128-2000-20/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.07 seconds (average 0.000268, setup 0.00)

Time for model construction: 0.115 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/cluster.128-2000-20/model.umb_rep2.gz"...
Time for exporting: 1.521 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/cluster.128-2000-20/model.umb_rep2.gz:	Size of output file is 66915127 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_default_cluster.128-2000-20_rep3.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/cluster.128-2000-20/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 3.277 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:27:47 GMT+01:00 2026
Hostname: r23m0212.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/cluster.128-2000-20/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.08 seconds (average 0.000307, setup 0.00)

Time for model construction: 0.183 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/cluster.128-2000-20/model.umb_rep3.gz"...
Time for exporting: 1.657 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/cluster.128-2000-20/model.umb_rep3.gz:	Size of output file is 66915127 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_default_cluster.128-2000-20_rep4.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/cluster.128-2000-20/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 1.968 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:14 GMT+01:00 2026
Hostname: n23m0171.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/cluster.128-2000-20/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.06 seconds (average 0.000230, setup 0.00)

Time for model construction: 0.096 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/cluster.128-2000-20/model.umb_rep4.gz"...
Time for exporting: 1.371 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/cluster.128-2000-20/model.umb_rep4.gz:	Size of output file is 66915127 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_default_cluster.128-2000-20_rep5.log

```
Command(s):
../bin/prism  models/cluster.128-2000-20/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/cluster.128-2000-20/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 1.946 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:26:01 GMT+01:00 2026
Hostname: n23m0202.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/cluster.128-2000-20/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/cluster.128-2000-20/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/cluster.128-2000-20/model.prism"...

Type:        CTMC
Modules:     Left Right Repairman Line ToLeft ToRight
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   left_n left right_n right r line line_n toleft toleft_n toright toright_n
Labels:      "minimum"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 261 iterations in 0.07 seconds (average 0.000268, setup 0.00)

Time for model construction: 0.098 seconds.

Type:        CTMC
States:      597012 (1 initial)
Transitions: 2908192

Rate matrix: 17481 nodes (134 terminal), 2908192 minterms, vars: 25r/25c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/cluster.128-2000-20/model.umb_rep5.gz"...
Time for exporting: 1.347 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/cluster.128-2000-20/model.umb_rep5.gz:	Size of output file is 66915127 bytes
Removing output file to save space for repetition #5
```

