# Log files

Tool configuration: modest_from-jani_to-umb-xz_memory
Benchmark: [fms.8](../../models/fms.8)
Parsed values: [, ERR, ERR, ERR, ERR]



### Log file: modest_from-jani_to-umb-xz_memory_fms.8_rep2.log

```
Command(s):
../bin/modest mcsta models/fms.8/model.jani --umb out/modest_from-jani_to-umb-xz_memory/fms.8/model.umb_rep2.xz out/modest_from-jani_to-umb-xz_memory/fms.8/umbxz.properties_rep2.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 0.198 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/fms.8/model.jani --umb out/modest_from-jani_to-umb-xz_memory/fms.8/model.umb_rep2.xz out/modest_from-jani_to-umb-xz_memory/fms.8/umbxz.properties_rep2.txt --umb-compress XZ -S Memory -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.

##############################Output to stderr##############################
Unhandled exception. System.InvalidOperationException: Sequence contains no elements
   at System.Linq.ThrowHelper.ThrowNoElementsException()
   at System.Linq.Enumerable.MinMaxInteger[T,TMinMax](IEnumerable`1 source)
   at Modest.ModelChecking.MAModelChecker`1.StateSpaceExplorer..ctor(Network`1 network, ExpressionsInfo expInfo, Int32[][] terminatingStateExpressions, Int32[] reachAndInvariantGoalExpressions, Boolean terminateOnReach, Boolean enablePartitioning, DirectoryInfo storageLocation, StorageMode storageMode, CompressionMode compressionMode, Boolean fixDeadlocks, Boolean useDtmcSemantics, Boolean compressStateChains, Boolean isContinuousTimeMarkovModel, Scheduler`1 scheduler, Boolean useRationalValues, Boolean collectDiagnostics)
   at Modest.ModelChecking.MAModelChecker`1.ExploreStateSpace(String experimentStatusString, OperationState operationState, ComponentErrorHandler ceh)
   at Modest.ModelChecking.MAModelChecker`1.ModelCheck(String experimentString, OperationState operationState, ComponentErrorHandler ceh)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheckGeneric[T](Network`1 network, UmbModel umbModel, Object expInfoObj, String experimentString, Object propertiesObj, Object parametersObj, ILocation documentLocation, OperationState operationState, ComponentErrorHandler ceh)
   at invoke Modest.Exploration.Network`1__CompiledAutomata.State1\, CompiledAutomata-20260129084510-288074069\, Version=0.0.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(Object, Object[], MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(MethodInfo method, Object instance, Object[] parameters)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)

############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/fms.8/model.umb_rep2.xz:	File does not exist.
out/modest_from-jani_to-umb-xz_memory/fms.8/umbxz.properties_rep2.txt:	File does not exist.
```



### Log file: modest_from-jani_to-umb-xz_memory_fms.8_rep3.log

```
Command(s):
../bin/modest mcsta models/fms.8/model.jani --umb out/modest_from-jani_to-umb-xz_memory/fms.8/model.umb_rep3.xz out/modest_from-jani_to-umb-xz_memory/fms.8/umbxz.properties_rep3.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 0.207 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/fms.8/model.jani --umb out/modest_from-jani_to-umb-xz_memory/fms.8/model.umb_rep3.xz out/modest_from-jani_to-umb-xz_memory/fms.8/umbxz.properties_rep3.txt --umb-compress XZ -S Memory -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.

##############################Output to stderr##############################
Unhandled exception. System.InvalidOperationException: Sequence contains no elements
   at System.Linq.ThrowHelper.ThrowNoElementsException()
   at System.Linq.Enumerable.MinMaxInteger[T,TMinMax](IEnumerable`1 source)
   at Modest.ModelChecking.MAModelChecker`1.StateSpaceExplorer..ctor(Network`1 network, ExpressionsInfo expInfo, Int32[][] terminatingStateExpressions, Int32[] reachAndInvariantGoalExpressions, Boolean terminateOnReach, Boolean enablePartitioning, DirectoryInfo storageLocation, StorageMode storageMode, CompressionMode compressionMode, Boolean fixDeadlocks, Boolean useDtmcSemantics, Boolean compressStateChains, Boolean isContinuousTimeMarkovModel, Scheduler`1 scheduler, Boolean useRationalValues, Boolean collectDiagnostics)
   at Modest.ModelChecking.MAModelChecker`1.ExploreStateSpace(String experimentStatusString, OperationState operationState, ComponentErrorHandler ceh)
   at Modest.ModelChecking.MAModelChecker`1.ModelCheck(String experimentString, OperationState operationState, ComponentErrorHandler ceh)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheckGeneric[T](Network`1 network, UmbModel umbModel, Object expInfoObj, String experimentString, Object propertiesObj, Object parametersObj, ILocation documentLocation, OperationState operationState, ComponentErrorHandler ceh)
   at invoke Modest.Exploration.Network`1__CompiledAutomata.State1\, CompiledAutomata-20260129084741-1089620769\, Version=0.0.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(Object, Object[], MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(MethodInfo method, Object instance, Object[] parameters)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)

############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/fms.8/model.umb_rep3.xz:	File does not exist.
out/modest_from-jani_to-umb-xz_memory/fms.8/umbxz.properties_rep3.txt:	File does not exist.
```



