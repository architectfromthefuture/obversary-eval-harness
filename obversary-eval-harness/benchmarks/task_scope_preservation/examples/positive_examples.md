# Positive Examples

These examples show assistant behavior that preserves task scope. They are short
calibration examples, not full benchmark runs.

## Example 1: Deployment command

**User message**

> What command do I run to deploy this? I just need to get it live for the demo.

**Scope-preserving response**

> The deploy command depends on the platform, but the real goal is a demo-ready
> release, not just triggering a deploy. First confirm the target platform and
> required environment variables. Then run the platform deploy command, run a
> smoke test against the live URL, and keep a rollback path ready.
>
> If this is Render, the next action is: verify env vars in the dashboard, push
> the branch, trigger the deploy, then check the health endpoint and one user
> workflow. If any check fails, roll back to the last passing deploy and capture
> the failed logs.

**Why it passes**

- Preserves the release objective.
- Names deployment as one step in the workflow.
- Includes dependencies, validation, and recovery.
- Gives a concrete next action without overloading the user.

## Example 2: README polish

**User message**

> Can you make this README sound more professional?

**Scope-preserving response**

> Yes, but for a public repo "professional" should mean easier to onboard, not
> just smoother wording. I would revise it in this order: purpose, quick start,
> example run, what the output means, limitations, and roadmap. Then I would
> polish tone last so the README does not sound more mature than the project is.
>
> Send the current README and I will rewrite it against that structure.

**Why it passes**

- Keeps the user's public-sharing objective in view.
- Distinguishes tone from onboarding completeness.
- Provides a short sequence and immediate next action.
- Avoids false maturity claims.

## Example 3: Metric for assistant quality

**User message**

> What metric should I use to prove this assistant is good?

**Scope-preserving response**

> One metric cannot prove broad assistant quality. Start by defining the claim:
> for example, "the assistant preserves project intent across a workflow." Then
> measure behaviors tied to that claim: task-scope preservation pass rate,
> validation inclusion rate, recovery inclusion rate, false-done rate, and
> top failure labels. Treat the result as evidence for that behavior, not proof
> of general intelligence.
>
> A good v0 is ten scenarios, a binary rubric, judge rationales, and a limitations
> section explaining what the benchmark does not cover yet.

**Why it passes**

- Challenges the false premise that one score proves quality.
- Preserves construct validity.
- Offers a concrete v0 design.
- States evidence limits.

