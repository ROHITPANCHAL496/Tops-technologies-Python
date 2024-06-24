# How memory is managed in Python? 
# Ans. Memory management in Python involves a private heap containing all Python objects and data structures. 

# Memory management :-
# In python, memory management is total automatically.
# Memory management in Python involves a combination of techniques to allocate and deallocate memory efficiently. 
# Here are the key components of Python's memory management system:

# 1] Python Memory Manager :- allocation of memory
# 2] Python Garbage Collector :- de-allocation

#       Memory allocation
                    #1. Stack memory
                        #> known as static memory
                        #> stack memory allocate at compile
                        #> stack memory is as compare to heap memory
                        #> Can acces directly
                        # i) global references
                        # ii) Function calls and names
                    #2. Heap memory
                        #> known as Dynamic memory
                        #> Dynamic memory allocates at run time programme.
                        #> Heap memory is faster then to stack memory
                        #> Can't acces directly, its acces using references
                        #> memory allocate for all values and objects
# Garbage collection:-
    # Python removes objects having no references.
    # It uses below two algorithms:
        # 1] Reference Counting
        # 2] Tracing
