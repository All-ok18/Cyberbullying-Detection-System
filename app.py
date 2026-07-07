from flask import Flask, render_template, request, redirect, session, url_for
import joblib
import sqlite3

app = Flask(__name__)
app.secret_key = "cyber123"

model = joblib.load("model.pkl")

ADMIN_EMAIL = "admin@gmail.com"
ADMIN_PASSWORD = "admin123"


# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT * FROM users
            WHERE email=?
            AND password=?
            """,
            (email, password)
        )

        user = cursor.fetchone()

        conn.close()

        if user:

            session["user"] = email

            return redirect(
                url_for("predict_page")
            )

        return render_template(
            "login.html",
            error="Wrong Email or Password"
        )

    return render_template(
        "login.html"
    )
# HOME
@app.route("/")
def home():

    return render_template(
        "index.html"
    )
    
    
#prdecition page
@app.route("/predict-page")
def predict_page():

    if "user" not in session:

        return redirect(
            url_for("login")
        )

    return render_template(
        "predict.html"
    )
    

# SIGNUP
@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm = request.form["confirm_password"]

        if password != confirm:

            return render_template(
                "signup.html",
                error="Passwords do not match"
            )

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users
            (name,email,password)
            VALUES (?,?,?)
            """,
            (name,email,password)
        )

        conn.commit()
        conn.close()

        return redirect(
            url_for("login")
        )

    return render_template(
        "signup.html"
    )


# PREDICT
@app.route("/predict", methods=["POST"])
def predict():

    if "user" not in session:

        return redirect(
            url_for("login")
        )

    text = request.form["sentence"]

    result = str(
        model.predict([text])[0]
    ).lower()

    safe_words = [
    "like",
    "good",
    "nice",
    "thank",
    "love",
    "happy",
    "great"
]

    if any(word in text.lower() for word in safe_words):
        result = "not_cyberbullying"

        output = """
✅ Non Cyberbullying

Reason:
The text does not contain harmful or offensive language.

Suggestion:
Continue using respectful and positive communication.
"""

    else:

        text_lower = text.lower()

        if "hate" in text_lower:

            output = """
⚠ Cyberbullying Detected

Reason:
The sentence contains hostile and aggressive language.

Impact:
This type of language may hurt a person's feelings and create a harmful online environment.

Suggestion:
Express disagreement politely without using offensive language.
"""

        elif "stupid" in text_lower:

            output = """
⚠ Cyberbullying Detected

Reason:
The sentence contains insulting language targeting an individual.

Impact:
Personal insults can reduce confidence and self-esteem.

Suggestion:
Use respectful and constructive words when communicating online.
"""

        elif "idiot" in text_lower:

            output = """
⚠ Cyberbullying Detected

Reason:
The sentence contains offensive language.

Impact:
Offensive comments may cause emotional distress.

Suggestion:
Avoid name-calling and communicate respectfully.
"""

        else:

            output = f"""
⚠ Cyberbullying Detected

Category:
{result}

Reason:
The text contains harmful or abusive language.

Impact:
Cyberbullying can negatively affect mental health and emotional well-being.

Suggestion:
Use positive and respectful communication.
"""

    try:

        conn = sqlite3.connect(
            "database.db",
            timeout=30
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO history
            (
            user_email,
            text_data,
            prediction
            )
            VALUES
            (
            ?,
            ?,
            ?
            )
            """,
            (
                session["user"],
                text,
                result
            )
        )

        conn.commit()

    except Exception as e:

        print("Database Error:", e)

    finally:

        conn.close()

    return render_template(
        "predict.html",
        prediction=output,
        sentence=text
    )


# ABOUT
@app.route("/about")
def about():

    return render_template(
        "about.html"
    )

# LOGOUT
@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("login")
    )

@app.route(
"/admin",
methods=["GET","POST"]
)
def admin():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        if (
            email == ADMIN_EMAIL
            and
            password == ADMIN_PASSWORD
        ):

            session["admin"] = True

            return redirect(
                url_for(
                    "dashboard"
                )
            )

    return render_template(
        "admin_login.html",
        error=None
    )

@app.route("/dashboard")
def dashboard():

    if "admin" not in session:

        return redirect(
            url_for("admin")
        )

    conn = sqlite3.connect(
        "database.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM users"
    )

    total_users = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM history"
    )

    total_predictions = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT *
        FROM history
        ORDER BY created_at DESC
        """
    )

    activities = cursor.fetchall()

    conn.close()

    return render_template(
        "dashboard.html",
        total_users=total_users,
        total_predictions=total_predictions,
        activities=activities
    )
    
if __name__ == "__main__":

    app.run(
        debug=True
    )