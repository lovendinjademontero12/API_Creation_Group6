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

if __name__ == "__main__":
    app.run(debug=True)

#Update endpoint ni lovendin
@app.route("/attendance/<int:record_id>", methods=["PUT"])
def update_attendance(record_id):
    record = find_record(record_id)
    record_data = request.get_json()
    if record is None:
        return jsonify({"error": "Record not found"}), 404
    
    return jsonify(record), 200
