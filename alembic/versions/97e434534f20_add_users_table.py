"""add users table

Revision ID: 97e434534f20
Revises: 985556f21f11
Create Date: 2023-02-27 03:51:14.710435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97e434534f20'
down_revision = '985556f21f11'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",
    sa.Column("id", sa.Integer(), nullable= False),
    sa.Column("email", sa.String(), nullable= False),
    sa.Column("password", sa.String(), nullable = False),
    sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default= sa.text("now()"), nullable= False),
    sa.PrimaryKeyConstraint("id"),
    sa.UniqueConstraint("email"))
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
