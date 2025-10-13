# Workflow Refinement Example

## Scenario
A student is building a research assistant agent and provides this rough workflow description to an LLM with the refinement guide attached as context.

---

## Student's Draft Workflow (Rough)

```
Build a research assistant that helps analyze competitor products.

The agent should:
- Search for competitor information online
- Look at their websites and social media
- Figure out their pricing and features
- Make a comparison and write it up
- If something goes wrong, try again or skip it
- Save the results somewhere
```

---

## LLM Response (Using the Refinement Guide)

I'll refine your competitor research assistant workflow into a clear, executable prompt.

---

# Competitor Research Assistant Workflow

## Overview
This agent conducts automated competitive analysis by gathering information from multiple sources, extracting key product details, and generating a structured comparison report. The workflow handles data collection, validation, analysis, and report generation with built-in error handling.

## Workflow Steps

### 1. Initialize Research
**Input Required:**
- `competitor_list`: Array of competitor company names (e.g., ["Company A", "Company B", "Company C"])
- `research_focus`: Specific areas to analyze (default: ["pricing", "features", "target_market"])
- `output_directory`: Path to save results (default: `output/research/`)

**Actions:**
- Create timestamped research session: `research_{competitor_name}_{YYYY-MM-DD}.md`
- Initialize results tracking object with fields: `{name, website, pricing, features, social_presence, status}`
- Log start time and parameters to `research_log.txt`

### 2. Discover Online Presence
For each competitor in `competitor_list`:

**2.1 Find Official Website**
- Use `web_search()` tool with query: `"{competitor_name}" official website`
- Extract top 3 results
- Identify official domain by checking for:
  - Company name in domain
  - HTTPS certificate
  - Professional design indicators
- **If no official site found**: Mark status as "limited_data" and log to skipped list, continue to next competitor

**2.2 Find Social Media Profiles**
- Search for presence on platforms: LinkedIn, Twitter, Facebook
- Use `web_search()` tool with query: `"{competitor_name}" site:linkedin.com OR site:twitter.com OR site:facebook.com`
- Store URLs in `social_presence` array
- **If no social profiles found**: Continue (this is optional data)

### 3. Extract Product Information

**3.1 Analyze Website Content**
- Use `fetch_webpage()` tool to retrieve HTML from official website
- Extract sections containing:
  - Product/service descriptions (look for keywords: "products", "services", "solutions")
  - Pricing information (keywords: "pricing", "plans", "cost", "$")
  - Feature lists (keywords: "features", "capabilities", "includes")
- Parse text content and remove navigation/footer noise

**3.2 Validate Extracted Data**
Check that minimum required fields are populated:
- At least 1 product/service description found
- At least 1 feature identified OR pricing information found

**If validation fails:**
- Log: `"Insufficient data for {competitor_name}: {reason}"`
- Set status to "incomplete"
- Flag for manual review in final report
- Continue to next competitor

### 4. Structure Competitive Data

**4.1 Normalize Pricing**
- If pricing found, extract:
  - Currency and amount
  - Billing cycle (monthly/annual)
  - Plan tiers (basic/pro/enterprise)
- Convert to standard format: `{"tier": "Pro", "price": 99, "currency": "USD", "billing": "monthly"}`
- **If multiple plans**: Store as array
- **If no pricing**: Mark as "Contact for pricing"

**4.2 Categorize Features**
Group features into categories:
- **Core Features**: Primary product capabilities
- **Integrations**: Third-party connections
- **Support**: Customer support options
- **Security**: Security/compliance features

Use keyword matching or LLM classification for categorization.

### 5. Generate Comparison Report

**5.1 Create Markdown Table**
Structure:
```markdown
| Competitor | Pricing | Key Features | Social Presence | Data Quality |
|------------|---------|--------------|-----------------|--------------|
| Company A  | $99/mo  | Feature 1, 2 | LinkedIn, Twitter | Complete    |
```

**5.2 Add Detailed Sections**
For each competitor, include:
```markdown
## [Competitor Name]
**Website**: [URL]
**Pricing**: [Structured pricing info]
**Key Features**:
- Feature 1
- Feature 2
- Feature 3

**Target Market**: [Inferred from messaging]
**Differentiators**: [Unique selling points]
```

**5.3 Add Executive Summary**
At the top of report, include:
- Total competitors analyzed successfully
- Common pricing range: `$X - $Y per month`
- Feature gaps identified
- Recommendations (2-3 bullet points)

### 6. Handle Errors and Edge Cases

**Network Errors:**
- If `web_search()` or `fetch_webpage()` fails:
  - Wait 2 seconds
  - Retry up to 2 times
  - If still failing: Log error and mark competitor status as "error_network"

**Rate Limiting:**
- If rate limit detected (HTTP 429):
  - Wait 60 seconds before next request
  - Log: `"Rate limited at {timestamp}, pausing..."`

**Incomplete Data:**
- If competitor has < 50% of required fields:
  - Include in report with "Incomplete Data" flag
  - Add to "Requires Manual Review" section at end

### 7. Save and Finalize

**7.1 Save Report**
- Write to: `{output_directory}/competitor_analysis_{YYYY-MM-DD_HH-MM}.md`
- Ensure proper markdown formatting
- Include metadata header:
  ```yaml
  ---
  generated: YYYY-MM-DD HH:MM:SS
  competitors_analyzed: N
  success_rate: X%
  ---
  ```

**7.2 Save Raw Data**
- Export structured data as JSON: `{output_directory}/competitor_data_{timestamp}.json`
- Include all fields, even if null

**7.3 Log Summary**
Append to `research_log.txt`:
```
[YYYY-MM-DD HH:MM:SS] Research completed
- Competitors: N
- Successful: N
- Incomplete: N
- Errors: N
- Output: {filepath}
```

## Success Criteria

✅ **Must Have:**
- Markdown report generated with comparison table
- At least 70% of competitors have "Complete" or "Incomplete" status (not "error")
- All successfully analyzed competitors included in report
- Executive summary present with recommendations

✅ **Quality Indicators:**
- Pricing information extracted for at least 50% of competitors
- Minimum 3 features identified per competitor
- All URLs validated and accessible

✅ **Error Handling:**
- All errors logged with timestamps and reasons
- Failed competitors listed in "Manual Review" section
- No crashes or unhandled exceptions

---

## Tools Required

- `web_search(query: str) -> List[SearchResult]`: Search the web
- `fetch_webpage(url: str) -> str`: Retrieve webpage HTML/text
- `extract_text(html: str) -> str`: Parse HTML to clean text
- `save_file(path: str, content: str) -> bool`: Write files
- `log(message: str, level: str) -> None`: Logging utility

