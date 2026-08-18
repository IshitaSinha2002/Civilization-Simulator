# Civilization Simulator

An AI-powered Civilization Simulator built using LangChain and LangGraph, where a user-defined civilization evolves over time through simulated economic, social, technological, and historical events.

## Overview

Civilization Simulator models the long-term development of a civilization using a combination of deterministic simulation logic and LLM-based reasoning.

The user provides a description of a civilization and specifies how many years it should be simulated. The system generates an initial civilization state and then repeatedly advances the civilization through time.

During each simulation cycle:

1. The civilization's numerical state is updated.
2. The LLM evaluates the current conditions and generates a plausible historical event.
3. The LLM determines the consequences of that event.
4. The consequences are applied to the civilization state.
5. LangGraph determines whether the simulation should continue or end.

## Architecture

```text
Civilization Description
          ↓
   Initial State Generation
          ↓
    Civilization State
          ↓
┌───────────────────────────┐
│       LangGraph Loop      │
│                           │
│     Simulate Year         │
│          ↓                │
│     Generate Event        │
│          ↓                │
│  Apply Consequences       │
│          ↓                │
│   Check Simulation        │
│       ↙       ↘           │
│  Continue      End        │
│      │                      │
│      └──────→ Next Year    │
└───────────────────────────┘
          ↓
     Final Civilization
```

## Key Features

* Dynamic civilization creation from natural-language descriptions
* Long-term stateful civilization simulation
* LLM-generated historical events
* LLM-based event consequence generation
* Deterministic numerical state updates
* LangGraph conditional simulation loop
* Structured LLM outputs using Pydantic
* Configurable simulation duration
* Terminal-based execution

## Tech Stack

* Python
* LangChain
* LangGraph
* Groq
* GPT-OSS 120B
* Pydantic
* python-dotenv

## Project Structure

```text
civilization-simulator/
│
├── graph/
│   ├── __init__.py
│   ├── state.py
│   ├── nodes.py
│   └── workflow.py
│
├── simulation/
│   ├── __init__.py
│   └── civilization.py
│
├── llm/
│   ├── __init__.py
│   ├── prompts.py
│   └── chains.py
│
├── main.py
├── config.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Simulation State

The civilization maintains a shared state containing attributes such as:

* Civilization name
* Population
* Food
* Wealth
* Stability
* Military strength
* Technology level
* Infrastructure
* Current event
* Event history
* Current simulation year
* Simulation status

## Example Input

```text
Describe your civilization:

A civilization developed around a large river. It relies heavily
on agriculture, has recently discovered metalworking, and has
several neighboring tribes.

How many years should the civilization be simulated?

100
```

The LLM dynamically generates an appropriate starting state rather than relying on predefined civilization values.

## Design Philosophy

The project follows a hybrid simulation approach.

### LLM

The LLM is responsible for reasoning-heavy tasks such as:

* Creating the initial civilization state
* Generating historical events
* Determining plausible event consequences

### Python

Python handles deterministic simulation logic such as:

* Population changes
* Resource consumption
* Economic calculations
* State boundaries
* Simulation conditions

### LangGraph

LangGraph orchestrates the complete simulation:

* Maintains shared civilization state
* Executes simulation nodes
* Controls the simulation loop
* Routes between continuation and termination

This separation allows the project to combine **LLM reasoning with deterministic simulation mechanics**.

## Running the Project

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Run the simulator:

```bash
python main.py
```

## Project Goal

The goal of Civilization Simulator is to demonstrate how **LangGraph can be used to build stateful, long-running simulation systems**, where an evolving environment is repeatedly evaluated, modified, and fed back into the next simulation cycle.
