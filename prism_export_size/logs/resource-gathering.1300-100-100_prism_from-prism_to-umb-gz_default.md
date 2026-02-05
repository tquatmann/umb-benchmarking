# Log files

Tool configuration: prism_from-prism_to-umb-gz_default
Benchmark: [resource-gathering.1300-100-100](../../models/resource-gathering.1300-100-100)
Parsed values: [76768962.0, 76768962.0, 76768962.0, 76768962.0, 76768962.0]



### Log file: prism_from-prism_to-umb-gz_default_resource-gathering.1300-100-100_rep1.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/resource-gathering.1300-100-100/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 2.618 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:32:00 GMT+01:00 2026
Hostname: n23m0110.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/resource-gathering.1300-100-100/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/resource-gathering.1300-100-100/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1215 iterations in 0.42 seconds (average 0.000346, setup 0.00)

Time for model construction: 0.446 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/resource-gathering.1300-100-100/model.umb.gz"...
Time for exporting: 1.639 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/resource-gathering.1300-100-100/model.umb.gz:	Size of output file is 76768962 bytes
```



### Log file: prism_from-prism_to-umb-gz_default_resource-gathering.1300-100-100_rep2.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/resource-gathering.1300-100-100/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 2.431 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:39:06 GMT+01:00 2026
Hostname: n23m0041.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/resource-gathering.1300-100-100/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/resource-gathering.1300-100-100/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1215 iterations in 0.38 seconds (average 0.000313, setup 0.00)

Time for model construction: 0.408 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/resource-gathering.1300-100-100/model.umb_rep2.gz"...
Time for exporting: 1.522 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/resource-gathering.1300-100-100/model.umb_rep2.gz:	Size of output file is 76768962 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_default_resource-gathering.1300-100-100_rep3.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/resource-gathering.1300-100-100/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 2.794 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:01 GMT+01:00 2026
Hostname: r23m0029.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/resource-gathering.1300-100-100/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/resource-gathering.1300-100-100/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1215 iterations in 0.47 seconds (average 0.000387, setup 0.00)

Time for model construction: 0.498 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/resource-gathering.1300-100-100/model.umb_rep3.gz"...
Time for exporting: 1.681 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/resource-gathering.1300-100-100/model.umb_rep3.gz:	Size of output file is 76768962 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_default_resource-gathering.1300-100-100_rep4.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/resource-gathering.1300-100-100/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 3.015 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:01 GMT+01:00 2026
Hostname: r23m0195.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/resource-gathering.1300-100-100/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/resource-gathering.1300-100-100/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1215 iterations in 0.54 seconds (average 0.000444, setup 0.00)

Time for model construction: 0.579 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/resource-gathering.1300-100-100/model.umb_rep4.gz"...
Time for exporting: 1.746 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/resource-gathering.1300-100-100/model.umb_rep4.gz:	Size of output file is 76768962 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_default_resource-gathering.1300-100-100_rep5.log

```
Command(s):
../bin/prism  models/resource-gathering.1300-100-100/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/resource-gathering.1300-100-100/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 2.790 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:51:17 GMT+01:00 2026
Hostname: n23m0063.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/resource-gathering.1300-100-100/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/resource-gathering.1300-100-100/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1215 iterations in 0.52 seconds (average 0.000428, setup 0.00)

Time for model construction: 0.565 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 898 nodes (4 terminal), 3325526 minterms, vars: 23r/23c/4nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/resource-gathering.1300-100-100/model.umb_rep5.gz"...
Time for exporting: 1.577 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/resource-gathering.1300-100-100/model.umb_rep5.gz:	Size of output file is 76768962 bytes
Removing output file to save space for repetition #5
```

