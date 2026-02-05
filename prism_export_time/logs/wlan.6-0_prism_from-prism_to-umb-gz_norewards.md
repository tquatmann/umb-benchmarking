# Log files for prism_from-prism_to-umb-gz_norewards on model [wlan.6-0](../../models/wlan.6-0)

Parsed values: `[8.218, 8.787, 9.473, 8.179, 8.184]`



### Log file: prism_from-prism_to-umb-gz_norewards_wlan.6-0_rep1.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/wlan.6-0/model.umb.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 9.092 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:39:25 GMT+01:00 2026
Hostname: r23m0047.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/wlan.6-0/model.umb.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.28 seconds (average 0.001436, setup 0.00)

Time for model construction: 0.327 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/wlan.6-0/model.umb.gz"...
Time for exporting: 8.218 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/wlan.6-0/model.umb.gz:	Size of output file is 255342633 bytes
```



### Log file: prism_from-prism_to-umb-gz_norewards_wlan.6-0_rep2.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/wlan.6-0/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 9.810 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:13:31 GMT+01:00 2026
Hostname: r23m0196.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/wlan.6-0/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.32 seconds (average 0.001641, setup 0.00)

Time for model construction: 0.382 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/wlan.6-0/model.umb_rep2.gz"...
Time for exporting: 8.787 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/wlan.6-0/model.umb_rep2.gz:	Size of output file is 255342633 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_norewards_wlan.6-0_rep3.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/wlan.6-0/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 10.483 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:26:01 GMT+01:00 2026
Hostname: n23m0008.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/wlan.6-0/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.34 seconds (average 0.001744, setup 0.00)

Time for model construction: 0.393 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/wlan.6-0/model.umb_rep3.gz"...
Time for exporting: 9.473 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/wlan.6-0/model.umb_rep3.gz:	Size of output file is 255342633 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_norewards_wlan.6-0_rep4.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/wlan.6-0/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 9.030 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:29:17 GMT+01:00 2026
Hostname: n23m0043.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/wlan.6-0/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.28 seconds (average 0.001436, setup 0.00)

Time for model construction: 0.321 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/wlan.6-0/model.umb_rep4.gz"...
Time for exporting: 8.179 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/wlan.6-0/model.umb_rep4.gz:	Size of output file is 255342633 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_norewards_wlan.6-0_rep5.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/wlan.6-0/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 9.022 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:39 GMT+01:00 2026
Hostname: n23m0058.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/wlan.6-0/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.28 seconds (average 0.001436, setup 0.00)

Time for model construction: 0.319 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/wlan.6-0/model.umb_rep5.gz"...
Time for exporting: 8.184 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/wlan.6-0/model.umb_rep5.gz:	Size of output file is 255342633 bytes
Removing output file to save space for repetition #5
```

