"""add foreign key

Revision ID: 5a304edc2b3a
Revises: d9d3b63cb30f
Create Date: 2023-02-27 04:43:36.130584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a304edc2b3a'
down_revision = 'd9d3b63cb30f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable = False))
    op.create_foreign_key("posts_users_fk", source_table= "posts", referent_table= "users", local_cols=["id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
