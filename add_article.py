from db import db_session
from model import Article_run


first_article = Article_run(title = 'qwe', text = 'ashhjjhvdfghj')
db_session.add(first_article)
db_session.commit()