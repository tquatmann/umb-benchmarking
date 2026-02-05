# Log files

Tool configuration: prism_from-prism_to-umb-gz_default
Benchmark: [pnueli-zuck.10](../../models/pnueli-zuck.10)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_to-umb-gz_default_pnueli-zuck.10_rep1.log

```
Command(s):
../bin/prism  models/pnueli-zuck.10/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/pnueli-zuck.10/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 1.192 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:26:26 GMT+01:00 2026
Hostname: n23m0128.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.10/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/pnueli-zuck.10/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.57 seconds (average 0.007808, setup 0.00)

Time for model construction: 0.649 seconds.

Type:        MDP
States:      69994757110 (1 initial)
Transitions: 891923978050

Transition matrix: 22186 nodes (3 terminal), 891923978050 minterms, vars: 40r/40c/10nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/pnueli-zuck.10/model.umb.gz"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 69994757110 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/pnueli-zuck.10/model.umb.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_default_pnueli-zuck.10_rep2.log

```
Command(s):
../bin/prism  models/pnueli-zuck.10/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/pnueli-zuck.10/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 1.590 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:10:29 GMT+01:00 2026
Hostname: n23m0099.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.10/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/pnueli-zuck.10/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.87 seconds (average 0.011918, setup 0.00)

Time for model construction: 0.971 seconds.

Type:        MDP
States:      69994757110 (1 initial)
Transitions: 891923978050

Transition matrix: 22186 nodes (3 terminal), 891923978050 minterms, vars: 40r/40c/10nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/pnueli-zuck.10/model.umb_rep2.gz"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 69994757110 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/pnueli-zuck.10/model.umb_rep2.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_default_pnueli-zuck.10_rep3.log

```
Command(s):
../bin/prism  models/pnueli-zuck.10/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/pnueli-zuck.10/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 1.466 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:01 GMT+01:00 2026
Hostname: n23m0244.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.10/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/pnueli-zuck.10/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.76 seconds (average 0.010411, setup 0.00)

Time for model construction: 0.863 seconds.

Type:        MDP
States:      69994757110 (1 initial)
Transitions: 891923978050

Transition matrix: 22186 nodes (3 terminal), 891923978050 minterms, vars: 40r/40c/10nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/pnueli-zuck.10/model.umb_rep3.gz"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 69994757110 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/pnueli-zuck.10/model.umb_rep3.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_default_pnueli-zuck.10_rep4.log

```
Command(s):
../bin/prism  models/pnueli-zuck.10/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/pnueli-zuck.10/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 1.347 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:25:24 GMT+01:00 2026
Hostname: n23m0041.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.10/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/pnueli-zuck.10/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.73 seconds (average 0.010000, setup 0.00)

Time for model construction: 0.807 seconds.

Type:        MDP
States:      69994757110 (1 initial)
Transitions: 891923978050

Transition matrix: 22186 nodes (3 terminal), 891923978050 minterms, vars: 40r/40c/10nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/pnueli-zuck.10/model.umb_rep4.gz"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 69994757110 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/pnueli-zuck.10/model.umb_rep4.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_default_pnueli-zuck.10_rep5.log

```
Command(s):
../bin/prism  models/pnueli-zuck.10/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/pnueli-zuck.10/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 1.298 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:29:30 GMT+01:00 2026
Hostname: r23m0015.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.10/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/pnueli-zuck.10/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.57 seconds (average 0.007808, setup 0.00)

Time for model construction: 0.645 seconds.

Type:        MDP
States:      69994757110 (1 initial)
Transitions: 891923978050

Transition matrix: 22186 nodes (3 terminal), 891923978050 minterms, vars: 40r/40c/10nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/pnueli-zuck.10/model.umb_rep5.gz"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 69994757110 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/pnueli-zuck.10/model.umb_rep5.gz:	File does not exist.
```

