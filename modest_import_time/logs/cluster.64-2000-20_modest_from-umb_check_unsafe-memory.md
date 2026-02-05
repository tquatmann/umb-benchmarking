# Log files for modest_from-umb_check_unsafe-memory on model [cluster.64-2000-20](../../models/cluster.64-2000-20)

Parsed values: `[TO, TO, TO, TO, TO]`



### Log file: modest_from-umb_check_unsafe-memory_cluster.64-2000-20_rep1.log

```
Command(s):
../bin/modest mcsta models/cluster.64-2000-20/modest.model.umb models/cluster.64-2000-20/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.007 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.64-2000-20/modest.model.umb models/cluster.64-2000-20/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.
```



### Log file: modest_from-umb_check_unsafe-memory_cluster.64-2000-20_rep2.log

```
Command(s):
../bin/modest mcsta models/cluster.64-2000-20/modest.model.umb models/cluster.64-2000-20/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.007 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.64-2000-20/modest.model.umb models/cluster.64-2000-20/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.

##############################Output to stderr##############################
Fatal error. System.AccessViolationException: Attempted to read or write protected memory. This is often an indication that other memory is corrupt.
   at Modest.ModelChecking.UnifPlus.CalculateBound(Modest.ModelChecking.PropertyAnalysisTask, Modest.StateSpace.StateSpace, Double, Double, Boolean, Int32 ByRef, Int32 ByRef, Modest.Modularity.LocationErrorHandler, System.Threading.CancellationToken)
   at Modest.ModelChecking.UnifPlus.CalculateOuterBound(Modest.ModelChecking.PropertyAnalysisTask, Modest.StateSpace.StateSpace, Double, Double, Int32 ByRef, Int32 ByRef, Modest.Modularity.LocationErrorHandler, System.Threading.CancellationToken)
   at Modest.ModelChecking.UnifPlus.Calculate(Modest.ModelChecking.PropertyAnalysisTask, Modest.StateSpace.StateSpace, Modest.Modularity.AnalysisDataSet, System.String, Modest.Modularity.OperationState, Modest.Modularity.LocationErrorHandler)
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



### Log file: modest_from-umb_check_unsafe-memory_cluster.64-2000-20_rep3.log

```
Command(s):
../bin/modest mcsta models/cluster.64-2000-20/modest.model.umb models/cluster.64-2000-20/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.034 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.64-2000-20/modest.model.umb models/cluster.64-2000-20/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.

##############################Output to stderr##############################
Fatal error. System.AccessViolationException: Attempted to read or write protected memory. This is often an indication that other memory is corrupt.
   at Modest.ModelChecking.UnifPlus.CalculateBound(Modest.ModelChecking.PropertyAnalysisTask, Modest.StateSpace.StateSpace, Double, Double, Boolean, Int32 ByRef, Int32 ByRef, Modest.Modularity.LocationErrorHandler, System.Threading.CancellationToken)
   at Modest.ModelChecking.UnifPlus.CalculateOuterBound(Modest.ModelChecking.PropertyAnalysisTask, Modest.StateSpace.StateSpace, Double, Double, Int32 ByRef, Int32 ByRef, Modest.Modularity.LocationErrorHandler, System.Threading.CancellationToken)
```



### Log file: modest_from-umb_check_unsafe-memory_cluster.64-2000-20_rep4.log

```
Command(s):
../bin/modest mcsta models/cluster.64-2000-20/modest.model.umb models/cluster.64-2000-20/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.030 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.64-2000-20/modest.model.umb models/cluster.64-2000-20/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.

##############################Output to stderr##############################
Fatal error. System.AccessViolationException: Attempted to read or write protected memory. This is often an indication that other memory is corrupt.
   at Modest.ModelChecking.UnifPlus.CalculateBound(Modest.ModelChecking.PropertyAnalysisTask, Modest.StateSpace.StateSpace, Double, Double, Boolean, Int32 ByRef, Int32 ByRef, Modest.Modularity.LocationErrorHandler, System.Threading.CancellationToken)
   at Modest.ModelChecking.UnifPlus.CalculateOuterBound(Modest.ModelChecking.PropertyAnalysisTask, Modest.StateSpace.StateSpace, Double, Double, Int32 ByRef, Int32 ByRef, Modest.Modularity.LocationErrorHandler, System.Threading.CancellationToken)
   at Modest.ModelChecking.UnifPlus.Calculate(Modest.ModelChecking.PropertyAnalysisTask, Modest.StateSpace.StateSpace, Modest.Modularity.AnalysisDataSet, System.String, Modest.Modularity.OperationState, Modest.Modularity.LocationErrorHandler)
   at Modest.ModelChecking.MAModelChecker`1[[Modest.StateSpace.UnifiedBinaryFormat+UmbState, Modest.StateSpace, Version=3.1.0.0, Culture=neutral, PublicKeyToken=null]].CheckProperty(Modest.StateSpace.StateSpace, Modest.ModelChecking.ReachabilityPropertyInfo, System.String, System.String, Modest.StateSpace.StateSet`1<UmbState>, System.IDisposable ByRef, System.Func`3<Boolean,Boolean,Boolean>, System.String, Modest.Modularity.AnalysisDataSet, Modest.Modularity.OperationState, Modest.Modularity.ComponentErrorHandler)
   at Modest.ModelChecking.MAModelChecker`1[[Modest.StateSpace.UnifiedBinaryFormat+UmbState, Modest.StateSpace, Version=3.1.0.0, Culture=neutral, PublicKeyToken=null]].CheckProperties(Modest.StateSpace.StateSpace, Modest.StateSpace.StateSet`1<UmbState>, Boolean[], System.String, Modest.Modularity.OperationState, Modest.Modularity.ComponentErrorHandler)
```



### Log file: modest_from-umb_check_unsafe-memory_cluster.64-2000-20_rep5.log

```
Command(s):
../bin/modest mcsta models/cluster.64-2000-20/modest.model.umb models/cluster.64-2000-20/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.015 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.64-2000-20/modest.model.umb models/cluster.64-2000-20/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.
```

