# Log files

Tool configuration: prism_from-prism_to-umb_norewards
Benchmark: [embedded.8-12](../../models/embedded.8-12)
Parsed values: [872448.0, 872448.0, 872448.0, 872448.0, 872448.0]



### Log file: prism_from-prism_to-umb_norewards_embedded.8-12_rep1.log

```
Command(s):
../bin/prism  models/embedded.8-12/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/embedded.8-12/model.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 0.725 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:42:08 GMT+01:00 2026
Hostname: r23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/embedded.8-12/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/embedded.8-12/model.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 21 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.016 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 1819 nodes (9 terminal), 36041 minterms, vars: 16r/16c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/embedded.8-12/model.umb"...
Model export size: 852 Kb
Time for exporting: 0.199 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/embedded.8-12/model.umb:	Size of output file is 872448 bytes
```



### Log file: prism_from-prism_to-umb_norewards_embedded.8-12_rep2.log

```
Command(s):
../bin/prism  models/embedded.8-12/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/embedded.8-12/model_rep2.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 1.367 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:27 GMT+01:00 2026
Hostname: n23m0273.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/embedded.8-12/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/embedded.8-12/model_rep2.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 21 iterations in 0.01 seconds (average 0.000476, setup 0.00)

Time for model construction: 0.043 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 1819 nodes (9 terminal), 36041 minterms, vars: 16r/16c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/embedded.8-12/model_rep2.umb"...
Model export size: 852 Kb
Time for exporting: 0.364 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/embedded.8-12/model_rep2.umb:	Size of output file is 872448 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_norewards_embedded.8-12_rep3.log

```
Command(s):
../bin/prism  models/embedded.8-12/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/embedded.8-12/model_rep3.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 0.700 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:27:59 GMT+01:00 2026
Hostname: n23m0383.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/embedded.8-12/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/embedded.8-12/model_rep3.umb:states=false,obs=false,rewards=false,zip=false'

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

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/embedded.8-12/model_rep3.umb"...
Model export size: 852 Kb
Time for exporting: 0.195 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/embedded.8-12/model_rep3.umb:	Size of output file is 872448 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_norewards_embedded.8-12_rep4.log

```
Command(s):
../bin/prism  models/embedded.8-12/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/embedded.8-12/model_rep4.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 0.752 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:47:42 GMT+01:00 2026
Hostname: n23m0244.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/embedded.8-12/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/embedded.8-12/model_rep4.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 21 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.016 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 1819 nodes (9 terminal), 36041 minterms, vars: 16r/16c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/embedded.8-12/model_rep4.umb"...
Model export size: 852 Kb
Time for exporting: 0.233 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/embedded.8-12/model_rep4.umb:	Size of output file is 872448 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_norewards_embedded.8-12_rep5.log

```
Command(s):
../bin/prism  models/embedded.8-12/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/embedded.8-12/model_rep5.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 0.733 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:22:09 GMT+01:00 2026
Hostname: n23m0256.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/embedded.8-12/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/embedded.8-12/model_rep5.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 21 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.016 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 1819 nodes (9 terminal), 36041 minterms, vars: 16r/16c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/embedded.8-12/model_rep5.umb"...
Model export size: 852 Kb
Time for exporting: 0.204 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/embedded.8-12/model_rep5.umb:	Size of output file is 872448 bytes
Removing output file to save space for repetition #5
```

