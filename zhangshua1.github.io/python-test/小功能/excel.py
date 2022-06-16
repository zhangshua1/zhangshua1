import pandas as pd
from sqlalchemy import create_engine 
df = pd.read_excel("./456/456.csv")
df.head()
#展示索引的name
df.index.name = "id"
df.head()

engine = create_engine("mysql+mysqlconnector://root:123456@192.168.107.106:3306/test", echo=False)

df.to_sql(name='student', con=engine, if_exists='replace')
print(engine.execute("show create table student").first()[1])
engine.execute("select count(1) from student").first()
engine.execute("select * from student limit 5").fetchall()
