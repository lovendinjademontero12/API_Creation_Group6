from flask import Flask, jsonify, request

app = Flask(__name__)

attendance = [
    {
        "id": 1,
        "student_id": "2024-0001",
        "student_name": "Montero, Lovendin Jade D.",
        "event": "event ng mga pogi lang.",
        "status": "present",
    }
]

VALID_STATUSES = ["present", "late", "absent"]


def find_record(record_id):
    """Return the record with the given id, or None if it doesn't exist."""
    for record in attendance:
        if record["id"] == record_id:
            return record
    return None


def next_id():
    """Generate the next id, safe even after deletions."""
    return max((r["id"] for r in attendance), default=0) + 1


@app.route("/")
def home():
    return jsonify({"message": "Campus Event Attendance API is running"})

#KIAN PART GET METHOD TO LIST ALL ATTENDANCE
@app.route("/attendance", methods=["GET"])
def get_all_attendance():
    """Retrieve all attendance records."""
    return jsonify({
        "success": True,
        "count": len(attendance),
        "data": attendance
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
