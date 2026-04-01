from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'kodland_secret'

# Perguntas do quiz
questions = [
    {"id": 1, "question": "Qual comando imprime algo na tela?", 
     "options": ["a) print()", "b) echo()", "c) console.log()", "d) display()"], 
     "correct": "a", "explanation": "print() é a função correta."},
    {"id": 2, "question": "Como se cria uma variável?", 
     "options": ["a) var x = 10", "b) x = 10", "c) let x = 10", "d) int x = 10"], 
     "correct": "b", "explanation": "Basta atribuir o valor."},
    {"id": 3, "question": "Qual estrutura usamos para repetir código?", 
     "options": ["a) for", "b) repeat", "c) loop", "d) while only"], 
     "correct": "a", "explanation": "O for é muito usado."},
    {"id": 4, "question": "O que 'if' significa?", 
     "options": ["a) if-else", "b) Condicional", "c) Loop", "d) Função"], 
     "correct": "b", "explanation": "if serve para decisões."},
    {"id": 5, "question": "Como definir uma função?", 
     "options": ["a) def nome():", "b) function nome():", "c) create nome():", "d) func nome():"], 
     "correct": "a", "explanation": "Usamos a palavra def."},
    {"id": 6, "question": "Qual tipo representa números inteiros?", 
     "options": ["a) int", "b) float", "c) str", "d) bool"], 
     "correct": "a", "explanation": "int é para números inteiros."},
    {"id": 7, "question": "O que len() faz?", 
     "options": ["a) Retorna o tamanho", "b) Soma valores", "c) Imprime", "d) Define variáveis"], 
     "correct": "a", "explanation": "len() retorna o comprimento."},
    {"id": 8, "question": "Como importar uma biblioteca?", 
     "options": ["a) import nome", "b) include nome", "c) use nome", "d) require nome"], 
     "correct": "a", "explanation": "O comando é import."}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    results = []
    for q in questions:
        answer = request.form.get(f'q_{q["id"]}')
        correct = answer == q["correct"]
        if correct:
            score += 1
        results.append({
            "question": q["question"],
            "user_answer": answer or "Não respondeu",
            "correct_answer": q["correct"],
            "explanation": q["explanation"],
            "is_correct": correct
        })
    session['score'] = score
    session['total'] = len(questions)
    session['results'] = results
    return redirect(url_for('results'))

@app.route('/results')
def results():
    score = session.get('score', 0)
    total = session.get('total', 8)
    results = session.get('results', [])
    return render_template('results.html', score=score, total=total, results=results)

if __name__ == '__main__':
    app.run(debug=True)