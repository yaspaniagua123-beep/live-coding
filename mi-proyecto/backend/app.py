from flask import Flask, request, jsonify, session
from flask_cors import CORS
from utils import init_db, hash_password, check_password, get_db_connection

app = Flask(__name__)
app.secret_key = 'supersecretkey'  
CORS(app, supports_credentials=True)

init_db()

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    usuario = data.get('usuario')
    email = data.get('email')
    password = data.get('password')

    if not usuario or not email or not password:
        return jsonify({'error':'Todos los campos son obligatorios'}), 400

    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO usuarios (usuario,email,password) VALUES (?,?,?)',
                     (usuario,email,hash_password(password)))
        conn.commit()
        return jsonify({'message':'Usuario registrado correctamente'}), 201
    except:
        return jsonify({'error':'Usuario o email ya existe'}), 400
    finally:
        conn.close()

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    password = data.get('password')

    if not usuario or not password:
        return jsonify({'error':'Todos los campos son obligatorios'}), 400

    conn = get_db_connection()
    user = conn.execute('SELECT * FROM usuarios WHERE usuario = ?', (usuario,)).fetchone()
    conn.close()

    if user and check_password(user['password'], password):
        session['user_id'] = user['id']
        session['usuario'] = user['usuario']
        return jsonify({'message':'Login exitoso'})
    else:
        return jsonify({'error':'Usuario o contraseña incorrectos'}), 401

@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message':'Sesión cerrada'})

@app.route('/api/mensajes', methods=['GET','POST'])
def mensajes():
    conn = get_db_connection()

    if request.method == 'POST':
        if 'user_id' not in session:
            return jsonify({'error':'No autenticado'}), 401
        data = request.get_json()
        texto = data.get('texto','').strip()
        if not texto:
            return jsonify({'error':'Mensaje vacío'}), 400
        conn.execute('INSERT INTO mensajes (user_id,texto) VALUES (?,?)',
                     (session['user_id'], texto))
        conn.commit()
        conn.close()
        return jsonify({'message':'Mensaje publicado'}), 201

    msgs = conn.execute('''
        SELECT m.id,u.usuario as autor,m.texto,m.created_at 
        FROM mensajes m JOIN usuarios u ON u.id = m.user_id 
        ORDER BY m.created_at DESC LIMIT 50
    ''').fetchall()
    conn.close()
    return jsonify([{'id':m['id'],'autor':m['autor'],'texto':m['texto'],'fecha':m['created_at']} for m in msgs])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')