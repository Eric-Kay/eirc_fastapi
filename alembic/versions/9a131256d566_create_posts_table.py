"""create posts table

Revision ID: 9a131256d566
Revises: 
Create Date: 2023-02-26 18:56:34.234307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a131256d566'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable= False, primary_key= True), sa.Column("title", sa.String(), nullable = False))
    pass


def downgrade():
    op.drop_table("posts")
    pass
