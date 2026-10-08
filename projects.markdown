---
layout: page
title: Projects
permalink: /projects/
---

A selection of software and hardware projects. Source code is on
[GitHub](https://github.com/gareths1).

## Software

### The Daily Waddle
A public REST API serving penguin species data, paired with an automated bot
that posts a daily penguin.

- Endpoints for all species, lookup by species, a random penguin, and a
  "penguin of the day" that is the same for everyone on a given date
- [One sentence on the bot, e.g. posts the daily penguin to Discord/Bluesky]
- [One sentence on a challenge you solved, e.g. making the daily pick deterministic by date]

**Tech:** Python, FastAPI, [SQLite/MongoDB] · [Source](https://github.com/gareths1/REPO-NAME)

### Browser History Simulator
A browser history simulator built on custom stack and queue implementations
instead of standard library containers.

- Dynamically allocated linked lists with leak-free memory management
- Unit tests to verify reliability in a Linux environment

**Tech:** C++, Linux

### Library Database
A searchable book database that handles hundreds of books.

- Skew trees and dynamic memory allocation for efficient storage
- Search by title and by content

**Tech:** C++, data structures (skew tree)

### C Shell
A simple command-line shell built in C with custom command parsing and built-in commands.

- Command history and /proc file reading
- Environment variable expansion and quoted arguments
- Process creation using fork() and execvp()

Tech: C, Linux


## Hardware

### Raspberry Pi Stoplight Simulator
A stoplight simulator running on a Raspberry Pi.

- Controlled through GPIO under embedded Linux
- [One or two sentences on what it does, e.g. timing cycles, a pedestrian button]

**Tech:** Raspberry Pi, [Python]

### Pipelined UMBC Power Processor
A pipelined general-purpose processor designed in MATLAB Simulink.

- Built the ALU, register file, 8-bit register, and decoder
- Connected the data path and control logic so the processor correctly runs
  instructions and moves data efficiently

**Tech:** MATLAB Simulink, digital circuit design