import os
from sqlalchemy import create_engine, text

engine = create_engine(os.environ['DB_CONNECTION_STRING'],
  connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
    })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))
    jobs = []
    for row in result.all():
      jobs.append(row._mapping)
      # this is how we convert it to a dict
      # note that dict(row) doesn't work in > 1.4 vers of sqlalchemy
    return jobs
    