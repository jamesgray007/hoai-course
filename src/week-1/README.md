# Week 1: AI Assistant Foundations

## Overview
This week focuses on mastering prompt engineering and understanding AI assistant capabilities. You'll learn to craft effective prompts, create style guides, and use templates to get consistent, high-quality results from AI assistants.

## Learning Objectives
- Master prompt engineering fundamentals
- Create audience-specific style guides
- Use prompt templates for consistent results
- Understand prompt optimization techniques
- Leverage AI assistants across different platforms (OpenAI, Anthropic, Google)

## Prerequisites
- Access to an AI assistant (ChatGPT, Claude, or Gemini)
- Basic understanding of how to interact with AI chatbots
- **No coding required** - this week is all about prompt engineering

## Week 1 Structure

### Prompt Templates (`prompt-templates/`)

These are reusable prompt templates you can use with any AI assistant.

#### 1. **Prompt Improvers**
Transform basic prompts into powerful, effective instructions.

- **prompt-improver.md** - Universal prompt optimizer
  - Works with any AI platform
  - Analyzes and enhances your prompts
  - Provides structured improvements

- **prompt-improver-openai.md** - OpenAI/ChatGPT optimized
  - Tailored for GPT models
  - OpenAI best practices included

- **prompt-improver-anthropic.md** - Claude optimized
  - Follows Claude's prompt engineering guide
  - Anthropic-specific techniques

- **prompt-improver-google.md** - Gemini optimized
  - Google AI best practices
  - Gemini-specific optimizations

**How to Use:**
1. Copy the entire template
2. Paste into your AI assistant
3. Replace `[YOUR PROMPT HERE]` with your prompt
4. Review the improved version

**Example:**
```
Original: "Write a blog post about AI"

After improvement: "Write a 1000-word blog post about AI's
impact on healthcare. Target audience: hospital administrators.
Include 3 real-world examples, data points, and actionable
recommendations. Tone: professional but accessible."
```

#### 2. **Audience Style Guide Creator**

- **audience-style-guide-creator.md** - Generate custom style guides
  - Define your audience and brand voice
  - Create consistent content guidelines
  - Reusable across all content creation

- **audience-style-guide.md** - Template for manual creation
  - Framework for building style guides
  - Customizable sections
  - Best practices included

**How to Use:**
1. Copy the style guide creator prompt
2. Answer questions about your audience and brand
3. Save the generated style guide
4. Reference it in future prompts for consistent voice

**Example:**
```
"Using the style guide for [tech startup targeting developers],
write a product announcement..."
```

### Prompt Examples (`prompt-examples/`)

Real-world examples and case studies.

#### **Everyday_AI_Style_Guide.md**
- Complete style guide example
- Shows professional implementation
- Ready to use as reference

**What it includes:**
- Target audience definition
- Tone and voice guidelines
- Content structure templates
- Do's and don'ts
- Example content

## Key Concepts

### 1. The Anatomy of a Good Prompt

**Basic Structure:**
```
[ROLE] + [TASK] + [CONTEXT] + [FORMAT] + [CONSTRAINTS]
```

**Example:**
```
You are an experienced technical writer [ROLE]
Create a how-to guide for setting up Python [TASK]
Targeting beginners with no programming experience [CONTEXT]
Format: numbered steps with screenshots descriptions [FORMAT]
Keep under 1000 words, avoid jargon [CONSTRAINTS]
```

### 2. Prompt Engineering Techniques

#### **Specificity**
❌ Bad: "Write about marketing"
✅ Good: "Write a 500-word LinkedIn post about email marketing best practices for B2B SaaS companies"

#### **Context Setting**
```
You are a [ROLE] with expertise in [DOMAIN]
Your audience is [DESCRIPTION]
They need help with [PROBLEM]
```

#### **Output Format**
```
Provide your response as:
- Bullet points
- Numbered steps
- Table format
- JSON structure
- Markdown document
```

#### **Examples (Few-Shot Prompting)**
```
Here are 2 examples of the style I want:

Example 1: [show example]
Example 2: [show example]

Now create one for: [your topic]
```

#### **Constraints**
```
- Length: 300-500 words
- Tone: Professional but friendly
- Avoid: Jargon, clichés
- Include: Data points, examples
```

### 3. Style Guides

Style guides ensure consistency across all AI-generated content.

**Key Elements:**
1. **Audience Profile**
   - Demographics
   - Pain points
   - Goals
   - Knowledge level

2. **Voice and Tone**
   - Personality traits
   - Communication style
   - Emotional range

3. **Content Structure**
   - Preferred formats
   - Section organization
   - Length guidelines

4. **Language Guidelines**
   - Vocabulary preferences
   - Words to use/avoid
   - Complexity level

5. **Examples**
   - Good examples to follow
   - Bad examples to avoid

### 4. Platform Differences

Different AI assistants have different strengths:

| Platform | Strengths | Best For |
|----------|-----------|----------|
| **ChatGPT** (OpenAI) | Versatile, code generation | General tasks, coding |
| **Claude** (Anthropic) | Long context, analysis | Document analysis, research |
| **Gemini** (Google) | Multimodal, data integration | Images, Google Workspace |

