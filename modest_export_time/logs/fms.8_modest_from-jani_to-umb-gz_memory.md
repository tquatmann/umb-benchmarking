# Log files

Tool configuration: modest_from-jani_to-umb-gz_memory
Benchmark: [fms.8](../../models/fms.8)
Parsed values: [, ERR, ERR, ERR, ERR]



### Log file: modest_from-jani_to-umb-gz_memory_fms.8_rep2.log

```
Command(s):
../bin/modest mcsta models/fms.8/model.jani --umb out/modest_from-jani_to-umb-gz_memory/fms.8/model.umb_rep2.gz out/modest_from-jani_to-umb-gz_memory/fms.8/umbgz.properties_rep2.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 0.224 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/fms.8/model.jani --umb out/modest_from-jani_to-umb-gz_memory/fms.8/model.umb_rep2.gz out/modest_from-jani_to-umb-gz_memory/fms.8/umbgz.properties_rep2.txt --umb-compress GZIP -S Memory -D --exhaustive




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
   at invoke Modest.Exploration.Network`1__CompiledAutomata.State1\, CompiledAutomata-20260129084740-813655771\, Version=0.0.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(Object, Object[], MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(MethodInfo method, Object instance, Object[] parameters)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)

############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/fms.8/model.umb_rep2.gz:	File does not exist.
out/modest_from-jani_to-umb-gz_memory/fms.8/umbgz.properties_rep2.txt:	File does not exist.
```



### Log file: modest_from-jani_to-umb-gz_memory_fms.8_rep3.log

```
Command(s):
../bin/modest mcsta models/fms.8/model.jani --umb out/modest_from-jani_to-umb-gz_memory/fms.8/model.umb_rep3.gz out/modest_from-jani_to-umb-gz_memory/fms.8/umbgz.properties_rep3.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 0.314 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/fms.8/model.jani --umb out/modest_from-jani_to-umb-gz_memory/fms.8/model.umb_rep3.gz out/modest_from-jani_to-umb-gz_memory/fms.8/umbgz.properties_rep3.txt --umb-compress GZIP -S Memory -D --exhaustive




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
   at invoke Modest.Exploration.Network`1__CompiledAutomata.State1\, CompiledAutomata-20260129073711-2125737132\, Version=0.0.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(Object, Object[], MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(MethodInfo method, Object instance, Object[] parameters)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)

############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/fms.8/model.umb_rep3.gz:	File does not exist.
out/modest_from-jani_to-umb-gz_memory/fms.8/umbgz.properties_rep3.txt:	File does not exist.
```



### Log file: modest_from-jani_to-umb-gz_memory_fms.8_rep4.log

```
Command(s):
../bin/modest mcsta models/fms.8/model.jani --umb out/modest_from-jani_to-umb-gz_memory/fms.8/model.umb_rep4.gz out/modest_from-jani_to-umb-gz_memory/fms.8/umbgz.properties_rep4.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 0.219 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/fms.8/model.jani --umb out/modest_from-jani_to-umb-gz_memory/fms.8/model.umb_rep4.gz out/modest_from-jani_to-umb-gz_memory/fms.8/umbgz.properties_rep4.txt --umb-compress GZIP -S Memory -D --exhaustive




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
   at invoke Modest.Exploration.Network`1__CompiledAutomata.State1\, CompiledAutomata-20260129082525-753389404\, Version=0.0.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(Object, Object[], MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(MethodInfo method, Object instance, Object[] parameters)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)

############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/fms.8/model.umb_rep4.gz:	File does not exist.
out/modest_from-jani_to-umb-gz_memory/fms.8/umbgz.properties_rep4.txt:	File does not exist.
```



### Log file: modest_from-jani_to-umb-gz_memory_fms.8_rep5.log

```
Command(s):
../bin/modest mcsta models/fms.8/model.jani --umb out/modest_from-jani_to-umb-gz_memory/fms.8/model.umb_rep5.gz out/modest_from-jani_to-umb-gz_memory/fms.8/umbgz.properties_rep5.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 0.310 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/fms.8/model.jani --umb out/modest_from-jani_to-umb-gz_memory/fms.8/model.umb_rep5.gz out/modest_from-jani_to-umb-gz_memory/fms.8/umbgz.properties_rep5.txt --umb-compress GZIP -S Memory -D --exhaustive




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
   at invoke Modest.Exploration.Network`1__CompiledAutomata.State1\, CompiledAutomata-20260129091129-1970578211\, Version=0.0.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(Object, Object[], MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(MethodInfo method, Object instance, Object[] parameters)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)

############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/fms.8/model.umb_rep5.gz:	File does not exist.
out/modest_from-jani_to-umb-gz_memory/fms.8/umbgz.properties_rep5.txt:	File does not exist.
```

