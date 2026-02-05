# Log files

Tool configuration: prism_from-prism_to-umb-gz_default
Benchmark: [fms.8](../../models/fms.8)
Parsed values: [46.249, 50.487, 54.658, 46.862, 48.014]



### Log file: prism_from-prism_to-umb-gz_default_fms.8_rep1.log

```
Command(s):
../bin/prism  models/fms.8/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/fms.8/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 50.124 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:33:33 GMT+01:00 2026
Hostname: n23m0276.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/fms.8/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 65 iterations in 3.17 seconds (average 0.048769, setup 0.00)

Time for model construction: 3.339 seconds.

Type:        CTMC
States:      4459455 (1 initial)
Transitions: 38533968

Rate matrix: 215250 nodes (84 terminal), 38533968 minterms, vars: 70r/70c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/fms.8/model.umb.gz"...
Time for exporting: 46.249 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/fms.8/model.umb.gz:	Size of output file is 1055004649 bytes
```



### Log file: prism_from-prism_to-umb-gz_default_fms.8_rep2.log

```
Command(s):
../bin/prism  models/fms.8/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/fms.8/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 57.465 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:55 GMT+01:00 2026
Hostname: n23m0113.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/fms.8/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 65 iterations in 6.03 seconds (average 0.092769, setup 0.00)

Time for model construction: 6.311 seconds.

Type:        CTMC
States:      4459455 (1 initial)
Transitions: 38533968

Rate matrix: 215250 nodes (84 terminal), 38533968 minterms, vars: 70r/70c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/fms.8/model.umb_rep2.gz"...
Time for exporting: 50.487 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/fms.8/model.umb_rep2.gz:	Size of output file is 1055004649 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_default_fms.8_rep3.log

```
Command(s):
../bin/prism  models/fms.8/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/fms.8/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 58.806 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:08:58 GMT+01:00 2026
Hostname: n23m0042.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/fms.8/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 65 iterations in 3.28 seconds (average 0.050462, setup 0.00)

Time for model construction: 3.485 seconds.

Type:        CTMC
States:      4459455 (1 initial)
Transitions: 38533968

Rate matrix: 215250 nodes (84 terminal), 38533968 minterms, vars: 70r/70c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/fms.8/model.umb_rep3.gz"...
Time for exporting: 54.658 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/fms.8/model.umb_rep3.gz:	Size of output file is 1055004649 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_default_fms.8_rep4.log

```
Command(s):
../bin/prism  models/fms.8/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/fms.8/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 52.325 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:23:53 GMT+01:00 2026
Hostname: r23m0016.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/fms.8/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 65 iterations in 4.64 seconds (average 0.071385, setup 0.00)

Time for model construction: 4.884 seconds.

Type:        CTMC
States:      4459455 (1 initial)
Transitions: 38533968

Rate matrix: 215250 nodes (84 terminal), 38533968 minterms, vars: 70r/70c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/fms.8/model.umb_rep4.gz"...
Time for exporting: 46.862 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/fms.8/model.umb_rep4.gz:	Size of output file is 1055004649 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_default_fms.8_rep5.log

```
Command(s):
../bin/prism  models/fms.8/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/fms.8/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 55.873 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:45:40 GMT+01:00 2026
Hostname: n23m0041.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/fms.8/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 65 iterations in 6.87 seconds (average 0.105692, setup 0.00)

Time for model construction: 7.148 seconds.

Type:        CTMC
States:      4459455 (1 initial)
Transitions: 38533968

Rate matrix: 215250 nodes (84 terminal), 38533968 minterms, vars: 70r/70c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/fms.8/model.umb_rep5.gz"...
Time for exporting: 48.014 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/fms.8/model.umb_rep5.gz:	Size of output file is 1055004649 bytes
Removing output file to save space for repetition #5
```

