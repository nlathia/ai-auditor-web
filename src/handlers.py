from flask import render_template, jsonify, request
from src.data import db, AuditResult

def get_index():
    rows = AuditResult.get_all()
    return render_template("index.html", rows=rows)

def post_audit():
    content = request.get_json()
    result = AuditResult(content)
    db.session.add(result)
    db.session.commit()
    return jsonify({})
