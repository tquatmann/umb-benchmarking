# Log files for prism_from-prism_to-umb-gz_default on model [mapk-cascade.4-30](../../models/mapk-cascade.4-30)

Parsed values: `[22829859.0, 22829859.0, 22829859.0, 22829859.0, 22829859.0]`



### Log file: prism_from-prism_to-umb-gz_default_mapk-cascade.4-30_rep1.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/mapk-cascade.4-30/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 3.382 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:25:54 GMT+01:00 2026
Hostname: n23m0128.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/mapk-cascade.4-30/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 1.55 seconds (average 0.035227, setup 0.00)

Time for model construction: 1.653 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/mapk-cascade.4-30/model.umb.gz"...
Time for exporting: 1.194 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/mapk-cascade.4-30/model.umb.gz:	Size of output file is 22829859 bytes
```



### Log file: prism_from-prism_to-umb-gz_default_mapk-cascade.4-30_rep2.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/mapk-cascade.4-30/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 3.503 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:41:07 GMT+01:00 2026
Hostname: n23m0063.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/mapk-cascade.4-30/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 1.67 seconds (average 0.037955, setup 0.00)

Time for model construction: 1.771 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/mapk-cascade.4-30/model.umb_rep2.gz"...
Time for exporting: 1.212 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/mapk-cascade.4-30/model.umb_rep2.gz:	Size of output file is 22829859 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_default_mapk-cascade.4-30_rep3.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/mapk-cascade.4-30/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 4.165 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:16 GMT+01:00 2026
Hostname: n23m0061.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/mapk-cascade.4-30/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

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

Time for model construction: 1.767 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/mapk-cascade.4-30/model.umb_rep3.gz"...
Time for exporting: 1.249 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/mapk-cascade.4-30/model.umb_rep3.gz:	Size of output file is 22829859 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_default_mapk-cascade.4-30_rep4.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/mapk-cascade.4-30/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 4.481 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:07 GMT+01:00 2026
Hostname: n23m0344.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/mapk-cascade.4-30/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 2.21 seconds (average 0.050227, setup 0.00)

Time for model construction: 2.354 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/mapk-cascade.4-30/model.umb_rep4.gz"...
Time for exporting: 1.455 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/mapk-cascade.4-30/model.umb_rep4.gz:	Size of output file is 22829859 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_default_mapk-cascade.4-30_rep5.log

```
Command(s):
../bin/prism  models/mapk-cascade.4-30/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/mapk-cascade.4-30/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 6.276 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:55 GMT+01:00 2026
Hostname: n23m0346.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/mapk-cascade.4-30/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/mapk-cascade.4-30/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/mapk-cascade.4-30/model.prism"...

Type:        CTMC
Modules:     E1 E2 KPTASE KKPTASE MAPK MAPKK MAPKKK
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   e1 e2 kptase kkptase k k_kkpp kp kp_kkpp kp_ptase kpp kpp_ptase kk kk_kkkp kkp kkp_kkkp kkp_ptase kkpp kkpp_ptase kkk kkk_e1 kkkp kkkp_e2
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 44 iterations in 3.72 seconds (average 0.084545, setup 0.00)

Time for model construction: 3.94 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 111563 nodes (14 terminal), 910872 minterms, vars: 58r/58c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/mapk-cascade.4-30/model.umb_rep5.gz"...
Time for exporting: 1.503 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/mapk-cascade.4-30/model.umb_rep5.gz:	Size of output file is 22829859 bytes
Removing output file to save space for repetition #5
```

