# AI Job Application Automation

An AI-powered job application pipeline built with n8n, Python, PostgreSQL, and OpenAI.

The system automatically:

* Collects job postings from supported sources
* Scores jobs against a master resume
* Generates ATS-friendly resumes
* Generates tailored cover letters
* Sends review notifications
* Allows manual approval before applying

---

## Features

### Job Collection

* Collect jobs from multiple sources
* Store job data in PostgreSQL
* Prevent duplicate processing

### AI Job Scoring

Evaluate jobs using:

* Skill match
* Experience match
* Role relevance
* Career growth potential
* Salary alignment (optional)

Each job receives a score between 0 and 100.

### ATS Resume Generation

Generate a customized resume for each job:

* ATS-friendly formatting
* Keyword optimization
* Experience prioritization
* Truthful content preservation
* DOCX and PDF export

### Cover Letter Generation

Generate role-specific cover letters based on:

* Job description
* Resume content
* Company information

### Review Workflow

Human-in-the-loop review:

* Approve application
* Reject application
* Open job posting
* Download generated files

### Notifications

Supported channels:

* Telegram
* Email
* Discord (optional)

---

## Architecture

```text
Job Sources
     │
     ▼
Job Collector
     │
     ▼
PostgreSQL
     │
     ▼
AI Job Scorer
     │
     ▼
Score Filter
     │
     ▼
Resume Generator
     │
     ▼
Cover Letter Generator
     │
     ▼
Notification Service
     │
     ▼
Review Dashboard
     │
     ▼
Manual Application Submission
```

---

## Tech Stack

### Workflow Automation

* n8n

### Backend

* Python
* FastAPI

### Database

* PostgreSQL

### AI

* OpenAI API

### Infrastructure

* Docker
* Docker Compose

### Notifications

* Telegram Bot API

---

## Project Structure

```text
job-automation/

├── docker-compose.yml
├── .env

├── n8n/
│   └── workflows/

├── backend/
│   ├── app.py
│   ├── ai/
│   ├── db/
│   ├── services/
│   └── templates/

├── dashboard/

├── postgres/

└── README.md
```

---

## Setup

### Clone Repository

```bash
git clone <repository-url>
cd job-automation
```

### Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key

POSTGRES_DB=jobs
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

TELEGRAM_BOT_TOKEN=your_token
TELEGRAM_CHAT_ID=your_chat_id
```

### Start Services

```bash
docker compose up -d
```

Services:

| Service     | Port |
| ----------- | ---- |
| n8n         | 5678 |
| Backend API | 8000 |
| PostgreSQL  | 5432 |

---

## Workflow

### Step 1

Collect jobs from configured sources.

### Step 2

Store jobs in PostgreSQL.

### Step 3

Score jobs against the master resume.

### Step 4

Filter jobs above the minimum score threshold.

### Step 5

Generate:

* ATS Resume
* Cover Letter

### Step 6

Send review notification.

### Step 7

Approve or reject.

### Step 8

Open application page and submit manually.

---

## API Endpoints

### Score Job

```http
POST /score
```

### Generate Resume

```http
POST /generate-resume
```

### Generate Cover Letter

```http
POST /generate-cover-letter
```

### List Jobs

```http
GET /jobs
```

---

## Security Notes

* Never store API keys in source control.
* Use environment variables.
* Enable authentication for n8n.
* Restrict database access.
* Review generated applications before submission.

---

## Roadmap

### Phase 1

* Job collection
* Job scoring
* Resume generation

### Phase 2

* Cover letter generation
* Telegram notifications
* Review dashboard

### Phase 3

* Skill gap analysis
* Interview preparation packs
* Resume version history
* Analytics dashboard

### Phase 4

* Multi-resume support
* Company research agent
* AI interview simulator

---

## Disclaimer

This project is designed to assist with job discovery and application preparation. Users are responsible for reviewing generated content and complying with the terms of any job platform they use.
