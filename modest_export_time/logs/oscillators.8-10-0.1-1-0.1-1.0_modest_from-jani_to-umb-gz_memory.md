# Log files for modest_from-jani_to-umb-gz_memory on model [oscillators.8-10-0.1-1-0.1-1.0](../../models/oscillators.8-10-0.1-1-0.1-1.0)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: modest_from-jani_to-umb-gz_memory_oscillators.8-10-0.1-1-0.1-1.0_rep1.log

```
Command(s):
../bin/modest mcsta models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/model.umb.gz out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/umbgz.properties.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 41.179 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/model.umb.gz out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/umbgz.properties.txt --umb-compress GZIP -S Memory -D --exhaustive




model.jani:model: info: model is a DTMC model.

##############################Output to stderr##############################
Unhandled exception. System.Runtime.InteropServices.COMException (0x80131198): No logical space left to create more user strings. (0x80131198)
   at System.Reflection.Emit.RuntimeModuleBuilder.<GetStringConstant>g____PInvoke|26_0(QCallModule __module_native, UInt16* __str_native, Int32 __length_native)
   at System.Reflection.Emit.RuntimeModuleBuilder.<GetStringConstant>g____PInvoke|26_0(QCallModule __module_native, UInt16* __str_native, Int32 __length_native)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_3.<CreateJump>b__4(Int32 assignmentIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_2.<CreateJump>b__3(Int32 targetIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_1.<CreateJump>b__2(Int32 edgeIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_0.<CreateJump>b__1(Int32 locationIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.CreateJump(TypeBuilder tb)
   at Modest.Exploration.Compiled.CompiledAutomaton.Compile(Dictionary`2 edgeLabelMapping)
   at Modest.Exploration.Compiled.NetworkCompiler.CompileNetwork(NetworkCompilationState compilationState, Expression[] expressions, Expression[] timeConstraints)
   at Modest.Exploration.NetworkCompilerHelper.Compile(AutomataNetwork automataNetwork, ExplorationConfiguration config, Expression[] expressions, Expression[] timeConstraints, Dictionary`2 clockBounds, HashSet`1 extraSymbolicVariables, StateProjection[] projections, OperationState operationState, String extraStatusString)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)

############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/model.umb.gz:	File does not exist.
out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/umbgz.properties.txt:	File does not exist.
```



### Log file: modest_from-jani_to-umb-gz_memory_oscillators.8-10-0.1-1-0.1-1.0_rep2.log

```
Command(s):
../bin/modest mcsta models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep2.gz out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/umbgz.properties_rep2.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 40.349 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep2.gz out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/umbgz.properties_rep2.txt --umb-compress GZIP -S Memory -D --exhaustive




model.jani:model: info: model is a DTMC model.

