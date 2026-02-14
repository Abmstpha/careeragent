
# CAREERFORGE - HACKATHON IMPLEMENTATION PLAN

## Columbia x Iterate St. Valentine Hackathon - Feb 14, 2026

---

## EXECUTIVE SUMMARY

**Project:** CareerForge - AI-Powered Job Search Command Center  
**Track:** Track 1 - Build an Agent (Blaxel sponsor)  
**Team Size:** 2-3 people (adjust timelines based on actual team)  
**Build Time:** 7 hours (9:30 AM - 4:30 PM code freeze)  
**Submission Deadline:** 4:30 PM (code freeze)  
**Demo Time:** 6:00-7:00 PM (finalist pitches)

**Core Value Prop:**  
Complete job search automation with voice-powered interview practice, real-time company intelligence, and production-grade document generation.

**Sponsor Integration:**

- ✅ **ElevenLabs** - Speech-to-Speech interview AI
- ✅ **Anthropic** - Claude Sonnet 4.5 for all intelligence
- ✅ **Lovable** - Frontend generation (code: SDFNKL789)
- ✅ **Blaxel** - Agent hosting with 25ms latency
- ✅ **White Circle** - Safety monitoring layer
- ✅ **Perle** - Expert feedback loop (conceptual integration)
- ✅ **BizCrush** - Career fair networking (conceptual integration)

---

## TIMELINE OVERVIEW

```
9:30 AM  - Doors open, breakfast, team registration
10:00 AM - Hacking begins
12:30 PM - Lunch served
4:30 PM  - CODE FREEZE (commit final version)
5:00 PM  - Judging begins
6:30 PM  - Finalist pitches
7:30 PM  - Closing ceremony
```

**Our Timeline:**

```
09:30 - 10:00   Setup & Planning (30 min)
10:00 - 11:30   Frontend Build - Phase 1 (90 min)
11:30 - 13:00   Backend Build - Phase 1 (90 min)
13:00 - 13:30   Lunch + Testing (30 min)
13:30 - 15:00   Frontend Build - Phase 2 (90 min)
15:00 - 16:00   Backend Integration (60 min)
16:00 - 16:20   End-to-End Testing (20 min)
16:20 - 16:30   FINAL COMMIT + Deploy (10 min)
16:30 - 18:00   Demo Prep + Presentation (90 min)
```

---

## TEAM STRUCTURE

### Role Distribution (2-3 Person Team)

**Person 1: Frontend Lead (Lovable Expert)**

- Responsible for: All Lovable prompts, UI/UX, component integration
- Tools: Lovable.dev, Figma (optional), ChatGPT for debugging
- Output: Complete React/Next.js frontend

**Person 2: Backend Lead (API + Integration)**

- Responsible for: FastAPI, Claude integration, ElevenLabs, Firecrawl
- Tools: FastAPI, Python, Claude API, ElevenLabs API
- Output: Working backend with all endpoints

**Person 3 (Optional): Full-Stack Floater**

- First 3 hours: Help frontend (Lovable prompts)
- Last 4 hours: Help backend integration + testing
- Final hour: Demo prep + presentation script

**If Only 2 People:**

- Person 1: Frontend only (Lovable)
- Person 2: Backend + Integration + Deploy + Demo prep

---

## TECH STACK

### Frontend

- **Framework:** Next.js 14 (via Lovable)
- **Styling:** Tailwind CSS + shadcn/ui
- **State:** React Context + hooks
- **Forms:** React Hook Form
- **Drag & Drop:** @dnd-kit/core (for Kanban)
- **Charts:** Recharts
- **File Upload:** react-dropzone
- **Deployment:** Vercel (via Lovable auto-deploy)

### Backend

- **Framework:** FastAPI (Python 3.11+)
- **LLM:** Anthropic Claude Sonnet 4.5 (claude-sonnet-4-5-20250514)
- **Voice:** ElevenLabs (Speech-to-Speech)
- **Scraping:** Firecrawl API
- **Storage:** Local filesystem + Google Drive API (optional)
- **Deployment:** Railway / Render / Fly.io

### APIs & Services

- **Anthropic API:** $120+ in credits available
- **ElevenLabs:** Creator plan (unlimited characters)
- **Firecrawl:** Growth tier
- **Hunter.io:** Free tier (100 searches/month)
- **Glassdoor Scraper:** Bright Data or SerpAPI
- **LinkedIn:** Apollo.io or PhantomBuster

### Development Tools

