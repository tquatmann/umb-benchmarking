# Log files

Tool configuration: modest_from-jani_to-aut_default
Benchmark: [kanban.5](../../models/kanban.5)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: modest_from-jani_to-aut_default_kanban.5_rep1.log

```
Command(s):
../bin/modest mcsta models/kanban.5/model.jani --statespace out/modest_from-jani_to-aut_default/kanban.5/model.aut AUT  -D --exhaustive
Wallclock time: 0.771 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/kanban.5/model.jani --statespace out/modest_from-jani_to-aut_default/kanban.5/model.aut AUT -D --exhaustive




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
   at invoke Modest.Exploration.Network`1__CompiledAutomata.State1\, CompiledAutomata-20260128154534-330770564\, Version=0.0.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(Object, Object[], MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(MethodInfo method, Object instance, Object[] parameters)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)

############################## Output files ##############################
out/modest_from-jani_to-aut_default/kanban.5/model.aut:	File does not exist.
```



### Log file: modest_from-jani_to-aut_default_kanban.5_rep2.log

```
Command(s):
../bin/modest mcsta models/kanban.5/model.jani --statespace out/modest_from-jani_to-aut_default/kanban.5/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 0.228 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/kanban.5/model.jani --statespace out/modest_from-jani_to-aut_default/kanban.5/model_rep2.aut AUT -D --exhaustive




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
   at invoke Modest.Exploration.Network`1__CompiledAutomata.State1\, CompiledAutomata-20260129084340-1882666298\, Version=0.0.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(Object, Object[], MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(MethodInfo method, Object instance, Object[] parameters)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)

############################## Output files ##############################
out/modest_from-jani_to-aut_default/kanban.5/model_rep2.aut:	File does not exist.
```



### Log file: modest_from-jani_to-aut_default_kanban.5_rep3.log

```
Command(s):
../bin/modest mcsta models/kanban.5/model.jani --statespace out/modest_from-jani_to-aut_default/kanban.5/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 0.196 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/kanban.5/model.jani --statespace out/modest_from-jani_to-aut_default/kanban.5/model_rep3.aut AUT -D --exhaustive




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
   at invoke Modest.Exploration.Network`1__CompiledAutomata.State1\, CompiledAutomata-20260129085448-1993175136\, Version=0.0.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(Object, Object[], MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(MethodInfo method, Object instance, Object[] parameters)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)

############################## Output files ##############################
out/modest_from-jani_to-aut_default/kanban.5/model_rep3.aut:	File does not exist.
```



### Log file: modest_from-jani_to-aut_default_kanban.5_rep4.log

```
Command(s):
../bin/modest mcsta models/kanban.5/model.jani --statespace out/modest_from-jani_to-aut_default/kanban.5/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 0.222 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/kanban.5/model.jani --statespace out/modest_from-jani_to-aut_default/kanban.5/model_rep4.aut AUT -D --exhaustive




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
   at invoke Modest.Exploration.Network`1__CompiledAutomata.State1\, CompiledAutomata-20260129072714-1300365906\, Version=0.0.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(Object, Object[], MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(MethodInfo method, Object instance, Object[] parameters)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)

############################## Output files ##############################
out/modest_from-jani_to-aut_default/kanban.5/model_rep4.aut:	File does not exist.
```



### Log file: modest_from-jani_to-aut_default_kanban.5_rep5.log

```
Command(s):
../bin/modest mcsta models/kanban.5/model.jani --statespace out/modest_from-jani_to-aut_default/kanban.5/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 0.187 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/kanban.5/model.jani --statespace out/modest_from-jani_to-aut_default/kanban.5/model_rep5.aut AUT -D --exhaustive




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
   at invoke Modest.Exploration.Network`1__CompiledAutomata.State1\, CompiledAutomata-20260129083131-1758412171\, Version=0.0.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(Object, Object[], MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(MethodInfo method, Object instance, Object[] parameters)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)

############################## Output files ##############################
out/modest_from-jani_to-aut_default/kanban.5/model_rep5.aut:	File does not exist.
```

