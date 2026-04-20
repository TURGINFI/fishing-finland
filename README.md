# Fishing in Finland for Foreign Anglers

A Dockerized Django MVP for Sara's AISWD personal project. The site is an English web platform for foreign fishing enthusiasts in Finland. It includes public information pages, member features, admin moderation, catch logging, goals, events, and gear recommendations.

## Tech stack
- Django
- PostgreSQL
- Docker + Docker Compose
- Django templates + HTML + CSS + JS
- Django admin

## MVP modules
- Public pages: home, regulations, fish species, methods, events, blog, spots, gear
- Member features: register/login, profile, event registration, blog submission, inbox, catch log, fishing goals, delete account
- Admin: moderate blog posts, manage events, messages, regulations, fish species, gear recommendations, spots

## Quick start in WSL2 Ubuntu
1. Install Docker Desktop and enable WSL2 integration.
2. Open your Ubuntu terminal.
3. Copy `.env.example` to `.env`.
4. Build and start containers:
   ```bash
   docker compose up --build
   ```
5. Open a new terminal and create a superuser:
   ```bash
   docker compose exec web python manage.py createsuperuser
   ```
6. Open the site:
   - App: http://localhost:8000/    # if 8000 is occupied, you can define your port 
   - Admin: http://localhost:8000/admin/  # if 8000 is occupied, you can define your port 

## Useful Docker commands
```bash
docker compose up --build
docker compose down
docker compose logs -f web
docker compose exec web python manage.py createsuperuser
docker compose exec web python manage.py shell
```

## Recommended implementation order
1. Start the project with Docker.
2. Create a superuser and log into Django admin.
3. Add demo data for regulations, fish species, gear, spots, events.
4. Test register/login/profile.
5. Test blog submission and admin moderation.
6. Test event registration, inbox, catch log, goals.
7. Capture screenshots and prompts for Version 2 documentation.
