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


#Update endpoint ni lovendin
@app.route("/attendance/<int:record_id>", methods=["PUT"])
def update_attendance(record_id):
    record = find_record(record_id)
    if record is None:
        return jsonify({"error": "Record not found"}), 404

    data = request.get_json(silent=True)
    if not data or "status" not in data:
        return jsonify({"error": "status is required"}), 400

    if data["status"] not in VALID_STATUSES:
        return jsonify({"error": "Invalid status. Use: present, late, absent"}), 400

    record["status"] = data["status"]

    return jsonify(record), 200

if __name__ == "__main__":
    app.run(debug=True)