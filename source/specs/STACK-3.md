---
layout: spec
title: STACK-3 Authorization
status: draft
---

This document proposes conventions for authorization middlewares to follow in
order for applications and authentication middlewares to be able to interact
with each other.

 * Name: {{ page.title }}
 * Editor: Beau Simensen <[beau@dflydev.com](mailto:beau@dflydev.com)>


### Language

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [RFC 2119](http://www.ietf.org/rfc/rfc2119.txt).


### Goals

 * To instruct authorization middlewares on how to determine if a request has
   been authenticated by a Stack authentication middleware.
 * To instruct authorization middlewares on how to respond in the event that
   authorization fails when a request is authenticated.
 * To instruct authorization middlewares on how to respond in the event that
   authorization fails when a request is not authenticated.


### Stack Authorization Middlewares and Applications

Authorization MUST be based on the token stored in the `stack.authn.token`
request attribute.

If a token exists but the request is not authorized, a Stack authorization
middleware MUST return a `403` response.

If a token does not exist, a Stack authorization middleware SHOULD return a
`401` response with a `WWW-Authenticate: Stack` header. This will give the
appropriate Stack authentication middlewares an opportunity to challenge as
appropriate.


### Implementations

 * None
