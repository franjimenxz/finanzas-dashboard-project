"""Añadir rol a Usuario

Revision ID: e28023a8f1d1
Revises: 13f7913e579c
Create Date: 2024-09-07 10:45:54.886020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e28023a8f1d1'
down_revision = '13f7913e579c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rol', sa.String(length=50), nullable=False, server_default='usuario'))


    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.drop_column('rol')

    # ### end Alembic commands ###
