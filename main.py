from core.parser import NoSQLParser
from core.optimizer import optimize_query

def main():
    sql = """
    SELECT user_id, COUNT(*) AS cnt 
    FROM events 
    WHERE date > '2023-01-01' AND user_id = user_id
    GROUP BY user_id
    LIMIT 50
    """
    
    parser = NoSQLParser()
    query = parser.parse(sql)
    optimized = optimize_query(query)
    
    print("Original AST:", query.json(indent=2))
    print("Optimized AST:", optimized.json(indent=2))

if __name__ == "__main__":
    main()