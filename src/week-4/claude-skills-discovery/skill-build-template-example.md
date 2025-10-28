# Agent Skill Build Template - EXAMPLE

This is a complete example showing how to fill out the template. Use this as reference when building your own skills.

**Skill Being Built**: Meeting Notes → Action Items Generator

---

## STEP 1: Define Your Skill (5 minutes)

### Basic Info

**Skill Name** (action-oriented, clear):
Meeting Notes → Action Items Generator

**One-sentence description** (what problem does this solve?):
Converts messy meeting notes or transcripts into a formatted table of action items with clear owners, deadlines, and priorities.

**Who is this for?** (just me, my team, specific role):
Just me - I lead 3-5 meetings per week and spend 30-45 minutes after each one figuring out who's doing what.

---

### The Use Case

**When do I use this?** (trigger/frequency):
After any team meeting, client call, or strategy session where decisions were made or tasks assigned. I use this 4-5 times per week.

**What's my input?** (what do I provide each time):
Raw meeting notes (either my typed notes, an audio transcript from Otter.ai, or a rough bullet list). Usually 500-2000 words of messy text.

**What's my desired output?** (what do I want to receive):
A clean markdown table with 4 columns: Action Item, Owner, Deadline, Priority. Ready to paste directly into Slack or email without editing.

**What does success look like?** (how do I know it worked):
- I can copy-paste the table into Slack with ZERO edits
- Every action item is specific enough that someone could start working on it
- Owners are clear (even if some are "TBD")
- Deadlines are realistic based on the discussion
- I saved 30 minutes of post-meeting cleanup

---

### The Context (this is the magic)

**What instructions do I give repeatedly?**

- **Tone/voice**: Direct, no fluff. Professional but not overly formal. Action-oriented language (start with verbs).

- **Format requirements**: 
  - Markdown table only, no preamble or explanation
  - Exactly 4 columns: Action Item | Owner | Deadline | Priority
  - Use @mentions for owners when names are clear (e.g., @sarah, @james)
  - Priority must be High, Medium, or Low (not numbers or other terms)

- **Must always include**:
  - Every commitment or task mentioned in the meeting
  - Specific context in the action item (not "follow up" but "follow up with Sarah re: Q4 budget")
  - If no owner is clear, put "TBD - needs assignment"
  - If no deadline mentioned, infer one: "This week" for urgent, "By next meeting" for others
  - Flag unclear or incomplete items with ⚠️

- **Must never include**:
  - Meeting summaries or discussion notes
  - Commentary like "This seems important" or "You should prioritize this"
  - Preambles like "Here are the action items..."
  - Multiple tables or sections

- **Quality standards**:
  - Action items are specific enough to be immediately actionable
  - Each action item is independent (not dependent on reading other rows)
  - Owners are real people mentioned in the meeting (not generic roles)
  - Deadlines are concrete dates or clear timeframes

**Example to show Claude** (optional but helpful):

Here's what a perfect output looks like:

| Action Item | Owner | Deadline | Priority |
|------------|-------|----------|----------|
| Follow up with Sarah re: Q4 budget approval for new hires | @james | Oct 30 | High |
| Draft initial proposal for customer dashboard redesign with mobile mockups | @alex | Nov 3 | Medium |
| Research competitor pricing for enterprise plans (Salesforce, HubSpot, Zendesk) | @taylor | Next meeting | Low |
| Schedule follow-up with engineering to review API capacity | @chris | This week | High |
| ⚠️ Confirm attendees for offsite planning session (location TBD) | TBD | Nov 10 | Medium |

---

## STEP 2: Build Your Skill (15 minutes)

Go to Claude.ai → Start a new chat

