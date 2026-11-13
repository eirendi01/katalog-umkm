
from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Keripik Pisang", "price": 15000},
    {"id": 2, "name": "Kopi Lokal", "price": 25000},
    {"id": 3, "name": "Tas Anyaman", "price": 45000}
]

@app.route("/")
def home():
    items = ""
    for p in products:
        items += f"<li>{p['name']} - Rp{p['price']:,}</li>"

    return f"""
    <h1>Katalog Produk UMKM</h1>
    <p>Contoh aplikasi menggunakan Docker.</p>
    <ul>{items}</ul>
    <a href="/api/products">Lihat Data Produk (API)</a>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy")

@app.route("/api/products")
def api_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
