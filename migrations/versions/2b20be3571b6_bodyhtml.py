"""bodyhtml

Revision ID: 2b20be3571b6
Revises: 4e9cd029ec10
Create Date: 2017-11-27 16:23:41.323974

"""

# revision identifiers, used by Alembic.
revision = '2b20be3571b6'
down_revision = '4e9cd029ec10'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###
