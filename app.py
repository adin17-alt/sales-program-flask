from flask import Flask, render_template
# from flask_mysqldb import MySQL
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pos"
)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/masterbarang")
def masterbarang():
    cur = db.cursor()
    cur.execute("SELECT * FROM masterbarang")
    barang = cur.fetchall()
    cur.close()
    return render_template('masterbarang.html', menu = 'master', submenu = 'barang', data = barang)

@app.route("/mastersupplier")
def mastersupplier():
    cur = db.cursor()
    cur.execute("SELECT * FROM mastersupplier")
    supplier = cur.fetchall()
    cur.close()
    return render_template('mastersupplier.html', menu = 'master', submenu = 'supplier', data = supplier)

@app.route("/masterpelanggan")
def masterpelanggan():
    cur = db.cursor()
    cur.execute("SELECT * FROM masterpelanggan")
    pelanggan = cur.fetchall()
    cur.close()
    return render_template('masterpelanggan.html', menu = 'master', submenu = 'pelanggan', data = pelanggan)


@app.route("/formpembelian")
def formpembelian():
    return render_template('formpembelian.html', menu = 'pembelian', submenu = 'formpembelian')

@app.route("/datapembelian")
def datapembelian():
    return render_template('datapembelian.html', menu = 'pembelian', submenu = 'datapembelian')


@app.route("/formpenjualan")
def formpenjualan():
    return render_template('formpenjualan.html', menu = 'penjualan', submenu = 'formpenjualan')

@app.route("/datapenjualan")
def datapenjualan():
    return render_template('datapenjualan.html', menu = 'penjualan', submenu = 'datapenjualan')




if __name__ == "__main__":
    app.run(debug=True)