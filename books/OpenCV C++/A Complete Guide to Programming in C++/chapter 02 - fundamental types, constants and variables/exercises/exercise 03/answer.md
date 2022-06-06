**Invalid/Nonsensical variable definitions:**
- *int a(2.5);*                 - the value of the variable *a* would be "ceiled" (lose its' decimal point).
- *int b = '?';*                - if ASCII is taken into account, the definition is sensical, otherwise - not (if the programmer does not know the value of '?').
- *char z(500);*                - no such character exists (exceeds the ASCII table);
- *double he's(1.2E+5);*        - invalid name (cannot contain quotes);
- *unsigned size(40000);*       - no data type specified;
- *float val = 12345.12345;*    - exceeds *float*s' (6) accuracy.