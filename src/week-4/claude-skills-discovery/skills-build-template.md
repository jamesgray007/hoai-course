# Claud Agent Skill Build Template

Use this template to build any Agent Skill. Follow the steps in order.

---

## STEP 1: Define Your Skill (5 minutes)

Before you open Claude, answer these questions:

### Basic Info

**Skill Name** (action-oriented, clear):


**One-sentence description** (what problem does this solve?):


**Who is this for?** (just me, my team, specific role):


---

### The Use Case

**When do I use this?** (trigger/frequency):  
Example: "Every Monday morning" or "Before client meetings" or "Whenever I get meeting notes"


**What's my input?** (what do I provide each time):  
Example: "Meeting transcript", "List of competitors", "Draft email"


**What's my desired output?** (what do I want to receive):  
Example: "Markdown table of action items", "3-paragraph executive brief", "Formatted LinkedIn post"


**What does success look like?** (how do I know it worked):  
Example: "I can copy-paste directly into Slack with zero edits"


---

### The Context (this is the magic)

**What instructions do I give repeatedly?**  
List everything you usually have to explain:

- Tone/voice:

- Format requirements:

- Must always include:

- Must never include:

- Quality standards:


**Example to show Claude** (optional but helpful):  
Paste or describe a "perfect" output:




---

## STEP 2: Build Your Skill (15 minutes)

Go to Claude.ai → Start a new chat

Paste this prompt (Claude will automatically guide you through skill creation):
```markdown
Help me create a new Agent Skill.

**Skill Name**: [Copy from Step 1]

**Purpose**: [Copy from Step 1]

**When I use this**: [Copy from Step 1]

**Input I provide**: [Copy from Step 1]

**Output I want**: [Copy from Step 1]

**Instructions I usually give**:
[Paste your "What instructions do I give repeatedly" section from Step 1]

**Example of perfect output** (if you have one):
[Paste your example]

Guide me through creating this skill with proper structure, format requirements, 
edge case handling, and quality criteria.
```

### What to Expect

**Claude will help you:**
- ✅ Structure your instructions properly
- ✅ Identify edge cases you might have missed
- ✅ Format requirements clearly
- ✅ Add quality criteria
- ✅ Choose appropriate tools (if needed)

**You'll answer questions like:**
- "What should happen if [edge case]?"
- "How should I handle ambiguous input?"
- "What tone/voice should the output have?"
- "Are there any constraints or rules?"

**The result:**  
Well-structured skill instructions that handle edge cases and produce consistent output.

### Save Your Skill

Follow Claude's guidance to finalize and save your skill:
1. Review the generated instructions
2. Confirm the skill name and description
3. Select any tools needed (read/write files, search, calendar)
4. Save and prepare to test

---

## STEP 3: Test Your Skill (10 minutes)

**CRITICAL**: Never trust a skill until you test it.

### Test 1: Happy Path
Use real data that's typical/normal. Does it work as expected?

**Test input:**  
[Paste what you're testing with]


**Result**: ✅ Worked / ❌ Failed / ⚠️ Needs adjustment


**Notes:**


---

### Test 2: Edge Case
Use messy/incomplete/weird data. Does it handle it gracefully?

**Test input:**  
[Paste what you're testing with]


**Result**: ✅ Worked / ❌ Failed / ⚠️ Needs adjustment


**Notes:**


---

### Test 3: Real World
Use it for an actual task. Is the output actually useful?

**Test input:**  
[Paste what you're testing with]


**Result**: ✅ Worked / ❌ Failed / ⚠️ Needs adjustment


**Notes:**


---

## STEP 4: Iterate (5 minutes)

Based on your tests, what needs adjustment?

### Changes to Make

**Issue 1:**
- **Problem**: [What didn't work]
- **Fix**: [What instruction to add/change]
- **Updated**: ✅ / ⏳

**Issue 2:**
- **Problem**: [What didn't work]
- **Fix**: [What instruction to add/change]
- **Updated**: ✅ / ⏳

**Issue 3:**
- **Problem**: [What didn't work]
- **Fix**: [What instruction to add/change]
- **Updated**: ✅ / ⏳

---

## STEP 5: Document & Share (2 minutes)

### Quick Stats
- **Time to build**: ___ minutes
- **Time to use it**: ___ minutes (vs. ___ minutes doing it manually)
- **Time savings**: ___ minutes per use
- **Frequency**: ___ times per week/month
- **Monthly time savings**: ___ hours

### Share Your Win
Post in Slack/community:
```
✅ Built: [Skill Name]
🎯 It does: [One sentence]
⏱️ Time to build: X minutes
💰 Saves me: X hours per month
🔥 Best part: [What surprised you or what you love about it]
```

---

## Troubleshooting Guide

### "My skill gives inconsistent outputs"
**Fix**: Add more specific format requirements. Show an example output in your instructions.

### "It's not following my tone/voice"
**Fix**: Be MORE specific. Instead of "professional," say "professional but conversational, like I'm explaining to a colleague, avoid jargon."

### "It includes stuff I don't want"
**Fix**: Add to your "Never" list. Be explicit: "Never include preambles like 'Here is...' or 'I've analyzed...'"

### "It misses important context"
**Fix**: Add to your "Always" list. Example: "Always consider the audience is non-technical executives."

### "Output is too long/short"
**Fix**: Specify length. "Maximum 3 paragraphs" or "Between 500-750 words" or "Exactly 5 bullet points."

### "It doesn't handle edge cases well"
**Fix**: Add specific instructions for those cases. "If no deadline is mentioned, suggest 'This week' for urgent items, 'Next meeting' for others."

---

## Skill Evolution Tracker

Skills improve over time. Track your iterations:

### Version History

**v1.0** - [Date]
- Initial build
- [What it did]

**v1.1** - [Date]
- [What you changed]
- [Why you changed it]

**v1.2** - [Date]
- [What you changed]
- [Why you changed it]

---

## Template Complete! 

### Next Steps:
1. ✅ Build this skill in Claude
2. ✅ Test it 3 times
3. ✅ Use it for real work
4. ✅ Share your win
5. ✅ Build your next skill

### Remember:
- Skills get better with use
- Iterate based on real usage, not hypotheticals
- The best skill is one you actually use
- Start simple, add complexity only if needed

---

**Pro tip**: After you use a skill 5 times, review it. Is there anything that consistently needs manual adjustment? That's your next iteration opportunity.

---

Created by James Gray | [JamesGray.AI](https://jamesgray.ai)