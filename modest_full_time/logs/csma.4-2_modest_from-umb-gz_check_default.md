# Log files

Tool configuration: modest_from-umb-gz_check_default
Benchmark: [csma.4-2](../../models/csma.4-2)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: modest_from-umb-gz_check_default_csma.4-2_rep1.log

```
Command(s):
../bin/modest mcsta models/csma.4-2/modest.model.umb.gz models/csma.4-2/modest.umbgz.properties.txt -I UMB  -D --exhaustive
Wallclock time: 0.266 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/csma.4-2/modest.model.umb.gz models/csma.4-2/modest.umbgz.properties.txt -I UMB -D --exhaustive




##############################Output to stderr##############################
Unhandled exception. System.Collections.Generic.KeyNotFoundException: The given key 'ap_1' was not present in the dictionary.
   at System.Collections.Generic.Dictionary`2.get_Item(TKey key)
   at Modest.StateSpace.StateSpace.GetAtomicProposition(String key, UnsafeBitSet& ap)
   at Modest.ModelChecking.MAModelChecker`1.CheckProperty(StateSpace stateSpace, ReachabilityPropertyInfo prop, String avoidStatesKey, String targetStatesKey, StateSet`1 stateSet, IDisposable& previousBoundedIterationInfo, Func`3 onProbabilityNotZeroOrOne, String propertyStatusString, AnalysisDataSet info, OperationState operationState, ComponentErrorHandler ceh)
   at Modest.ModelChecking.MAModelChecker`1.CheckProperties(StateSpace ss, StateSet`1 states, Boolean[] reachAndInvariantPropertyResults, String experimentStatusString, OperationState operationState, ComponentErrorHandler ceh)
   at Modest.ModelChecking.MAModelChecker`1.ModelCheck(String experimentString, OperationState operationState, ComponentErrorHandler ceh)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheckGeneric[T](Network`1 network, UmbModel umbModel, Object expInfoObj, String experimentString, Object propertiesObj, Object parametersObj, ILocation documentLocation, OperationState operationState, ComponentErrorHandler ceh)
   at invoke Modest.Exploration.Network`1__Modest.StateSpace.UnifiedBinaryFormat\.UmbState\, Modest.StateSpace\, Version=3.1.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(Object, Object[], MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(MethodInfo method, Object instance, Object[] parameters)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)
```



### Log file: modest_from-umb-gz_check_default_csma.4-2_rep2.log

```
Command(s):
../bin/modest mcsta models/csma.4-2/modest.model.umb.gz models/csma.4-2/modest.umbgz.properties.txt -I UMB  -D --exhaustive
Wallclock time: 0.301 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/csma.4-2/modest.model.umb.gz models/csma.4-2/modest.umbgz.properties.txt -I UMB -D --exhaustive




##############################Output to stderr##############################
Unhandled exception. System.Collections.Generic.KeyNotFoundException: The given key 'ap_1' was not present in the dictionary.
   at System.Collections.Generic.Dictionary`2.get_Item(TKey key)
   at Modest.StateSpace.StateSpace.GetAtomicProposition(String key, UnsafeBitSet& ap)
   at Modest.ModelChecking.MAModelChecker`1.CheckProperty(StateSpace stateSpace, ReachabilityPropertyInfo prop, String avoidStatesKey, String targetStatesKey, StateSet`1 stateSet, IDisposable& previousBoundedIterationInfo, Func`3 onProbabilityNotZeroOrOne, String propertyStatusString, AnalysisDataSet info, OperationState operationState, ComponentErrorHandler ceh)
   at Modest.ModelChecking.MAModelChecker`1.CheckProperties(StateSpace ss, StateSet`1 states, Boolean[] reachAndInvariantPropertyResults, String experimentStatusString, OperationState operationState, ComponentErrorHandler ceh)
   at Modest.ModelChecking.MAModelChecker`1.ModelCheck(String experimentString, OperationState operationState, ComponentErrorHandler ceh)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheckGeneric[T](Network`1 network, UmbModel umbModel, Object expInfoObj, String experimentString, Object propertiesObj, Object parametersObj, ILocation documentLocation, OperationState operationState, ComponentErrorHandler ceh)
   at invoke Modest.Exploration.Network`1__Modest.StateSpace.UnifiedBinaryFormat\.UmbState\, Modest.StateSpace\, Version=3.1.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(Object, Object[], MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(MethodInfo method, Object instance, Object[] parameters)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)
```



### Log file: modest_from-umb-gz_check_default_csma.4-2_rep3.log

