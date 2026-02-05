# Log files

Tool configuration: prism_from-prism_to-umb-gz_ex
Benchmark: [resource-gathering.1300-100-100](../../models/resource-gathering.1300-100-100)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_to-umb-gz_ex_resource-gathering.1300-100-100_rep1.log

```
Command(s):
../bin/prism -ex models/resource-gathering.1300-100-100/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/resource-gathering.1300-100-100/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 20.543 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:48:24 GMT+01:00 2026
Hostname: n23m0383.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/resource-gathering.1300-100-100/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/resource-gathering.1300-100-100/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Building model (engine:explicit)...

Computing reachable states... 469150 860492 958894 states
Reachable states exploration and model construction done in 7.698 secs.
Sorting reachable states list...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at explicit.ChoiceActionsSimple.<init>(ChoiceActionsSimple.java:95)
	at explicit.MDPSparse.<init>(MDPSparse.java:305)
	at explicit.ConstructModel.constructModel(ConstructModel.java:447)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/resource-gathering.1300-100-100/model.umb.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_resource-gathering.1300-100-100_rep2.log

```
Command(s):
../bin/prism -ex models/resource-gathering.1300-100-100/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/resource-gathering.1300-100-100/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 21.167 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:54 GMT+01:00 2026
Hostname: n23m0191.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/resource-gathering.1300-100-100/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/resource-gathering.1300-100-100/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Building model (engine:explicit)...

Computing reachable states... 504957 921992 958894 states
Reachable states exploration and model construction done in 7.227 secs.
Sorting reachable states list...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at explicit.ChoiceActionsSimple.<init>(ChoiceActionsSimple.java:95)
	at explicit.MDPSparse.<init>(MDPSparse.java:305)
	at explicit.ConstructModel.constructModel(ConstructModel.java:447)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/resource-gathering.1300-100-100/model.umb_rep2.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_resource-gathering.1300-100-100_rep3.log

```
Command(s):
../bin/prism -ex models/resource-gathering.1300-100-100/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/resource-gathering.1300-100-100/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 28.937 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:26 GMT+01:00 2026
Hostname: r23m0016.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/resource-gathering.1300-100-100/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/resource-gathering.1300-100-100/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Building model (engine:explicit)...

Computing reachable states... 320513 609085 878876 958894 states
Reachable states exploration and model construction done in 11.184 secs.
Sorting reachable states list...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at explicit.ChoiceActionsSimple.<init>(ChoiceActionsSimple.java:95)
	at explicit.MDPSparse.<init>(MDPSparse.java:305)
	at explicit.ConstructModel.constructModel(ConstructModel.java:447)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/resource-gathering.1300-100-100/model.umb_rep3.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_resource-gathering.1300-100-100_rep4.log

```
Command(s):
../bin/prism -ex models/resource-gathering.1300-100-100/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/resource-gathering.1300-100-100/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 19.882 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:41:08 GMT+01:00 2026
Hostname: n23m0281.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/resource-gathering.1300-100-100/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/resource-gathering.1300-100-100/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Building model (engine:explicit)...

Computing reachable states... 450825 837964 958894 states
Reachable states exploration and model construction done in 7.537 secs.
Sorting reachable states list...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.Arrays.copyOf(Arrays.java:3481)
	at java.base/java.util.ArrayList.toArray(ArrayList.java:370)
	at java.base/java.util.ArrayList.<init>(ArrayList.java:182)
	at explicit.ChoiceActionsSimple.<init>(ChoiceActionsSimple.java:95)
	at explicit.MDPSparse.<init>(MDPSparse.java:305)
	at explicit.ConstructModel.constructModel(ConstructModel.java:447)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/resource-gathering.1300-100-100/model.umb_rep4.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_resource-gathering.1300-100-100_rep5.log

```
Command(s):
../bin/prism -ex models/resource-gathering.1300-100-100/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/resource-gathering.1300-100-100/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 21.104 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:07 GMT+01:00 2026
Hostname: r23m0090.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/resource-gathering.1300-100-100/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/resource-gathering.1300-100-100/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/resource-gathering.1300-100-100/model.prism"...

Type:        MDP
Modules:     robot goldcounter gemcounter
Actions:     [right] [left] [top] [down]
Variables:   gold gem attacked x y required_gold required_gem
Labels:      "success"

Building model (engine:explicit)...

Computing reachable states... 477626 881466 958894 states
Reachable states exploration and model construction done in 7.471 secs.
Sorting reachable states list...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at explicit.ChoiceActionsSimple.<init>(ChoiceActionsSimple.java:95)
	at explicit.MDPSparse.<init>(MDPSparse.java:305)
	at explicit.ConstructModel.constructModel(ConstructModel.java:447)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/resource-gathering.1300-100-100/model.umb_rep5.gz:	File does not exist.
```

