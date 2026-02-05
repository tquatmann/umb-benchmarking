# Log files for modest_from-umb_check_unsafe-memory on model [majority.2100](../../models/majority.2100)

Parsed values: `[TO, TO, TO, TO, TO]`



### Log file: modest_from-umb_check_unsafe-memory_majority.2100_rep1.log

```
Command(s):
../bin/modest mcsta models/majority.2100/modest.model.umb models/majority.2100/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.030 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/modest.model.umb models/majority.2100/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.
```



### Log file: modest_from-umb_check_unsafe-memory_majority.2100_rep2.log

```
Command(s):
../bin/modest mcsta models/majority.2100/modest.model.umb models/majority.2100/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.009 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/modest.model.umb models/majority.2100/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.
```



### Log file: modest_from-umb_check_unsafe-memory_majority.2100_rep3.log

```
Command(s):
../bin/modest mcsta models/majority.2100/modest.model.umb models/majority.2100/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.017 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/modest.model.umb models/majority.2100/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.
```



### Log file: modest_from-umb_check_unsafe-memory_majority.2100_rep4.log

```
Command(s):
../bin/modest mcsta models/majority.2100/modest.model.umb models/majority.2100/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.017 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/modest.model.umb models/majority.2100/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.

##############################Output to stderr##############################
Fatal error. System.AccessViolationException: Attempted to read or write protected memory. This is often an indication that other memory is corrupt.
   at Modest.ModelChecking.IntervalIteration.PerformUnboundedIntervalIteration(Modest.ModelChecking.PropertyAnalysisTask, Modest.StateSpace.StateSpace, System.Nullable`1<UInt64>, Modest.Modularity.LocationErrorHandler, System.Threading.CancellationToken, Boolean, Int64 ByRef, Double ByRef)
   at Modest.ModelChecking.UnifPlus.CalculateBound(Modest.ModelChecking.PropertyAnalysisTask, Modest.StateSpace.StateSpace, Double, Double, Boolean, Int32 ByRef, Int32 ByRef, Modest.Modularity.LocationErrorHandler, System.Threading.CancellationToken)
   at Modest.ModelChecking.UnifPlus.CalculateOuterBound(Modest.ModelChecking.PropertyAnalysisTask, Modest.StateSpace.StateSpace, Double, Double, Int32 ByRef, Int32 ByRef, Modest.Modularity.LocationErrorHandler, System.Threading.CancellationToken)
   at Modest.ModelChecking.UnifPlus.Calculate(Modest.ModelChecking.PropertyAnalysisTask, Modest.StateSpace.StateSpace, Modest.Modularity.AnalysisDataSet, System.String, Modest.Modularity.OperationState, Modest.Modularity.LocationErrorHandler)
```



### Log file: modest_from-umb_check_unsafe-memory_majority.2100_rep5.log

```
Command(s):
../bin/modest mcsta models/majority.2100/modest.model.umb models/majority.2100/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.028 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/modest.model.umb models/majority.2100/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.

##############################Output to stderr##############################
Fatal error. System.AccessViolationException: Attempted to read or write protected memory. This is often an indication that other memory is corrupt.
   at Modest.ModelChecking.UnifPlus.CalculateBound(Modest.ModelChecking.PropertyAnalysisTask, Modest.StateSpace.StateSpace, Double, Double, Boolean, Int32 ByRef, Int32 ByRef, Modest.Modularity.LocationErrorHandler, System.Threading.CancellationToken)
   at Modest.ModelChecking.UnifPlus.CalculateOuterBound(Modest.ModelChecking.PropertyAnalysisTask, Modest.StateSpace.StateSpace, Double, Double, Int32 ByRef, Int32 ByRef, Modest.Modularity.LocationErrorHandler, System.Threading.CancellationToken)
   at Modest.ModelChecking.UnifPlus.Calculate(Modest.ModelChecking.PropertyAnalysisTask, Modest.StateSpace.StateSpace, Modest.Modularity.AnalysisDataSet, System.String, Modest.Modularity.OperationState, Modest.Modularity.LocationErrorHandler)
```