Paste this prompt (Claude will automatically guide you through skill creation):
```markdown
Help me create a new Agent Skill.

**Skill Name**: Meeting Notes → Action Items Generator

**Purpose**: Converts messy meeting notes or transcripts into a formatted table of action items with clear owners, deadlines, and priorities.

**When I use this**: After any team meeting, client call, or strategy session where decisions were made or tasks assigned. I use this 4-5 times per week.

**Input I provide**: Raw meeting notes (either my typed notes, an audio transcript from Otter.ai, or a rough bullet list). Usually 500-2000 words of messy text.

**Output I want**: A clean markdown table with 4 columns: Action Item, Owner, Deadline, Priority. Ready to paste directly into Slack or email without editing.

**Instructions I usually give**:
- Tone/voice: Direct, no fluff. Professional but not overly formal. Action-oriented language (start with verbs).
- Format requirements: Markdown table only with exactly 4 columns (Action Item | Owner | Deadline | Priority). Use @mentions for owners. Priority must be High, Medium, or Low.
- Must always include: Every commitment mentioned, specific context in action items, TBD for unclear owners, inferred deadlines if not mentioned, ⚠️ flag for unclear items
- Must never include: Meeting summaries, commentary, preambles, multiple tables
- Quality standards: Action items specific enough to be immediately actionable, each item independent, real people as owners, concrete deadlines

**Example of perfect output**:

| Action Item | Owner | Deadline | Priority |
|------------|-------|----------|----------|
| Follow up with Sarah re: Q4 budget approval for new hires | @james | Oct 30 | High |
| Draft initial proposal for customer dashboard redesign with mobile mockups | @alex | Nov 3 | Medium |
| Research competitor pricing for enterprise plans (Salesforce, HubSpot, Zendesk) | @taylor | Next meeting | Low |
| Schedule follow-up with engineering to review API capacity | @chris | This week | High |
| ⚠️ Confirm attendees for offsite planning session (location TBD) | TBD | Nov 10 | Medium |

Guide me through creating this skill with proper structure, format requirements, 
edge case handling, and quality criteria.
```

### What Happened

**Claude asked me:**
- "What should I do if action items don't have clear verbs?"
- "How should I prioritize when priority isn't discussed?"
- "What if someone's name is ambiguous (like 'Alex' when there are two Alexes)?"
- "Should I include decisions that were made but don't require action?"

**I answered:**
- Make the action item start with a verb even if I have to infer it
- Default to Medium priority if not discussed, unless the deadline is urgent (then High)
- Use whatever name/identifier was used in the meeting and let me clarify later
- No - only items that require someone to DO something

**The result:**  
Claude generated well-structured instructions with all edge cases covered. It included a section on "ambiguous scenarios" that handles things like:
- Multiple people with similar names
- Vague action items like "think about X"
- Decisions vs. action items
- Recurring tasks vs. one-time tasks

---

## STEP 3: Test Your Skill (10 minutes)

**CRITICAL**: Never trust a skill until you test it.

### Test 1: Happy Path
Use real data that's typical/normal. Does it work as expected?

**Test input:**  
```
Team standup notes 10/25:
- Sarah said she'll get budget approval by end of week for the 2 engineering roles
- Alex is working on the dashboard redesign, should have mockups ready by Nov 3
- Taylor volunteered to research competitor pricing (Salesforce, HubSpot, Zendesk) before next meeting
- Chris needs to follow up with eng team this week about API capacity for the new integration
- We need to figure out who's organizing the offsite in November - target date is Nov 10 but need to confirm location and attendees
```

**Result**: ✅ Worked

