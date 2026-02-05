# Log files for prism_from-prism_to-umb-gz_default on model [wlan.6-0](../../models/wlan.6-0)

Parsed values: `[8.281, 9.137, 9.972, 8.657, 9.03]`



### Log file: prism_from-prism_to-umb-gz_default_wlan.6-0_rep1.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/wlan.6-0/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 9.135 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:25:23 GMT+01:00 2026
Hostname: r23m0139.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/wlan.6-0/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.30 seconds (average 0.001538, setup 0.00)

Time for model construction: 0.339 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/wlan.6-0/model.umb.gz"...
Time for exporting: 8.281 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/wlan.6-0/model.umb.gz:	Size of output file is 255342633 bytes
```



### Log file: prism_from-prism_to-umb-gz_default_wlan.6-0_rep2.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/wlan.6-0/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 10.282 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:29:48 GMT+01:00 2026
Hostname: n23m0166.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/wlan.6-0/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.40 seconds (average 0.002051, setup 0.00)

Time for model construction: 0.475 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/wlan.6-0/model.umb_rep2.gz"...
Time for exporting: 9.137 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/wlan.6-0/model.umb_rep2.gz:	Size of output file is 255342633 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_default_wlan.6-0_rep3.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/wlan.6-0/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 11.291 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:55 GMT+01:00 2026
Hostname: n23m0343.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/wlan.6-0/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.46 seconds (average 0.002359, setup 0.00)

Time for model construction: 0.577 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/wlan.6-0/model.umb_rep3.gz"...
Time for exporting: 9.972 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/wlan.6-0/model.umb_rep3.gz:	Size of output file is 255342633 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_default_wlan.6-0_rep4.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/wlan.6-0/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 9.911 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:10 GMT+01:00 2026
Hostname: r23m0023.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/wlan.6-0/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.30 seconds (average 0.001538, setup 0.00)

Time for model construction: 0.362 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/wlan.6-0/model.umb_rep4.gz"...
Time for exporting: 8.657 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/wlan.6-0/model.umb_rep4.gz:	Size of output file is 255342633 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_default_wlan.6-0_rep5.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/wlan.6-0/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 9.990 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:27:29 GMT+01:00 2026
Hostname: n23m0252.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/wlan.6-0/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.30 seconds (average 0.001538, setup 0.00)

Time for model construction: 0.357 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/wlan.6-0/model.umb_rep5.gz"...
Time for exporting: 9.03 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/wlan.6-0/model.umb_rep5.gz:	Size of output file is 255342633 bytes
Removing output file to save space for repetition #5
```

