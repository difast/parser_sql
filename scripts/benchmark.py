import time
from core.parser import NoSQLParser

def benchmark():
    parser = NoSQLParser()
    queries = [
        "SELECT a FROM t",
        "SELECT a, b FROM t WHERE x > 10",
        "SELECT * FROM t GROUP BY y LIMIT 100"
    ]
    
    for q in queries:
        start = time.time()
        for _ in range(1000):
            parser.parse(q)
        print(f"{q[:20]}...: {time.time() - start:.4f}s")

if __name__ == "__main__":
    benchmark()