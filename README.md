# Django Inertia Vite React

A modern web application stack combining Django, Inertia.js, Vite, and React with TypeScript support.

## Tech Stack

- **Backend**: Django 5.2
- **Frontend**: React with TypeScript
- **Build Tool**: Vite
- **State Management**: Inertia.js
- **Package Manager**: pnpm

## Features

- Full-stack TypeScript support
- Hot Module Replacement (HMR)
- Modern React with TypeScript
- Django backend with Inertia.js integration
- Vite for fast development and optimized builds
- CSRF protection
- Progress indicators for page transitions

## Prerequisites

- Python 3.13+
- Node.js 20+
- pnpm

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd django-inertia-vite-react
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Install Node.js dependencies:
```bash
pnpm install
```

5. Start the development servers:

In one terminal:
```bash
pnpm dev
```

In another terminal:
```bash
python manage.py runserver
```

## Project Structure

```
django-inertia-vite-react/
├── app/                    # Django app directory
├── config/                 # Django project settings
├── static/                 # Static files
│   └── src/               # Frontend source files
│       ├── pages/         # React page components
│       └── main.tsx       # Frontend entry point
├── templates/             # Django templates
├── vite.config.ts         # Vite configuration
├── tsconfig.json          # TypeScript configuration
└── manage.py             # Django management script
```

## Development

- Frontend code is in `static/src/`
- Backend code is in `app/` and `config/`
- Templates are in `templates/`

## Building for Production

1. Build the frontend:
```bash
pnpm build
```

2. Collect static files:
```bash
python manage.py collectstatic
```