## Practical Exercises

### Exercise 1: Prompt Improvement
1. Take a basic prompt you've used before
2. Run it through a prompt improver template
3. Compare results from original vs. improved
4. Document what made the difference

### Exercise 2: Create Your Style Guide
1. Use the audience-style-guide-creator.md template
2. Define your target audience
3. Generate a complete style guide
4. Test it with 3 different content requests

### Exercise 3: Platform Comparison
1. Take the same prompt
2. Run through ChatGPT, Claude, and Gemini
3. Note differences in output
4. Adjust prompt for each platform
5. Compare which works best for your use case

### Exercise 4: Progressive Refinement
1. Start with a basic prompt
2. Add context → observe changes
3. Add format requirements → observe changes
4. Add constraints → observe changes
5. Document the evolution

## Best Practices

### ✅ Do's
- Be specific about what you want
- Provide context and examples
- Specify output format clearly
- Set appropriate constraints
- Iterate and refine prompts
- Save successful prompts for reuse
- Use style guides for consistency

### ❌ Don'ts
- Don't be vague ("write something about...")
- Don't assume AI knows your context
- Don't skip format specifications
- Don't use prompts without testing
- Don't ignore platform differences
- Don't forget to iterate

## Common Use Cases

### Content Creation
```
Using [style guide], write a [content type] about [topic]
Target audience: [description]
Length: [word count]
Include: [specific elements]
Tone: [voice characteristics]
```

### Analysis and Research
```
Analyze [topic/document]
Focus on: [specific aspects]
Provide: [type of insights]
Format: [structure]
Audience: [who will read this]
```

### Editing and Improvement
```
Review this [content type]:
[paste content]

Improve:
- Clarity and flow
- Grammar and style
- Engagement
- [specific aspects]

Maintain: [tone/voice]
```

### Brainstorming
```
Generate [number] ideas for [objective]
Criteria:
- [requirement 1]
- [requirement 2]
- [requirement 3]

Format: [how to present ideas]
```

## Tools and Resources

### AI Assistants to Explore
- **ChatGPT**: chat.openai.com
- **Claude**: claude.ai
- **Gemini**: gemini.google.com
- **Perplexity**: perplexity.ai (research-focused)

### Prompt Libraries
- Save your best prompts in a document
- Organize by use case and category
- Include notes on what works and why
- Share with team members

### Testing Framework
```
1. Original prompt
2. Platform used
3. Output received
4. What worked well
5. What to improve
6. Refined version
7. Results comparison
```

## Real-World Applications

### Business Use Cases
- Email drafting and responses
- Report writing and summaries
- Presentation content
- Marketing copy
- Social media posts
- Meeting agendas and notes

### Personal Use Cases
- Learning and research
- Writing and editing
- Planning and organization
- Creative projects
- Problem-solving
- Decision-making support

## Success Metrics

Track your prompt engineering progress:

- **Iterations needed**: Fewer = better prompts
- **Output quality**: Rate 1-10 against requirements
- **Time saved**: Compare to manual creation
- **Consistency**: Using style guides
- **Reusability**: How often you reuse prompts

## Tips for Success

1. **Start Simple**: Begin with basic prompts and add complexity
2. **Build a Library**: Save and organize successful prompts
3. **Learn Platform Quirks**: Each AI has unique characteristics
4. **Iterate Quickly**: Don't aim for perfection on first try
5. **Use Templates**: Adapt proven patterns to new uses
6. **Document Learning**: Note what works and why
7. **Share Knowledge**: Collaborate with others on prompt techniques

## Week 1 Checklist

- [ ] Try all prompt improver templates
- [ ] Create a personal style guide
- [ ] Test prompts on different platforms
- [ ] Build a prompt library (at least 5 prompts)
- [ ] Complete practical exercises
- [ ] Document lessons learned
- [ ] Identify 3 use cases for your work

## Next Steps

After completing Week 1:
- ✓ You can craft effective prompts consistently
- ✓ You have a personal style guide
- ✓ You understand platform differences
- → Move to Week 2 to build no-code AI workflows
- → Start automating repetitive tasks

## Additional Resources

### External Learning
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Prompt Library](https://docs.anthropic.com/claude/prompt-library)
- [Google AI Prompting Guide](https://ai.google.dev/docs/prompt_best_practices)

### Course Resources
- Main README.md for course overview
- docs/local_setup.md for Week 3-4 preparation
- Course community on Maven for discussion

## Questions and Support

Common questions:
- **"How long should a prompt be?"** → As long as needed for clarity, but concise
- **"Which AI assistant is best?"** → Depends on your use case; try all three
- **"How do I know if my prompt is good?"** → If it gives consistent, quality results
- **"Can I use these commercially?"** → Check each platform's terms of service

For more help:
- Review the example prompts in this directory
- Join the course community discussions
- Experiment and iterate
- Share your discoveries

---

**Remember**: Prompt engineering is a skill that improves with practice. Don't expect perfection immediately—focus on consistent improvement!
