"""empty message

Revision ID: 7cefbb54e06
Revises: None
Create Date: 2015-03-18 19:36:48.263919

"""

# revision identifiers, used by Alembic.
revision = '7cefbb54e06'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('access_token', sa.String(), nullable=True),
    sa.Column('access_token_secret', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    ### end Alembic commands ###