##############################Output to stderr##############################
Unhandled exception. System.Runtime.InteropServices.COMException (0x80131198): No logical space left to create more user strings. (0x80131198)
   at System.Reflection.Emit.RuntimeModuleBuilder.<GetStringConstant>g____PInvoke|26_0(QCallModule __module_native, UInt16* __str_native, Int32 __length_native)
   at System.Reflection.Emit.RuntimeModuleBuilder.<GetStringConstant>g____PInvoke|26_0(QCallModule __module_native, UInt16* __str_native, Int32 __length_native)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_3.<CreateJump>b__4(Int32 assignmentIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_2.<CreateJump>b__3(Int32 targetIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_1.<CreateJump>b__2(Int32 edgeIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_0.<CreateJump>b__1(Int32 locationIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.CreateJump(TypeBuilder tb)
   at Modest.Exploration.Compiled.CompiledAutomaton.Compile(Dictionary`2 edgeLabelMapping)
   at Modest.Exploration.Compiled.NetworkCompiler.CompileNetwork(NetworkCompilationState compilationState, Expression[] expressions, Expression[] timeConstraints)
   at Modest.Exploration.NetworkCompilerHelper.Compile(AutomataNetwork automataNetwork, ExplorationConfiguration config, Expression[] expressions, Expression[] timeConstraints, Dictionary`2 clockBounds, HashSet`1 extraSymbolicVariables, StateProjection[] projections, OperationState operationState, String extraStatusString)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)

############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep2.gz:	File does not exist.
out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/umbgz.properties_rep2.txt:	File does not exist.
```



### Log file: modest_from-jani_to-umb-gz_memory_oscillators.8-10-0.1-1-0.1-1.0_rep3.log

```
Command(s):
../bin/modest mcsta models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep3.gz out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/umbgz.properties_rep3.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 48.196 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep3.gz out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/umbgz.properties_rep3.txt --umb-compress GZIP -S Memory -D --exhaustive




model.jani:model: info: model is a DTMC model.

##############################Output to stderr##############################
Unhandled exception. System.Runtime.InteropServices.COMException (0x80131198): No logical space left to create more user strings. (0x80131198)
   at System.Reflection.Emit.RuntimeModuleBuilder.<GetStringConstant>g____PInvoke|26_0(QCallModule __module_native, UInt16* __str_native, Int32 __length_native)
   at System.Reflection.Emit.RuntimeModuleBuilder.<GetStringConstant>g____PInvoke|26_0(QCallModule __module_native, UInt16* __str_native, Int32 __length_native)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_3.<CreateJump>b__4(Int32 assignmentIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_2.<CreateJump>b__3(Int32 targetIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_1.<CreateJump>b__2(Int32 edgeIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_0.<CreateJump>b__1(Int32 locationIndex)
   at Modest.Exploration.Compiled.CompiledAutomaton.CreateJump(TypeBuilder tb)
   at Modest.Exploration.Compiled.CompiledAutomaton.Compile(Dictionary`2 edgeLabelMapping)
   at Modest.Exploration.Compiled.NetworkCompiler.CompileNetwork(NetworkCompilationState compilationState, Expression[] expressions, Expression[] timeConstraints)
   at Modest.Exploration.NetworkCompilerHelper.Compile(AutomataNetwork automataNetwork, ExplorationConfiguration config, Expression[] expressions, Expression[] timeConstraints, Dictionary`2 clockBounds, HashSet`1 extraSymbolicVariables, StateProjection[] projections, OperationState operationState, String extraStatusString)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)

############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep3.gz:	File does not exist.
out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/umbgz.properties_rep3.txt:	File does not exist.
```



### Log file: modest_from-jani_to-umb-gz_memory_oscillators.8-10-0.1-1-0.1-1.0_rep4.log

```
Command(s):
../bin/modest mcsta models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep4.gz out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/umbgz.properties_rep4.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 43.810 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep4.gz out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/umbgz.properties_rep4.txt --umb-compress GZIP -S Memory -D --exhaustive




model.jani:model: info: model is a DTMC model.

##############################Output to stderr##############################
Unhandled exception. System.Runtime.InteropServices.COMException (0x80131198): No logical space left to create more user strings. (0x80131198)
   at System.Reflection.Emit.RuntimeModuleBuilder.<GetStringConstant>g____PInvoke|26_0(QCallModule __module_native, UInt16* __str_native, Int32 __length_native)
   at System.Reflection.Emit.RuntimeModuleBuilder.<GetStringConstant>g____PInvoke|26_0(QCallModule __module_native, UInt16* __str_native, Int32 __length_native)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_3.<CreateJump>b__4(Int32 assignmentIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_2.<CreateJump>b__3(Int32 targetIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_1.<CreateJump>b__2(Int32 edgeIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_0.<CreateJump>b__1(Int32 locationIndex)
   at Modest.Exploration.Compiled.CompiledAutomaton.CreateJump(TypeBuilder tb)
   at Modest.Exploration.Compiled.CompiledAutomaton.Compile(Dictionary`2 edgeLabelMapping)
   at Modest.Exploration.Compiled.NetworkCompiler.CompileNetwork(NetworkCompilationState compilationState, Expression[] expressions, Expression[] timeConstraints)
   at Modest.Exploration.NetworkCompilerHelper.Compile(AutomataNetwork automataNetwork, ExplorationConfiguration config, Expression[] expressions, Expression[] timeConstraints, Dictionary`2 clockBounds, HashSet`1 extraSymbolicVariables, StateProjection[] projections, OperationState operationState, String extraStatusString)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)

############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep4.gz:	File does not exist.
out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/umbgz.properties_rep4.txt:	File does not exist.
```



### Log file: modest_from-jani_to-umb-gz_memory_oscillators.8-10-0.1-1-0.1-1.0_rep5.log

```
Command(s):
../bin/modest mcsta models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep5.gz out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/umbgz.properties_rep5.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 41.307 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep5.gz out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/umbgz.properties_rep5.txt --umb-compress GZIP -S Memory -D --exhaustive




model.jani:model: info: model is a DTMC model.

##############################Output to stderr##############################
Unhandled exception. System.Runtime.InteropServices.COMException (0x80131198): No logical space left to create more user strings. (0x80131198)
   at System.Reflection.Emit.RuntimeModuleBuilder.<GetStringConstant>g____PInvoke|26_0(QCallModule __module_native, UInt16* __str_native, Int32 __length_native)
   at System.Reflection.Emit.RuntimeModuleBuilder.<GetStringConstant>g____PInvoke|26_0(QCallModule __module_native, UInt16* __str_native, Int32 __length_native)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_3.<CreateJump>b__4(Int32 assignmentIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_2.<CreateJump>b__3(Int32 targetIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_1.<CreateJump>b__2(Int32 edgeIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_0.<CreateJump>b__1(Int32 locationIndex)
   at Modest.Exploration.Compiled.CompiledAutomaton.CreateJump(TypeBuilder tb)
   at Modest.Exploration.Compiled.CompiledAutomaton.Compile(Dictionary`2 edgeLabelMapping)
   at Modest.Exploration.Compiled.NetworkCompiler.CompileNetwork(NetworkCompilationState compilationState, Expression[] expressions, Expression[] timeConstraints)
   at Modest.Exploration.NetworkCompilerHelper.Compile(AutomataNetwork automataNetwork, ExplorationConfiguration config, Expression[] expressions, Expression[] timeConstraints, Dictionary`2 clockBounds, HashSet`1 extraSymbolicVariables, StateProjection[] projections, OperationState operationState, String extraStatusString)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)

############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/model.umb_rep5.gz:	File does not exist.
out/modest_from-jani_to-umb-gz_memory/oscillators.8-10-0.1-1-0.1-1.0/umbgz.properties_rep5.txt:	File does not exist.
```

