# Log files for modest_from-jani_check_default on model [fms.8](../../models/fms.8)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: modest_from-jani_check_default_fms.8_rep1.log

```
Command(s):
../bin/modest mcsta models/fms.8/model.jani  -D --exhaustive
Wallclock time: 0.672 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/fms.8/model.jani -D --exhaustive




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
   at invoke Modest.Exploration.Network`1__CompiledAutomata.State1\, CompiledAutomata-20260128024958-1346954699\, Version=0.0.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(Object, Object[], MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(MethodInfo method, Object instance, Object[] parameters)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)
```



### Log file: modest_from-jani_check_default_fms.8_rep2.log

```
Command(s):
../bin/modest mcsta models/fms.8/model.jani  -D --exhaustive
Wallclock time: 0.304 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/fms.8/model.jani -D --exhaustive




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
   at invoke Modest.Exploration.Network`1__CompiledAutomata.State1\, CompiledAutomata-20260129010503-227979438\, Version=0.0.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(Object, Object[], MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(MethodInfo method, Object instance, Object[] parameters)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)
```



### Log file: modest_from-jani_check_default_fms.8_rep3.log

```
Command(s):
../bin/modest mcsta models/fms.8/model.jani  -D --exhaustive
Wallclock time: 0.263 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/fms.8/model.jani -D --exhaustive




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
   at invoke Modest.Exploration.Network`1__CompiledAutomata.State1\, CompiledAutomata-20260129011010-2110286601\, Version=0.0.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(Object, Object[], MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(MethodInfo method, Object instance, Object[] parameters)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)
```



### Log file: modest_from-jani_check_default_fms.8_rep4.log

```
Command(s):
../bin/modest mcsta models/fms.8/model.jani  -D --exhaustive
Wallclock time: 0.333 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/fms.8/model.jani -D --exhaustive




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
   at invoke Modest.Exploration.Network`1__CompiledAutomata.State1\, CompiledAutomata-20260129030738-1397821145\, Version=0.0.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(Object, Object[], MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(MethodInfo method, Object instance, Object[] parameters)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)
```



### Log file: modest_from-jani_check_default_fms.8_rep5.log

```
Command(s):
../bin/modest mcsta models/fms.8/model.jani  -D --exhaustive
Wallclock time: 0.200 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/fms.8/model.jani -D --exhaustive




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
   at invoke Modest.Exploration.Network`1__CompiledAutomata.State1\, CompiledAutomata-20260128202902-1318497802\, Version=0.0.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(Object, Object[], MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(MethodInfo method, Object instance, Object[] parameters)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)
```