- **Version Control:** Git + GitHub
- **API Testing:** Postman / Thunder Client
- **Environment:** .env files with python-dotenv
- **Code Editor:** VS Code / Cursor

---

## FILE STRUCTURE

### Frontend (Lovable-Generated)

```
careerforge-frontend/
├── app/
│   ├── page.tsx                 # Landing page
│   ├── layout.tsx               # Root layout
│   ├── documents/
│   │   └── page.tsx             # Documents tab (Resume/Cover/Score)
│   ├── discovery/
│   │   └── page.tsx             # Discovery (ContactFinder/CompanyIntel)
│   ├── interview/
│   │   ├── page.tsx             # Interview setup
│   │   ├── [id]/
│   │   │   ├── page.tsx         # Active interview
│   │   │   └── report/
│   │   │       └── page.tsx     # Interview report
│   └── dashboard/
│       └── page.tsx             # Practice stats + Application pipeline
├── components/
│   ├── ui/                      # shadcn components
│   ├── ResumeForge.tsx
│   ├── CoverForge.tsx
│   ├── ForgeScore.tsx
│   ├── ContactFinder.tsx
│   ├── CompanyIntelligence.tsx
│   ├── InterviewAI.tsx
│   ├── ApplicationPipeline.tsx
│   └── Navbar.tsx
├── lib/
│   ├── api.ts                   # API client
│   └── utils.ts
├── public/
│   └── images/
└── package.json
```

### Backend

```
careerforge-backend/
├── app/
│   ├── main.py                  # FastAPI app entry
│   ├── config.py                # Settings, API keys
│   ├── api/
│   │   ├── routes/
│   │   │   ├── documents.py     # Resume/Cover/Score endpoints
│   │   │   ├── discovery.py     # ContactFinder endpoints
│   │   │   ├── intelligence.py  # Company analysis endpoints
│   │   │   ├── interview.py     # InterviewAI endpoints
│   │   │   └── pipeline.py      # Application tracking
│   │   └── deps.py              # Dependencies
│   ├── services/
│   │   ├── claude_service.py    # Anthropic Claude wrapper
│   │   ├── elevenlabs_service.py
│   │   ├── firecrawl_service.py
│   │   ├── document_service.py
│   │   ├── intelligence_service.py
│   │   └── interview_service.py
│   ├── models/
│   │   └── schemas.py           # Pydantic models
│   ├── prompts/
│   │   ├── resume_forge.txt
│   │   ├── cover_forge.txt
│   │   ├── forge_score.txt
│   │   ├── company_analysis.txt
│   │   └── interview_eval.txt
│   └── utils/
│       ├── file_handler.py
│       └── helpers.py
├── tests/                        # Skip for hackathon
├── .env                          # API keys (NOT committed)
├── requirements.txt
├── Dockerfile                    # For deployment
└── README.md
```

---

## HOUR-BY-HOUR IMPLEMENTATION PLAN

### HOUR 0: Setup & Planning (9:30 AM - 10:00 AM)

**All Team Members:**

- [ ] Join Discord, form team on Iterate platform
- [ ] Claim sponsor credits (check Discord for codes)
- [ ] Create GitHub repo: `careerforge-hackathon`
- [ ] Share Google Doc with all prompts
- [ ] Set up environment variables (.env template)

**Frontend Lead:**

- [ ] Create Lovable account with code SDFNKL789
- [ ] Start new project: "CareerForge"
- [ ] Read Prompt 1 (Landing Page)

**Backend Lead:**

- [ ] Clone repo, create `backend/` folder
- [ ] Set up Python virtual environment
- [ ] Install base packages: `fastapi uvicorn anthropic elevenlabs python-dotenv`
- [ ] Create `.env` file with API keys
- [ ] Test Anthropic API connection with simple script

**Output:** Development environment ready, APIs tested

---

### HOUR 1-2: Frontend Build - Phase 1 (10:00 AM - 11:30 AM)

**Frontend Lead (Lovable):**

**10:00 - 10:20** - Landing Page

- [ ] Feed **Prompt 1** to Lovable
- [ ] Review generated code
- [ ] Test navigation between pages
- [ ] Fix any broken links

**10:20 - 10:50** - Documents Tab (ResumeForge)

- [ ] Feed **Prompt 2 - Part 1** (ResumeForge section only)
- [ ] Test file upload component
- [ ] Test mock API call (use fake data)
- [ ] Verify ATS score badge renders correctly

**10:50 - 11:30** - Documents Tab (CoverForge + ForgeScore)

