# Log files for prism_from-prism_to-tra_norewards on model [wlan.6-0](../../models/wlan.6-0)

Parsed values: `[255342682.0, 255342682.0, 255342682.0, 255342682.0, 255342682.0]`



### Log file: prism_from-prism_to-tra_norewards_wlan.6-0_rep1.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/wlan.6-0/model.tra,lab:precision=17
Wallclock time: 9.066 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:26:27 GMT+01:00 2026
Hostname: n23m0248.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/wlan.6-0/model.tra,lab:precision=17'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.27 seconds (average 0.001385, setup 0.00)

Time for model construction: 0.328 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/wlan.6-0/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/wlan.6-0/model.lab"...
Time for exporting: 8.218 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/wlan.6-0/model.tra:	Size of output file is 255342633 bytes
out/prism_from-prism_to-tra_norewards/wlan.6-0/model.lab:	Size of output file is 49 bytes
```



### Log file: prism_from-prism_to-tra_norewards_wlan.6-0_rep2.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep2.tra,lab:precision=17
Wallclock time: 9.289 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:40:37 GMT+01:00 2026
Hostname: n23m0168.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep2.tra,lab:precision=17'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.28 seconds (average 0.001436, setup 0.00)

Time for model construction: 0.326 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep2.lab"...
Time for exporting: 8.408 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep2.tra:	Size of output file is 255342633 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep2.lab:	Size of output file is 49 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_norewards_wlan.6-0_rep3.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep3.tra,lab:precision=17
Wallclock time: 10.627 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:56 GMT+01:00 2026
Hostname: r23m0198.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep3.tra,lab:precision=17'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.39 seconds (average 0.002000, setup 0.00)

Time for model construction: 0.472 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep3.lab"...
Time for exporting: 9.502 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep3.tra:	Size of output file is 255342633 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep3.lab:	Size of output file is 49 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_norewards_wlan.6-0_rep4.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep4.tra,lab:precision=17
Wallclock time: 9.839 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:27:59 GMT+01:00 2026
Hostname: n23m0342.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep4.tra,lab:precision=17'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.32 seconds (average 0.001641, setup 0.00)

Time for model construction: 0.367 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep4.lab"...
Time for exporting: 8.822 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep4.tra:	Size of output file is 255342633 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep4.lab:	Size of output file is 49 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_norewards_wlan.6-0_rep5.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep5.tra,lab:precision=17
Wallclock time: 9.100 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:25:43 GMT+01:00 2026
Hostname: n23m0036.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep5.tra,lab:precision=17'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.28 seconds (average 0.001436, setup 0.00)

Time for model construction: 0.322 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep5.lab"...
Time for exporting: 8.25 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep5.tra:	Size of output file is 255342633 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_norewards/wlan.6-0/model_rep5.lab:	Size of output file is 49 bytes
Removing output file to save space for repetition #5
```

