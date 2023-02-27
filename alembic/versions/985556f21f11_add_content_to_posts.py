"""add content to posts

Revision ID: 985556f21f11
Revises: 9a131256d566
Create Date: 2023-02-27 03:43:30.521181

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '985556f21f11'
down_revision = '9a131256d566'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts",sa.Column("content", sa.String(), nullable= False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
