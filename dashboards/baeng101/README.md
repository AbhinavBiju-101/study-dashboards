# BAENG101 Modules 3 & 4: Flask notes, dashboard and quiz
    pip install -r requirements.txt
    python app.py     # http://127.0.0.1:5000
Routes: `/` dashboard, `/module/3`, `/module/4` illustrated notes, `/quiz` setup, `POST /quiz/start`.
Data: `data/syllabus.json` (modules, topics, subtopic summaries, note anchors), `data/quiz_bank.json` (424 questions with Bloom's levels).
Notes live in `templates/module3.html` and `templates/module4.html`. Quiz progress is kept in the browser (localStorage).