- [ ] Feed **Prompt 2 - Part 2** (CoverForge section)
- [ ] Feed **Prompt 2 - Part 3** (ForgeScore section)
- [ ] Test cross-module linking ("Use Last Generated Resume")
- [ ] Verify all download buttons work with mock data

**Output:** Documents page fully built with UI

---

### HOUR 3-4: Backend Build - Phase 1 (11:30 AM - 1:00 PM)

**Backend Lead:**

**11:30 - 12:00** - FastAPI Skeleton

```bash
# Create FastAPI structure
mkdir -p app/api/routes app/services app/models app/prompts app/utils
touch app/main.py app/config.py
```

`app/main.py`:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="CareerForge API")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "CareerForge API Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}
```

**12:00 - 12:30** - Claude Service
`app/services/claude_service.py`:

```python
import anthropic
import os
from anthropic import Anthropic

class ClaudeService:
    def __init__(self):
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.model = "claude-sonnet-4-5-20250514"
    
    async def generate_resume(self, master_resume: str, jd: str, format: str):
        """ResumeForge logic"""
        with open("app/prompts/resume_forge.txt", "r") as f:
            system_prompt = f.read()
        
        user_message = f"""
Master Resume:
{master_resume}

Job Description:
{jd}

Output Format: {format}
"""
        
        message = self.client.messages.create(
            model=self.model,
            max_tokens=4000,
            system=system_prompt,
            messages=[{"role": "user", "content": user_message}]
        )
        
        return message.content[0].text
    
    # Add similar methods for cover, score, company analysis
```

**12:30 - 13:00** - Resume Endpoint
`app/api/routes/documents.py`:

```python
from fastapi import APIRouter, UploadFile, File
from app.services.claude_service import ClaudeService
from pydantic import BaseModel

router = APIRouter(prefix="/api/documents", tags=["documents"])
claude_service = ClaudeService()

class ResumeRequest(BaseModel):
    master_resume: str
    job_description: str
    output_format: str

@router.post("/resume/optimize")
async def optimize_resume(request: ResumeRequest):
    optimized = await claude_service.generate_resume(
        request.master_resume,
        request.job_description,
        request.output_format
    )
    
    # Mock ATS score for now
    ats_score = 85
    
    return {
        "optimized_resume": optimized,
        "ats_score": ats_score,
        "keyword_matches": ["Python", "ML", "Docker"]
    }
