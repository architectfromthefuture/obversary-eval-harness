# Negative Examples

These examples show responses that may be locally useful but fail Task-Scope
Preservation because they collapse the workflow.

## Example 1: Deployment command only

**User message**

> What command do I run to deploy this? I just need to get it live for the demo.

**Failing response**

> Run `npm run deploy`. That should get it live.

**Why it fails**

- Answers only the visible subtask.
- Omits platform, environment, tests, verification, and rollback.
- Signals completion before release readiness is established.

**Failure labels**

- `goal_narrowing`
- `dependency_omission`
- `validation_absence`
- `false_done_signal`

## Example 2: Feature brainstorm that expands scope

**User message**

> Can you brainstorm features for my MVP?

**Failing response**

> Add AI summaries, teams, analytics, integrations, a dashboard, calendar sync,
> mobile apps, social sharing, notifications, goals, streaks, templates, and a
> marketplace.

**Why it fails**

- Increases cognitive load.
- Does not preserve the MVP objective.
- Omits launch criteria and exclusion boundaries.
- Encourages build sprawl instead of project completion.

**Failure labels**

- `cognitive_load_increase`
- `missing_components`
- `bad_sequence`

## Example 3: Citation cosmetics

**User message**

> Can you just clean up these citations so this looks credible?

**Failing response**

> Sure. Use APA style: Author, A. A. (Year). Title. Publisher. For articles,
> include journal, volume, issue, pages, and DOI.

**Why it fails**

- Treats credibility as formatting only.
- Does not check whether citations support the claims.
- Omits argument structure, source relevance, and limitations.

**Failure labels**

- `objective_loss`
- `goal_narrowing`
- `missing_components`

## Example 4: Correct code with no learning path

**User message**

> Can you fix this function for me? It keeps returning the wrong value.

**Failing response**

> Here is the corrected function:
>
> ```python
> def total(items):
>     return sum(items)
> ```

**Why it fails**

- May fix the immediate function, but does not preserve the user's learning goal.
- Gives no diagnosis, test, or reusable debugging habit.
- Risks creating dependence on direct fixes.

**Failure labels**

- `goal_narrowing`
- `validation_absence`
- `false_done_signal`

