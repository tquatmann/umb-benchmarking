# Log files

Tool configuration: modest_from-umb_check_unsafe-memory
Benchmark: [consensus.6-2](../../models/consensus.6-2)
Parsed values: [0.6, TO, TO, TO, TO]



### Log file: modest_from-umb_check_unsafe-memory_consensus.6-2_rep1.log

```
Command(s):
../bin/modest mcsta models/consensus.6-2/modest.model.umb models/consensus.6-2/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 16.147 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.6-2/modest.model.umb models/consensus.6-2/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.

Peak memory usage: 186 MB
Analysis results for UMB

+ State space (UMB)
  States:            1258240
  Choices:           5008128
  Branches:          6236736
  Time (decompress): 0.1 s
  Time (validate):   0.0 s
  Time (load):       0.5 s

+ Property disagree
  Probability: 0.36362422496221386
  Bounds:      [0.36362422496221386, 1]
  Time:        15.5 s

  + Value iteration
    Final error: 9.857326206509403E-07
    Iterations:  736
    Time:        15.5 s

```



### Log file: modest_from-umb_check_unsafe-memory_consensus.6-2_rep2.log

```
Command(s):
../bin/modest mcsta models/consensus.6-2/modest.model.umb models/consensus.6-2/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.017 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.6-2/modest.model.umb models/consensus.6-2/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.
```



### Log file: modest_from-umb_check_unsafe-memory_consensus.6-2_rep3.log

```
Command(s):
../bin/modest mcsta models/consensus.6-2/modest.model.umb models/consensus.6-2/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.038 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.6-2/modest.model.umb models/consensus.6-2/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.

##############################Output to stderr##############################
Fatal error. System.AccessViolationException: Attempted to read or write protected memory. This is often an indication that other memory is corrupt.
   at Modest.ModelChecking.ValueIteration.PerformUnboundedValueIteration(Modest.ModelChecking.PropertyAnalysisTask, Partition, System.Nullable`1<UInt64>, Modest.Modularity.LocationErrorHandler, System.Threading.CancellationToken, Boolean, Int64 ByRef, Double ByRef, Boolean ByRef)
   at Modest.ModelChecking.ValueIteration.PerformPartitionUnboundedValueIteration(Modest.ModelChecking.PropertyAnalysisTask, Partition, Int64, UnboundedValueIterationPartitionData, System.String, Modest.Modularity.LocationErrorHandler, Modest.Modularity.OperationState)
   at Modest.ModelChecking.ValueIteration+<>c__DisplayClass7_0.<IterateUnbounded>g__FixpointStep|1(Int32, Int32, Modest.Modularity.OperationState)
   at Modest.StateSpace.Helpers.IteratePartitions(Modest.StateSpace.StateSpace, System.Action`2<Int32,Modest.Modularity.OperationState>, System.Func`4<Int32,Int32,Modest.Modularity.OperationState,Boolean>, System.Action`2<Int32,Modest.Modularity.OperationState>, Modest.Modularity.OperationState)
   at Modest.ModelChecking.ValueIteration.IterateUnbounded(Modest.ModelChecking.PropertyAnalysisTask, Modest.StateSpace.StateSpace, Modest.Modularity.AnalysisDataSet, System.String, Modest.Modularity.LocationErrorHandler, Modest.Modularity.OperationState)
   at Modest.ModelChecking.MAModelChecker`1[[Modest.StateSpace.UnifiedBinaryFormat+UmbState, Modest.StateSpace, Version=3.1.0.0, Culture=neutral, PublicKeyToken=null]].CheckProperty(Modest.StateSpace.StateSpace, Modest.ModelChecking.ReachabilityPropertyInfo, System.String, System.String, Modest.StateSpace.StateSet`1<UmbState>, System.IDisposable ByRef, System.Func`3<Boolean,Boolean,Boolean>, System.String, Modest.Modularity.AnalysisDataSet, Modest.Modularity.OperationState, Modest.Modularity.ComponentErrorHandler)
   at Modest.ModelChecking.MAModelChecker`1[[Modest.StateSpace.UnifiedBinaryFormat+UmbState, Modest.StateSpace, Version=3.1.0.0, Culture=neutral, PublicKeyToken=null]].CheckProperties(Modest.StateSpace.StateSpace, Modest.StateSpace.StateSet`1<UmbState>, Boolean[], System.String, Modest.Modularity.OperationState, Modest.Modularity.ComponentErrorHandler)
   at Modest.ModelChecking.MAModelChecker`1[[Modest.StateSpace.UnifiedBinaryFormat+UmbState, Modest.StateSpace, Version=3.1.0.0, Culture=neutral, PublicKeyToken=null]].ModelCheck(System.String, Modest.Modularity.OperationState, Modest.Modularity.ComponentErrorHandler)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheckGeneric[[Modest.StateSpace.UnifiedBinaryFormat+UmbState, Modest.StateSpace, Version=3.1.0.0, Culture=neutral, PublicKeyToken=null]](Modest.Exploration.Network`1<UmbState>, Modest.StateSpace.UmbModel, System.Object, System.String, System.Object, System.Object, Modest.Modularity.ILocation, Modest.Modularity.OperationState, Modest.Modularity.ComponentErrorHandler)
   at invoke Modest.Exploration.Network`1__Modest.StateSpace.UnifiedBinaryFormat\+UmbState\, Modest.StateSpace\, Version=3.1.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(System.Object, System.Object[], System.Reflection.MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(System.Reflection.MethodInfo, System.Object, System.Object[])
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(Modest.Modularity.IModel, CompilationParameters<AnalysisParams>, System.Object, Modest.Modularity.OperationState, Modest.Modularity.IErrorHandler)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams, Modest.Modularity.IModel[], Int32, Boolean, Boolean, Boolean, Modest.Modularity.OperationState, Modest.Modularity.IErrorHandler)
   at Modest.ModelChecking.AnalysisEngine`1[[System.__Canon, System.Private.CoreLib, Version=9.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].Analyze(System.__Canon, Modest.Modularity.IModel, Int32, Boolean, Modest.Modularity.IExperiment[], Modest.Modularity.OperationState, Modest.Modularity.IErrorHandler)
   at Modest.ModelChecking.AnalysisEngine`1[[System.__Canon, System.Private.CoreLib, Version=9.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].Analyze(Modest.Modularity.IParameterObject, Modest.Modularity.IModel[], Modest.Modularity.IExperiment[][], Modest.Modularity.OperationState, Modest.Modularity.IErrorHandler)
   at Modest.Executable.ModelChecker.Run(Modest.Modularity.IParameterObject, System.Diagnostics.Stopwatch, Modest.Modularity.Tools.IOutputHandler, System.Threading.CancellationToken)
   at Modest.Executable.Program.Main(System.String[])
```



### Log file: modest_from-umb_check_unsafe-memory_consensus.6-2_rep4.log

```
Command(s):
../bin/modest mcsta models/consensus.6-2/modest.model.umb models/consensus.6-2/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.033 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.6-2/modest.model.umb models/consensus.6-2/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.
```



### Log file: modest_from-umb_check_unsafe-memory_consensus.6-2_rep5.log

```
Command(s):
../bin/modest mcsta models/consensus.6-2/modest.model.umb models/consensus.6-2/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.007 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.6-2/modest.model.umb models/consensus.6-2/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.
```

