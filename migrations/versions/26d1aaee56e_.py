"""empty message

Revision ID: 26d1aaee56e
Revises: e6acca6c5d2
Create Date: 2015-07-17 16:43:45.906488

"""

# revision identifiers, used by Alembic.
revision = '26d1aaee56e'
down_revision = 'e6acca6c5d2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('twitter_username', sa.String(length=255), nullable=True))
    op.create_unique_constraint(None, 'users', ['twitter_username'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'twitter_username')
    ### end Alembic commands ###
