# Log files

Tool configuration: prism_from-prism_to-umb-gz_ex
Benchmark: [pnueli-zuck.5](../../models/pnueli-zuck.5)
Parsed values: [2.216, 2.472, 2.144, 2.393, 2.272]



### Log file: prism_from-prism_to-umb-gz_ex_pnueli-zuck.5_rep1.log

```
Command(s):
../bin/prism -ex models/pnueli-zuck.5/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.5/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 5.926 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:22:44 GMT+01:00 2026
Hostname: n23m0110.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pnueli-zuck.5/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.5/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pnueli-zuck.5/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4
Actions:     []
Variables:   p0 p1 p2 p3 p4
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 397435 states
Reachable states exploration and model construction done in 2.475 secs.
Sorting reachable states list...

Time for model construction: 3.127 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2313746
Choices:     2145026
Max/avg:     10/5.40

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.5/model.umb.gz"...
Time for exporting: 2.216 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.5/model.umb.gz:	Size of output file is 41045749 bytes
```



### Log file: prism_from-prism_to-umb-gz_ex_pnueli-zuck.5_rep2.log

```
Command(s):
../bin/prism -ex models/pnueli-zuck.5/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.5/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 6.444 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:51 GMT+01:00 2026
Hostname: n23m0174.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pnueli-zuck.5/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.5/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pnueli-zuck.5/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4
Actions:     []
Variables:   p0 p1 p2 p3 p4
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 397435 states
Reachable states exploration and model construction done in 2.679 secs.
Sorting reachable states list...

Time for model construction: 3.34 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2313746
Choices:     2145026
Max/avg:     10/5.40

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.5/model.umb_rep2.gz"...
Time for exporting: 2.472 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.5/model.umb_rep2.gz:	Size of output file is 41045749 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_ex_pnueli-zuck.5_rep3.log

```
Command(s):
../bin/prism -ex models/pnueli-zuck.5/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.5/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 5.685 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:47:11 GMT+01:00 2026
Hostname: n23m0313.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pnueli-zuck.5/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.5/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pnueli-zuck.5/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4
Actions:     []
Variables:   p0 p1 p2 p3 p4
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 397435 states
Reachable states exploration and model construction done in 2.365 secs.
Sorting reachable states list...

Time for model construction: 2.976 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2313746
Choices:     2145026
Max/avg:     10/5.40

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.5/model.umb_rep3.gz"...
Time for exporting: 2.144 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.5/model.umb_rep3.gz:	Size of output file is 41045749 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_ex_pnueli-zuck.5_rep4.log

```
Command(s):
../bin/prism -ex models/pnueli-zuck.5/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.5/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 6.629 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:51:45 GMT+01:00 2026
Hostname: n23m0109.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pnueli-zuck.5/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.5/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pnueli-zuck.5/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4
Actions:     []
Variables:   p0 p1 p2 p3 p4
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 397435 states
Reachable states exploration and model construction done in 2.867 secs.
Sorting reachable states list...

Time for model construction: 3.596 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2313746
Choices:     2145026
Max/avg:     10/5.40

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.5/model.umb_rep4.gz"...
Time for exporting: 2.393 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.5/model.umb_rep4.gz:	Size of output file is 41045749 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_ex_pnueli-zuck.5_rep5.log

```
Command(s):
../bin/prism -ex models/pnueli-zuck.5/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.5/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 6.053 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:18:37 GMT+01:00 2026
Hostname: n23m0287.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pnueli-zuck.5/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.5/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pnueli-zuck.5/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4
Actions:     []
Variables:   p0 p1 p2 p3 p4
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 397435 states
Reachable states exploration and model construction done in 2.607 secs.
Sorting reachable states list...

Time for model construction: 3.182 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2313746
Choices:     2145026
Max/avg:     10/5.40

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.5/model.umb_rep5.gz"...
Time for exporting: 2.272 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.5/model.umb_rep5.gz:	Size of output file is 41045749 bytes
Removing output file to save space for repetition #5
```

