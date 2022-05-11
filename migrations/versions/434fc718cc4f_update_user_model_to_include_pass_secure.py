"""update user model to include pass_secure

Revision ID: 434fc718cc4f
Revises: 0a82a178d107
Create Date: 2022-05-11 14:29:36.781381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '434fc718cc4f'
down_revision = '0a82a178d107'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###