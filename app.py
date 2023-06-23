from __future__ import annotations
from snowflake.snowpark.session import Session
from snowflake.snowpark.mock.mock_connection import MockServerConnection
from snowflake.snowpark import DataFrame

import init_local

def hello(session: Session) -> DataFrame:
    df = session.table("products")
    return df

# For local debugging
if __name__ == "__main__":
    session = Session(MockServerConnection()) # type: ignore
    session = init_local.init(session)
    print(hello(session).show())
