# AN ASTERISK BASED VOIP GATEWAY SUPPORTING MFC-R2 PROTOCOL ON CENTOS 6

**By Reinaldo Martínez P.**

**Caracas, Venezuela:**

**TigerLinux AT gmail DOT com**


## Introduction

Before we start this recipe I want to say something: I REALLY REALLY HATE MFCR2 Telephony Protocol and I REALLY REALLY HATE every and each telephony provider still using it. Having say that, I want to state my motivation on documenting this recipe: I have been many years of my technical career working with asterisk in my country (Venezuela) and the providers here uses this long-forgotten and very obsoleted protocol. That means, we **NEED** to support this on Asterisk if we want asterisk to really work in Venezuela (and other countries still using R2).

In the moment I'm writing this recipe, I'm working for a call-center services company with all their services in OpenStack based cloud's (I'm the cloud arquitech by the way) and all VoIP systems we currently have are asterisk-based. Not all of them are in the cloud: The gateways are the exception.

Our gateways are, of course, Asterisk based. First we used to have very modified Elastix-based gateways, but then we decided to make our own "asterisk-recipe" based on Centos 6.

Why our gateways are not virtual ??.. Because the VoIP cards !. It is impractical to include in an OpenStack compute server a VoIP card, so, we need to create bare-metal based gateways !.

The recipe is using OpenSource software. Nothing here is licensed so you can replicate this recipe (and adapt it) to whatever environment you have, even if you are not using MFCR2.


## What kind of hardware and software you need ?.

This is aimed to production, so I pass the "testing" recomendations: You need a bare metal !. A physical server. Also you need a telephony card, fully compatible with asterisk/dahdi and with Centos 6 support. Why don't we use Centos 7 ??.. You can: But I recommend to keep Centos 6 as first option. Not all drivers are still fully tested on C-7.

About the software: You'll need a machine with the following software requeriments:

* Centos 6 (32 or 64) fully updated.
* EPEL Repository installed. For EPEL install instruction see: https://fedoraproject.org/wiki/EPEL.


## What knowledge should you need to have at hand ?:

* General Linux administration.
* Asterisk Knowledge.
* VoIP and Telephony concepts.


## What files you'll find here ?:

* [RECIPE-gateway-asterisk-R2-Centos6.md: Our recipe, in markdown format.](https://github.com/tigerlinux/tigerlinux.github.io/blob/master/recipes/asterisk/mfcr2-asterisk-gateway/RECIPE-gateway-asterisk-R2-Centos6.md "Our Asterisk R2 VoIP Gateway Recipe")

