# Log files

Tool configuration: prism_from-prism_to-umb-gz_norewards
Benchmark: [embedded.8-12](../../models/embedded.8-12)
Parsed values: [0.024, 0.024, 0.022, 0.025, 0.023]



### Log file: prism_from-prism_to-umb-gz_norewards_embedded.8-12_rep1.log

```
Command(s):
../bin/prism  models/embedded.8-12/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/embedded.8-12/model.umb.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 0.568 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:40:36 GMT+01:00 2026
Hostname: r23m0138.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/embedded.8-12/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/embedded.8-12/model.umb.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 21 iterations in 0.01 seconds (average 0.000476, setup 0.00)

Time for model construction: 0.017 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 1819 nodes (9 terminal), 36041 minterms, vars: 16r/16c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/embedded.8-12/model.umb.gz"...
Time for exporting: 0.024 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/embedded.8-12/model.umb.gz:	Size of output file is 1246405 bytes
```



### Log file: prism_from-prism_to-umb-gz_norewards_embedded.8-12_rep2.log

```
Command(s):
../bin/prism  models/embedded.8-12/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/embedded.8-12/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 0.571 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:48:13 GMT+01:00 2026
Hostname: n23m0055.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/embedded.8-12/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/embedded.8-12/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 21 iterations in 0.01 seconds (average 0.000476, setup 0.00)

Time for model construction: 0.015 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 1819 nodes (9 terminal), 36041 minterms, vars: 16r/16c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/embedded.8-12/model.umb_rep2.gz"...
Time for exporting: 0.024 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/embedded.8-12/model.umb_rep2.gz:	Size of output file is 1246405 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_norewards_embedded.8-12_rep3.log

```
Command(s):
../bin/prism  models/embedded.8-12/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/embedded.8-12/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 0.578 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:50:46 GMT+01:00 2026
Hostname: n23m0055.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/embedded.8-12/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/embedded.8-12/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 21 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.017 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 1819 nodes (9 terminal), 36041 minterms, vars: 16r/16c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/embedded.8-12/model.umb_rep3.gz"...
Time for exporting: 0.022 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/embedded.8-12/model.umb_rep3.gz:	Size of output file is 1246405 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_norewards_embedded.8-12_rep4.log

```
Command(s):
../bin/prism  models/embedded.8-12/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/embedded.8-12/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 0.632 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:37:05 GMT+01:00 2026
Hostname: n23m0043.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/embedded.8-12/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/embedded.8-12/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 21 iterations in 0.01 seconds (average 0.000476, setup 0.00)

Time for model construction: 0.018 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 1819 nodes (9 terminal), 36041 minterms, vars: 16r/16c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/embedded.8-12/model.umb_rep4.gz"...
Time for exporting: 0.025 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/embedded.8-12/model.umb_rep4.gz:	Size of output file is 1246405 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_norewards_embedded.8-12_rep5.log

```
Command(s):
../bin/prism  models/embedded.8-12/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/embedded.8-12/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 0.523 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:51 GMT+01:00 2026
Hostname: n23m0351.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/embedded.8-12/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/embedded.8-12/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 21 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.015 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 1819 nodes (9 terminal), 36041 minterms, vars: 16r/16c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/embedded.8-12/model.umb_rep5.gz"...
Time for exporting: 0.023 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/embedded.8-12/model.umb_rep5.gz:	Size of output file is 1246405 bytes
Removing output file to save space for repetition #5
```

