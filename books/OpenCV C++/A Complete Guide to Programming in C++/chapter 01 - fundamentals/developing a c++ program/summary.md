**Steps of creating and translating a C++ program:**

1. *Source code* creation and saving to a *source file* using a text editor. Larger projects use *modular programming* (the process of splitting the source code into several source files);
2. The source file(-s) is/are translated using a *compiler*. On success, an object made up of *machine code* is created (it may some times be referred to as a *module*);
3. The *linker* combines the object file with other modules (*standard libraries*, which contain predefined functions that are available for any compiler, or previously compiled objects) to form an *executable file*.


**Further notes:**

- the most common C++ source file extensions are: *.cpp* and *.cc*;
- prior to compilation, *header files* (also referred to as *include files*), which store information needed by source files, such as type definitions, variable and function declarations, can be copied to the source file. Their extension is *.h*;
- modern compilers offer an *Integrated Development Environment* (IDE for short), which combines all of the aformentioned steps into a single task;
- a compiler will report an *error* if a source file contains a *syntax error* and a *warning*, which is intended to draw a persons' attention to a possible mistake in the programs' logic.