# Personal Website (Flask)

A clean, application-ready portfolio for college applications.

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Visit http://127.0.0.1:5000/

## Customize Content

Edit `data.py`:
- Add awards in `AWARDS`
- Add quotes to `TESTIMONIALS`
- Add projects to `PROJECTS`

Update the hero text and contact info in `templates/home.html`.
Replace `static/img/profile.svg` with your photo named `profile.jpg` or `profile.png` and update the `<img>` path.

## Deploy (one easy option: Render)

1. Push this folder to a GitHub repo.
2. On [Render](https://render.com), create a new Web Service from your repo.
3. Set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
4. Add a `render.yaml` later if you want infra-as-code.

(You can also use Railway, Fly.io, or a school server.)

## Structure

```
personal_site_flask/
├─ app.py
├─ data.py
├─ requirements.txt
├─ templates/
│  ├─ base.html
│  ├─ home.html
│  ├─ awards.html
│  ├─ testimonials.html
│  └─ projects.html
└─ static/
   ├─ css/
   │  └─ styles.css
   └─ img/
      ├─ profile.svg
      └─ favicon.svg
```

Good luck on your applications!
