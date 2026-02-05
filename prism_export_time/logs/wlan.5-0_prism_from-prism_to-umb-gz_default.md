# Log files

Tool configuration: prism_from-prism_to-umb-gz_default
Benchmark: [wlan.5-0](../../models/wlan.5-0)
Parsed values: [2.167, 10.188, 2.151, 2.449, 2.568]



### Log file: prism_from-prism_to-umb-gz_default_wlan.5-0_rep1.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/wlan.5-0/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 3.011 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:34:05 GMT+01:00 2026
Hostname: n23m0275.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/wlan.5-0/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.17 seconds (average 0.001000, setup 0.00)

Time for model construction: 0.262 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/wlan.5-0/model.umb.gz"...
Time for exporting: 2.167 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/wlan.5-0/model.umb.gz:	Size of output file is 61393433 bytes
```



### Log file: prism_from-prism_to-umb-gz_default_wlan.5-0_rep2.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/wlan.5-0/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 13.234 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:55:56 GMT+01:00 2026
Hostname: r23m0215.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/wlan.5-0/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.78 seconds (average 0.004588, setup 0.00)

Time for model construction: 0.978 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/wlan.5-0/model.umb_rep2.gz"...
Time for exporting: 10.188 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/wlan.5-0/model.umb_rep2.gz:	Size of output file is 61393433 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_default_wlan.5-0_rep3.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/wlan.5-0/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 2.899 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:53:47 GMT+01:00 2026
Hostname: n23m0307.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/wlan.5-0/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.20 seconds (average 0.001176, setup 0.00)

Time for model construction: 0.252 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/wlan.5-0/model.umb_rep3.gz"...
Time for exporting: 2.151 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/wlan.5-0/model.umb_rep3.gz:	Size of output file is 61393433 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_default_wlan.5-0_rep4.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/wlan.5-0/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 4.927 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:38 GMT+01:00 2026
Hostname: n23m0008.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/wlan.5-0/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.19 seconds (average 0.001118, setup 0.00)

Time for model construction: 0.269 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/wlan.5-0/model.umb_rep4.gz"...
Time for exporting: 2.449 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/wlan.5-0/model.umb_rep4.gz:	Size of output file is 61393433 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_default_wlan.5-0_rep5.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/wlan.5-0/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 3.616 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:31:02 GMT+01:00 2026
Hostname: n23m0042.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/wlan.5-0/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.20 seconds (average 0.001176, setup 0.00)

Time for model construction: 0.322 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/wlan.5-0/model.umb_rep5.gz"...
Time for exporting: 2.568 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/wlan.5-0/model.umb_rep5.gz:	Size of output file is 61393433 bytes
Removing output file to save space for repetition #5
```