**Notes:**
Perfect! Generated exactly the table format I wanted. Correctly identified owners, inferred the deadline for Sarah ("end of week" became "Oct 30"), added specificity to action items (included "with mobile mockups" for Alex's task), and flagged the offsite item as unclear with ⚠️.

---

### Test 2: Edge Case
Use messy/incomplete/weird data. Does it handle it gracefully?

**Test input:**  
```
Quick meeting - talked about stuff

maybe we should think about the marketing campaign?
jim or john (forgot which) said they'd look into it
deadline is soon
also need to update docs
```

**Result**: ⚠️ Needs adjustment

**Notes:**
It tried its best but made some guesses I didn't love:
- Put "Jim/John" as owner (good - shows ambiguity)
- Said "This week" for deadline on marketing (reasonable inference)
- Created action item "Think about marketing campaign" which is too vague
- "Update docs" became "Update documentation" without specifying what docs

**What I learned:** Need to add instruction about vague action items - if something is too vague (like "think about X"), flag it with ⚠️ and suggest making it more specific.

---

### Test 3: Real World
Use it for an actual task. Is the output actually useful?

**Test input:**  
[Pasted my actual notes from yesterday's leadership team meeting - about 1200 words]

**Result**: ✅ Worked

**Notes:**
Incredible! Used this for a real meeting and it:
- Caught all 8 action items from a long rambling discussion
- Correctly identified that one "action" was actually just a decision (didn't include it)
- Inferred that our VP was the owner of one task even though we just said "the VP should..."
- Properly prioritized the budget item as High because we said "urgent"
- Saved me 35 minutes of post-meeting cleanup

One minor thing: It put "@james" for me when I was the note-taker, which made sense but I might want to clarify if I should be included or excluded.

---

## STEP 4: Iterate (5 minutes)

Based on your tests, what needs adjustment?

### Changes to Make

**Issue 1:**
- **Problem**: Vague action items like "think about X" aren't flagged
- **Fix**: Add rule: "If an action item is vague (think about, consider, maybe), flag it with ⚠️ and suggest making it more specific in parentheses"
- **Updated**: ✅

**Issue 2:**
- **Problem**: Unclear if the note-taker (me) should be included as an owner
- **Fix**: Add rule: "If the note-taker is assigned something, include them as owner unless they say 'someone else should handle this'"
- **Updated**: ✅

**Issue 3:**
- **Problem**: Sometimes deadlines like "EOW" aren't converted to actual dates
- **Fix**: Add rule: "Convert time abbreviations to actual dates. EOW = end of current week (Friday), EOM = last day of current month, Q2 = June 30, etc."
- **Updated**: ✅

---

## STEP 5: Document & Share (2 minutes)

### Quick Stats
- **Time to build**: 18 minutes (including iterations)
- **Time to use it**: 2 minutes (paste notes, get table)
- **Time saved**: 33 minutes per use (used to take 35 min, now takes 2 min)
- **Frequency**: 4-5 times per week
- **Monthly time savings**: ~10 hours per month!

### Share Your Win
Post in Slack/community:
```
✅ Built: Meeting Notes → Action Items Generator
🎯 It does: Turns messy meeting notes into a clean action items table with owners, deadlines, and priorities
⏱️ Time to build: 18 minutes
💰 Saves me: 10 hours per month
🔥 Best part: I tested it with real meeting notes and it actually worked perfectly. Just copy-paste into Slack and I'm done. No more "wait, who was supposed to do what?" confusion.
```

---

## Skill Evolution Tracker

### Version History

**v1.0** - Oct 25, 2025
- Initial build
- Basic table generation with 4 columns
- Handles clear action items well

**v1.1** - Oct 25, 2025 (same day, after testing)
- Added ⚠️ flag for vague action items
- Clarified note-taker inclusion
- Added time abbreviation conversion (EOW, EOM, Q2, etc.)
- Better edge case handling for ambiguous owners

**v1.2** - Oct 30, 2025 (after 1 week of use)
- Added rule: If multiple similar tasks for same person, group them into one item
- Added rule: If deadline is "before [meeting name]", convert to actual date of that meeting
- Added priority inference: mentions of "urgent", "ASAP", "critical" automatically get High priority

---

## What I Learned Building This Skill

### What Worked Great:
✅ Being super specific about format requirements (exactly 4 columns, no preamble)  
✅ Showing an example output - Claude matched that format perfectly  
✅ Defining edge cases upfront (TBD for unclear owners, ⚠️ for vague items)  
✅ Testing with REAL data, not made-up examples  
✅ Iterating immediately after first test instead of trying to be perfect first try  

### What I'd Do Differently:
- Should have tested with messy data FIRST - would have caught the vague action item issue sooner
- Could have been more specific about priority inference rules from the start
- Should have asked Claude more questions during creation about edge cases I hadn't thought of

### Tips for Others Building Similar Skills:
1. **Show, don't just tell** - That example output table was worth 1000 words
2. **Test the extremes** - Super clear notes AND super messy notes
3. **Real beats hypothetical** - Use actual meeting notes, not fake examples
4. **Iterate fast** - v1.0 → v1.1 in the same day based on testing
5. **Use it immediately** - Don't wait to "perfect" it, just use it and fix as you go

---

## Template Complete! 

This skill is now in production and I'm using it 4-5x per week. Already saved about 10 hours in the first month.

**Next skill I'm building**: "Client Strategy Session → Executive Brief Generator" (similar pattern, different output format)

---

Created by James Gray | [JamesGray.AI](https://jamesgray.ai)
