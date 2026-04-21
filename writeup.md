# Daily Reflection Tree – Write-up

## Objective
The goal of this project is to design a deterministic reflection system that helps users evaluate their day across three psychological dimensions: control (locus), contribution, and perspective (radius).

## Question Design
The questions were designed to be simple and relatable for a user at the end of the day. Each question offers fixed options to eliminate ambiguity and ensure determinism.

Each axis includes:
- A classification question (to identify user tendency)
- A follow-up question (to deepen reflection)

## Branching Logic
The system uses decision nodes to route users based on their selected answers.

- No randomness is used
- Same answers always lead to the same path
- Signals track user tendencies across axes

Signals used:
- Axis 1: Internal vs External control
- Axis 2: Contribution vs Entitlement
- Axis 3: Self vs Others focus

## Psychological Foundations
The tree is based on:
- Locus of Control (Julian Rotter)
- Growth Mindset (Carol Dweck)
- Contribution vs Entitlement concepts
- Self-transcendence (Maslow)

## Design Choices
- Fixed options instead of free text for clarity
- Non-judgmental reflection tone
- Smooth transitions between axes using bridge nodes

## Limitations
- Limited depth due to predefined options
- No personalization
- Cannot capture complex emotions fully

## Future Improvements
- Add more branches for edge cases
- Include weighted scoring system
- Build an interactive UI for better usability
