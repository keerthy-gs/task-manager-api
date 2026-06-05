from flask import Flask, request, jsonify
from database import get_db_connection, init_db

app = Flask(__name__)

# Initialize database when app starts
with app.app_context():
    init_db()

# ─── GET ALL TASKS ───────────────────────────────────────
@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return jsonify([dict(task) for task in tasks]), 200

# ─── GET ONE TASK ────────────────────────────────────────
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (id,)).fetchone()
    conn.close()
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(dict(task)), 200

# ─── CREATE TASK ─────────────────────────────────────────
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO tasks (title, description) VALUES (?, ?)',
        (data['title'], data.get('description', ''))
    )
    conn.commit()
    conn.close()
    return jsonify({'message': 'Task created successfully'}), 201

# ─── UPDATE TASK ─────────────────────────────────────────
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (id,)).fetchone()
    if task is None:
        conn.close()
        return jsonify({'error': 'Task not found'}), 404
    conn.execute(
        'UPDATE tasks SET title = ?, description = ?, status = ? WHERE id = ?',
        (
            data.get('title', task['title']),
            data.get('description', task['description']),
            data.get('status', task['status']),
            id
        )
    )
    conn.commit()
    conn.close()
    return jsonify({'message': 'Task updated successfully'}), 200

# ─── DELETE TASK ─────────────────────────────────────────
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (id,)).fetchone()
    if task is None:
        conn.close()
        return jsonify({'error': 'Task not found'}), 404
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Task deleted successfully'}), 200

# ─────────────────────────────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True)