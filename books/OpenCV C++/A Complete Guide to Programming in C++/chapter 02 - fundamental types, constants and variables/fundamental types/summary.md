**The type of data defines:**
- the internal representation of data;
- the amount of memory to allocate.

**A *boolean* value:**
- is a result of a comparison or a logical association using AND or OR;
- can be of true (1 as a numerical value) or false (0 as a numerical value) value.

***char* and *wchar_t*:**
- are used to store *character codes* (integers associated with characters (A = 65)):
    - a *character set* defines which code represents a certain character.
- *wchar_t* comprises at least 2 bytes, which allows it to store modern Unicode (a 16-bit code used in Windows NT, which contains codes for approximately 35,000 characters in 24 languages) characters.

In general, C++ uses a character set which contains the *ASCII (American Standard Code for Information Interchange) code* (a 7-bit code which defines 32 control and 96 printable characters.