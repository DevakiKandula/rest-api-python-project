"""empty message

Revision ID: 547d623150f5
Revises: 51afdded11c6
Create Date: 2023-10-12 14:16:02.387718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '547d623150f5'
down_revision = '51afdded11c6'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
