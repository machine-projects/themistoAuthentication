"""person address

Revision ID: 68283b6dac6b
Revises: 3a7109b510b8
Create Date: 2020-05-31 18:18:58.869316

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68283b6dac6b'
down_revision = '3a7109b510b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person_address',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('address_id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.Column('modification_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['address_id'], ['address.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id', 'address_id', 'person_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('person_address')
    # ### end Alembic commands ###
