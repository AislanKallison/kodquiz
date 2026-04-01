from flask import Flask, render_template, request, redirect, url_for, session
import sys

app = Flask(__name__)
app.secret_key = 'kodland_secret'

# ====================== PERGUNTAS DO QUIZ ======================
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

# ====================== QUIZ NO TERMINAL ======================
def run_terminal_quiz():
    print("\n" + "="*55)
    print("   🎯  KODQUIZ - MODO TERMINAL")
    print("="*55)
    
    score = 0
    for q in questions:
        print(f"\nPergunta {q['id']}: {q['question']}")
        for option in q['options']:
            print(option)
        
        answer = input("\nSua resposta (a/b/c/d): ").strip().lower()
        
        if answer == q['correct']:
            print("✅ Correto!\n")
            score += 1
        else:
            print(f"❌ Errado! Resposta correta: {q['correct']}")
            print(f"   {q['explanation']}\n")
    
    print("="*55)
    print(f"RESULTADO FINAL: {score}/{len(questions)} acertos")
    if score == 8:
        print("🏆 Parabéns! Você gabaritou o quiz!")
    elif score >= 6:
        print("👏 Muito bom!")
    else:
        print("📚 Continue estudando Python!")
    print("="*55 + "\n")


# ====================== ROTAS WEB ======================
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


# ====================== EXECUÇÃO ======================
if __name__ == '__main__':
    # Pergunta simples: quer rodar no terminal ou na web?
    print("KodQuiz iniciado!")
    print("Como você quer rodar?")
    print("1 → Apenas no navegador (Web)")
    print("2 → Apenas no terminal (Texto)")
    
    escolha = input("\nDigite 1 ou 2: ").strip()

    if escolha == "2":
        # Roda só o quiz no terminal e termina
        run_terminal_quiz()
        print("Programa finalizado.")
        sys.exit(0)
    
    else:
        # Roda o servidor web (padrão)
        print("\n🚀 Iniciando o servidor web...")
        print("Acesse no navegador: http://127.0.0.1:5000")
        print("Pressione Ctrl + C para parar\n")
        app.run(host='127.0.0.1', port=5000, debug=True)