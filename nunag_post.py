
from flask import Flask, request, jsonify
from datetime import date

app = Flask(__name__)

attendance_records = []

@app.route('/post/attendance', methods=['POST'])
def add_attendance():

    data = request.get_json()

    student_id = data.get("student_id")
    student_name = data.get("student_name")
    attendance_date = data.get("date", str(date.today()))
    status = data.get("status", "Present po ako po")

    if not student_id or not student_name:
        return jsonify({
            "error": "Student ID and student name are required"
        }), 400

    attendance = {
        "student_id": student_id,
        "student_name": student_name,
        "date": attendance_date,
        "status": status
    }

    attendance_records.append(attendance)

    return jsonify({
        "message": "Attendance added successfully!",
        "attendance": attendance
    }), 201


if __name__ == '__main__':
    app.run(debug=True)
