from flask import Flask, jsonify, request

app = Flask(__name__)

attendance = [
    {
        "id": 1,
        "student_id": "2024-0001",
        "student_name": "Montero, Lovendin Jade D.",
        "event": "event ng mga pogi lang.",
        "status": "present",
    },
    {
        "id": 2,
        "student_id": "2024-0002",
        "student_name": "Agustin, Kian Gabriel P.",
        "event": "awarding of most handsome person in the world",
        "status": "present",
    }
    {"id: 3
     "student_id": "2024-0002",
     "student_name": "David Kimberly p.",
     "event": "pak ganern competition",
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
#Kim part get method to get attendance by id
@app.route("/attendance/<student_id>", methods=["GET"])
def get_attendance_by_studentID(student_id):
    records = [r for r in attendance if r["student_id"] == student_id]
    if not records:
        return jsonify({"success": False, "message": "Student not found"}), 404
    return jsonify({"success": True, "data": records}), 200
if __name__ == "__main__":
    app.run(debug=True)
