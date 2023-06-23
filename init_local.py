from snowflake.snowpark.session import Session

def init(session) -> Session:
    df = session.create_dataframe([
            [1, 2, "abc"],
            [3, 4, "def"],
            [6, 5, "ghi"]])
    df.write.mode("overwrite").save_as_table("products")
    return session