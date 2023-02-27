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
    result = conn.execute(text('SELECT * FROM jobs'))
    jobs = []
    for row in result.all():
      jobs.append(row._mapping)
      # this is how we convert it to a dict
      # note that dict(row) doesn't work in > 1.4 vers of sqlalchemy
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"SELECT * FROM jobs WHERE id={id}")
      )
    rows = []
    for row in result.all():
      rows.append(row._mapping)
    if len(rows) == 0:
      return None
    else:
      return [dict(row) for row in rows]
    
    