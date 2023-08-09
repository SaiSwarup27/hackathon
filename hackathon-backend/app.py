from flask import Flask, jsonify, redirect, render_template
import subprocess

app = Flask(__name__)

@app.route("/execute-python", methods=["GET"])
def execute_python_script():
    print("executing python script...")
    try:
        subprocess.run(["python", "hackathon.py"], check=True)
        print("python execution completed")
        return redirect('/')
    except subprocess.CalledProcessError:
        return jsonify({"error": "Error executing script"}), 500
    except Exception:
        print("Error")

@app.route("/", methods=["GET", "POST"])
def eshow():
    with open('output.txt', 'r') as file:
        text_content = file.readlines()
    return render_template("index.html", text_content=text_content)
if __name__ == "__main__":
    app.run(debug=True)