### Log file: modest_from-jani_to-umb-xz_memory_fms.8_rep4.log

```
Command(s):
../bin/modest mcsta models/fms.8/model.jani --umb out/modest_from-jani_to-umb-xz_memory/fms.8/model.umb_rep4.xz out/modest_from-jani_to-umb-xz_memory/fms.8/umbxz.properties_rep4.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 0.199 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/fms.8/model.jani --umb out/modest_from-jani_to-umb-xz_memory/fms.8/model.umb_rep4.xz out/modest_from-jani_to-umb-xz_memory/fms.8/umbxz.properties_rep4.txt --umb-compress XZ -S Memory -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.

##############################Output to stderr##############################
Unhandled exception. System.InvalidOperationException: Sequence contains no elements
   at System.Linq.ThrowHelper.ThrowNoElementsException()
   at System.Linq.Enumerable.MinMaxInteger[T,TMinMax](IEnumerable`1 source)
   at Modest.ModelChecking.MAModelChecker`1.StateSpaceExplorer..ctor(Network`1 network, ExpressionsInfo expInfo, Int32[][] terminatingStateExpressions, Int32[] reachAndInvariantGoalExpressions, Boolean terminateOnReach, Boolean enablePartitioning, DirectoryInfo storageLocation, StorageMode storageMode, CompressionMode compressionMode, Boolean fixDeadlocks, Boolean useDtmcSemantics, Boolean compressStateChains, Boolean isContinuousTimeMarkovModel, Scheduler`1 scheduler, Boolean useRationalValues, Boolean collectDiagnostics)
   at Modest.ModelChecking.MAModelChecker`1.ExploreStateSpace(String experimentStatusString, OperationState operationState, ComponentErrorHandler ceh)
   at Modest.ModelChecking.MAModelChecker`1.ModelCheck(String experimentString, OperationState operationState, ComponentErrorHandler ceh)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheckGeneric[T](Network`1 network, UmbModel umbModel, Object expInfoObj, String experimentString, Object propertiesObj, Object parametersObj, ILocation documentLocation, OperationState operationState, ComponentErrorHandler ceh)
   at invoke Modest.Exploration.Network`1__CompiledAutomata.State1\, CompiledAutomata-20260129091526-1376355170\, Version=0.0.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(Object, Object[], MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(MethodInfo method, Object instance, Object[] parameters)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)

############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/fms.8/model.umb_rep4.xz:	File does not exist.
out/modest_from-jani_to-umb-xz_memory/fms.8/umbxz.properties_rep4.txt:	File does not exist.
```



### Log file: modest_from-jani_to-umb-xz_memory_fms.8_rep5.log

```
Command(s):
../bin/modest mcsta models/fms.8/model.jani --umb out/modest_from-jani_to-umb-xz_memory/fms.8/model.umb_rep5.xz out/modest_from-jani_to-umb-xz_memory/fms.8/umbxz.properties_rep5.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 0.217 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/fms.8/model.jani --umb out/modest_from-jani_to-umb-xz_memory/fms.8/model.umb_rep5.xz out/modest_from-jani_to-umb-xz_memory/fms.8/umbxz.properties_rep5.txt --umb-compress XZ -S Memory -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.

##############################Output to stderr##############################
Unhandled exception. System.InvalidOperationException: Sequence contains no elements
   at System.Linq.ThrowHelper.ThrowNoElementsException()
   at System.Linq.Enumerable.MinMaxInteger[T,TMinMax](IEnumerable`1 source)
   at Modest.ModelChecking.MAModelChecker`1.StateSpaceExplorer..ctor(Network`1 network, ExpressionsInfo expInfo, Int32[][] terminatingStateExpressions, Int32[] reachAndInvariantGoalExpressions, Boolean terminateOnReach, Boolean enablePartitioning, DirectoryInfo storageLocation, StorageMode storageMode, CompressionMode compressionMode, Boolean fixDeadlocks, Boolean useDtmcSemantics, Boolean compressStateChains, Boolean isContinuousTimeMarkovModel, Scheduler`1 scheduler, Boolean useRationalValues, Boolean collectDiagnostics)
   at Modest.ModelChecking.MAModelChecker`1.ExploreStateSpace(String experimentStatusString, OperationState operationState, ComponentErrorHandler ceh)
   at Modest.ModelChecking.MAModelChecker`1.ModelCheck(String experimentString, OperationState operationState, ComponentErrorHandler ceh)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheckGeneric[T](Network`1 network, UmbModel umbModel, Object expInfoObj, String experimentString, Object propertiesObj, Object parametersObj, ILocation documentLocation, OperationState operationState, ComponentErrorHandler ceh)
   at invoke Modest.Exploration.Network`1__CompiledAutomata.State1\, CompiledAutomata-20260129092038-1161559536\, Version=0.0.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(Object, Object[], MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(MethodInfo method, Object instance, Object[] parameters)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)

############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/fms.8/model.umb_rep5.xz:	File does not exist.
out/modest_from-jani_to-umb-xz_memory/fms.8/umbxz.properties_rep5.txt:	File does not exist.
```

