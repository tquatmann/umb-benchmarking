# Log files

Tool configuration: prism_from-prism_to-umb_ex
Benchmark: [polling.18-16](../../models/polling.18-16)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_to-umb_ex_polling.18-16_rep1.log

```
Command(s):
../bin/prism -ex models/polling.18-16/model.prism -exportmodel out/prism_from-prism_to-umb_ex/polling.18-16/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 50.811 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:21:42 GMT+01:00 2026
Hostname: n23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/polling.18-16/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/polling.18-16/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Building model (engine:explicit)...

Computing reachable states... 194218 397779 608969 811732 979603 1022027 1034311 1043459 1049371 1053372 1056223 1057943 1058724 1060038
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
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
out/prism_from-prism_to-umb_ex/polling.18-16/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_polling.18-16_rep2.log

```
Command(s):
../bin/prism -ex models/polling.18-16/model.prism -exportmodel out/prism_from-prism_to-umb_ex/polling.18-16/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 46.211 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:50:16 GMT+01:00 2026
Hostname: n23m0250.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/polling.18-16/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/polling.18-16/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Building model (engine:explicit)...

Computing reachable states... 216753 440852 667538 900801 1008221 1027966 1039753 1048183 1052949 1056374 1058092 1059236 1060378
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at simulator.ChoiceListFlexi.add(ChoiceListFlexi.java:133)
	at simulator.Updater.processUpdatesAndCreateNewChoice(Updater.java:380)
	at simulator.Updater.calculateTransitions(Updater.java:216)
	at simulator.ModulesFileModelGenerator.getTransitionListScalars(ModulesFileModelGenerator.java:827)
	at simulator.ModulesFileModelGenerator.getTransitionList(ModulesFileModelGenerator.java:814)
	at simulator.ModulesFileModelGenerator.getNumChoices(ModulesFileModelGenerator.java:513)
	at explicit.ConstructModel.constructModel(ConstructModel.java:273)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/polling.18-16/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_polling.18-16_rep3.log

```
Command(s):
../bin/prism -ex models/polling.18-16/model.prism -exportmodel out/prism_from-prism_to-umb_ex/polling.18-16/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 49.928 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:57:21 GMT+01:00 2026
Hostname: n23m0041.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/polling.18-16/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/polling.18-16/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Building model (engine:explicit)...

Computing reachable states... 191436 401555 610612 811736 977467 1018015 1032764 1042413 1049089 1052898 1055748 1058042 1058994 1059757
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
out/prism_from-prism_to-umb_ex/polling.18-16/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_polling.18-16_rep4.log

```
Command(s):
../bin/prism -ex models/polling.18-16/model.prism -exportmodel out/prism_from-prism_to-umb_ex/polling.18-16/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 50.051 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:53 GMT+01:00 2026
Hostname: n23m0165.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/polling.18-16/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/polling.18-16/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Building model (engine:explicit)...

Computing reachable states... 183083 383301 585825 789237 961184 1019837 1033582 1044825 1050925 1054541 1057398 1058543 1059496 1060636
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at simulator.Updater.processUpdatesAndCreateNewChoice(Updater.java:379)
	at simulator.Updater.calculateTransitions(Updater.java:196)
	at simulator.ModulesFileModelGenerator.getTransitionListScalars(ModulesFileModelGenerator.java:827)
	at simulator.ModulesFileModelGenerator.getTransitionList(ModulesFileModelGenerator.java:814)
	at simulator.ModulesFileModelGenerator.getNumChoices(ModulesFileModelGenerator.java:513)
	at explicit.ConstructModel.constructModel(ConstructModel.java:273)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/polling.18-16/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_polling.18-16_rep5.log

```
Command(s):
../bin/prism -ex models/polling.18-16/model.prism -exportmodel out/prism_from-prism_to-umb_ex/polling.18-16/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 41.751 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:53:16 GMT+01:00 2026
Hostname: n23m0307.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/polling.18-16/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/polling.18-16/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Building model (engine:explicit)...

Computing reachable states... 229941 471636 716727 965225 1021902 1036048 1048210 1053738 1056782 1058500 1059453 1060783
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
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
out/prism_from-prism_to-umb_ex/polling.18-16/model_rep5.umb:	File does not exist.
```

