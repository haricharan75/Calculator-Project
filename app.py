from fastapi import FastAPI
from calculator import (
    add,
    subtract,
    multiply,
    divide,
    power,
    modulus,
    factorial,
)

app = FastAPI(
    title="Calculator API",
    description="A simple Calculator API built using FastAPI",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Calculator API",
        "docs": "/docs"
    }


@app.get("/add")
def add_numbers(a: float, b: float):
    return {"operation": "addition", "result": add(a, b)}


@app.get("/subtract")
def subtract_numbers(a: float, b: float):
    return {"operation": "subtraction", "result": subtract(a, b)}


@app.get("/multiply")
def multiply_numbers(a: float, b: float):
    return {"operation": "multiplication", "result": multiply(a, b)}


@app.get("/divide")
def divide_numbers(a: float, b: float):
    return {"operation": "division", "result": divide(a, b)}


@app.get("/power")
def power_numbers(a: float, b: float):
    return {"operation": "power", "result": power(a, b)}


@app.get("/modulus")
def modulus_numbers(a: float, b: float):
    return {"operation": "modulus", "result": modulus(a, b)}


@app.get("/factorial")
def factorial_number(n: int):
    return {"operation": "factorial", "result": factorial(n)}