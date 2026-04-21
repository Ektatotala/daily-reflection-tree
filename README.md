# daily-reflection-tree
Deterministic reflection tool using decision tree (DeepThought assignment)
# Daily Reflection Tree

## Overview
This project is a deterministic reflection tool designed to help users analyze their day through a structured decision tree.

It guides users across three psychological dimensions:
1. Locus of Control (internal vs external)
2. Contribution vs Entitlement
3. Self vs Others (radius of concern)

## Features
- Fully deterministic system (no AI at runtime)
- Fixed options for all questions
- Structured branching logic using decision nodes
- Reflection statements based on user path

## Project Structure
/tree/reflection-tree.tsv → main decision tree  
write-up.md → explanation of design  
tree-diagram.png → visual representation  

## How It Works
- User answers predefined questions
- Each answer leads to a specific branch
- Signals track tendencies across axes
- Final summary reflects user's overall pattern

## Constraints Followed
- No randomness
- No free-text input
- No LLM usage at runtime
- Same input always produces same output

## How to Run
cd agent  
python app.py

## Author
Ekta Totala
