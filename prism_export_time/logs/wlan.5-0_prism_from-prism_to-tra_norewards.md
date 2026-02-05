# Log files for prism_from-prism_to-tra_norewards on model [wlan.5-0](../../models/wlan.5-0)

Parsed values: `[2.205, 2.572, 2.27, 2.146, 2.666]`



### Log file: prism_from-prism_to-tra_norewards_wlan.5-0_rep1.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/wlan.5-0/model.tra,lab:precision=17
Wallclock time: 5.902 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:28:03 GMT+01:00 2026
Hostname: n23m0095.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/wlan.5-0/model.tra,lab:precision=17'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.19 seconds (average 0.001118, setup 0.00)

Time for model construction: 0.41 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/wlan.5-0/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/wlan.5-0/model.lab"...
Time for exporting: 2.205 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/wlan.5-0/model.tra:	Size of output file is 61393433 bytes
out/prism_from-prism_to-tra_norewards/wlan.5-0/model.lab:	Size of output file is 48 bytes
```



### Log file: prism_from-prism_to-tra_norewards_wlan.5-0_rep2.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep2.tra,lab:precision=17
Wallclock time: 3.679 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:25:13 GMT+01:00 2026
Hostname: n23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep2.tra,lab:precision=17'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.30 seconds (average 0.001765, setup 0.00)

Time for model construction: 0.374 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep2.lab"...
Time for exporting: 2.572 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep2.tra:	Size of output file is 61393433 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep2.lab:	Size of output file is 48 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_norewards_wlan.5-0_rep3.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep3.tra,lab:precision=17
Wallclock time: 3.199 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:25:56 GMT+01:00 2026
Hostname: n23m0342.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep3.tra,lab:precision=17'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.19 seconds (average 0.001118, setup 0.00)

Time for model construction: 0.266 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep3.lab"...
Time for exporting: 2.27 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep3.tra:	Size of output file is 61393433 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep3.lab:	Size of output file is 48 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_norewards_wlan.5-0_rep4.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep4.tra,lab:precision=17
Wallclock time: 2.871 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:59:22 GMT+01:00 2026
Hostname: n23m0380.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep4.tra,lab:precision=17'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.17 seconds (average 0.001000, setup 0.00)

Time for model construction: 0.222 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep4.lab"...
Time for exporting: 2.146 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep4.tra:	Size of output file is 61393433 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep4.lab:	Size of output file is 48 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_norewards_wlan.5-0_rep5.log

```
Command(s):
../bin/prism  models/wlan.5-0/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep5.tra,lab:precision=17
Wallclock time: 3.969 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:20 GMT+01:00 2026
Hostname: n23m0174.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.5-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep5.tra,lab:precision=17'

Parsing PRISM model file "models/wlan.5-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 170 iterations in 0.30 seconds (average 0.001765, setup 0.00)

Time for model construction: 0.384 seconds.

Type:        MDP
States:      1295218 (1 initial)
Transitions: 2929960

Transition matrix: 17250 nodes (7 terminal), 2929960 minterms, vars: 45r/45c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep5.lab"...
Time for exporting: 2.666 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep5.tra:	Size of output file is 61393433 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_norewards/wlan.5-0/model_rep5.lab:	Size of output file is 48 bytes
Removing output file to save space for repetition #5
```

