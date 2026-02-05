# Log files for prism_from-prism_to-umb_norewards on model [mapk-cascade.4-30](../../models/mapk-cascade.4-30)

Parsed values: `[5.078, 5.061, 5.647, 6.176, 5.614]`



### Log file: prism_from-prism_to-umb_norewards_mapk-cascade.4-30_rep1.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/mapk-cascade.4-30/model.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 7.269 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:37:50 GMT+01:00 2026
Hostname: n23m0275.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/mapk-cascade.4-30/model.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 1.61 seconds (average 0.036591, setup 0.00)

Time for model construction: 1.715 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/mapk-cascade.4-30/model.umb"...
Model export size: 19380 Kb
Time for exporting: 5.078 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/mapk-cascade.4-30/model.umb:	Size of output file is 19845632 bytes
```



### Log file: prism_from-prism_to-umb_norewards_mapk-cascade.4-30_rep2.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/mapk-cascade.4-30/model_rep2.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 7.536 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:44:39 GMT+01:00 2026
Hostname: n23m0383.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/mapk-cascade.4-30/model_rep2.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 1.87 seconds (average 0.042500, setup 0.00)

Time for model construction: 1.979 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/mapk-cascade.4-30/model_rep2.umb"...
Model export size: 19380 Kb
Time for exporting: 5.061 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/mapk-cascade.4-30/model_rep2.umb:	Size of output file is 19845632 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_norewards_mapk-cascade.4-30_rep3.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/mapk-cascade.4-30/model_rep3.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 9.979 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:09:59 GMT+01:00 2026
Hostname: n23m0063.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/mapk-cascade.4-30/model_rep3.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 3.50 seconds (average 0.079545, setup 0.00)

Time for model construction: 3.712 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/mapk-cascade.4-30/model_rep3.umb"...
Model export size: 19380 Kb
Time for exporting: 5.647 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/mapk-cascade.4-30/model_rep3.umb:	Size of output file is 19845632 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_norewards_mapk-cascade.4-30_rep4.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/mapk-cascade.4-30/model_rep4.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 10.537 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:18:07 GMT+01:00 2026
Hostname: n23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/mapk-cascade.4-30/model_rep4.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 3.50 seconds (average 0.079545, setup 0.00)

Time for model construction: 3.706 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/mapk-cascade.4-30/model_rep4.umb"...
Model export size: 19380 Kb
Time for exporting: 6.176 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/mapk-cascade.4-30/model_rep4.umb:	Size of output file is 19845632 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_norewards_mapk-cascade.4-30_rep5.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/mapk-cascade.4-30/model_rep5.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 8.160 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:32:32 GMT+01:00 2026
Hostname: n23m0252.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/mapk-cascade.4-30/model_rep5.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 1.81 seconds (average 0.041136, setup 0.00)

Time for model construction: 1.94 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/mapk-cascade.4-30/model_rep5.umb"...
Model export size: 19380 Kb
Time for exporting: 5.614 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/mapk-cascade.4-30/model_rep5.umb:	Size of output file is 19845632 bytes
Removing output file to save space for repetition #5
```

