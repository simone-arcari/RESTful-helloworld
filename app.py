from flask import Flask, jsonify, request

app = Flask(__name__)

# Dati fittizi
students = [
    {"id": 1, "name": "Mario Rossi", "age": 22, "course": "Informatica"},
    {"id": 2, "name": "Luigi Bianchi", "age": 24, "course": "Matematica"}
]

# Ottieni tutti gli studenti
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# Ottieni uno studente specifico
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if student:
        return jsonify(student)
    return jsonify({"error": "Studente non trovato"}), 404

# Aggiungi un nuovo studente
@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.json
    new_student["id"] = max(s["id"] for s in students) + 1
    students.append(new_student)
    return jsonify(new_student), 201

# Modifica uno studente esistente
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if student:
        data = request.json
        student.update(data)
        return jsonify(student)
    return jsonify({"error": "Studente non trovato"}), 404

# Elimina uno studente
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [s for s in students if s["id"] != student_id]
    return jsonify({"message": "Studente eliminato"}), 200

if __name__ == '__main__':
    app.run(debug=True)
