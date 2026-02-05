# Log files

Tool configuration: prism_from-prism_to-umb_ex
Benchmark: [nand.60-4](../../models/nand.60-4)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_to-umb_ex_nand.60-4_rep1.log

```
Command(s):
../bin/prism -ex models/nand.60-4/model.prism -exportmodel out/prism_from-prism_to-umb_ex/nand.60-4/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 22.366 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:41:32 GMT+01:00 2026
Hostname: n23m0275.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/nand.60-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/nand.60-4/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 1948708 2920031 2979780 2996004 3007115 3011688
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at parser.State.<init>(State.java:50)
	at parser.State.<init>(State.java:59)
	at simulator.ChoiceListFlexi.computeTarget(ChoiceListFlexi.java:257)
	at simulator.ModulesFileModelGenerator.computeTransitionTarget(ModulesFileModelGenerator.java:664)
	at explicit.ConstructModel.constructModel(ConstructModel.java:295)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/nand.60-4/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_nand.60-4_rep2.log

```
Command(s):
../bin/prism -ex models/nand.60-4/model.prism -exportmodel out/prism_from-prism_to-umb_ex/nand.60-4/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 21.543 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:39:07 GMT+01:00 2026
Hostname: n23m0063.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/nand.60-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/nand.60-4/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 2054479 2916875 2984734 3002664 3009524
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.DTMCSimple.addToProbability(DTMCSimple.java:258)
	at explicit.ConstructModel.constructModel(ConstructModel.java:316)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/nand.60-4/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_nand.60-4_rep3.log

```
Command(s):
../bin/prism -ex models/nand.60-4/model.prism -exportmodel out/prism_from-prism_to-umb_ex/nand.60-4/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 91.869 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:56:27 GMT+01:00 2026
Hostname: r23m0217.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/nand.60-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/nand.60-4/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 402739 907267 1370609 1862522 2344325 2728580 2883616 2921995 2950049 2964458 2980106 2989841 2996347 2999573 3004146 3006433 3007576 3009860 3012146
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.DTMCSimple.addToProbability(DTMCSimple.java:259)
	at explicit.ConstructModel.constructModel(ConstructModel.java:316)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/nand.60-4/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_nand.60-4_rep4.log

```
Command(s):
../bin/prism -ex models/nand.60-4/model.prism -exportmodel out/prism_from-prism_to-umb_ex/nand.60-4/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 22.264 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:56:19 GMT+01:00 2026
Hostname: n23m0241.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/nand.60-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/nand.60-4/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 2017433 2907279 2981633 2999435 3008581
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at parser.State.<init>(State.java:50)
	at parser.State.<init>(State.java:59)
	at simulator.ChoiceListFlexi.computeTarget(ChoiceListFlexi.java:257)
	at simulator.ModulesFileModelGenerator.computeTransitionTarget(ModulesFileModelGenerator.java:664)
	at explicit.ConstructModel.constructModel(ConstructModel.java:295)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/nand.60-4/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_nand.60-4_rep5.log

```
Command(s):
../bin/prism -ex models/nand.60-4/model.prism -exportmodel out/prism_from-prism_to-umb_ex/nand.60-4/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 22.435 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:23:23 GMT+01:00 2026
Hostname: r23m0016.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/nand.60-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/nand.60-4/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 2030254 2911571 2984271 3002012 3008871
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.DTMCSimple.addToProbability(DTMCSimple.java:259)
	at explicit.ConstructModel.constructModel(ConstructModel.java:316)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/nand.60-4/model_rep5.umb:	File does not exist.
```

