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
- role: "intern", "fte" (full-time / placement) or "unknown".
- source_ids: ids of the messages this share came from.
- questions: one entry per question with a short title, the full question text (transcribed
  from attachments when needed; include constraints and examples if visible), and 1-3 topics
  from exactly this list: {topics}

Return {{"shares": []}} if no message shares OA questions.

Messages:

{messages}
