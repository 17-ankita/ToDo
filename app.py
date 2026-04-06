from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        with open("tasks.txt", "a") as f:
            f.write(task + "\n")
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()
    tasks.pop(id)
    with open("tasks.txt", "w") as f:
        f.writelines(tasks)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)