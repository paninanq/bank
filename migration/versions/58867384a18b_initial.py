"""initial

Revision ID: 58867384a18b
Revises: 
Create Date: 2024-04-07 14:28:15.433901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58867384a18b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('deposits',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_summ', sa.Integer(), nullable=False),
    sa.Column('rate', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('finish_date', sa.Date(), nullable=False),
    sa.Column('type_of_deposit', sa.String(), nullable=False),
    sa.Column('exit_summ', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('deposits')
    # ### end Alembic commands ###
