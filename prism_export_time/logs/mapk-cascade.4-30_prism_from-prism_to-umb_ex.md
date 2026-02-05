# Log files

Tool configuration: prism_from-prism_to-umb_ex
Benchmark: [mapk-cascade.4-30](../../models/mapk-cascade.4-30)
Parsed values: [0.348, 0.487, 0.396, 0.431, 0.408]



### Log file: prism_from-prism_to-umb_ex_mapk-cascade.4-30_rep1.log

```
Command(s):
../bin/prism -ex models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb_ex/mapk-cascade.4-30/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 2.276 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:42:05 GMT+01:00 2026
Hostname: n23m0275.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/mapk-cascade.4-30/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 99535 states
Reachable states exploration and model construction done in 1.229 secs.
Sorting reachable states list...

Time for model construction: 1.348 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/mapk-cascade.4-30/model.umb"...
Model export size: 20159 Kb
Time for exporting: 0.348 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/mapk-cascade.4-30/model.umb:	Size of output file is 20642816 bytes
```



### Log file: prism_from-prism_to-umb_ex_mapk-cascade.4-30_rep2.log

```
Command(s):
../bin/prism -ex models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb_ex/mapk-cascade.4-30/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 2.978 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:39 GMT+01:00 2026
Hostname: r23m0052.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/mapk-cascade.4-30/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 99535 states
Reachable states exploration and model construction done in 1.346 secs.
Sorting reachable states list...

Time for model construction: 1.522 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/mapk-cascade.4-30/model_rep2.umb"...
Model export size: 20159 Kb
Time for exporting: 0.487 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/mapk-cascade.4-30/model_rep2.umb:	Size of output file is 20642816 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_ex_mapk-cascade.4-30_rep3.log

```
Command(s):
../bin/prism -ex models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb_ex/mapk-cascade.4-30/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 2.102 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:40 GMT+01:00 2026
Hostname: n23m0202.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/mapk-cascade.4-30/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 99535 states
Reachable states exploration and model construction done in 1.068 secs.
Sorting reachable states list...

Time for model construction: 1.215 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/mapk-cascade.4-30/model_rep3.umb"...
Model export size: 20159 Kb
Time for exporting: 0.396 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/mapk-cascade.4-30/model_rep3.umb:	Size of output file is 20642816 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_ex_mapk-cascade.4-30_rep4.log

```
Command(s):
../bin/prism -ex models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb_ex/mapk-cascade.4-30/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 2.553 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:11 GMT+01:00 2026
Hostname: n23m0019.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/mapk-cascade.4-30/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 99535 states
Reachable states exploration and model construction done in 1.349 secs.
Sorting reachable states list...

Time for model construction: 1.488 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/mapk-cascade.4-30/model_rep4.umb"...
Model export size: 20159 Kb
Time for exporting: 0.431 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/mapk-cascade.4-30/model_rep4.umb:	Size of output file is 20642816 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_ex_mapk-cascade.4-30_rep5.log

```
Command(s):
../bin/prism -ex models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb_ex/mapk-cascade.4-30/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 2.673 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:13 GMT+01:00 2026
Hostname: n23m0229.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/mapk-cascade.4-30/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:explicit)...

Computing reachable states... 99535 states
Reachable states exploration and model construction done in 1.398 secs.
Sorting reachable states list...

Time for model construction: 1.539 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Exporting model in UMB format to file "out/prism_from-prism_to-umb_ex/mapk-cascade.4-30/model_rep5.umb"...
Model export size: 20159 Kb
Time for exporting: 0.408 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/mapk-cascade.4-30/model_rep5.umb:	Size of output file is 20642816 bytes
Removing output file to save space for repetition #5
```

