Task-Scope Preservation Benchmark

This evaluates whether an AI assistant can preserve the user’s larger project objective instead of collapsing into one narrow answer. Your uploaded draft already has the core structure: construct definition, scenario details, user contexts, user messages, judge prompt, positive examples, negative examples, and an Open Benchmark submission draft.

That maps well to the Open Benchmark project because their stated focus is measuring AI’s impact on human well-being across physical, psychological, and societal dimensions, not just raw model capability.

The human-impact angle is strong:

Bad AI planning increases cognitive load, user dependence, false confidence, and unfinished work.
Good AI planning preserves autonomy, competence, recovery, and task completion.

Very much your lane. Annoyingly coherent, even.

Build direction

We should not start with “low-latency benchmark” as the first submission.

That idea matters, but for the submission, the cleanest first construct is:

Task-Scope Preservation

Then we add latency as a sub-dimension:

Latency-aware task preservation

Meaning:

Can the assistant give the user the shortest useful path to forward motion without duct-taping one shallow answer onto a complex project?

In your language:

Not just answering.
Not just planning forever.
Actually organizing the task so the user can move without spiraling.

That connects your themes:

Your theme	Benchmark expression
Failure as priority	Does the model notice workflow failure before it happens?
Memory substrates	Does the model preserve prior task context and dependencies?
Low latency / zero-latency	Does the model reduce friction and produce constrained next actions?
No duct tape	Does the model build a staged workflow instead of patching one visible issue?
Cognitive systems	Does the assistant preserve the loop: goal → plan → action → evaluation → update?