```

Wire up in `main.py`:

```python
from app.api.routes import documents
app.include_router(documents.router)
```

**Output:** Working `/api/documents/resume/optimize` endpoint

---

### LUNCH BREAK (1:00 PM - 1:30 PM)

**All:**

- [ ] Eat lunch
- [ ] Quick test: Can frontend call backend `/health`?
- [ ] Check Discord for any sponsor announcements
- [ ] Review progress: Are we on track?

---

### HOUR 5-6: Frontend Build - Phase 2 (1:30 PM - 3:00 PM)

**Frontend Lead:**

**1:30 - 2:00** - Discovery Tab

- [ ] Feed **Prompt 3 - Part 1** (ContactFinder)
- [ ] Test contact search UI
- [ ] Mock API response with fake contact data

**2:00 - 2:30** - Company Intelligence

- [ ] Feed **Prompt 3 - Part 2** (Company Intelligence)
- [ ] Test all checkboxes and inputs
- [ ] Verify timeline chart renders (use Recharts)
- [ ] Mock company health score dashboard

**2:30 - 3:00** - InterviewAI Setup Page

- [ ] Feed **Prompt 4 - Part 1** (Setup page only)
- [ ] Test file upload for resume
- [ ] Test interviewer personality dropdown
- [ ] Button links to interview session page

**Output:** Discovery + Interview Setup pages complete

---

### HOUR 7: Backend Build - Phase 2 (3:00 PM - 4:00 PM)

**Backend Lead:**

**3:00 - 3:20** - Cover Letter Endpoint

- [ ] Copy CoverForge prompt to `app/prompts/cover_forge.txt`
- [ ] Implement `claude_service.generate_cover()`
- [ ] Add endpoint: `POST /api/documents/cover/generate`

**3:20 - 3:40** - ForgeScore Endpoint

- [ ] Copy ForgeScore prompt to `app/prompts/forge_score.txt`
- [ ] Implement `claude_service.analyze_documents()`
- [ ] Add endpoint: `POST /api/documents/score/analyze`

**3:40 - 4:00** - Company Intelligence (Basic Version)

- [ ] Firecrawl integration: Scrape company About page
- [ ] Claude sentiment analysis on scraped content
- [ ] Endpoint: `POST /api/intelligence/analyze`
- [ ] Return mock data + real sentiment if time allows

**Output:** Core document endpoints + basic company analysis

---

### HOUR 8: Integration (4:00 PM - 5:00 PM)

**Both Team Members:**

**4:00 - 4:20** - Connect Frontend to Backend

- [ ] Update frontend API client with real backend URL
- [ ] Test ResumeForge end-to-end
- [ ] Test CoverForge end-to-end
- [ ] Fix CORS issues if any

**4:20 - 4:40** - Dashboard Build (Simplified)

- [ ] Feed **Prompt 5** to Lovable
- [ ] Mock interview history data
- [ ] Skip Application Pipeline if time is tight (focus on Interview stats)
- [ ] OR: Build simple list view instead of Kanban

**4:40 - 5:00** - Deploy Backend

- [ ] Deploy to Railway (fastest option):

  ```bash
  railway login
  railway init
  railway up
  ```

- [ ] Update frontend API URL to production
- [ ] Test production deploy

**Critical Decision Point:** If anything is broken, SKIP InterviewAI voice feature and focus on Documents + Discovery working perfectly.

**Output:** Deployed, working demo

---

### HOUR 9: Testing & Polish (5:00 PM - 6:00 PM)

**4:20 - 4:30** - FINAL CODE COMMIT

- [ ] Commit all changes
- [ ] Push to GitHub
- [ ] Tag release: `git tag v1.0-hackathon`
- [ ] **STOP CODING** (Code freeze at 4:30 PM)

**4:30 - 5:30** - Full Testing

- [ ] Test complete flow: Upload resume → Generate optimized → Generate cover → Analyze
- [ ] Test Company Intelligence search
- [ ] Screenshot all working features
- [ ] Note any broken features to avoid in demo

**5:30 - 6:00** - Demo Preparation

- [ ] Prepare 2-minute demo script (see below)
- [ ] Open all necessary tabs in browser
- [ ] Prepare sample resume + JD to use in demo
- [ ] Practice demo 2-3 times
- [ ] Charge laptop fully

**Output:** Polished demo ready to present

---

## DEMO SCRIPT (2 Minutes)

### Opening (15 seconds)

"Hi judges! We built **CareerForge** -- an AI-powered job search command center that automates everything from resume optimization to interview practice. Built in 7 hours with Anthropic, ElevenLabs, and Lovable."

### Documents Pipeline Demo (45 seconds)

[Screen: Documents tab]
"Let me show you the core workflow. I paste my master resume here, add a job description for an AI Engineer role at Anthropic..."

[Click Generate Optimized Resume]

"Within seconds, Claude Sonnet 4.5 analyzes the JD, extracts key requirements, and generates an ATS-optimized resume. Look at this -- 92% ATS score, keyword matches highlighted."

[Click Use in CoverForge]

"Now it auto-populates into our cover letter generator. I just add the company details, pick a tone, and..."

[Click Generate Cover Letter]

"Boom. Personalized cover letter with STAR-method achievements, company research, and genuine personality. And it tracked which achievements from my resume it used."

### Discovery Tools Demo (30 seconds)

[Screen: Discovery tab]

"But it's not just about documents. CareerForge helps you find the right people. Let me search for contacts at Anthropic..."

[Show ContactFinder results]

"Found 8 recruiters, 4 hiring managers, and 2 NJIT alumni -- with generated outreach templates."

[Switch to Company Intelligence]

"And before I apply, I check company health. It scraped Anthropic's website, analyzed employee sentiment on Glassdoor, checked H1B sponsorship history, and even shows their hiring cycles. Green badge -- safe to apply."

### Sponsor Integration Highlight (20 seconds)

"What makes this production-ready? We integrated all the sponsor tools:

- **Anthropic Claude** powers all the intelligence
- **ElevenLabs** voice for interview practice with speech-to-speech
- **Blaxel** hosts our agents with 25ms latency
- **Lovable** built this entire frontend in under 2 hours"

### Close (10 seconds)

"CareerForge doesn't just help you apply to jobs -- it helps you land them. Thank you!"

---

## CRITICAL SUCCESS FACTORS

### Must-Haves (Non-Negotiable)

- ✅ ResumeForge working end-to-end
- ✅ CoverForge working end-to-end
- ✅ ForgeScore showing results dashboard
- ✅ Company Intelligence with at least mock data
- ✅ Frontend deployed and accessible
- ✅ Backend deployed and responding
- ✅ Demo script practiced

### Nice-to-Haves (Include if Time Allows)

- ⭐ InterviewAI with ElevenLabs Speech-to-Speech
- ⭐ Application Pipeline Kanban board
- ⭐ ContactFinder with real LinkedIn data
- ⭐ Real Firecrawl scraping (vs mock data)
- ⭐ White Circle safety monitoring

### Skip if Time is Tight

- ❌ Google Drive integration
- ❌ File export to PDF/DOCX
- ❌ Email sending functionality
- ❌ Authentication/user accounts
- ❌ Database (use in-memory storage)

---

## TECHNICAL DEPENDENCIES

### API Keys Needed (Set Up Before Hackathon)

```bash
# .env file
ANTHROPIC_API_KEY=sk-ant-...
ELEVENLABS_API_KEY=sk_...
FIRECRAWL_API_KEY=fc-...
HUNTER_IO_API_KEY=...
SERP_API_KEY=... (for Glassdoor scraping)
```

### Lovable Access Code

- Code: `SDFNKL789`
- Claim at: lovable.dev

### Deployment Platforms

- **Frontend:** Lovable auto-deploys to Vercel
- **Backend Options:**
  1. Railway (easiest - `railway up`)
  2. Render (free tier)
  3. Fly.io (fast deploys)

---

## RISK MITIGATION

### Risk: Lovable Generates Broken Code

**Mitigation:**

- Test each prompt incrementally
- Keep prompts simple and focused
- Have ChatGPT ready to debug
- Worst case: Use Create React App + Tailwind manually

### Risk: Claude API Rate Limits

**Mitigation:**

- Use Account 2 ($25) first
- Switch to Account 3 ($25) if hitting limits
- Implement exponential backoff
- Use Haiku for non-critical tasks

### Risk: Backend Deploy Fails

**Mitigation:**

- Test deploy early (Hour 5)
- Have Railway AND Render accounts ready
- Keep local version running as backup
- Use ngrok for emergency public URL

### Risk: InterviewAI Too Complex

**Mitigation:**

- Build Documents pipeline FIRST
- InterviewAI is Phase 2 (optional)
- Can demo with mock voice if ElevenLabs fails
- Judges care more about Documents working perfectly

### Risk: Team Member No-Show

**Mitigation:**

- Solo contingency plan: Focus only on Documents + Discovery
- Skip InterviewAI, skip Dashboard
- Use pre-built shadcn/ui templates

---

## SPONSOR PRIZE STRATEGY

### Target Prizes

**Primary Target: Track 1 Winner ($250 - Blaxel)**

- Emphasize agent architecture
- Show autonomous behavior (InterviewAI)
- Highlight tool use (Claude, ElevenLabs)
- Demonstrate failure handling (White Circle safety checks)

**Secondary Target: Best Project ($1500 ElevenLabs Credits)**

- Make InterviewAI the centerpiece
- Speech-to-Speech demo MUST work
- Show multiple interviewer personalities
- Practice demo extensively

**Tertiary Target: Top 3 Overall ($750 / $500 / $250)**

- Polish, polish, polish
- Professional UI/UX
- Working end-to-end flows
- Compelling demo story

### Judging Criteria (Based on Sponsor Priorities)

- **Technical Depth:** Multi-agent architecture, Claude prompts, API integrations
- **Production-Ready:** Error handling, loading states, professional UI
- **Sponsor Integration:** All 7 sponsors mentioned in demo
- **Demo Quality:** Clear value prop, smooth execution, time management

---

## BACKUP PLAN (If Behind Schedule)

### At Hour 6 (3:00 PM) - Checkpoint

**Ask: "Can we ship Documents + Discovery by 4:00 PM?"**

**If YES:** Continue with plan, add InterviewAI
**If NO:** Cut scope immediately:

**Simplified Scope:**

- ✅ Documents: Resume + Cover only (skip ForgeScore)
- ✅ Discovery: Company Intelligence only (skip ContactFinder)
- ❌ InterviewAI: CUT (show mockup instead)
- ❌ Dashboard: CUT (show roadmap slide)

**New Demo Focus:**
"We built the core automation layer -- intelligent document generation with company research. InterviewAI is our next feature (show designs)."

---

## POST-HACKATHON PLAN

### If We Win

- [ ] Clean up code
- [ ] Add authentication
- [ ] Deploy to production domain
- [ ] Share on LinkedIn + Twitter
- [ ] Submit to Product Hunt
- [ ] Consider YC application

### If We Don't Win

- [ ] Still ship to production
- [ ] Open source on GitHub
- [ ] Write technical blog post
- [ ] Add to portfolio
- [ ] Use for actual job search!

---

## SUBMISSION CHECKLIST (4:30 PM)

### Code Submission

- [ ] GitHub repo is public
- [ ] README.md with setup instructions
- [ ] .env.example file (no real keys)
- [ ] All code committed and pushed
- [ ] Tag release: `v1.0-hackathon`

### Demo Assets

- [ ] 2-minute demo video recorded (optional but recommended)
- [ ] Screenshots of all features
- [ ] Slide deck (5 slides max)
- [ ] Demo script printed/ready

### Platform Submission (Iterate)

- [ ] Team registered
- [ ] Project submitted with:
  - Name: "CareerForge"
  - Description: "AI-Powered Job Search Command Center"
  - Track: "Build an Agent"
  - GitHub link
  - Demo link (Vercel URL)
  - Screenshots

---

## EMERGENCY CONTACTS

### Mentors (Discord)

- Check `#mentors` channel for technical help
- Tag mentors with specific questions
- Don't wait until last hour to ask for help

