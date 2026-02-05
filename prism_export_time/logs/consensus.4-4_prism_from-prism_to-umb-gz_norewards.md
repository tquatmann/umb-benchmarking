# Log files

Tool configuration: prism_from-prism_to-umb-gz_norewards
Benchmark: [consensus.4-4](../../models/consensus.4-4)
Parsed values: [0.114, 0.084, 0.088, 0.108, 0.095]



### Log file: prism_from-prism_to-umb-gz_norewards_consensus.4-4_rep1.log

```
Command(s):
../bin/prism  models/consensus.4-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/consensus.4-4/model.umb.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 0.963 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:23:48 GMT+01:00 2026
Hostname: n23m0113.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.4-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/consensus.4-4/model.umb.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/consensus.4-4/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4
Labels:      "finished" "agree"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.02 seconds (average 0.000103, setup 0.00)

Time for model construction: 0.058 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352

Transition matrix: 2336 nodes (3 terminal), 144352 minterms, vars: 18r/18c/4nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/consensus.4-4/model.umb.gz"...
Time for exporting: 0.114 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/consensus.4-4/model.umb.gz:	Size of output file is 2350318 bytes
```



### Log file: prism_from-prism_to-umb-gz_norewards_consensus.4-4_rep2.log

```
Command(s):
../bin/prism  models/consensus.4-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/consensus.4-4/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 0.770 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:03:25 GMT+01:00 2026
Hostname: n23m0041.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.4-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/consensus.4-4/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/consensus.4-4/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4
Labels:      "finished" "agree"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.02 seconds (average 0.000103, setup 0.00)

Time for model construction: 0.051 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352

Transition matrix: 2336 nodes (3 terminal), 144352 minterms, vars: 18r/18c/4nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/consensus.4-4/model.umb_rep2.gz"...
Time for exporting: 0.084 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/consensus.4-4/model.umb_rep2.gz:	Size of output file is 2350318 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_norewards_consensus.4-4_rep3.log

```
Command(s):
../bin/prism  models/consensus.4-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/consensus.4-4/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 1.039 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:34 GMT+01:00 2026
Hostname: n23m0281.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.4-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/consensus.4-4/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/consensus.4-4/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4
Labels:      "finished" "agree"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.03 seconds (average 0.000154, setup 0.00)

Time for model construction: 0.069 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352

Transition matrix: 2336 nodes (3 terminal), 144352 minterms, vars: 18r/18c/4nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/consensus.4-4/model.umb_rep3.gz"...
Time for exporting: 0.088 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/consensus.4-4/model.umb_rep3.gz:	Size of output file is 2350318 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_norewards_consensus.4-4_rep4.log

```
Command(s):
../bin/prism  models/consensus.4-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/consensus.4-4/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 3.166 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:12 GMT+01:00 2026
Hostname: n23m0230.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.4-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/consensus.4-4/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/consensus.4-4/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4
Labels:      "finished" "agree"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.03 seconds (average 0.000154, setup 0.00)

Time for model construction: 0.084 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352

Transition matrix: 2336 nodes (3 terminal), 144352 minterms, vars: 18r/18c/4nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/consensus.4-4/model.umb_rep4.gz"...
Time for exporting: 0.108 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/consensus.4-4/model.umb_rep4.gz:	Size of output file is 2350318 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_norewards_consensus.4-4_rep5.log

```
Command(s):
../bin/prism  models/consensus.4-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/consensus.4-4/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 0.754 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:24:25 GMT+01:00 2026
Hostname: n23m0331.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.4-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/consensus.4-4/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/consensus.4-4/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4
Labels:      "finished" "agree"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.02 seconds (average 0.000103, setup 0.00)

Time for model construction: 0.048 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352

Transition matrix: 2336 nodes (3 terminal), 144352 minterms, vars: 18r/18c/4nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/consensus.4-4/model.umb_rep5.gz"...
Time for exporting: 0.095 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/consensus.4-4/model.umb_rep5.gz:	Size of output file is 2350318 bytes
Removing output file to save space for repetition #5
```

