Boundary Mapping for Task-Scope Preservation

The umbrella thesis:

Models do not only fail by answering incorrectly. They fail by losing the user’s objective at specific boundaries in the workflow.

That sentence is sharp. Use it.

What to build first

Do not try to implement a full Petri clone. That would be how we summon suffering from the dependency graph.

Build this order:

Phase A: Static v0

Already planned:

README
rubric
8 prompts
judge prompt
positive/negative examples
submission draft
portfolio note
Phase B: Behavioral eval design

Add:

behavior.md
methodology.md
failure_taxonomy.md
scenario_generator_prompt.md
graded_behavior_judge.md
result_schema.example.json
petri_bloom_comparison.md
Phase C: Simple generated scenarios

Use an LLM manually or via script to generate 20 scenario candidates.

Then manually select 10.

Do not automate everything yet.

Phase D: Execution harness

Run models against the scenarios.

Save:

prompt
response
judge score
failure labels
rationale
metadata
Phase E: Report

Generate:

collapse rate
mean preservation score
top failure modes
examples
limitations

Now you have a real eval artifact.

The clean public framing

For your website / docs:

Task-Scope Preservation is a behavioral benchmark for evaluating whether AI assistants preserve a user's project-level objective across a constrained workflow.

Unlike correctness-only benchmarks, TSP focuses on workflow collapse: cases where a model gives a plausible answer to one visible subtask while omitting the structure needed for the user to complete the real project.

The benchmark is designed around graded behavioral assessment, scenario generation, failure taxonomy, transcript review, and suite-level reporting.

That connects directly to your Obversary thesis:

memory, mistakes, and judgment should be observable

TSP makes task loss observable.

That’s the bridge. Not decorative. Actually structural. 🧠

