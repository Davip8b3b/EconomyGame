from app import db

class User(db.Model):
  #criei uma tabela chamada users
  __tablename__  = 'users'
  # criei uma coluna em miha tabela com paramentros 
  id = db.column(db.Integer, primary_key = True)
  username = db.column(db.String, unique = True)
  password = db.column(db.String)
  
  def __init__(self, username, password):
    self.username = username
    self.password = password
  #Mostrar de forma organizada os dados na tabela 
  def __repr__(self): 
    return '<User %r>' % self.username
    
class Post(db.Model):
  
  __tablename__ = 'posts'
  
  id = db.column(db.Integer, primary_key = True)
  content = db.column(db.Text)
  user_id = db.column(db.Integer, db.ForeignKey('users.id'))
  
  user = db.relationship('User', foreign_keys = user_id)
  
  def __init__(self, content, user_id): 
    self.content = content
    self.user_id = user_id
    
  def __repr__(self): 
    return '<Post %r>' % self.id