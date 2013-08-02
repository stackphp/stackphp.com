---
layout: spec
title: STACK-2 Authentication
status: draft
---

This document proposes conventions for authentication middlewares to follow in
order for applications and authorization middlewares to be able to interact
with each other.

 * Name: {{ page.title }}
 * Editor: Beau Simensen <[beau@dflydev.com](mailto:beau@dflydev.com)>


### Language

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [RFC 2119](http://www.ietf.org/rfc/rfc2119.txt).


### Goals

 * To allow authentication middlewares to communicate when a request has been
   authenticated.
 * To allow other middlewares or applications to communicate whether or not
   the authentication was accepted (for example, authorization failed or is
   required).
 * To allow for some coexistence between multiple Stack authentiation
   middlewares for the same request.


### Stack Authentication Middlewares

#### Token

A Stack authentication token represents the user or service driving the user
agent making a request. The token MUST be stored as the `stack.authn.token`
request attribute. The token MUST either be a string or serializable.


#### Authentication

A Stack authentication middleware is free to use whatever means necessary to
authenticate a request. The end result of a successfully authenticated request
should be that the `stack.authn.token` attribute on the request is set to a
valid token.

If a request has authentication credentials that are invalid for any reason a
Stack authentication middleware MAY either immediately challenge or return
another reaponse (for example, a 400 error response).

If a request already has the `stack.authn.token` attribute set a Stack
authentication middleware MUST NOT attempt to further authenticate the request.
However, the Stack authentication middleware MAY act further upon inspecting
the response.


#### Integration with Stack Authorization

Stack authentication middlewares SHOULD inspect the response from the wrapped
app to see if it has a status code of `401` and a `WWW-Authenticate: Stack`
header. In this case, the Stack authentication middleware can use its own best
judgement to determine whether or not it should issue a challenge.

Modifying or replacing the response is allowed but a Stack authentication
middleware MUST NOT challenge unless the response is in this state. If a Stack
authentication middleware does not change the `WWW-Authenticate` value other
Stack authentication middlewares will be given an opportunity to challenge.


### Implementations

 * [dflydev/stack-authentication](https://github.com/dflydev/dflydev-stack-authentication)
   A collection of middlewares designed to help authentication middleware
   implementors adhere to the STACK-2 Authentication conventions.
 * [dflydev/stack-hawk](https://github.com/dflydev/dflydev-stack-hawk)
   [Hawk](https://github.com/hueniverse/hawk) authentication middleware.
 * [dflydev/stack-basic-authentication](https://github.com/dflydev/dflydev-stack-basic-authentication)
   HTTP Basic Authentication middleware.
