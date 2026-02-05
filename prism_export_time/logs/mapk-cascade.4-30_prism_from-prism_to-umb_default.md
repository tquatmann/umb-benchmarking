# Log files

Tool configuration: prism_from-prism_to-umb_default
Benchmark: [mapk-cascade.4-30](../../models/mapk-cascade.4-30)
Parsed values: [6.157, 5.257, 5.282, 5.233, 5.092]



### Log file: prism_from-prism_to-umb_default_mapk-cascade.4-30_rep1.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb_default/mapk-cascade.4-30/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 10.168 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:48:56 GMT+01:00 2026
Hostname: r23m0045.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/mapk-cascade.4-30/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 3.18 seconds (average 0.072273, setup 0.00)

Time for model construction: 3.363 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/mapk-cascade.4-30/model.umb"...
Model export size: 20159 Kb
Time for exporting: 6.157 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/mapk-cascade.4-30/model.umb:	Size of output file is 20642816 bytes
```



### Log file: prism_from-prism_to-umb_default_mapk-cascade.4-30_rep2.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb_default/mapk-cascade.4-30/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 7.478 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:26:58 GMT+01:00 2026
Hostname: n23m0169.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/mapk-cascade.4-30/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 1.66 seconds (average 0.037727, setup 0.00)

Time for model construction: 1.766 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/mapk-cascade.4-30/model_rep2.umb"...
Model export size: 20159 Kb
Time for exporting: 5.257 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/mapk-cascade.4-30/model_rep2.umb:	Size of output file is 20642816 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_default_mapk-cascade.4-30_rep3.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb_default/mapk-cascade.4-30/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 8.714 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:19:07 GMT+01:00 2026
Hostname: r23m0196.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/mapk-cascade.4-30/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 2.71 seconds (average 0.061591, setup 0.00)

Time for model construction: 2.871 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/mapk-cascade.4-30/model_rep3.umb"...
Model export size: 20159 Kb
Time for exporting: 5.282 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/mapk-cascade.4-30/model_rep3.umb:	Size of output file is 20642816 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_default_mapk-cascade.4-30_rep4.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb_default/mapk-cascade.4-30/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 9.024 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:56 GMT+01:00 2026
Hostname: r23m0076.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/mapk-cascade.4-30/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 1.62 seconds (average 0.036818, setup 0.00)

Time for model construction: 1.756 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/mapk-cascade.4-30/model_rep4.umb"...
Model export size: 20159 Kb
Time for exporting: 5.233 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/mapk-cascade.4-30/model_rep4.umb:	Size of output file is 20642816 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_default_mapk-cascade.4-30_rep5.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb_default/mapk-cascade.4-30/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 7.541 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:41:37 GMT+01:00 2026
Hostname: n23m0313.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/mapk-cascade.4-30/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 1.84 seconds (average 0.041818, setup 0.00)

Time for model construction: 1.97 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/mapk-cascade.4-30/model_rep5.umb"...
Model export size: 20159 Kb
Time for exporting: 5.092 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/mapk-cascade.4-30/model_rep5.umb:	Size of output file is 20642816 bytes
Removing output file to save space for repetition #5
```

