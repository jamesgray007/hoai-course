# Claude Skill Build Quick Reference

# Skill Build Quick Reference

## The 5-Minute Build

1. **Define it**: Name, purpose, input, output, instructions

2. **Ask Claude to create it**: 
   - Open Claude.ai (new chat)
   - Say: "Help me create a new Agent Skill"
   - Paste your definition
   - Answer Claude's questions
   - Review the generated instructions

3. **Save it**: Follow Claude's guidance

4. **Test it**: Happy path, edge case, real world

5. **Iterate**: Fix what didn't work

Done. Use it.

---

## The Skill Creation Prompt Template

Just paste this into a new Claude chat:
```markdown
Help me create a new Agent Skill.

**Skill Name**: [Action-oriented name]

**Purpose**: [One sentence - what problem it solves]

**When I use this**: [Trigger/frequency]

**Input I provide**: [What you give it each time]

**Output I want**: [What you want to receive]

**Instructions I usually give**:
- [Tone/voice requirements]
- [Format requirements]
- [Must always include]
- [Must never include]
- [Quality standards]
- [Edge case handling]

**Example of perfect output** (optional):
[Paste or describe an ideal result]

Guide me through creating this skill properly.
```

Claude will automatically help you build it. No special commands needed.

---

## Common Skill Patterns

### Meeting Notes → Output
**Process**: Read notes → Extract [X] → Format as [Y]

**Example**: Meeting Notes → Action Items Table

### Research → Brief
**Process**: Analyze sources → Identify themes → Synthesize into [format]

**Example**: Competitor Research → Executive Brief

### Draft → Polish
**Process**: Read draft → Apply style guide → Refine structure → Check quality

**Example**: Rough Email → Professional Message

### Data → Story
**Process**: Analyze numbers → Find insights → Craft narrative → Format for audience

**Example**: Sales Data → Executive Summary

---

## Quality Checklist

Before you save your skill, verify:

- [ ] **Clear process** - Step-by-step instructions
- [ ] **Exact output format** - Show an example
- [ ] **Edge cases covered** - "If X, then Y" rules
- [ ] **Tone/voice defined** - Specific style guidance
- [ ] **Quality criteria** - What makes output "good"
- [ ] **Guardrails** - "Never do X" rules

---

## Pro Tips

**Make the ask natural:**
- ✅ "Help me create a skill that..."
- ✅ "I want to build a skill for..."
- ✅ "Can you help me create an Agent Skill?"

**Don't overthink it:**
- ❌ No need for special syntax or commands
- ❌ No need to tag or mention anything special
- ✅ Just describe what you want naturally

**Test immediately:**
- Always test with real data, not hypotheticals
- Test happy path AND edge cases
- Use it for actual work right away

**Iterate based on usage:**
- v1.0 → test → v1.1 → test
- Never try to make it perfect the first time
- Real usage reveals what needs fixing

---

## Quick Build Example

**User**: "Help me create a skill that turns my messy meeting notes into a clean action items table with owners and deadlines."

**Claude**: [Asks clarifying questions about format, edge cases, tone]

**User**: [Answers questions]

**Claude**: [Generates structured skill instructions]

**User**: [Reviews, saves, tests]

**Total time**: 15 minutes

**Result**: Skill that saves 30+ minutes per week

---

Created by James Gray | [JamesGray.AI](https://jamesgray.ai)