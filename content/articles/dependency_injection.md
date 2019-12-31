Title: Dependency Injection
Date: Mon 28 Oct 16:59:55 CET 2019
Category: Programming
Tags: Programming

> In software engineering, dependency injection is a technique whereby one object supplies the dependencies of another object. A "dependency" is an object that can be used, for example as a service. Instead of a client specifying which service it will use, something tells the client what service to use. The "injection" refers to the passing of a dependency (a service) into the object (a client) that would use it. The service is made part of the client's state.[1] Passing the service to the client, rather than allowing a client to build or find the service, is the fundamental requirement of the pattern.
<br><br>
> Dependency injection is one form of the broader technique of inversion of control. The client delegates the responsibility of providing its dependencies to external code (the injector).

\- from [WiKi](https://en.wikipedia.org/wiki/Dependency_injection)



##Pros:
- loosely coupled code via interface
- increase testability
  - mocking

## Cons:
- increase code complexity
- class hierarchy
    - new factory functions to orchestrates the creation of resources
    - Dependency injection forces complexity to move out of classes and into the
    linkages between classes which might not always be desirable or easily managed
  - harder to understand initially
  - performance

## Via Template parameterization
  - static binding
  - limited flexibility at runtime
  - no interface hierarchy
    - coupled to the implementation
    - not an issue if all implementations are internal

## Via interface (pointer/reference)
  - dynamic binding
  1. constructor injection
  2. setter injection
