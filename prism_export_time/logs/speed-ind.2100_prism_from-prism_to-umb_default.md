# Log files for prism_from-prism_to-umb_default on model [speed-ind.2100](../../models/speed-ind.2100)

Parsed values: `[26.934, 28.105, 30.254, 114.813, 24.737]`



### Log file: prism_from-prism_to-umb_default_speed-ind.2100_rep1.log

```
Command(s):
../bin/prism  models/speed-ind.2100/model.prism -exportmodel out/prism_from-prism_to-umb_default/speed-ind.2100/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 47.851 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:36:11 GMT+01:00 2026
Hostname: n23m0249.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/speed-ind.2100/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/speed-ind.2100/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/speed-ind.2100/model.prism"...

Type:        CTMC
Modules:     S1_def S2_def S3_def S4_def Y_def Z_def CC_def XX_def
Actions:     []
Variables:   S1 S2 S3 S4 Y Z CC XX
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.65 seconds (average 0.017105, setup 0.00)

Time for model construction: 20.199 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 33024 nodes (187 terminal), 9518080 minterms, vars: 58r/58c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/speed-ind.2100/model.umb"...
Model export size: 160524 Kb
Time for exporting: 26.934 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/speed-ind.2100/model.umb:	Size of output file is 164376576 bytes
```



### Log file: prism_from-prism_to-umb_default_speed-ind.2100_rep2.log

```
Command(s):
../bin/prism  models/speed-ind.2100/model.prism -exportmodel out/prism_from-prism_to-umb_default/speed-ind.2100/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 50.216 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:37 GMT+01:00 2026
Hostname: r23m0029.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/speed-ind.2100/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/speed-ind.2100/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/speed-ind.2100/model.prism"...

Type:        CTMC
Modules:     S1_def S2_def S3_def S4_def Y_def Z_def CC_def XX_def
Actions:     []
Variables:   S1 S2 S3 S4 Y Z CC XX
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.67 seconds (average 0.017632, setup 0.00)

Time for model construction: 20.895 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 33024 nodes (187 terminal), 9518080 minterms, vars: 58r/58c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/speed-ind.2100/model_rep2.umb"...
Model export size: 160524 Kb
Time for exporting: 28.105 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/speed-ind.2100/model_rep2.umb:	Size of output file is 164376576 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_default_speed-ind.2100_rep3.log

```
Command(s):
../bin/prism  models/speed-ind.2100/model.prism -exportmodel out/prism_from-prism_to-umb_default/speed-ind.2100/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 64.661 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:00 GMT+01:00 2026
Hostname: r23m0016.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/speed-ind.2100/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/speed-ind.2100/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/speed-ind.2100/model.prism"...

Type:        CTMC
Modules:     S1_def S2_def S3_def S4_def Y_def Z_def CC_def XX_def
Actions:     []
Variables:   S1 S2 S3 S4 Y Z CC XX
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.95 seconds (average 0.025000, setup 0.00)

Time for model construction: 33.346 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 33024 nodes (187 terminal), 9518080 minterms, vars: 58r/58c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/speed-ind.2100/model_rep3.umb"...
Model export size: 160524 Kb
Time for exporting: 30.254 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/speed-ind.2100/model_rep3.umb:	Size of output file is 164376576 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_default_speed-ind.2100_rep4.log

```
Command(s):
../bin/prism  models/speed-ind.2100/model.prism -exportmodel out/prism_from-prism_to-umb_default/speed-ind.2100/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 170.410 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:09:05 GMT+01:00 2026
Hostname: r23m0215.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/speed-ind.2100/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/speed-ind.2100/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/speed-ind.2100/model.prism"...

Type:        CTMC
Modules:     S1_def S2_def S3_def S4_def Y_def Z_def CC_def XX_def
Actions:     []
Variables:   S1 S2 S3 S4 Y Z CC XX
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 2.02 seconds (average 0.053158, setup 0.00)

Time for model construction: 52.846 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 33024 nodes (187 terminal), 9518080 minterms, vars: 58r/58c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/speed-ind.2100/model_rep4.umb"...
Model export size: 160524 Kb
Time for exporting: 114.813 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/speed-ind.2100/model_rep4.umb:	Size of output file is 164376576 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_default_speed-ind.2100_rep5.log

```
Command(s):
../bin/prism  models/speed-ind.2100/model.prism -exportmodel out/prism_from-prism_to-umb_default/speed-ind.2100/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 46.031 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:51:15 GMT+01:00 2026
Hostname: n23m0044.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/speed-ind.2100/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/speed-ind.2100/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/speed-ind.2100/model.prism"...

Type:        CTMC
Modules:     S1_def S2_def S3_def S4_def Y_def Z_def CC_def XX_def
Actions:     []
Variables:   S1 S2 S3 S4 Y Z CC XX
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.65 seconds (average 0.017105, setup 0.00)

Time for model construction: 20.634 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 33024 nodes (187 terminal), 9518080 minterms, vars: 58r/58c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/speed-ind.2100/model_rep5.umb"...
Model export size: 160524 Kb
Time for exporting: 24.737 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/speed-ind.2100/model_rep5.umb:	Size of output file is 164376576 bytes
Removing output file to save space for repetition #5
```

