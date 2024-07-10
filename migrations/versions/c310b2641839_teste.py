"""teste

Revision ID: c310b2641839
Revises: 
Create Date: 2024-07-09 23:25:43.449348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c310b2641839'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.alter_column('data_nascimento',
               existing_type=sa.DATE(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.alter_column('data_nascimento',
               existing_type=sa.DATE(),
               nullable=False)

    # ### end Alembic commands ###
