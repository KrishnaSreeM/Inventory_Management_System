from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ==============================
# DATABASE MODELS
# ==============================
class Product(db.Model):
    product_id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    movements = db.relationship('ProductMovement', backref='product', lazy=True)

class Location(db.Model):
    location_id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    from_movements = db.relationship('ProductMovement', foreign_keys='ProductMovement.from_location', backref='from_loc', lazy=True)
    to_movements = db.relationship('ProductMovement', foreign_keys='ProductMovement.to_location', backref='to_loc', lazy=True)

class ProductMovement(db.Model):
    movement_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    from_location = db.Column(db.String(20), db.ForeignKey('location.location_id'))
    to_location = db.Column(db.String(20), db.ForeignKey('location.location_id'))
    product_id = db.Column(db.String(20), db.ForeignKey('product.product_id'))
    qty = db.Column(db.Integer, nullable=False)


# ==============================
# ROUTES
# ==============================
@app.route('/')
def index():
    return render_template('index.html')

# --- Product Routes ---
@app.route('/products')
def view_products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@app.route('/add_product', methods=['POST'])
def add_product():
    pid = request.form['product_id']
    name = request.form['name']
    db.session.add(Product(product_id=pid, name=name))
    db.session.commit()
    return redirect(url_for('view_products'))

# --- Location Routes ---
@app.route('/locations')
def view_locations():
    locations = Location.query.all()
    return render_template('locations.html', locations=locations)

@app.route('/add_location', methods=['POST'])
def add_location():
    lid = request.form['location_id']
    name = request.form['name']
    db.session.add(Location(location_id=lid, name=name))
    db.session.commit()
    return redirect(url_for('view_locations'))

# --- Product Movement Routes ---
@app.route('/movements')
def view_movements():
    movements = ProductMovement.query.all()
    return render_template('movements.html', movements=movements,
                           products=Product.query.all(), locations=Location.query.all())

@app.route('/add_movement', methods=['POST'])
def add_movement():
    movement = ProductMovement(
        product_id=request.form['product_id'],
        from_location=request.form['from_location'] or None,
        to_location=request.form['to_location'] or None,
        qty=int(request.form['qty'])
    )
    db.session.add(movement)
    db.session.commit()
    return redirect(url_for('view_movements'))

# --- Report Route ---
@app.route('/report')
def report():
    # --- Movement details ---
    movements = ProductMovement.query.order_by(ProductMovement.timestamp.desc()).all()

    # --- Balance details ---
    products = Product.query.all()
    locations = Location.query.all()
    report_data = []

    for loc in locations:
        for prod in products:
            moved_in = db.session.query(db.func.sum(ProductMovement.qty)) \
                .filter_by(product_id=prod.product_id, to_location=loc.location_id).scalar() or 0
            moved_out = db.session.query(db.func.sum(ProductMovement.qty)) \
                .filter_by(product_id=prod.product_id, from_location=loc.location_id).scalar() or 0
            balance = moved_in - moved_out
            if balance != 0:
                report_data.append((prod.name, loc.name, balance))

    return render_template('report.html', movements=movements, report=report_data)




# ==============================
# MAIN
# ==============================
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
