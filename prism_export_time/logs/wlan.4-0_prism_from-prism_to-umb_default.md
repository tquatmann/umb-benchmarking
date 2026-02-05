# Log files for prism_from-prism_to-umb_default on model [wlan.4-0](../../models/wlan.4-0)

Parsed values: `[2.075, 2.225, 2.487, 2.151, 2.259]`



### Log file: prism_from-prism_to-umb_default_wlan.4-0_rep1.log

```
Command(s):
../bin/prism  models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-umb_default/wlan.4-0/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 2.718 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:40:28 GMT+01:00 2026
Hostname: r23m0077.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/wlan.4-0/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 145 iterations in 0.13 seconds (average 0.000897, setup 0.00)

Time for model construction: 0.175 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252

Transition matrix: 14365 nodes (6 terminal), 762252 minterms, vars: 43r/43c/7nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/wlan.4-0/model.umb"...
Model export size: 19859 Kb
Time for exporting: 2.075 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/wlan.4-0/model.umb:	Size of output file is 20335616 bytes
```



### Log file: prism_from-prism_to-umb_default_wlan.4-0_rep2.log

```
Command(s):
../bin/prism  models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-umb_default/wlan.4-0/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 2.947 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:23:52 GMT+01:00 2026
Hostname: n23m0313.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/wlan.4-0/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 145 iterations in 0.13 seconds (average 0.000897, setup 0.00)

Time for model construction: 0.179 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252

Transition matrix: 14365 nodes (6 terminal), 762252 minterms, vars: 43r/43c/7nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/wlan.4-0/model_rep2.umb"...
Model export size: 19859 Kb
Time for exporting: 2.225 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/wlan.4-0/model_rep2.umb:	Size of output file is 20335616 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_default_wlan.4-0_rep3.log

```
Command(s):
../bin/prism  models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-umb_default/wlan.4-0/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 3.729 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:17:04 GMT+01:00 2026
Hostname: n23m0307.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/wlan.4-0/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 145 iterations in 0.16 seconds (average 0.001103, setup 0.00)

Time for model construction: 0.238 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252

Transition matrix: 14365 nodes (6 terminal), 762252 minterms, vars: 43r/43c/7nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/wlan.4-0/model_rep3.umb"...
Model export size: 19859 Kb
Time for exporting: 2.487 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/wlan.4-0/model_rep3.umb:	Size of output file is 20335616 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_default_wlan.4-0_rep4.log

```
Command(s):
../bin/prism  models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-umb_default/wlan.4-0/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 2.845 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:51 GMT+01:00 2026
Hostname: n23m0111.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/wlan.4-0/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 145 iterations in 0.15 seconds (average 0.001034, setup 0.00)

Time for model construction: 0.184 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252

Transition matrix: 14365 nodes (6 terminal), 762252 minterms, vars: 43r/43c/7nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/wlan.4-0/model_rep4.umb"...
Model export size: 19859 Kb
Time for exporting: 2.151 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/wlan.4-0/model_rep4.umb:	Size of output file is 20335616 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_default_wlan.4-0_rep5.log

```
Command(s):
../bin/prism  models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-umb_default/wlan.4-0/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 3.336 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:16 GMT+01:00 2026
Hostname: n23m0287.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/wlan.4-0/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 145 iterations in 0.14 seconds (average 0.000966, setup 0.00)

Time for model construction: 0.205 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252

Transition matrix: 14365 nodes (6 terminal), 762252 minterms, vars: 43r/43c/7nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/wlan.4-0/model_rep5.umb"...
Model export size: 19859 Kb
Time for exporting: 2.259 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/wlan.4-0/model_rep5.umb:	Size of output file is 20335616 bytes
Removing output file to save space for repetition #5
```

