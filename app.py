from flask import render_template
from application import create_app
from dotenv import load_dotenv
from application.models import get_database, Providers


load_dotenv()

app = create_app()




if __name__ == "__main__":
    app.run(debug=False)




@app.route('/')
def index():
    db = get_database()
    providers = db.session.execute(db.select(Providers).order_by(Providers.name)).scalars()
    return render_template("index.html", providers=providers)