**Structure of a C++ program:**

- made up of objects with their accompanying *member functions* and *global functions*, which do not belong to any single particular class:
    - each function fulfills its' own tasks and can call other functions;
- the entry point is the *main()* function.


**Description of the *structure-of-the-main-function.png* file:**
- the first line starts with a hash symbol (*#*), which indicates that the line is intended for the *preprocessor*;
- following is the keyword *include <iostream>* (*iostream* - header file, which comprises the convention of the input/output streams (flows) of data), which indicates that the preprocessor should copy the quoted (*<>*) file to this position in the source code;
- *using namespace std;* - predefined names in C++ are found in the *std* (standard) *namespace*. *using* allows direct access to the names in the namespace;
- program execution begins with the first instruction within the *main()* function (in our case, this function contains two *statements*);
- the first statement: *cout << "Enjoy yourself with C++!" << endl;* - outputs *Enjoy yourself with C++!* on screen:
    - *cout* (console output) - designates an object responsible for output;
    - *<<* - indicate that characters are to be "pushed" to the output stream;
    - *endl* (end of line) - causes a line feed.
- the second statement: *return 0;*: terminates the *main()* function and returns an exit code of *0* (it is common practice to return *0* on successful program termination).