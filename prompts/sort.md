You are sorting messages from an Indian campus-placement group chat where students share
online-assessment (OA) questions from companies' hiring tests.

Below are chat messages. Each starts with `[id] date college-tag` of the poster (e.g. IITD =
IIT Delhi, NITR = NIT Rourkela, KGP/IITKGP = IIT Kharagpur). A message may be a reply (the
replied-to text is shown), and may have an attachment path. Attachments are screenshots or
PDFs of OA questions: open them with the Read tool and transcribe the questions.

Find every message (or group of consecutive messages) that actually shares OA questions.
Ignore requests ("anyone has X OA?"), greetings, results, referrals and other chatter.
For each share, return:
- company: the hiring company. Reuse one of these existing names when it matches: {companies}
- college: full canonical name of the campus where the OA was held, e.g. "IIT Kharagpur",
  "IIT Bombay", "NIT Trichy". Use the poster's college tag unless the text says otherwise.
  Use "Unknown" if there is no clue.
- date: YYYY-MM-DD the OA was held if the message says so ("yesterday", "on 12th"),
  otherwise the message date.
- role: "intern" if the message or the replied-to text mentions an internship (intern, SDE
  intern, summer intern); otherwise "fte" (full-time), because these are placement groups.
  Use "unknown" only for prep material not tied to one hiring drive.
- source_ids: ids of the messages this share came from.
- questions: one entry per question:
  - title: a short, specific title ("Longest substring without repeats", not "Coding Q1").
  - text: the full question as asked, in Markdown. Transcribe attachments when needed. Keep
    every number, constraint and example exactly. Put input/output examples and code in
    fenced code blocks (```), and put each MCQ option on its own line ("A. ...").
    Never invent details. If the poster only half-remembered the question, write what they
    gave and add one short line saying what is missing.
  - topics: 1-3 from exactly this list: {topics}
    Prefer a specific topic to "Other". Electronics and electrical questions go to Circuits,
    Analog Electronics, Digital Electronics, Signals & Systems, Control Systems or
    Communication; mechanical engineering to Mechanical; "predict the output" or "find the
    error" code questions to Code Output (C/C++/Java/Python); English grammar and reading to
    Verbal. A message that only describes what an OA contained (sections, number of
    questions, topics) is one entry with topic OA Format.
  - leetcode: only for a coding question with a clear statement: if it is the same problem as
    a LeetCode problem, or a close variant of one (same core task), its LeetCode number and
    exact title. Otherwise null. Never guess; null is always acceptable.

Return {{"shares": []}} if no message shares OA questions.

Messages:

{messages}