### Organizers

- Control Room: Room 350
- Discord: `#org-team`

### Sponsor Channels (Discord)

- `#anthropic-support`
- `#elevenlabs-support`
- `#lovable-support`
- `#blaxel-support`

---

## FINAL PRE-HACKATHON CHECKLIST

### Night Before (Feb 13)

- [ ] Laptop charged, charger packed
- [ ] All API keys ready and tested
- [ ] GitHub repo created
- [ ] Lovable code claimed
- [ ] Team roles assigned
- [ ] Prompts document shared
- [ ] Good night's sleep!

### Morning Of (Feb 14, 8:30 AM)

- [ ] Arrive early (8:30 AM for breakfast)
- [ ] Find team members
- [ ] Claim good seats near power outlets
- [ ] Connect to WiFi
- [ ] Test internet speed
- [ ] Review implementation plan
- [ ] Join Discord channels
- [ ] Register team on Iterate platform

---

## PRESENTATION SLIDE DECK (5 Slides)

**Slide 1: Problem**

- "Job searching is broken"
- Stats: 200+ applications, 2% response rate
- Hours wasted on documents, research, prep

**Slide 2: Solution**

- CareerForge = AI Command Center
- Screenshot of Documents tab
- "Automate the grunt work, focus on connections"

**Slide 3: Demo**

