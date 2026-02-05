# Log files for prism_from-prism_to-umb-gz_default on model [wlan.4-0](../../models/wlan.4-0)

Parsed values: `[15199275.0, 15199275.0, 15199275.0, 15199275.0, 15199275.0]`



### Log file: prism_from-prism_to-umb-gz_default_wlan.4-0_rep1.log

```
Command(s):
../bin/prism  models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/wlan.4-0/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 1.400 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:23:48 GMT+01:00 2026
Hostname: n23m0110.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/wlan.4-0/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 145 iterations in 0.18 seconds (average 0.001241, setup 0.00)

Time for model construction: 0.217 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252

Transition matrix: 14365 nodes (6 terminal), 762252 minterms, vars: 43r/43c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/wlan.4-0/model.umb.gz"...
Time for exporting: 0.606 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/wlan.4-0/model.umb.gz:	Size of output file is 15199275 bytes
```



### Log file: prism_from-prism_to-umb-gz_default_wlan.4-0_rep2.log

```
Command(s):
../bin/prism  models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/wlan.4-0/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 1.688 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:40 GMT+01:00 2026
Hostname: n23m0364.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/wlan.4-0/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 145 iterations in 0.22 seconds (average 0.001517, setup 0.00)

Time for model construction: 0.275 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252

Transition matrix: 14365 nodes (6 terminal), 762252 minterms, vars: 43r/43c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/wlan.4-0/model.umb_rep2.gz"...
Time for exporting: 0.717 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/wlan.4-0/model.umb_rep2.gz:	Size of output file is 15199275 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_default_wlan.4-0_rep3.log

```
Command(s):
../bin/prism  models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/wlan.4-0/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 1.834 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:25 GMT+01:00 2026
Hostname: n23m0364.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/wlan.4-0/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 145 iterations in 0.21 seconds (average 0.001448, setup 0.00)

Time for model construction: 0.27 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252

Transition matrix: 14365 nodes (6 terminal), 762252 minterms, vars: 43r/43c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/wlan.4-0/model.umb_rep3.gz"...
Time for exporting: 0.809 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/wlan.4-0/model.umb_rep3.gz:	Size of output file is 15199275 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_default_wlan.4-0_rep4.log

```
Command(s):
../bin/prism  models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/wlan.4-0/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 1.374 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:30:01 GMT+01:00 2026
Hostname: n23m0055.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/wlan.4-0/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 145 iterations in 0.15 seconds (average 0.001034, setup 0.00)

Time for model construction: 0.195 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252

Transition matrix: 14365 nodes (6 terminal), 762252 minterms, vars: 43r/43c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/wlan.4-0/model.umb_rep4.gz"...
Time for exporting: 0.627 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/wlan.4-0/model.umb_rep4.gz:	Size of output file is 15199275 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_default_wlan.4-0_rep5.log

```
Command(s):
../bin/prism  models/wlan.4-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/wlan.4-0/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 1.638 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:08 GMT+01:00 2026
Hostname: r23m0181.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.4-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/wlan.4-0/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/wlan.4-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 145 iterations in 0.17 seconds (average 0.001172, setup 0.00)

Time for model construction: 0.217 seconds.

Type:        MDP
States:      345000 (1 initial)
Transitions: 762252

Transition matrix: 14365 nodes (6 terminal), 762252 minterms, vars: 43r/43c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/wlan.4-0/model.umb_rep5.gz"...
Time for exporting: 0.75 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/wlan.4-0/model.umb_rep5.gz:	Size of output file is 15199275 bytes
Removing output file to save space for repetition #5
```

