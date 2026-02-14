import os
from flask import Flask, render_template, jsonify
from models import (
    init_db, get_all_projects, get_all_services,
    get_all_skills, get_approved_testimonials
)
from seed_db import seed

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production-aditya-2026'


# ─── Initialize & seed DB on startup ───────────────────────

with app.app_context():
    init_db()
    seed()


# ═══════════════════════════════════════════════════════════
#  PUBLIC ROUTES
# ═══════════════════════════════════════════════════════════

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/services')
def services():
    services = get_all_services()
    return render_template('services.html', services=services)


@app.route('/projects')
def projects():
    projects = get_all_projects()
    return render_template('projects.html', projects=projects)


@app.route('/testimonials')
def testimonials():
    testimonials = get_approved_testimonials()
    return render_template('testimonials.html', testimonials=testimonials)


@app.route('/contact')
def contact():
    return render_template('contact.html')


# ─── API endpoints for Vue.js ────────────────────────────────

@app.route('/api/projects')
def api_projects():
    projects = get_all_projects()
    return jsonify([dict(p) for p in projects])


@app.route('/api/services')
def api_services():
    services = get_all_services()
    return jsonify([dict(s) for s in services])


@app.route('/api/skills')
def api_skills():
    skills = get_all_skills()
    return jsonify([dict(s) for s in skills])


# ═══════════════════════════════════════════════════════════
#  RUN
# ═══════════════════════════════════════════════════════════

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