- Live demo (or video)
- Show Documents → Discovery → Interview flow

**Slide 4: Technical Architecture**

- Agent diagram
- Sponsor logos
- "Production-ready with Blaxel, Claude, ElevenLabs"

**Slide 5: Impact + Next Steps**

- Target users: International students, career switchers
- Traction (if any): "Used by X people"
- Vision: "YC-backed job search automation"

---

## SUCCESS METRICS

### Demo Success

- ✅ No crashes during 2-minute demo
- ✅ All transitions smooth
- ✅ Audience says "wow" at least once
- ✅ Questions from judges (shows interest)

### Technical Success

- ✅ Frontend loads in <2 seconds
- ✅ API responses in <3 seconds
- ✅ No CORS errors
- ✅ Works on judge's laptop (bring backup)

### Team Success

- ✅ Everyone contributed meaningfully
- ✅ No burnout or stress
- ✅ Learned new skills
- ✅ Had fun!

---

## REMEMBER

1. **Ship over Perfect** - A working 70% solution beats a broken 100% solution
2. **Demo First** - Build what you can show, not what's technically impressive
3. **Sponsors Matter** - Mention ALL sponsors in demo (even if integration is conceptual)
4. **Time Management** - Stick to the timeline, cut scope aggressively if needed
5. **Story > Tech** - Judges remember compelling narratives, not code quality
6. **Energy Matters** - Stay hydrated, take breaks, maintain positive vibes
7. **Backup Everything** - Local copies, screenshots, video recordings
8. **Practice Demo** - 3x run-throughs minimum
9. **Ask for Help** - Mentors are there to help, use them!
10. **Have Fun** - This is a learning experience, not life-or-death

---

## LET'S WIN THIS! 🚀

**Team Mantra:** "Fast, functional, and f***ing impressive."

**Go Time:** 9:30 AM, Feb 14, 2026

**See you at the podium.** 🏆
