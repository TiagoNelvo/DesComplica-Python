from api import ma
from .. models import aluno_model
from marshmallow import fields

class AlunoSchema(ma.SQLAlchemyAutoSchema)