## Access Ability
Public
Private


### note
1. signature should be same during development in case many users call this method
2. start with lower visibility i.e other many call your public attribute and method

## inheritance, interface, Abstract Class
Base case --> Derived Class

```cpp
public interface Employee{
    // no instance level data fields
    // more like a plan here what is going to define
    
    // method implementation
    public int calculateSalay(double performanceScore); 
    
    
}
```

```cpp
public abstract Employee{
    // will come with some data and implementation
}
```


interface vs. abstract class

1. abstract provide a common base class implementation to derived classes
2. interface helps you to focus on the API signature definition


