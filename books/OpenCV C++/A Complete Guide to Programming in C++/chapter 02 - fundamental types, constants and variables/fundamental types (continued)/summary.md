**Integral types:**

- the *int* (integer) type adapts to the length of a register on the computer (for 16-bit computers, *int* is equivalent to *short*, for 32-bit - to *long*);
- character codes in C++ are treated like regular integers;
- *char* is an integral type with a size of one byte (size is from -127 to 128 or from 0 to 255 (depending on whether it is signed or unsigned));
- *wchar_t* is an integral type, which is normally defined as *unsigned short*.

**The *signed* and *unsigned* modifiers:**

- *short*, *int*, and *long* types are normally interpreted as signed, with the highest bit representing the sign;
- unsigned types no longer require the highest bit to be the sign, thus the value of ranges change.

**Floating-point types:**
- numbers with a fraction part are indicated by a decimal point in C++ and are referred to as floating-point numbers;
- floating-points numbers have a preset accuracy:
    - *float* - lowest accuracy;
    - *double* - higher accuracy;
    - *long double* - highest accuracy.

**The *sizeof* operator:**
- yields the size of an object in bytes.