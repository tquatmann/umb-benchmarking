# Log files

Tool configuration: prism_from-prism_to-tra_norewards
Benchmark: [zeroconf.1000-8-false](../../models/zeroconf.1000-8-false)
Parsed values: [5.543, 6.742, 6.794, 5.489, 5.713]



### Log file: prism_from-prism_to-tra_norewards_zeroconf.1000-8-false_rep1.log

```
Command(s):
../bin/prism  models/zeroconf.1000-8-false/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model.tra,lab:precision=17
Wallclock time: 45.630 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:46:17 GMT+01:00 2026
Hostname: n23m0380.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/zeroconf.1000-8-false/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model.tra,lab:precision=17'

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 592 iterations in 39.09 seconds (average 0.066030, setup 0.00)

Time for model construction: 39.546 seconds.

Type:        MDP
States:      1870338 (1 initial)
Transitions: 4245554

Transition matrix: 154038 nodes (6 terminal), 4245554 minterms, vars: 58r/58c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model.lab"...
Time for exporting: 5.543 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model.tra:	Size of output file is 117022857 bytes
out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model.lab:	Size of output file is 171569 bytes
```



### Log file: prism_from-prism_to-tra_norewards_zeroconf.1000-8-false_rep2.log

```
Command(s):
../bin/prism  models/zeroconf.1000-8-false/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep2.tra,lab:precision=17
Wallclock time: 62.056 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:56:20 GMT+01:00 2026
Hostname: n23m0128.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/zeroconf.1000-8-false/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep2.tra,lab:precision=17'

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 592 iterations in 53.22 seconds (average 0.089899, setup 0.00)

Time for model construction: 53.967 seconds.

Type:        MDP
States:      1870338 (1 initial)
Transitions: 4245554

Transition matrix: 154038 nodes (6 terminal), 4245554 minterms, vars: 58r/58c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep2.lab"...
Time for exporting: 6.742 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep2.tra:	Size of output file is 117022857 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep2.lab:	Size of output file is 171569 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_norewards_zeroconf.1000-8-false_rep3.log

```
Command(s):
../bin/prism  models/zeroconf.1000-8-false/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep3.tra,lab:precision=17
Wallclock time: 74.663 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:12 GMT+01:00 2026
Hostname: n23m0227.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/zeroconf.1000-8-false/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep3.tra,lab:precision=17'

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 592 iterations in 66.25 seconds (average 0.111909, setup 0.00)

Time for model construction: 67.097 seconds.

Type:        MDP
States:      1870338 (1 initial)
Transitions: 4245554

Transition matrix: 154038 nodes (6 terminal), 4245554 minterms, vars: 58r/58c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep3.lab"...
Time for exporting: 6.794 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep3.tra:	Size of output file is 117022857 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep3.lab:	Size of output file is 171569 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_norewards_zeroconf.1000-8-false_rep4.log

```
Command(s):
../bin/prism  models/zeroconf.1000-8-false/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep4.tra,lab:precision=17
Wallclock time: 44.966 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:24:12 GMT+01:00 2026
Hostname: n23m0380.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/zeroconf.1000-8-false/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep4.tra,lab:precision=17'

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 592 iterations in 38.46 seconds (average 0.064966, setup 0.00)

Time for model construction: 38.907 seconds.

Type:        MDP
States:      1870338 (1 initial)
Transitions: 4245554

Transition matrix: 154038 nodes (6 terminal), 4245554 minterms, vars: 58r/58c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep4.lab"...
Time for exporting: 5.489 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep4.tra:	Size of output file is 117022857 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep4.lab:	Size of output file is 171569 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_norewards_zeroconf.1000-8-false_rep5.log

```
Command(s):
../bin/prism  models/zeroconf.1000-8-false/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep5.tra,lab:precision=17
Wallclock time: 45.104 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:09 GMT+01:00 2026
Hostname: n23m0112.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/zeroconf.1000-8-false/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep5.tra,lab:precision=17'

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 592 iterations in 38.32 seconds (average 0.064730, setup 0.00)

Time for model construction: 38.797 seconds.

Type:        MDP
States:      1870338 (1 initial)
Transitions: 4245554

Transition matrix: 154038 nodes (6 terminal), 4245554 minterms, vars: 58r/58c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep5.lab"...
Time for exporting: 5.713 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep5.tra:	Size of output file is 117022857 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_norewards/zeroconf.1000-8-false/model_rep5.lab:	Size of output file is 171569 bytes
Removing output file to save space for repetition #5
```

