# n8n-automatic-job-applier
End to end application to job seeker


job-automation/
│
├── docker-compose.yml
├── .env
│
├── n8n/
│   └── workflows/
│
├── backend/
│   ├── app.py
│   ├── ai/
│   │   ├── scorer.py
│   │   ├── resume_generator.py
│   │   └── cover_letter.py
│   │
│   ├── db/
│   │   ├── models.py
│   │   └── database.py
│   │
│   └── templates/
│       ├── resume.docx
│       └── cover_letter.docx
│
├── dashboard/
│   ├── index.html
│   ├── jobs.html
│   └── review.html
│
└── postgres/
