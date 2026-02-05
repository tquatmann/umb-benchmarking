# Log files

Tool configuration: prism_from-prism_to-umb_default
Benchmark: [consensus.4-4](../../models/consensus.4-4)
Parsed values: [4071936.0, 4071936.0, 4071936.0, 4071936.0, 4071936.0]



### Log file: prism_from-prism_to-umb_default_consensus.4-4_rep1.log

```
Command(s):
../bin/prism  models/consensus.4-4/model.prism -exportmodel out/prism_from-prism_to-umb_default/consensus.4-4/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 0.881 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:38:21 GMT+01:00 2026
Hostname: n23m0241.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.4-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/consensus.4-4/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/consensus.4-4/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4
Labels:      "finished" "agree"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.02 seconds (average 0.000103, setup 0.00)

Time for model construction: 0.036 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352

Transition matrix: 2336 nodes (3 terminal), 144352 minterms, vars: 18r/18c/4nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/consensus.4-4/model.umb"...
Model export size: 3976 Kb
Time for exporting: 0.386 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/consensus.4-4/model.umb:	Size of output file is 4071936 bytes
```



### Log file: prism_from-prism_to-umb_default_consensus.4-4_rep2.log

```
Command(s):
../bin/prism  models/consensus.4-4/model.prism -exportmodel out/prism_from-prism_to-umb_default/consensus.4-4/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 1.104 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:53:48 GMT+01:00 2026
Hostname: n23m0247.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.4-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/consensus.4-4/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/consensus.4-4/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4
Labels:      "finished" "agree"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.02 seconds (average 0.000103, setup 0.00)

Time for model construction: 0.036 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352

Transition matrix: 2336 nodes (3 terminal), 144352 minterms, vars: 18r/18c/4nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/consensus.4-4/model_rep2.umb"...
Model export size: 3976 Kb
Time for exporting: 0.392 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/consensus.4-4/model_rep2.umb:	Size of output file is 4071936 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_default_consensus.4-4_rep3.log

```
Command(s):
../bin/prism  models/consensus.4-4/model.prism -exportmodel out/prism_from-prism_to-umb_default/consensus.4-4/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 1.259 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:26:59 GMT+01:00 2026
Hostname: n23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.4-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/consensus.4-4/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/consensus.4-4/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4
Labels:      "finished" "agree"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.02 seconds (average 0.000103, setup 0.00)

Time for model construction: 0.05 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352

Transition matrix: 2336 nodes (3 terminal), 144352 minterms, vars: 18r/18c/4nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/consensus.4-4/model_rep3.umb"...
Model export size: 3976 Kb
Time for exporting: 0.57 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/consensus.4-4/model_rep3.umb:	Size of output file is 4071936 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_default_consensus.4-4_rep4.log

```
Command(s):
../bin/prism  models/consensus.4-4/model.prism -exportmodel out/prism_from-prism_to-umb_default/consensus.4-4/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 1.303 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:26:01 GMT+01:00 2026
Hostname: n23m0019.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.4-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/consensus.4-4/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/consensus.4-4/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4
Labels:      "finished" "agree"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.02 seconds (average 0.000103, setup 0.00)

Time for model construction: 0.063 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352

Transition matrix: 2336 nodes (3 terminal), 144352 minterms, vars: 18r/18c/4nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/consensus.4-4/model_rep4.umb"...
Model export size: 3976 Kb
Time for exporting: 0.613 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/consensus.4-4/model_rep4.umb:	Size of output file is 4071936 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_default_consensus.4-4_rep5.log

```
Command(s):
../bin/prism  models/consensus.4-4/model.prism -exportmodel out/prism_from-prism_to-umb_default/consensus.4-4/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 0.951 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:31:51 GMT+01:00 2026
Hostname: n23m0044.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.4-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/consensus.4-4/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/consensus.4-4/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4
Labels:      "finished" "agree"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.02 seconds (average 0.000103, setup 0.00)

Time for model construction: 0.036 seconds.

Type:        MDP
States:      43136 (1 initial)
Transitions: 144352

Transition matrix: 2336 nodes (3 terminal), 144352 minterms, vars: 18r/18c/4nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/consensus.4-4/model_rep5.umb"...
Model export size: 3976 Kb
Time for exporting: 0.457 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/consensus.4-4/model_rep5.umb:	Size of output file is 4071936 bytes
Removing output file to save space for repetition #5
```

