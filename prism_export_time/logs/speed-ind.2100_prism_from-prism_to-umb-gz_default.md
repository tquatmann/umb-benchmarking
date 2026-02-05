# Log files for prism_from-prism_to-umb-gz_default on model [speed-ind.2100](../../models/speed-ind.2100)

Parsed values: `[9.119, 8.697, 7.558, 7.421, 35.36]`



### Log file: prism_from-prism_to-umb-gz_default_speed-ind.2100_rep1.log

```
Command(s):
../bin/prism  models/speed-ind.2100/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/speed-ind.2100/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 34.597 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:35:09 GMT+01:00 2026
Hostname: r23m0005.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/speed-ind.2100/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/speed-ind.2100/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/speed-ind.2100/model.prism"...

Type:        CTMC
Modules:     S1_def S2_def S3_def S4_def Y_def Z_def CC_def XX_def
Actions:     []
Variables:   S1 S2 S3 S4 Y Z CC XX
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.77 seconds (average 0.020263, setup 0.00)

Time for model construction: 24.571 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 33024 nodes (187 terminal), 9518080 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/speed-ind.2100/model.umb.gz"...
Time for exporting: 9.119 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/speed-ind.2100/model.umb.gz:	Size of output file is 258672581 bytes
```



### Log file: prism_from-prism_to-umb-gz_default_speed-ind.2100_rep2.log

```
Command(s):
../bin/prism  models/speed-ind.2100/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/speed-ind.2100/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 45.634 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:40:38 GMT+01:00 2026
Hostname: r23m0196.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/speed-ind.2100/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/speed-ind.2100/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/speed-ind.2100/model.prism"...

Type:        CTMC
Modules:     S1_def S2_def S3_def S4_def Y_def Z_def CC_def XX_def
Actions:     []
Variables:   S1 S2 S3 S4 Y Z CC XX
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 1.03 seconds (average 0.027105, setup 0.00)

Time for model construction: 35.945 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 33024 nodes (187 terminal), 9518080 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/speed-ind.2100/model.umb_rep2.gz"...
Time for exporting: 8.697 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/speed-ind.2100/model.umb_rep2.gz:	Size of output file is 258672581 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_default_speed-ind.2100_rep3.log

```
Command(s):
../bin/prism  models/speed-ind.2100/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/speed-ind.2100/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 28.869 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:14:31 GMT+01:00 2026
Hostname: n23m0308.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/speed-ind.2100/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/speed-ind.2100/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/speed-ind.2100/model.prism"...

Type:        CTMC
Modules:     S1_def S2_def S3_def S4_def Y_def Z_def CC_def XX_def
Actions:     []
Variables:   S1 S2 S3 S4 Y Z CC XX
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.62 seconds (average 0.016316, setup 0.00)

Time for model construction: 20.515 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 33024 nodes (187 terminal), 9518080 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/speed-ind.2100/model.umb_rep3.gz"...
Time for exporting: 7.558 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/speed-ind.2100/model.umb_rep3.gz:	Size of output file is 258672581 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_default_speed-ind.2100_rep4.log

```
Command(s):
../bin/prism  models/speed-ind.2100/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/speed-ind.2100/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 28.883 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:21 GMT+01:00 2026
Hostname: n23m0191.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/speed-ind.2100/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/speed-ind.2100/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/speed-ind.2100/model.prism"...

Type:        CTMC
Modules:     S1_def S2_def S3_def S4_def Y_def Z_def CC_def XX_def
Actions:     []
Variables:   S1 S2 S3 S4 Y Z CC XX
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.64 seconds (average 0.016842, setup 0.00)

Time for model construction: 20.448 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 33024 nodes (187 terminal), 9518080 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/speed-ind.2100/model.umb_rep4.gz"...
Time for exporting: 7.421 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/speed-ind.2100/model.umb_rep4.gz:	Size of output file is 258672581 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_default_speed-ind.2100_rep5.log

```
Command(s):
../bin/prism  models/speed-ind.2100/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/speed-ind.2100/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 93.343 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:45:48 GMT+01:00 2026
Hostname: r23m0217.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/speed-ind.2100/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/speed-ind.2100/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/speed-ind.2100/model.prism"...

Type:        CTMC
Modules:     S1_def S2_def S3_def S4_def Y_def Z_def CC_def XX_def
Actions:     []
Variables:   S1 S2 S3 S4 Y Z CC XX
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 2.03 seconds (average 0.053421, setup 0.00)

Time for model construction: 55.115 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 33024 nodes (187 terminal), 9518080 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/speed-ind.2100/model.umb_rep5.gz"...
Time for exporting: 35.36 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/speed-ind.2100/model.umb_rep5.gz:	Size of output file is 258672581 bytes
Removing output file to save space for repetition #5
```