```
Command(s):
../bin/modest mcsta models/csma.4-2/modest.model.umb.gz models/csma.4-2/modest.umbgz.properties.txt -I UMB  -D --exhaustive
Wallclock time: 0.356 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/csma.4-2/modest.model.umb.gz models/csma.4-2/modest.umbgz.properties.txt -I UMB -D --exhaustive




##############################Output to stderr##############################
Unhandled exception. System.Collections.Generic.KeyNotFoundException: The given key 'ap_1' was not present in the dictionary.
   at System.Collections.Generic.Dictionary`2.get_Item(TKey key)
   at Modest.StateSpace.StateSpace.GetAtomicProposition(String key, UnsafeBitSet& ap)
   at Modest.ModelChecking.MAModelChecker`1.CheckProperty(StateSpace stateSpace, ReachabilityPropertyInfo prop, String avoidStatesKey, String targetStatesKey, StateSet`1 stateSet, IDisposable& previousBoundedIterationInfo, Func`3 onProbabilityNotZeroOrOne, String propertyStatusString, AnalysisDataSet info, OperationState operationState, ComponentErrorHandler ceh)
   at Modest.ModelChecking.MAModelChecker`1.CheckProperties(StateSpace ss, StateSet`1 states, Boolean[] reachAndInvariantPropertyResults, String experimentStatusString, OperationState operationState, ComponentErrorHandler ceh)
   at Modest.ModelChecking.MAModelChecker`1.ModelCheck(String experimentString, OperationState operationState, ComponentErrorHandler ceh)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheckGeneric[T](Network`1 network, UmbModel umbModel, Object expInfoObj, String experimentString, Object propertiesObj, Object parametersObj, ILocation documentLocation, OperationState operationState, ComponentErrorHandler ceh)
   at invoke Modest.Exploration.Network`1__Modest.StateSpace.UnifiedBinaryFormat\.UmbState\, Modest.StateSpace\, Version=3.1.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(Object, Object[], MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(MethodInfo method, Object instance, Object[] parameters)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)
```



### Log file: modest_from-umb-gz_check_default_csma.4-2_rep4.log

```
Command(s):
../bin/modest mcsta models/csma.4-2/modest.model.umb.gz models/csma.4-2/modest.umbgz.properties.txt -I UMB  -D --exhaustive
Wallclock time: 0.315 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/csma.4-2/modest.model.umb.gz models/csma.4-2/modest.umbgz.properties.txt -I UMB -D --exhaustive




##############################Output to stderr##############################
Unhandled exception. System.Collections.Generic.KeyNotFoundException: The given key 'ap_1' was not present in the dictionary.
   at System.Collections.Generic.Dictionary`2.get_Item(TKey key)
   at Modest.StateSpace.StateSpace.GetAtomicProposition(String key, UnsafeBitSet& ap)
   at Modest.ModelChecking.MAModelChecker`1.CheckProperty(StateSpace stateSpace, ReachabilityPropertyInfo prop, String avoidStatesKey, String targetStatesKey, StateSet`1 stateSet, IDisposable& previousBoundedIterationInfo, Func`3 onProbabilityNotZeroOrOne, String propertyStatusString, AnalysisDataSet info, OperationState operationState, ComponentErrorHandler ceh)
   at Modest.ModelChecking.MAModelChecker`1.CheckProperties(StateSpace ss, StateSet`1 states, Boolean[] reachAndInvariantPropertyResults, String experimentStatusString, OperationState operationState, ComponentErrorHandler ceh)
   at Modest.ModelChecking.MAModelChecker`1.ModelCheck(String experimentString, OperationState operationState, ComponentErrorHandler ceh)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheckGeneric[T](Network`1 network, UmbModel umbModel, Object expInfoObj, String experimentString, Object propertiesObj, Object parametersObj, ILocation documentLocation, OperationState operationState, ComponentErrorHandler ceh)
   at invoke Modest.Exploration.Network`1__Modest.StateSpace.UnifiedBinaryFormat\.UmbState\, Modest.StateSpace\, Version=3.1.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(Object, Object[], MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(MethodInfo method, Object instance, Object[] parameters)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)
```



### Log file: modest_from-umb-gz_check_default_csma.4-2_rep5.log

```
Command(s):
../bin/modest mcsta models/csma.4-2/modest.model.umb.gz models/csma.4-2/modest.umbgz.properties.txt -I UMB  -D --exhaustive
Wallclock time: 0.262 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/csma.4-2/modest.model.umb.gz models/csma.4-2/modest.umbgz.properties.txt -I UMB -D --exhaustive




##############################Output to stderr##############################
Unhandled exception. System.Collections.Generic.KeyNotFoundException: The given key 'ap_1' was not present in the dictionary.
   at System.Collections.Generic.Dictionary`2.get_Item(TKey key)
   at Modest.StateSpace.StateSpace.GetAtomicProposition(String key, UnsafeBitSet& ap)
   at Modest.ModelChecking.MAModelChecker`1.CheckProperty(StateSpace stateSpace, ReachabilityPropertyInfo prop, String avoidStatesKey, String targetStatesKey, StateSet`1 stateSet, IDisposable& previousBoundedIterationInfo, Func`3 onProbabilityNotZeroOrOne, String propertyStatusString, AnalysisDataSet info, OperationState operationState, ComponentErrorHandler ceh)
   at Modest.ModelChecking.MAModelChecker`1.CheckProperties(StateSpace ss, StateSet`1 states, Boolean[] reachAndInvariantPropertyResults, String experimentStatusString, OperationState operationState, ComponentErrorHandler ceh)
   at Modest.ModelChecking.MAModelChecker`1.ModelCheck(String experimentString, OperationState operationState, ComponentErrorHandler ceh)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheckGeneric[T](Network`1 network, UmbModel umbModel, Object expInfoObj, String experimentString, Object propertiesObj, Object parametersObj, ILocation documentLocation, OperationState operationState, ComponentErrorHandler ceh)
   at invoke Modest.Exploration.Network`1__Modest.StateSpace.UnifiedBinaryFormat\.UmbState\, Modest.StateSpace\, Version=3.1.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(Object, Object[], MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(MethodInfo method, Object instance, Object[] parameters)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)
```

