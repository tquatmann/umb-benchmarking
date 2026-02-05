# Log files

Tool configuration: prism_from-prism_to-umb-gz_norewards
Benchmark: [zeroconf.1000-8-false](../../models/zeroconf.1000-8-false)
Parsed values: [5.452, 5.513, 6.464, 5.422, 5.452]



### Log file: prism_from-prism_to-umb-gz_norewards_zeroconf.1000-8-false_rep1.log

```
Command(s):
../bin/prism  models/zeroconf.1000-8-false/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/zeroconf.1000-8-false/model.umb.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 51.376 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:28:02 GMT+01:00 2026
Hostname: n23m0099.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/zeroconf.1000-8-false/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/zeroconf.1000-8-false/model.umb.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 592 iterations in 44.35 seconds (average 0.074916, setup 0.00)

Time for model construction: 44.897 seconds.

Type:        MDP
States:      1870338 (1 initial)
Transitions: 4245554

Transition matrix: 154038 nodes (6 terminal), 4245554 minterms, vars: 58r/58c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/zeroconf.1000-8-false/model.umb.gz"...
Time for exporting: 5.452 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/zeroconf.1000-8-false/model.umb.gz:	Size of output file is 92113083 bytes
```



### Log file: prism_from-prism_to-umb-gz_norewards_zeroconf.1000-8-false_rep2.log

```
Command(s):
../bin/prism  models/zeroconf.1000-8-false/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/zeroconf.1000-8-false/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 47.175 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:25:55 GMT+01:00 2026
Hostname: r23m0016.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/zeroconf.1000-8-false/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/zeroconf.1000-8-false/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 592 iterations in 40.61 seconds (average 0.068598, setup 0.00)

Time for model construction: 41.076 seconds.

Type:        MDP
States:      1870338 (1 initial)
Transitions: 4245554

Transition matrix: 154038 nodes (6 terminal), 4245554 minterms, vars: 58r/58c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/zeroconf.1000-8-false/model.umb_rep2.gz"...
Time for exporting: 5.513 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/zeroconf.1000-8-false/model.umb_rep2.gz:	Size of output file is 92113083 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_norewards_zeroconf.1000-8-false_rep3.log

```
Command(s):
../bin/prism  models/zeroconf.1000-8-false/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/zeroconf.1000-8-false/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 60.768 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:09 GMT+01:00 2026
Hostname: r23m0055.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/zeroconf.1000-8-false/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/zeroconf.1000-8-false/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 592 iterations in 52.93 seconds (average 0.089409, setup 0.00)

Time for model construction: 53.636 seconds.

Type:        MDP
States:      1870338 (1 initial)
Transitions: 4245554

Transition matrix: 154038 nodes (6 terminal), 4245554 minterms, vars: 58r/58c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/zeroconf.1000-8-false/model.umb_rep3.gz"...
Time for exporting: 6.464 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/zeroconf.1000-8-false/model.umb_rep3.gz:	Size of output file is 92113083 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_norewards_zeroconf.1000-8-false_rep4.log

```
Command(s):
../bin/prism  models/zeroconf.1000-8-false/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/zeroconf.1000-8-false/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 45.507 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:09 GMT+01:00 2026
Hostname: n23m0134.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/zeroconf.1000-8-false/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/zeroconf.1000-8-false/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 592 iterations in 39.11 seconds (average 0.066064, setup 0.00)

Time for model construction: 39.557 seconds.

Type:        MDP
States:      1870338 (1 initial)
Transitions: 4245554

Transition matrix: 154038 nodes (6 terminal), 4245554 minterms, vars: 58r/58c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/zeroconf.1000-8-false/model.umb_rep4.gz"...
Time for exporting: 5.422 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/zeroconf.1000-8-false/model.umb_rep4.gz:	Size of output file is 92113083 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_norewards_zeroconf.1000-8-false_rep5.log

```
Command(s):
../bin/prism  models/zeroconf.1000-8-false/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/zeroconf.1000-8-false/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 45.919 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:18:06 GMT+01:00 2026
Hostname: n23m0308.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/zeroconf.1000-8-false/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/zeroconf.1000-8-false/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 592 iterations in 39.37 seconds (average 0.066503, setup 0.00)

Time for model construction: 39.863 seconds.

Type:        MDP
States:      1870338 (1 initial)
Transitions: 4245554

Transition matrix: 154038 nodes (6 terminal), 4245554 minterms, vars: 58r/58c/7nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/zeroconf.1000-8-false/model.umb_rep5.gz"...
Time for exporting: 5.452 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/zeroconf.1000-8-false/model.umb_rep5.gz:	Size of output file is 92113083 bytes
Removing output file to save space for repetition #5
```

