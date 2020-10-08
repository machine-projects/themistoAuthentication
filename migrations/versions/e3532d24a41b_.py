"""empty message

Revision ID: e3532d24a41b
Revises: 57ded67ba129
Create Date: 2020-10-06 16:07:05.783285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3532d24a41b'
down_revision = '57ded67ba129'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('address', sa.Column('brei', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('address', 'brei')
    # ### end Alembic commands ###