"""remove role column to users table

Revision ID: 932a4ad3cdfd
Revises: 4e5e8ff50d05
Create Date: 2023-10-14 23:37:47.445924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '932a4ad3cdfd'
down_revision = '4e5e8ff50d05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('role')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.VARCHAR(length=20), nullable=False))

    # ### end Alembic commands ###
