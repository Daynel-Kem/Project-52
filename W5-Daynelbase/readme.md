custom database for storing stuff  
idk whats involved in making it yet but it sounds like a mighty neat project  
  
Ill reference the build-your-own-x github for it  
[github](https://github.com/codecrafters-io/build-your-own-x)  
  
  
Small excerpt from [this page](https://charlesleifer.com/blog/building-a-simple-redis-server-with-python/)  

>The server we'll be building will be able to respond to the following commands:  

    GET <key>  
    SET <key> <value>  
    DELETE <key>  
    FLUSH  
    MGET <key1> ... <keyn>  
    MSET <key1> <value1> ... <keyn> <valuen>  

>We'll support the following data-types as well:  

    Strings and Binary Data  
    Numbers  
    NULL  
    Arrays (which may be nested)  
    Dictionaries (which may be nested)  
    Error messages  
