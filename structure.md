labbook-4ways/
├── README.md                       👤 1   كيف تشغّل النظام كله
├── .gitignore                      👤 1
├── CONTRIBUTING.md                 👤 1   قواعد branches و commits
│
├── app/                            👤 2
│   ├── app.py (أو server.js)
│   ├── requirements.txt
│   ├── templates/index.html
│   ├── schema.sql                  جدول bookings
│   └── .env.example                بدون passwords حقيقية
│
├── vm/                             👤 3
│   ├── install-steps.md            خطوات قابلة للتكرار
│   ├── nginx-labbook.conf
│   ├── labbook.service             systemd
│   └── screenshots/
│
├── docker/                         👤 4
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── docker-compose.yml          (اختياري)
│   ├── commands.md                 network / volume / run
│   └── screenshots/
│
├── k8s/                            👤 5
│   ├── app-deployment.yaml         2 replicas
│   ├── app-service.yaml
│   ├── commands.md                 healing + scaling
│   └── screenshots/
│
├── hybrid/                         👤 6
│   ├── app-deployment-hybrid.yaml  يتصل بـ IP الـ VM
│   ├── db-service-external.yaml    (اختياري)
│   ├── architecture-diagram.png
│   ├── explanation.md              ليه كل component في مكانه
│   └── screenshots/
│
├── measurements/                   👤 6 + الكل يساهم
│   ├── measurement-plan.md
│   ├── results.csv
│   ├── table7.md
│   └── raw-output/
│
├── report/                         👤 1 يجمّع
│   ├── report.docx (أو .md → PDF)
│   ├── figures/
│   └── ai-usage-statement.md       إلزامي
│
├── presentation/                   👤 1
│   ├── slides.pptx
│   └── speaker-assignment.md
│
├── video/                          👤 6
│   └── README.md                   لينك الفيديو (مش الملف نفسه)
│
└── team/                           👤 1
    ├── roles.md
    ├── weekly-log.md               محاضر + ساعات كل فرد
    └── contributions.md            مصدر D7