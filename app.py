# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def home():
#     return 'Hello, World!'
#
#
# @app.route('/fun')
# def run_function():
#     return "Function executed successfully!"
#
#
# @app.route('/and_gate')
# def and_gate():
#     # AND gate truth table
#     truth_table = [
#         (0, 0, 0),  # (input1, input2, output)
#         (0, 1, 0),
#         (1, 0, 0),
#         (1, 1, 1),
#     ]
#
#     # Format the truth table as a string
#     table_str = "<h1>AND Gate Truth Table</h1><table border='1'><tr><th>Input 1</th><th>Input 2</th><th>Output</th></tr>"
#     for row in truth_table:
#         table_str += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>"
#     table_str += "</table>"
#
#     return table_str
#
#
# if __name__ == '__main__':
#     app.run(debug=True)



import os
import sqlite3
import subprocess
from datetime import datetime
from flask import Flask, render_template, redirect, url_for
from myhdl import *

app = Flask(__name__,template_folder='templates',static_folder="static")

# Database setup
DATABASE = "gates_simulation.db"

def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS simulation_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        gate_name TEXT NOT NULL,
        log_file TEXT NOT NULL,
        vcd_file TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

create_table()

# Gate logic functions
def AND_Gate(a, b, c):
    @always_comb
    def logic():
        c.next = a & b
    return logic

def OR_Gate(a, b, c):
    @always_comb
    def logic():
        c.next = a | b
    return logic

def NOT_Gate(a, b):
    @always_comb
    def logic():
        b.next = int(not a)
    return logic

def half_adder(a, b, s, c):
    @always_comb
    def logic():
        s.next = a ^ b
        c.next = a & b
    return logic

# Insert log into database
def insert_log(gate_name, log_file, vcd_file):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO simulation_logs (gate_name, log_file, vcd_file)
    VALUES (?, ?, ?)
    ''', (gate_name, log_file, vcd_file))
    conn.commit()
    conn.close()

# Function to run GTKWave
def run_gtkwave(vcd_file):
    subprocess.Popen(["gtkwave", vcd_file])

# Generic function for gate simulation
def simulate_gate_logic(gate_name, logic_function, vcd_filename):
    # Generate the VCD file
    result = logic_function()

    log_file = f"{gate_name}_log.txt"
    with open(log_file, 'w') as log:
        log.write(f"{datetime.now()}: {gate_name} simulation executed.\n")

    insert_log(gate_name, log_file, vcd_filename)

    return render_template("result.html", gate_name=gate_name, vcd_file=vcd_filename, log_file=log_file)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/not_gate")
def simulate_not_logic():
    a, b = [Signal(bool(0)) for _ in range(2)]

    def not_bench():
        not_inst = NOT_Gate(a, b)
        @instance
        def stimulus():
            yield delay(10)
        return not_inst, stimulus

    tb = traceSignals(not_bench)
    sim = Simulation(tb)
    sim.run()

    return simulate_gate_logic("NOT Gate", not_bench, "not_bench.vcd")

@app.route("/or_gate")
def simulate_or_logic():
    a, b, c = [Signal(bool(0)) for _ in range(3)]

    def or_bench():
        or_inst = OR_Gate(a, b, c)
        @instance
        def stimulus():
            yield delay(10)
        return or_inst, stimulus

    tb = traceSignals(or_bench)
    sim = Simulation(tb)
    sim.run()

    return simulate_gate_logic("OR Gate", or_bench, "or_bench.vcd")

@app.route("/and_gate")
def simulate_and_logic():
    a, b, c = [Signal(bool(0)) for _ in range(3)]

    def and_bench():
        and_inst = AND_Gate(a, b, c)
        @instance
        def stimulus():
            yield delay(10)
        return and_inst, stimulus

    tb = traceSignals(and_bench)
    sim = Simulation(tb)
    sim.run()

    return simulate_gate_logic("AND Gate", and_bench, "and_bench.vcd")

@app.route("/halfadder")
def simulate_halfadder_logic():
    a, b, s, c = [Signal(bool(0)) for _ in range(4)]

    def halfadder_bench():
        halfadder_inst = half_adder(a, b, s, c)
        @instance
        def stimulus():
            yield delay(10)
        return halfadder_inst, stimulus

    tb = traceSignals(halfadder_bench)
    sim = Simulation(tb)
    sim.run()

    return simulate_gate_logic("Half Adder", halfadder_bench, "halfadder_bench.vcd")

@app.route("/open_gtkwave/<vcd_file>")
def open_gtkwave(vcd_file):
    run_gtkwave(vcd_file)
    return f"Opening {vcd_file} in GTKWave!"

if __name__ == "__main__":
    app.run(debug=True)
