import os
import psycopg2
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)


def get_conn():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "appdb"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "changeme"),
    )


PAGE = """
<!doctype html>
<title>Lab Booking</title>
<h1>Laboratory Booking</h1>
<p><a href="/">Book</a> | <a href="/bookings">All bookings</a></p>
{% if error %}<p style="color:red">{{ error }}</p>{% endif %}
{% if equipment is defined %}
<form method="post" action="/book">
  <input name="student" placeholder="Student name" required>
  <select name="equipment_id">
    {% for e in equipment %}<option value="{{ e[0] }}">{{ e[1] }}</option>{% endfor %}
  </select>
  <input type="date" name="date" required>
  <select name="time">
    <option>09:00-11:00</option>
    <option>11:00-13:00</option>
    <option>13:00-15:00</option>
  </select>
  <button>Reserve</button>
</form>
{% endif %}
{% if rows is defined %}
<table border="1" cellpadding="6">
<tr><th>Equipment</th><th>Student</th><th>Date</th><th>Time</th></tr>
{% for r in rows %}<tr>{% for c in r %}<td>{{ c }}</td>{% endfor %}</tr>{% endfor %}
</table>
{% endif %}
"""


@app.route("/")
def index():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM equipment ORDER BY id")
    eq = cur.fetchall()
    conn.close()
    return render_template_string(PAGE, equipment=eq, error=request.args.get("error"))


@app.route("/book", methods=["POST"])
def book():
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO bookings (equipment_id, student_name, slot_date, slot_time) "
            "VALUES (%s,%s,%s,%s)",
            (request.form["equipment_id"], request.form["student"],
             request.form["date"], request.form["time"]),
        )
        conn.commit()
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        conn.close()
        return redirect("/?error=This slot is already booked")
    conn.close()
    return redirect("/bookings")


@app.route("/bookings")
def bookings():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """SELECT e.name, b.student_name, b.slot_date, b.slot_time
           FROM bookings b JOIN equipment e ON e.id = b.equipment_id
           ORDER BY b.slot_date, b.slot_time"""
    )
    rows = cur.fetchall()
    conn.close()
    return render_template_string(PAGE, rows=rows)


@app.route("/health")
def health():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
