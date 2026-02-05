# Log files

Tool configuration: prism_from-prism_to-umb-gz_norewards
Benchmark: [wlan.5-0](../../models/wlan.5-0)
Parsed values: [2.159, 2.658, 2.161, 2.143, 2.58]



### Log file: prism_from-prism_to-umb-gz_norewards_wlan.5-0_rep1.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/wlan.5-0/model.umb.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 4.385 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:42:37 GMT+01:00 2026
Hostname: r23m0066.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/wlan.5-0/model.umb.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.19 seconds (average 0.001118, setup 0.00)

Time for model construction: 0.268 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/wlan.5-0/model.umb.gz"...
Time for exporting: 2.159 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/wlan.5-0/model.umb.gz:	Size of output file is 61393433 bytes
```



### Log file: prism_from-prism_to-umb-gz_norewards_wlan.5-0_rep2.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/wlan.5-0/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 3.746 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:55 GMT+01:00 2026
Hostname: n23m0346.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/wlan.5-0/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.28 seconds (average 0.001647, setup 0.00)

Time for model construction: 0.346 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/wlan.5-0/model.umb_rep2.gz"...
Time for exporting: 2.658 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/wlan.5-0/model.umb_rep2.gz:	Size of output file is 61393433 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_norewards_wlan.5-0_rep3.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/wlan.5-0/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 3.132 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:29:00 GMT+01:00 2026
Hostname: n23m0380.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/wlan.5-0/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.20 seconds (average 0.001176, setup 0.00)

Time for model construction: 0.247 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/wlan.5-0/model.umb_rep3.gz"...
Time for exporting: 2.161 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/wlan.5-0/model.umb_rep3.gz:	Size of output file is 61393433 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_norewards_wlan.5-0_rep4.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/wlan.5-0/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 2.906 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:32:02 GMT+01:00 2026
Hostname: n23m0058.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/wlan.5-0/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.18 seconds (average 0.001059, setup 0.00)

Time for model construction: 0.239 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/wlan.5-0/model.umb_rep4.gz"...
Time for exporting: 2.143 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/wlan.5-0/model.umb_rep4.gz:	Size of output file is 61393433 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_norewards_wlan.5-0_rep5.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/wlan.5-0/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 3.700 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:18:07 GMT+01:00 2026
Hostname: n23m0043.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/wlan.5-0/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.30 seconds (average 0.001765, setup 0.00)

Time for model construction: 0.415 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/wlan.5-0/model.umb_rep5.gz"...
Time for exporting: 2.58 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/wlan.5-0/model.umb_rep5.gz:	Size of output file is 61393433 bytes
Removing output file to save space for repetition #5
```

